import datetime
from skyfield import almanac
from ..cache import get_ephemeris, get_timescale

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
