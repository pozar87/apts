from typing import Any, cast
from skyfield.api import Star
from ..cache import get_ephemeris, get_timescale
from ..utils import planetary
from .utils import find_solar_longitude_time
import numpy as np

def _get_drifted_radiant(data, peak_lon, current_lon):
    """
    Calculates the drifted radiant RA and Dec based on solar longitude difference.
    :param data: Shower data dictionary containing peak radiant and drift coefficients.
    :param peak_lon: Solar longitude at shower peak (degrees).
    :param current_lon: Solar longitude at calculation time (degrees).
    :return: (drifted_ra_hours, drifted_dec_degrees)
    """
    base_ra, base_dec = data["radiant"]
    d_ra = data.get("d_ra_h", 0.0)
    d_dec = data.get("d_dec_d", 0.0)

    # Handle longitude wrap-around
    diff = (current_lon - peak_lon + 180) % 360 - 180

    drifted_ra = (base_ra + diff * d_ra) % 24
    drifted_dec = base_dec + diff * d_dec

    return drifted_ra, drifted_dec

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

    # Drift coefficients (per degree of solar longitude) for major showers.
    # Sources: International Meteor Organization (IMO), Handbook for Meteor Observers.
    showers = {
        "Quadrantids": {
            "start": (1, 1),
            "peak_lon": 283.16,
            "end": (1, 5),
            "radiant": (15.3, 49.0),
            "d_ra_h": 0.021,
            "d_dec_d": -0.08,
        },
        "Lyrids": {
            "start": (4, 14),
            "peak_lon": 32.32,
            "end": (4, 30),
            "radiant": (18.1, 34.0),
            "d_ra_h": 0.033,
            "d_dec_d": 0.0,
        },
        "Eta Aquarids": {
            "start": (4, 19),
            "peak_lon": 45.5,
            "end": (5, 28),
            "radiant": (22.5, -1.0),
            "d_ra_h": 0.033,
            "d_dec_d": 0.15,
        },
        "Delta Aquarids": {
            "start": (7, 12),
            "peak_lon": 127.0,
            "end": (8, 23),
            "radiant": (22.6, -16.0),
            "d_ra_h": 0.03,
            "d_dec_d": -0.1,
        },
        "Perseids": {
            "start": (7, 17),
            "peak_lon": 140.0,
            "end": (8, 24),
            "radiant": (3.1, 58.0),
            "d_ra_h": 0.033,
            "d_dec_d": 0.13,
        },
        "Orionids": {
            "start": (10, 2),
            "peak_lon": 208.0,
            "end": (11, 7),
            "radiant": (6.3, 16.0),
            "d_ra_h": 0.025,
            "d_dec_d": 0.1,
        },
        "Leonids": {
            "start": (11, 6),
            "peak_lon": 235.27,
            "end": (11, 30),
            "radiant": (10.2, 22.0),
            "d_ra_h": 0.027,
            "d_dec_d": -0.21,
        },
        "Geminids": {
            "start": (12, 4),
            "peak_lon": 262.2,
            "end": (12, 17),
            "radiant": (7.5, 33.0),
            "d_ra_h": 0.038,
            "d_dec_d": -0.01,
        },
        "Ursids": {
            "start": (12, 17),
            "peak_lon": 270.7,
            "end": (12, 26),
            "radiant": (14.5, 76.0),
            "d_ra_h": 0.05,
            "d_dec_d": -0.1,
        },
    }

    events = []
    candidates = []

    for year in range(start_date.year, end_date.year + 1):
        for shower, data in showers.items():
            # 1. Determine Start, Peak, and End times
            t_s = ts.utc(year, data["start"][0], data["start"][1])
            t_e = ts.utc(year, data["end"][0], data["end"][1])
            if t_e < t_s:
                t_e = ts.utc(year + 1, data["end"][0], data["end"][1])

            peak_t = find_solar_longitude_time(t_s, t_e, data["peak_lon"])

            # Use current solar longitude at Start/End to calculate drifted radiant
            # For simplicity we use the UTC date start for 'Start' and 'End' events
            s_date = t_s.utc_datetime()
            e_date = t_e.utc_datetime()

            if start_date <= s_date <= end_date:
                candidates.append({
                    "time": t_s,
                    "date": s_date,
                    "shower_name": shower,
                    "phase": "Start",
                    "data": data
                })

            if peak_t is not None and start_date <= peak_t.utc_datetime() <= end_date:
                candidates.append({
                    "time": peak_t,
                    "date": peak_t.utc_datetime(),
                    "shower_name": shower,
                    "phase": "Peak",
                    "data": data
                })

            if start_date <= e_date <= end_date:
                candidates.append({
                    "time": t_e,
                    "date": e_date,
                    "shower_name": shower,
                    "phase": "End",
                    "data": data
                })

    if candidates:
        times_vec = ts.from_datetimes([c["date"] for c in candidates])

        # Geocentric solar longitude for all candidates (apparent)
        sun_lons = np.atleast_1d(cast(Any, earth).at(times_vec).observe(sun).apparent().ecliptic_latlon()[1].degrees)

        # Altitudes for Sun and Moon
        sun_alts = np.atleast_1d(
            observer.at(times_vec)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

        moon_alts = np.atleast_1d(
            observer.at(times_vec)
            .observe(moon)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

        moon_illums = np.atleast_1d(planetary.get_moon_illumination(times_vec))

        for i, c in enumerate(candidates):
            data = c["data"]
            peak_lon = data["peak_lon"]
            current_lon = sun_lons[i]

            # Calculate drifted radiant
            ra_h, dec_d = _get_drifted_radiant(data, peak_lon, current_lon)
            radiant_obj = Star(ra_hours=ra_h, dec_degrees=dec_d)

            r_alt, _, _ = (
                observer.at(c["time"])
                .observe(radiant_obj)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)
            )

            s_alt = sun_alts[i]
            is_visible = r_alt.degrees > 0 and s_alt <= -6

            events.append({
                "date": c["date"],
                "event": f"{c['shower_name']} {c['phase']}",
                "shower_name": c["shower_name"],
                "phase": c["phase"],
                "type": "Meteor Shower",
                "altitude": float(r_alt.degrees),
                "sun_altitude": float(s_alt),
                "moon_altitude": float(moon_alts[i]),
                "moon_illumination": float(moon_illums[i]),
                "is_visible": bool(is_visible),
            })

    return events
