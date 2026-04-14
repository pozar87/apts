import logging
import datetime
import pandas as pd
from skyfield import almanac
from .constants import FilterStrategy, ObjectTableLabels
from .scoring import SuitabilityScorer
from .cache import get_timescale, get_ephemeris
from .constants.twilight import Twilight

logger = logging.getLogger(__name__)

class DiscoveryService:
    """
    High-level discovery methods for astronomical targets.
    """

    @staticmethod
    def get_top_picks(place, equipment_path, catalogs, date=None, strategy=FilterStrategy.BROADBAND, limit=20):
        """
        Returns a ranked list of objects sorted by the Multi-Factor Score.
        """
        scorer = SuitabilityScorer(place, equipment_path, filter_strategy=strategy)

        all_objects = []

        # Collect from Messier and NGC
        messier_df = catalogs.MESSIER
        ngc_df = catalogs.NGC

        # Combine catalogs
        combined_df = pd.concat([messier_df, ngc_df], ignore_index=True)

        # Filtering for reasonable visibility (optional optimization)
        # For now, we'll score everything, but typically you'd filter by magnitude or altitude first

        scored_objects = []

        for _, row in combined_df.iterrows():
            score_data = scorer.calculate_total_score(row, time=date)
            if score_data:
                obj_info = {
                    "Name": row.get("Name") or row.get("Messier") or row.get("NGC"),
                    "Type": row.get(ObjectTableLabels.DSO_TYPE),
                    "Score": score_data["total_score"],
                    "Details": score_data
                }
                scored_objects.append(obj_info)

        # Sort by Score descending
        scored_objects.sort(key=lambda x: x["Score"], reverse=True)

        return scored_objects[:limit]

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
            t0_dt = place.date.utc_datetime().replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=datetime.timezone.utc)
        else:
            if isinstance(date, datetime.datetime):
                t0_dt = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=datetime.timezone.utc)
            else:
                t0_dt = datetime.datetime.combine(date, datetime.time.min).replace(tzinfo=datetime.timezone.utc)

        t0 = ts.utc(t0_dt)
        t1 = ts.utc(t0_dt + datetime.timedelta(days=1))

        # 1. Twilight phases
        f_twilight = almanac.dark_twilight_day(eph, place.location)
        times, events = almanac.find_discrete(t0, t1, f_twilight)

        twilight_events = []
        for t, e in zip(times, events):
            twilight_events.append({
                "time": t.utc_datetime(),
                "phase": Twilight(e).name if e in [1, 2, 3, 4] else "Day" if e == 4 else "Night",
                "event_id": e
            })

        # 2. Moon transit data
        f_moon = almanac.meridian_transits(eph, eph["moon"], place.location)
        m_times, m_events = almanac.find_discrete(t0, t1, f_moon)

        moon_events = []
        for t, e in zip(m_times, m_events):
            moon_events.append({
                "time": t.utc_datetime(),
                "type": "Upper Transit" if e == 1 else "Lower Transit"
            })

        return {
            "date": t0_dt.date(),
            "twilight_events": twilight_events,
            "moon_events": moon_events
        }
