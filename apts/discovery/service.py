import logging
from typing import cast

import numpy as np
import pandas as pd

from ..constants import FilterStrategy, ObjectTableLabels
from ..optics.utils import OpticsUtils
from ..scoring import SuitabilityScorer
from ..utils.astronomy.altaz import vectorized_geometric_altaz
from ..utils.astronomy.calculations import vectorized_geometric_imaging_duration
from ..utils.astronomy.refraction import calculate_refraction
from ..utils.astronomy.separation import vectorized_angular_separation

logger = logging.getLogger(__name__)


def _extract_arcmin_floats(arr) -> np.ndarray:
    """Helper to convert raw catalog dimensions (Pint Quantities, floats, or NaNs) to float arcminutes."""
    if arr is None or len(arr) == 0:
        return np.array([], dtype=float)
    if not isinstance(arr, np.ndarray):
        arr = np.asarray(arr)
    # Optimization: Direct return for numeric arrays bypasses element-by-element loops
    if arr.dtype != object:
        return np.asarray(arr, dtype=float)
    res = np.empty(len(arr), dtype=float)
    for i, val in enumerate(arr):
        if val is None or pd.isna(val):
            res[i] = np.nan
        else:
            mag = getattr(val, "magnitude", val)
            try:
                res[i] = float(mag)
            except (ValueError, TypeError):
                res[i] = np.nan
    return res


