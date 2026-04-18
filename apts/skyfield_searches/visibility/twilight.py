import datetime
import pytz
from typing import Any, cast
from skyfield import almanac
from skyfield.api import Topos, Time
from ...cache import get_timescale, get_ephemeris
from ...constants.twilight import Twilight

def get_twilight_time_utc(lat, lon, elevation, start_date, twilight, event):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))

    if isinstance(start_date, Time):
        t0 = start_date
        t1 = ts.tt_jd(t0.tt + 2.0)
    else:
        t0 = ts.utc(start_date)
        t1 = ts.utc(start_date + datetime.timedelta(days=2))

    f = almanac.dark_twilight_day(eph, location)
    times, events = almanac.find_discrete(t0, t1, f)

    # Define transitions for evening (set) and morning (rise)
    if event == "set":  # Evening: getting darker
        transitions = {
            Twilight.CIVIL: (3, 2),  # Civil -> Nautical
            Twilight.NAUTICAL: (2, 1),  # Nautical -> Astronomical
            Twilight.ASTRONOMICAL: (1, 0),  # Astronomical -> Night
        }
    else:  # Morning: getting lighter
        transitions = {
            Twilight.ASTRONOMICAL: (0, 1),  # Night -> Astronomical
            Twilight.NAUTICAL: (1, 2),  # Astronomical -> Nautical
            Twilight.CIVIL: (2, 3),  # Nautical -> Civil
        }

    trans = transitions.get(twilight)
    if trans is None:
        return None
    prev_event, next_event = trans

    # The first event is the state at t0
    previous_y = f(t0)
    if times is not None and events is not None:
        for t, y in zip(times, events):
            if previous_y == prev_event and y == next_event:
                return t.utc_datetime().replace(tzinfo=pytz.UTC)
            previous_y = y

    return None

def find_golden_blue_hours(observer, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]

    def sun_state(t):
        # We want to detect transitions at -6, -4, 6
        # Account for atmospheric refraction at standard conditions
        alt = (
            observer.at(t)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )
        return (
            (alt >= -6).astype(int) + (alt >= -4).astype(int) + (alt >= 6).astype(int)
        )

    setattr(sun_state, "step_days", 0.005)  # ~7.2 minutes

    t, y = almanac.find_discrete(t0, t1, sun_state)

    events = []
    y_prev = sun_state(t0)

    for ti, yi in zip(t, y):
        # Oracle: Handle potential state jumps (e.g., 0 -> 2) by iterating through
        # all intermediate transitions. This ensures accuracy at high latitudes
        # or when using coarser time steps.
        step = 1 if yi > y_prev else -1
        for current_y in range(y_prev + step, yi + step, step):
            prev_y = current_y - step
            # Transitions:
            # 0 -> 1: Rising, Blue Hour Start (-6)
            # 1 -> 2: Rising, Blue Hour End / Golden Hour Start (-4)
            # 2 -> 3: Rising, Golden Hour End (6)
            # 3 -> 2: Setting, Golden Hour Start (6)
            # 2 -> 1: Setting, Golden Hour End / Blue Hour Start (-4)
            # 1 -> 0: Setting, Blue Hour End (-6)

            if prev_y == 0 and current_y == 1:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Blue Hour",
                        "phase": "Start",
                        "type": "Blue Hour",
                    }
                )
            elif prev_y == 1 and current_y == 2:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Blue Hour",
                        "phase": "End",
                        "type": "Blue Hour",
                    }
                )
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Golden Hour",
                        "phase": "Start",
                        "type": "Golden Hour",
                    }
                )
            elif prev_y == 2 and current_y == 3:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Golden Hour",
                        "phase": "End",
                        "type": "Golden Hour",
                    }
                )
            elif prev_y == 3 and current_y == 2:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Golden Hour",
                        "phase": "Start",
                        "type": "Golden Hour",
                    }
                )
            elif prev_y == 2 and current_y == 1:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Golden Hour",
                        "phase": "End",
                        "type": "Golden Hour",
                    }
                )
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Blue Hour",
                        "phase": "Start",
                        "type": "Blue Hour",
                    }
                )
            elif prev_y == 1 and current_y == 0:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Blue Hour",
                        "phase": "End",
                        "type": "Blue Hour",
                    }
                )

        y_prev = yi

    return events
