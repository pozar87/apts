import datetime
import logging

import pandas as pd
from skyfield import almanac

from .cache import get_ephemeris, get_timescale
from .constants import FilterStrategy, ObjectTableLabels
from .scoring import SuitabilityScorer

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
        from .objects.messier import Messier
        from .objects.solar_objects import SolarObjects

        scorer = SuitabilityScorer(place, equipment_path, filter_strategy=strategy)

        # 1. Messier catalog
        messier_obj = Messier(place, catalogs)
        messier_obj.compute(calculation_date=date)

        # 2. Solar objects
        solar_obj = SolarObjects(place)
        solar_obj.compute(calculation_date=date)

        # Combine both for scoring
        combined_df = pd.concat(
            [messier_obj.objects, solar_obj.objects], ignore_index=True
        )

        # Exclude the Sun from discovery results since it is not a
        # valid astrophotography target and should not appear in top picks.
        combined_df = combined_df[combined_df["Name"] != "sun"]

        # Pre-calculate astronomical twilight for the given date
        # to avoid redundant searches for every object.
        from .constants.twilight import Twilight
        t_twilight = date if date is not None else place.date
        twilight_start = place.sunset_time(start_search_from=t_twilight, twilight=Twilight.ASTRONOMICAL)
        twilight_end = None
        if twilight_start:
            twilight_end = place.sunrise_time(start_search_from=twilight_start, twilight=Twilight.ASTRONOMICAL)
        twilight_times = (twilight_start, twilight_end) if twilight_start and twilight_end else None

        # ---------------------------------------------------------------------
        # Vectorized Bulk Pre-calculations (Optimization)
        # ---------------------------------------------------------------------
        import numpy as np
        from skyfield.api import Star
        from .objects.utils import vectorized_geometric_imaging_duration

        # 1. Bulk Moon Separation and Altitude
        t_twilight_sf = t_twilight if isinstance(t_twilight, type(place.ts.now())) else place.ts.utc(t_twilight)
        observer_at_t = place.observer.at(t_twilight_sf)
        moon_pos = observer_at_t.observe(place.moon).apparent()

        # Identify Stars for vectorized observation
        is_star = combined_df["skyfield_object"].apply(lambda x: isinstance(x, Star))
        stars_df = combined_df[is_star]

        if not stars_df.empty:
            stars_vector = Star(
                ra_hours=stars_df["ra_hours"].values.astype(float),
                dec_degrees=stars_df["dec_degrees"].values.astype(float)
            )
            stars_obs = observer_at_t.observe(stars_vector).apparent()
            combined_df.loc[is_star, "moon_separation"] = moon_pos.separation_from(stars_obs).degrees
            combined_df.loc[is_star, ObjectTableLabels.ALTITUDE] = stars_obs.altaz()[0].degrees

        # Other objects (moving) - still iterative but few (planets)
        for idx in combined_df[~is_star].index:
            obj = combined_df.loc[idx, "skyfield_object"]
            if obj:
                obj_obs = observer_at_t.observe(obj).apparent()
                combined_df.loc[idx, "moon_separation"] = moon_pos.separation_from(obj_obs).degrees
                combined_df.loc[idx, ObjectTableLabels.ALTITUDE] = obj_obs.altaz()[0].degrees

        # Ensure window_minutes column exists
        combined_df["window_minutes"] = 0.0

        # 2. Bulk Imaging Window (for Stars and Moving objects)
        if twilight_times:
            # Stars
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
                combined_df.loc[is_star, "window_minutes"] = durations

            # Moving objects (planets) - fall back to iterative get_imaging_window but only for planets
            for idx in combined_df[~is_star].index:
                obj = combined_df.loc[idx, "skyfield_object"]
                if obj:
                    window_info = place.get_imaging_window(
                        obj,
                        target_date=t_twilight,
                        astro_twilight_start=twilight_times[0],
                        astro_twilight_end=twilight_times[1],
                    )
                    combined_df.loc[idx, "window_minutes"] = window_info["total_minutes"]

        # 3. Bulk FOV Fit
        from .optics.utils import OpticsUtils
        sensor_size = (
            equipment_path.output.sensor_width.to("mm").magnitude,
            equipment_path.output.sensor_height.to("mm").magnitude,
        )
        focal_length = (
            (
                equipment_path.telescope.focal_length
                * equipment_path.effective_barlow()
            )
            .to("mm")
            .magnitude
        )
        combined_df["fov_ratio"] = OpticsUtils.calculate_fov_ratio(
            (combined_df[ObjectTableLabels.SIZE_MAJOR].values, combined_df[ObjectTableLabels.SIZE_MINOR].values),
            sensor_size,
            focal_length
        )

        # ---------------------------------------------------------------------

        # 4. Vectorized Scoring
        scores_df = scorer.calculate_scores_bulk(combined_df)

        # Update combined_df with score results and cleanup names
        combined_df["Score"] = scores_df["total_score"]

        # Prepare result dictionaries efficiently
        # Use a vectorized name fallback logic
        name_fallback = combined_df["Name"].fillna("-").replace({"-": "", "nan": ""})
        is_missing_name = (name_fallback == "")
        if is_missing_name.any():
            fallback_values = combined_df["Messier"].fillna(combined_df["NGC"]).fillna("Unknown")
            combined_df.loc[is_missing_name, "Name"] = fallback_values[is_missing_name]

        # Convert to final results list
        results_df = combined_df.sort_values("Score", ascending=False).head(limit)

        scored_objects = []
        for idx, row in results_df.iterrows():
            scored_objects.append({
                "Name": row["Name"],
                "Type": row[ObjectTableLabels.DSO_TYPE],
                "Score": row["Score"],
                "Details": scores_df.loc[idx].to_dict()
            })

        return scored_objects