class DiscoveryService:
    """
    High-level discovery methods for astronomical targets.
    """

    @staticmethod
    def get_top_picks(
        place,
        equipment_path,
        catalogs,
        date=None,
        strategy=FilterStrategy.BROADBAND,
        limit=20,
        include_ngc: bool = False,
        ngc_magnitude_limit: float | None = 13.0,
        min_fov_ratio: float | None = None,
    ):
        """
        Returns a ranked list of objects sorted by the Multi-Factor Score.
        Includes Messier and Solar objects, and optionally NGC objects.
        """
        scorer = SuitabilityScorer(place, equipment_path, filter_strategy=strategy)

        # Optimization: Normalize time once at the entry point to avoid redundant
        # conversions in downstream helper methods.
        t_calc = date if date is not None else place.date
        t_sf = (
            t_calc if isinstance(t_calc, type(place.ts.now())) else place.ts.utc(t_calc)
        )

        # Ensure date is converted to datetime for place helper methods that expect it
        from ..place.utils import get_scalar_datetime

        t_dt = get_scalar_datetime(t_sf)

        # 1. Collect combined targets (Messier + optional NGC + Solar)
        combined_df = DiscoveryService._get_combined_targets(
            place,
            catalogs,
            t_sf,
            include_ngc=include_ngc,
            ngc_magnitude_limit=ngc_magnitude_limit,
        )

        if combined_df.empty:
            return []

        # 2. Pre-calculate astronomical twilight
        twilight_times = DiscoveryService._get_twilight_window(place, t_dt)

        # 3. Vectorized Bulk Pre-calculations
        DiscoveryService._populate_bulk_data(
            place, equipment_path, combined_df, t_sf, twilight_times
        )

        # 4. Hard FOV ratio filter if min_fov_ratio is specified
        if min_fov_ratio is not None:
            combined_df = combined_df[combined_df["fov_ratio"] >= min_fov_ratio].copy()
            if combined_df.empty:
                return []

        # 5. Vectorized Scoring
        scores_df = scorer.calculate_scores_bulk(cast(pd.DataFrame, combined_df))
        combined_df["Score"] = scores_df["total_score"]

        # 6. Format and return results
        return DiscoveryService._format_discovery_results(combined_df, scores_df, limit)

    @staticmethod
    def _get_combined_targets(
        place,
        catalogs,
        date,
        include_ngc: bool = False,
        ngc_magnitude_limit: float | None = 13.0,
    ) -> pd.DataFrame:
        """Collects and combines Messier, Solar, and optional NGC objects, excluding the Sun."""
        from ..objects import SolarObjects
        from ..objects.messier import Messier

        # Optimization: Pass date to constructors to avoid redundant compute() calls.
        messier_obj = Messier(place, catalogs, calculation_date=date)
        messier_obj.compute(calculation_date=date)

        dfs = [messier_obj.objects]

        if include_ngc:
            from ..catalogs.ngc import normalize_name
            from ..objects.ngc import NGC

            ngc_obj = NGC(place, catalogs, calculation_date=date)
            ngc_df = ngc_obj.objects.copy()

            # Optimization: Magnitude pre-filter FIRST to prune ~80% of rows before deduplication,
            # drastically reducing string operations across ~14k rows.
            if ngc_magnitude_limit is not None:
                ngc_df = ngc_df[ngc_df["Magnitude_float"] <= ngc_magnitude_limit]

            # Deduplicate NGC entries against Messier catalog
            # Optimization: Reusing pre-calculated NGC_norm and IC_norm columns and using a set
            # for messier_ngc_ids avoids redundant normalize_name string parsing over filtered rows.
            messier_ngc_ids = set(
                cast(pd.Series, normalize_name(messier_obj.objects["NGC"])).dropna()
            )

            ngc_full_norm = "NGC" + ngc_df["NGC_norm"].fillna("")
            ic_full_norm = "IC" + ngc_df["IC_norm"].fillna("")

            is_messier_dup = (
                ngc_df["Name_norm"].isin(messier_ngc_ids)
                | ngc_full_norm.isin(messier_ngc_ids)
                | ic_full_norm.isin(messier_ngc_ids)
                | ngc_df["M"].notna()
            )
            ngc_df = ngc_df[~is_messier_dup]

            # Compute vectorized geometric coordinates for the filtered NGC subset
            ngc_df = ngc_obj.compute(calculation_date=date, df_to_compute=ngc_df)
            dfs.append(ngc_df)

        # SolarObjects.compute() is already called in its __init__ with calculation_date.
        solar_obj = SolarObjects(place, calculation_date=date)
        dfs.append(solar_obj.objects)

        combined_df = pd.concat(dfs, ignore_index=True)
        result = combined_df[combined_df["Name"] != "sun"].copy()
        return cast(pd.DataFrame, result)

    @staticmethod
    def _get_twilight_window(place, date):
        """Calculates astronomical twilight start and end times for the given date."""
        from ..constants.twilight import Twilight

        t_search = date if date is not None else place.date
        twilight_start = place.sunset_time(
            start_search_from=t_search, twilight=Twilight.ASTRONOMICAL
        )
        if not twilight_start:
            return None
        twilight_end = place.sunrise_time(
            start_search_from=twilight_start, twilight=Twilight.ASTRONOMICAL
        )
        return (twilight_start, twilight_end) if twilight_end else None

    @staticmethod
    def _populate_bulk_data(place, equipment_path, df, t_sf, twilight_times):
        """Performs bulk astronomical calculations (Altitude, Moon, Window, FOV)."""
        # 1. Altitude and Moon Separation (Lightning Fast Geometric Vectorization)
        # Optimization: Replacing Skyfield's high-precision .apparent() coordinate
        # transformations with vectorized NumPy geometric formulas provides a ~20x speedup
        # for this phase of discovery. The accuracy loss is negligible for scoring.
        DiscoveryService._populate_altitude_and_moon_data(place, df, t_sf)

        # 2. Imaging Window (Fully Vectorized)
        DiscoveryService._populate_imaging_window_data(place, df, twilight_times)

        # 3. FOV Fit
        # Optimization: Pre-extract sizes as float arrays and bypass Quantity handling
        # in the loop by passing them directly to calculate_fov_ratio.
        sensor_size = (
            equipment_path.output.sensor_width.to("mm").magnitude,
            equipment_path.output.sensor_height.to("mm").magnitude,
        )
        focal_length = (
            (equipment_path.telescope.focal_length * equipment_path.effective_barlow())
            .to("mm")
            .magnitude
        )

        size_major_raw = (
            df[ObjectTableLabels.SIZE_MAJOR].values
            if ObjectTableLabels.SIZE_MAJOR in df.columns
            else np.full(len(df), np.nan)
        )
        size_minor_raw = (
            df[ObjectTableLabels.SIZE_MINOR].values
            if ObjectTableLabels.SIZE_MINOR in df.columns
            else np.full(len(df), np.nan)
        )

        size_major_floats = _extract_arcmin_floats(size_major_raw)
        size_minor_floats = _extract_arcmin_floats(size_minor_raw)

        df["size_major_arcmin"] = size_major_floats
        df["size_minor_arcmin"] = size_minor_floats

        df["fov_ratio"] = OpticsUtils.calculate_fov_ratio(
            (size_major_floats, size_minor_floats),
            sensor_size,
            focal_length,
        )

    @staticmethod
    def _populate_altitude_and_moon_data(place, df, t_sf):
        """Calculates Altitude and Moon Separation in bulk using geometric formulas."""
        observer_at_t = place.observer.at(t_sf)
        moon_pos = observer_at_t.observe(place.moon).apparent()

        # Pre-calculated float coordinates (from catalog load)
        ras = df["ra_hours"].values.astype(float)
        decs = df["dec_degrees"].values.astype(float)

        # Geometric Altitude
        true_alt_deg, _ = vectorized_geometric_altaz(
            place.lat_decimal,
            place.lon_decimal,
            ras,
            decs,
            t_sf.gmst,
            sin_dec=df["sin_dec"].values if "sin_dec" in df.columns else None,
            cd_cr=df["cos_dec_cos_ra"].values if "cos_dec_cos_ra" in df.columns else None,
            cd_sr=df["cos_dec_sin_ra"].values if "cos_dec_sin_ra" in df.columns else None,
        )

        # Add first-order refraction for consistency with visibility gating
        df[ObjectTableLabels.ALTITUDE] = true_alt_deg + calculate_refraction(
            true_alt_deg
        )

        # Moon Separation
        moon_ra, moon_dec, _ = moon_pos.radec()
        df["moon_separation"] = vectorized_angular_separation(
            ras,
            decs,
            moon_ra.hours,
            moon_dec.degrees,
            sin_dec1=df["sin_dec"].values if "sin_dec" in df.columns else None,
            cd_cr1=df["cos_dec_cos_ra"].values if "cos_dec_cos_ra" in df.columns else None,
            cd_sr1=df["cos_dec_sin_ra"].values if "cos_dec_sin_ra" in df.columns else None,
        )

    @staticmethod
    def _populate_imaging_window_data(place, df, twilight_times):
        """Calculates imaging window duration in bulk."""
        df["window_minutes"] = 0.0
        if twilight_times:
            ras = df["ra_hours"].values.astype(float)
            decs = df["dec_degrees"].values.astype(float)
            # Optimization: All objects (stars and planets) use the fast vectorized geometric formula.
            # For planets, motion during a single night is negligible for discovery scoring.
            transits = pd.to_datetime(df[ObjectTableLabels.TRANSIT])

            # Ensure transits are UTC naive for vectorized_geometric_imaging_duration
            if transits.dt.tz is not None:
                transits_utc_naive = transits.dt.tz_convert("UTC").dt.tz_localize(None)
            else:
                transits_utc_naive = transits

            durations = vectorized_geometric_imaging_duration(
                place.lat_decimal,
                ras,
                decs,
                np.ones(len(df), dtype=bool),
                transits_utc_naive,
                twilight_times[0],
                twilight_times[1],
                sin_dec=df["sin_dec"].values if "sin_dec" in df.columns else None,
            )
            df["window_minutes"] = durations

    @staticmethod
    def _format_discovery_results(df, scores_df, limit):
        """Applies name fallbacks and formats the top N results into a list of dictionaries."""
        # Optimization: Slice top N results FIRST to avoid running string fallback logic
        # on thousands of candidates that will be discarded.
        results_df = df.sort_values("Score", ascending=False).head(limit).copy()

        name_fallback = results_df["Name"].fillna("-").replace({"-": "", "nan": ""})
        is_missing_name = name_fallback == ""
        if is_missing_name.any():
            fallback_values = results_df["Messier"].fillna(results_df["NGC"]).fillna("Unknown")
            results_df.loc[is_missing_name, "Name"] = fallback_values[is_missing_name]

        top_scores_dict = scores_df.loc[results_df.index].to_dict("index")
        type_col = ObjectTableLabels.DSO_TYPE

        top_results_list = results_df.to_dict("records")

        scored_objects = [
            {
                "Name": row["Name"],
                "Type": row[type_col],
                "Score": row["Score"],
                "Details": top_scores_dict[results_df.index[i]],
                "fov_ratio": float(row["fov_ratio"])
                if pd.notna(row.get("fov_ratio"))
                else 0.0,
                "size_major_arcmin": float(row["size_major_arcmin"])
                if pd.notna(row.get("size_major_arcmin"))
                else float("nan"),
                "size_minor_arcmin": float(row["size_minor_arcmin"])
                if pd.notna(row.get("size_minor_arcmin"))
                else float("nan"),
            }
            for i, row in enumerate(top_results_list)
        ]

        return scored_objects
