from datetime import timedelta
from typing import Any, cast

import numpy as np
from skyfield import almanac, eclipselib
from skyfield.searchlib import find_minima
from ..cache import get_timescale, get_ephemeris
from ..constants import astronomy
from ..utils import planetary

def find_lunar_eclipses(start_date, end_date, observer=None):
    """
    Finds lunar eclipses and provides visibility info if an observer is provided.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)
    events = []
    for i, (ti, yi) in enumerate(zip(t, y)):
        event = {
            "date": ti.utc_datetime(),
            "type": "Lunar Eclipse",
            "eclipse_kind": eclipselib.LUNAR_ECLIPSES[yi],
            "penumbral_magnitude": details["penumbral_magnitude"][i],
            "umbral_magnitude": details["umbral_magnitude"][i],
        }

        if observer is not None:
            moon = eph["moon"]
            sun = eph["sun"]

            m_obs = observer.at(ti).observe(moon).apparent()
            # Oracle: use refracted position and account for Moon's semi-diameter.
            m_alt_refracted, _, m_dist = m_obs.altaz(
                temperature_C=10.0, pressure_mbar=1013.25
            )
            rm = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist.km))

            s_alt = (
                observer.at(ti)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            # Visibility: Moon partially above horizon (refracted)
            # and Sun below horizon (refracted altitude < -0.26 deg approx semi-diameter)
            event.update(
                {
                    "altitude": float(m_alt_refracted.degrees),
                    "sun_altitude": float(s_alt),
                    "is_visible": bool(m_alt_refracted.degrees > -rm and s_alt < -0.26),
                }
            )

        events.append(event)
    return events

def find_solar_eclipses(observer, start_date, end_date):
    """
    Finds solar eclipses for a specific observer, providing classification
    (Total, Annular, Partial), magnitude, and obscuration.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")
    moon = planetary.get_skyfield_obj("moon")

    def solar_separation(t):
        s = observer.at(t).observe(sun).apparent()
        m = observer.at(t).observe(moon).apparent()

        # Calculate topocentric angular radii
        s_dist = s.distance().km
        m_dist = m.distance().km

        s_radius = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s_dist))
        m_radius = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist))

        sep = s.separation_from(m).degrees
        return sep - (s_radius + m_radius)

    # Optimization: Solar eclipses only occur during New Moon.
    # We find geocentric New Moons and search +/- 12 hours around them.
    # This avoids expensive topocentric calculations for most of the year.
    # We extend the search range by 12 hours to catch New Moons just outside
    # the requested range whose topocentric eclipse falls within the range.
    eph = get_ephemeris()
    t_phases, y_phases = almanac.find_discrete(
        t0 - 0.5, t1 + 0.5, almanac.moon_phases(eph)
    )
    new_moons = [t for t, y in zip(t_phases, y_phases) if y == 0]

    setattr(solar_separation, "step_days", 0.005)

    events = []
    for t_nm in new_moons:
        # Narrow search window around geocentric New Moon to account for parallax
        tn0 = ts.from_datetime(t_nm.utc_datetime() - timedelta(hours=12))
        tn1 = ts.from_datetime(t_nm.utc_datetime() + timedelta(hours=12))

        # Ensure the narrow search window does not exceed our padded range
        if tn0.tt < (t0 - 0.5).tt:
            tn0 = t0 - 0.5
        if tn1.tt > (t1 + 0.5).tt:
            tn1 = t1 + 0.5

        times, separations = find_minima(tn0, tn1, solar_separation)

        for t, s in zip(times, separations):
            if s > 0:
                continue

            s_pos = observer.at(t).observe(sun).apparent()
            m_pos = observer.at(t).observe(moon).apparent()

            d = s_pos.separation_from(m_pos).degrees
            rs = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s_pos.distance().km))
            rm = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_pos.distance().km))

            if d < rs + rm:
                # Visibility check: Is the Sun above the horizon for this observer?
                # Oracle: use refracted position and account for Sun's semi-diameter.
                # An eclipse is visible if any part of the solar disk is above the horizon.
                # Refracted altitude is used; center of Sun at horizon means alt=0.
                sun_alt = s_pos.altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
                if sun_alt <= -rs:
                    continue

                # Classification
                if d <= abs(rs - rm):
                    if rm >= rs:
                        kind = "Total"
                    else:
                        kind = "Annular"
                else:
                    kind = "Partial"

                # Magnitude (fraction of solar diameter covered)
                mag = (rs + rm - d) / (2 * rs)

                # Obscuration (fraction of solar area covered)
                # Area of intersection of two circles
                if d <= abs(rs - rm):
                    obs = 1.0 if rm >= rs else (rm / rs) ** 2
                else:
                    # Formula for area of overlap of two circles
                    # Source: http://mathworld.wolfram.com/Circle-CircleIntersection.html
                    def area(r1, r2, d):
                        if d >= r1 + r2:
                            return 0.0
                        if d <= abs(r1 - r2):
                            return np.pi * min(r1, r2) ** 2
                        r1sq = r1**2
                        r2sq = r2**2
                        dsq = d**2
                        part1 = r1sq * np.arccos((dsq + r1sq - r2sq) / (2 * d * r1))
                        part2 = r2sq * np.arccos((dsq + r2sq - r1sq) / (2 * d * r2))
                        part3 = 0.5 * np.sqrt(
                            (-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)
                        )
                        return part1 + part2 - part3

                    overlap_area = area(rs, rm, d)
                    sun_area = np.pi * rs**2
                    obs = overlap_area / sun_area

                # Ensure the final event date falls within the requested range
                if t.tt < t0.tt or t.tt > t1.tt:
                    continue

                events.append(
                    {
                        "date": t.utc_datetime(),
                        "type": "Solar Eclipse",
                        "eclipse_type": kind,
                        "magnitude": float(mag),
                        "obscuration": float(obs),
                        "separation_degrees": float(d),
                    }
                )
    return events

def find_seasons(start_date, end_date):
    """
    Finds the start of seasons (equinoxes and solstices).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())

    t, y = almanac.find_discrete(t0, t1, almanac.seasons(eph))

    events = []
    for ti, yi in zip(t, y):
        events.append(
            {
                "date": ti.utc_datetime(),
                "event": almanac.SEASON_EVENTS[yi],
                "type": "Season",
            }
        )
    return events
