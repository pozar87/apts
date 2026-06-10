import logging
import pandas as pd
import numpy as np
from skyfield.api import Star

from ..constants import FilterStrategy, ObjectTableLabels
from ..scoring import SuitabilityScorer
from ..objects.utils import vectorized_geometric_imaging_duration
from ..optics.utils import OpticsUtils

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
        DiscoveryService._populate_bulk_data(place, equipment_path, combined_df, date, twilight_times)

        # 4. Vectorized Scoring
        scores_df = scorer.calculate_scores_bulk(combined_df)
        combined_df["Score"] = scores_df["total_score"]

        # 5. Format and return results
        return DiscoveryService._format_discovery_results(combined_df, scores_df, limit)

    @staticmethod
    def _get_combined_targets(place, catalogs, date):
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
        return combined_df[combined_df["Name"] != "sun"].copy()

    @staticmethod
    def _get_twilight_window(place, date):
        """Calculates astronomical twilight start and end times for the given date."""
        from ..constants.twilight import Twilight
        t_search = date if date is not None else place.date
        twilight_start = place.sunset_time(start_search_from=t_search, twilight=Twilight.ASTRONOMICAL)
        if not twilight_start:
            return None
        twilight_end = place.sunrise_time(start_search_from=twilight_start, twilight=Twilight.ASTRONOMICAL)
        return (twilight_start, twilight_end) if twilight_end else None

    @staticmethod
    def _populate_bulk_data(place, equipment_path, df, date, twilight_times):
        """Performs bulk astronomical calculations (Altitude, Moon, Window, FOV)."""
        t_calc = date if date is not None else place.date
        t_sf = t_calc if isinstance(t_calc, type(place.ts.now())) else place.ts.utc(t_calc)
        observer_at_t = place.observer.at(t_sf)
        moon_pos = observer_at_t.observe(place.moon).apparent()

        # Identify Stars vs Moving Objects
        # Optimization: list comprehension over .values is faster than .apply() for type checking.
        is_star = np.array([isinstance(x, Star) for x in df["skyfield_object"].values])
        stars_df = df[is_star]

        # 1. Altitude and Moon Separation
        if not stars_df.empty:
            stars_vector = Star(
                ra_hours=stars_df["ra_hours"].values.astype(float),
                dec_degrees=stars_df["dec_degrees"].values.astype(float)
            )
            stars_obs = observer_at_t.observe(stars_vector).apparent()
            df.loc[is_star, "moon_separation"] = moon_pos.separation_from(stars_obs).degrees
            df.loc[is_star, ObjectTableLabels.ALTITUDE] = stars_obs.altaz()[0].degrees

        # Moving objects (iterative but minimal)
        for idx in df[~is_star].index:
            obj = df.loc[idx, "skyfield_object"]
            if obj:
                obj_obs = observer_at_t.observe(obj).apparent()
                df.loc[idx, "moon_separation"] = moon_pos.separation_from(obj_obs).degrees
                df.loc[idx, ObjectTableLabels.ALTITUDE] = obj_obs.altaz()[0].degrees

        # 2. Imaging Window
        df["window_minutes"] = 0.0
        if twilight_times:
            if not stars_df.empty:
                transits = pd.to_datetime(stars_df[ObjectTableLabels.TRANSIT])
                durations = vectorized_geometric_imaging_duration(
                    place.lat_decimal,
                    stars_df["ra_hours"].values.astype(float),
                    stars_df["dec_degrees"].values.astype(float),
                    np.ones(len(stars_df), dtype=bool),
                    transits,
                    twilight_times[0],
                    twilight_times[1]
                )
                df.loc[is_star, "window_minutes"] = durations

            for idx in df[~is_star].index:
                obj = df.loc[idx, "skyfield_object"]
                if obj:
                    window_info = place.get_imaging_window(
                        obj,
                        target_date=t_calc,
                        astro_twilight_start=twilight_times[0],
                        astro_twilight_end=twilight_times[1],
                    )
                    df.loc[idx, "window_minutes"] = window_info["total_minutes"]

        # 3. FOV Fit
        sensor_size = (
            equipment_path.output.sensor_width.to("mm").magnitude,
            equipment_path.output.sensor_height.to("mm").magnitude,
        )
        focal_length = (
            (equipment_path.telescope.focal_length * equipment_path.effective_barlow()).to("mm").magnitude
        )
        df["fov_ratio"] = OpticsUtils.calculate_fov_ratio(
            (df[ObjectTableLabels.SIZE_MAJOR].values, df[ObjectTableLabels.SIZE_MINOR].values),
            sensor_size,
            focal_length
        )

    @staticmethod
    def _format_discovery_results(df, scores_df, limit):
        """Applies name fallbacks and formats the top N results into a list of dictionaries."""
        name_fallback = df["Name"].fillna("-").replace({"-": "", "nan": ""})
        is_missing_name = (name_fallback == "")
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
