import datetime
from typing import Any, cast

import numpy as np
import pytz
from skyfield import almanac
from skyfield.api import Time, Topos

from ...cache import get_ephemeris, get_timescale
from ...constants.twilight import Twilight
from ..utils import fast_altaz


def get_twilight_time_utc(lat, lon, elevation, start_date, twilight, event):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(
        latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation)
    )

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

    jd0 = t0.tt
    jd1 = t1.tt
    step_days = 0.005  # ~7.2 minutes sampling grid
    num_steps = int((jd1 - jd0) / step_days) + 2
    jd_grid = np.linspace(jd0, jd1, num_steps)
    t_grid = ts.tt_jd(jd_grid)

    # Vectorized bulk fast_altaz evaluation across full time grid
    alt_grid = fast_altaz(
        observer.at(t_grid), sun, temperature_C=10.0, pressure_mbar=1013.25
    )[0].degrees
    y_grid = (
        (alt_grid >= -6).astype(int)
        + (alt_grid >= -4).astype(int)
        + (alt_grid >= 6).astype(int)
    )

    indices = np.flatnonzero(np.diff(y_grid))
    if len(indices) == 0:
        return []

    thresholds = [-6.0, -4.0, 6.0]

    trans_jd_a = []
    trans_jd_b = []
    trans_alt_a = []
    trans_alt_b = []
    trans_target_alt = []
    trans_meta = []

    for idx in indices:
        y_prev = y_grid[idx]
        yi = y_grid[idx + 1]
        jd_a = jd_grid[idx]
        jd_b = jd_grid[idx + 1]
        alt_a = alt_grid[idx]
        alt_b = alt_grid[idx + 1]

        step = 1 if yi > y_prev else -1
        for current_y in range(y_prev + step, yi + step, step):
            prev_y = current_y - step
            target_alt = thresholds[min(prev_y, current_y)]
            trans_jd_a.append(jd_a)
            trans_jd_b.append(jd_b)
            trans_alt_a.append(alt_a)
            trans_alt_b.append(alt_b)
            trans_target_alt.append(target_alt)
            trans_meta.append((prev_y, current_y))

    arr_jd_a = np.array(trans_jd_a)
    arr_jd_b = np.array(trans_jd_b)
    arr_alt_a = np.array(trans_alt_a)
    arr_alt_b = np.array(trans_alt_b)
    arr_target = np.array(trans_target_alt)

    # Initial linear guess
    frac = (arr_target - arr_alt_a) / (arr_alt_b - arr_alt_a)
    arr_jd_curr = arr_jd_a + frac * (arr_jd_b - arr_jd_a)

    # Bulk secant refinement pass across all candidate transitions simultaneously
    alt_curr = fast_altaz(
        observer.at(ts.tt_jd(arr_jd_curr)), sun, temperature_C=10.0, pressure_mbar=1013.25
    )[0].degrees

    slope = (arr_alt_b - arr_alt_a) / (arr_jd_b - arr_jd_a)
    arr_jd_refined = arr_jd_curr - (alt_curr - arr_target) / slope

    t_final = ts.tt_jd(arr_jd_refined)
    dts = t_final.utc_datetime()

    events = []
    for ti_dt, (prev_y, current_y) in zip(dts, trans_meta):
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
                    "date": ti_dt,
                    "event": "Blue Hour",
                    "phase": "Start",
                    "type": "Blue Hour",
                }
            )
        elif prev_y == 1 and current_y == 2:
            events.append(
                {
                    "date": ti_dt,
                    "event": "Blue Hour",
                    "phase": "End",
                    "type": "Blue Hour",
                }
            )
            events.append(
                {
                    "date": ti_dt,
                    "event": "Golden Hour",
                    "phase": "Start",
                    "type": "Golden Hour",
                }
            )
        elif prev_y == 2 and current_y == 3:
            events.append(
                {
                    "date": ti_dt,
                    "event": "Golden Hour",
                    "phase": "End",
                    "type": "Golden Hour",
                }
            )
        elif prev_y == 3 and current_y == 2:
            events.append(
                {
                    "date": ti_dt,
                    "event": "Golden Hour",
                    "phase": "Start",
                    "type": "Golden Hour",
                }
            )
        elif prev_y == 2 and current_y == 1:
            events.append(
                {
                    "date": ti_dt,
                    "event": "Golden Hour",
                    "phase": "End",
                    "type": "Golden Hour",
                }
            )
            events.append(
                {
                    "date": ti_dt,
                    "event": "Blue Hour",
                    "phase": "Start",
                    "type": "Blue Hour",
                }
            )
        elif prev_y == 1 and current_y == 0:
            events.append(
                {
                    "date": ti_dt,
                    "event": "Blue Hour",
                    "phase": "End",
                    "type": "Blue Hour",
                }
            )

    return events
