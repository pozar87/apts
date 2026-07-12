import logging
from typing import cast

import numpy as np
import pandas as pd

from ..constants import FilterStrategy, ObjectTableLabels
from ..optics.utils import OpticsUtils
from ..scoring import SuitabilityScorer
from ..utils.astronomy import (
    calculate_refraction,
    vectorized_geometric_altaz,
    vectorized_angular_separation,
    vectorized_geometric_imaging_duration,
)

logger = logging.getLogger(__name__)


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
    ):
        """
        Returns a ranked list of objects sorted by the Multi-Factor Score.
        Includes Messier and Solar objects.
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

        # 1. Collect combined targets (Messier + Solar)
        combined_df = DiscoveryService._get_combined_targets(place, catalogs, t_sf)

        # 2. Pre-calculate astronomical twilight
        twilight_times = DiscoveryService._get_twilight_window(place, t_dt)

        # 3. Vectorized Bulk Pre-calculations
        DiscoveryService._populate_bulk_data(
            place, equipment_path, combined_df, t_sf, twilight_times
        )

        # 4. Vectorized Scoring
        scores_df = scorer.calculate_scores_bulk(combined_df)
        combined_df["Score"] = scores_df["total_score"]

        # 5. Format and return results
        return DiscoveryService._format_discovery_results(combined_df, scores_df, limit)

    @staticmethod
    def _get_combined_targets(place, catalogs, date) -> pd.DataFrame:
        """Collects and combines Messier and Solar objects, excluding the Sun."""
        from ..objects.messier import Messier
        from ..objects import SolarObjects

        # Optimization: Pass date to constructors to avoid redundant compute() calls.
        messier_obj = Messier(place, catalogs, calculation_date=date)
        messier_obj.compute(calculation_date=date)

        # SolarObjects.compute() is already called in its __init__ with calculation_date.
        solar_obj = SolarObjects(place, calculation_date=date)

        combined_df = pd.concat(
            [messier_obj.objects, solar_obj.objects], ignore_index=True
        )
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

        size_major = df[ObjectTableLabels.SIZE_MAJOR].values
        size_minor = df[ObjectTableLabels.SIZE_MINOR].values

        # If they are Quantities, extract magnitudes once in bulk
        if len(size_major) > 0 and hasattr(size_major[0], "magnitude"):
            size_major = np.array([getattr(s, "magnitude", s) for s in size_major])
            size_minor = np.array([getattr(s, "magnitude", s) for s in size_minor])

        df["fov_ratio"] = OpticsUtils.calculate_fov_ratio(
            (size_major, size_minor),
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
        name_fallback = df["Name"].fillna("-").replace({"-": "", "nan": ""})
        is_missing_name = name_fallback == ""
        if is_missing_name.any():
            fallback_values = df["Messier"].fillna(df["NGC"]).fillna("Unknown")
            df.loc[is_missing_name, "Name"] = fallback_values[is_missing_name]

        results_df = df.sort_values("Score", ascending=False).head(limit)

        # Optimization: use itertuples() and a pre-converted details map instead of iterrows()
        # and row-wise .to_dict() for a significant speedup.
        top_scores_dict = scores_df.loc[results_df.index].to_dict("index")
        type_col = ObjectTableLabels.DSO_TYPE

        # Convert type column label to a valid itertuples name if needed,
        # but better to use itertuples(index=True, name='Pandas') and getattr or index-based access.
        # itertuples() can mangel column names with spaces.
        # Using to_dict('records') is safer and still very fast for small result sets.
        top_results_list = results_df.to_dict("records")

        scored_objects = [
            {
                "Name": row["Name"],
                "Type": row[type_col],
                "Score": row["Score"],
                "Details": top_scores_dict[results_df.index[i]],
            }
            for i, row in enumerate(top_results_list)
        ]

        return scored_objects
