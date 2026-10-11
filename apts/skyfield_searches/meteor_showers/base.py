from typing import Any, cast

import numpy as np

from ...cache import get_ephemeris, get_timescale
from ...utils import planetary
from ..utils import fast_altaz
from .calculations import (
    _calculate_radiant_altitudes,
    _generate_shower_candidates,
)


def find_meteor_showers(observer, start_date, end_date):
    """
    Finds meteor shower peaks and calculates radiant visibility for a given observer.
    Meteor shower peaks are determined by the Sun's ecliptic longitude (λ⊙).

    The presence and altitude of the Moon during the peak is a critical factor for
    astrophotographers, as high lunar illumination can significantly wash out
    fainter meteors.

    :param observer: Skyfield observer (Topos or VectorSum).
    :param start_date: Start of the search range (datetime).
    :param end_date: End of the search range (datetime).
    :return: List of event dictionaries.
    """
    ts = get_timescale()
    eph = get_ephemeris()
    sun = eph["sun"]
    moon = eph["moon"]
    earth = eph["earth"]

    candidates = _generate_shower_candidates(start_date, end_date, ts)
    if not candidates:
        return []

    times_vec = ts.from_datetimes([c["date"] for c in candidates])

    # Geocentric solar longitude for all candidates (apparent)
    sun_lons = np.atleast_1d(
        cast(Any, earth)
        .at(times_vec)
        .observe(sun)
        .apparent()
        .ecliptic_latlon()[1]
        .degrees
    )

    # Optimization: Hoist observer.at(times_vec) and use fast_altaz for Sun and Moon
    obs_at_times = observer.at(times_vec)
    sun_alts = np.atleast_1d(
        fast_altaz(obs_at_times, sun, temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
    )

    moon_alts = np.atleast_1d(
        fast_altaz(obs_at_times, moon, temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
    )

    moon_illums = np.atleast_1d(planetary.get_moon_illumination(times_vec))

    r_alts_geom = _calculate_radiant_altitudes(observer, candidates, times_vec, sun_lons)

    events = []
    for i, c in enumerate(candidates):
        s_alt = sun_alts[i]
        r_alt_deg = r_alts_geom[i]
        is_visible = r_alt_deg > 0 and s_alt <= -6

        events.append(
            {
                "date": c["date"],
                "event": f"{c['shower_name']} {c['phase']}",
                "shower_name": c["shower_name"],
                "phase": c["phase"],
                "type": "Meteor Shower",
                "altitude": float(r_alt_deg),
                "sun_altitude": float(s_alt),
                "moon_altitude": float(moon_alts[i]),
                "moon_illumination": float(moon_illums[i]),
                "is_visible": bool(is_visible),
            }
        )

    return events
