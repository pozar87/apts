import logging
from typing import cast

import numpy as np
import pandas as pd
from skyfield.api import Star

from ..constants import FilterStrategy, ObjectTableLabels
from ..objects.utils import vectorized_geometric_imaging_duration
from ..optics.utils import OpticsUtils
from ..scoring import SuitabilityScorer

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

        # 1. Collect combined targets (Messier + Solar)
        combined_df = DiscoveryService._get_combined_targets(place, catalogs, date)

        # 2. Pre-calculate astronomical twilight
        twilight_times = DiscoveryService._get_twilight_window(place, date)

        # 3. Vectorized Bulk Pre-calculations
        DiscoveryService._populate_bulk_data(
            place, equipment_path, combined_df, date, twilight_times
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
        from ..objects.solar_objects import SolarObjects

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
    def _populate_bulk_data(place, equipment_path, df, date, twilight_times):
        """Performs bulk astronomical calculations (Altitude, Moon, Window, FOV)."""
        t_calc = date if date is not None else place.date
        t_sf = (
            t_calc if isinstance(t_calc, type(place.ts.now())) else place.ts.utc(t_calc)
        )
        observer_at_t = place.observer.at(t_sf)
        moon_pos = observer_at_t.observe(place.moon).apparent()

        # 1. Altitude and Moon Separation (Fully Vectorized)
        # Optimization: We treat all objects (stars and planets) as fixed bodies at their current
        # RA/Dec for the purpose of this calculation. This eliminates iterative Skyfield calls
        # and provides sufficient accuracy for discovery scoring.
        ras = df["ra_hours"].values.astype(float)
        decs = df["dec_degrees"].values.astype(float)
        targets_vector = Star(ra_hours=ras, dec_degrees=decs)
        targets_obs = observer_at_t.observe(targets_vector).apparent()

        df["moon_separation"] = moon_pos.separation_from(targets_obs).degrees
        df[ObjectTableLabels.ALTITUDE] = targets_obs.altaz()[0].degrees

        # 2. Imaging Window (Fully Vectorized)
        df["window_minutes"] = 0.0
        if twilight_times:
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
            )
            df["window_minutes"] = durations

        # 3. FOV Fit
        sensor_size = (
            equipment_path.output.sensor_width.to("mm").magnitude,
            equipment_path.output.sensor_height.to("mm").magnitude,
        )
        focal_length = (
            (equipment_path.telescope.focal_length * equipment_path.effective_barlow())
            .to("mm")
            .magnitude
        )
        df["fov_ratio"] = OpticsUtils.calculate_fov_ratio(
            (
                df[ObjectTableLabels.SIZE_MAJOR].values,
                df[ObjectTableLabels.SIZE_MINOR].values,
            ),
            sensor_size,
            focal_length,
        )

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