class TimelineGenerator:
    """
    Generates a data structure containing twilight phases and Moon data.
    """

    @staticmethod
    def generate_timeline(place, date=None):
        """
        Export a data structure containing twilight phases (Civil, Nautical, Astronomical)
        and Moon transit data for a 24-hour period.
        """
        ts = get_timescale()
        eph = get_ephemeris()

        if date is None:
            t0_dt = place.date.utc_datetime().replace(
                hour=0, minute=0, second=0, microsecond=0, tzinfo=datetime.timezone.utc
            )
        else:
            if isinstance(date, datetime.datetime):
                t0_dt = date.replace(
                    hour=0,
                    minute=0,
                    second=0,
                    microsecond=0,
                    tzinfo=datetime.timezone.utc,
                )
            elif isinstance(date, datetime.date):
                t0_dt = datetime.datetime.combine(date, datetime.time.min).replace(
                    tzinfo=datetime.timezone.utc
                )
            else:
                # Assume Skyfield Time or other
                t0_dt = date.utc_datetime()
                if not isinstance(t0_dt, datetime.datetime):
                    t0_dt = t0_dt[0]
                t0_dt = t0_dt.replace(
                    hour=0,
                    minute=0,
                    second=0,
                    microsecond=0,
                    tzinfo=datetime.timezone.utc,
                )

        t0 = ts.utc(t0_dt)
        t1 = ts.utc(t0_dt + datetime.timedelta(days=1))

        # 1. Twilight phases
        # dark_twilight_day returns:
        # 0: Night
        # 1: Astronomical Twilight
        # 2: Nautical Twilight
        # 3: Civil Twilight
        # 4: Day
        f_twilight = almanac.dark_twilight_day(eph, place.location)
        times, events = almanac.find_discrete(t0, t1, f_twilight)

        twilight_map = {
            0: "Night",
            1: "Astronomical Twilight",
            2: "Nautical Twilight",
            3: "Civil Twilight",
            4: "Day",
        }

        twilight_events = []
        for t, e in zip(times, events):
            twilight_events.append(
                {
                    "time": t.utc_datetime(),
                    "phase": twilight_map.get(int(e), "Unknown"),
                    "event_id": int(e),
                }
            )

        # 2. Moon transit data
        f_moon = almanac.meridian_transits(eph, eph["moon"], place.location)
        m_times, m_events = almanac.find_discrete(t0, t1, f_moon)

        moon_events = []
        for t, e in zip(m_times, m_events):
            moon_events.append(
                {
                    "time": t.utc_datetime(),
                    "type": "Upper Transit" if int(e) == 1 else "Lower Transit",
                }
            )

        return {
            "date": t0_dt.date(),
            "twilight_events": twilight_events,
            "moon_events": moon_events,
        }
