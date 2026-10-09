from typing import cast

import numpy as np

from ..utils import find_solar_longitude_time

# Drift coefficients (per degree of solar longitude) for major showers.
# Sources: International Meteor Organization (IMO), Handbook for Meteor Observers.
METEOR_SHOWERS = {
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


def _generate_shower_candidates(start_date, end_date, ts, showers=None):
    """
    Generates candidate event dates and phases (Start, Peak, End) for meteor showers.
    """
    if showers is None:
        showers = METEOR_SHOWERS

    candidates = []
    for year in range(start_date.year, end_date.year + 1):
        for shower, data in showers.items():
            # Determine Start, Peak, and End times
            t_s = ts.utc(year, data["start"][0], data["start"][1])
            t_e = ts.utc(year, data["end"][0], data["end"][1])
            if t_e < t_s:
                t_e = ts.utc(year + 1, data["end"][0], data["end"][1])

            s_date = t_s.utc_datetime()
            e_date = t_e.utc_datetime()

            # Optimization: Fast window pre-filtering to skip showers outside the search range
            if e_date < start_date or s_date > end_date:
                continue

            peak_t = find_solar_longitude_time(t_s, t_e, data["peak_lon"])

            if start_date <= s_date <= end_date:
                candidates.append(
                    {
                        "time": t_s,
                        "date": s_date,
                        "shower_name": shower,
                        "phase": "Start",
                        "data": data,
                    }
                )

            if peak_t is not None and start_date <= peak_t.utc_datetime() <= end_date:
                candidates.append(
                    {
                        "time": peak_t,
                        "date": peak_t.utc_datetime(),
                        "shower_name": shower,
                        "phase": "Peak",
                        "data": data,
                    }
                )

            if start_date <= e_date <= end_date:
                candidates.append(
                    {
                        "time": t_e,
                        "date": e_date,
                        "shower_name": shower,
                        "phase": "End",
                        "data": data,
                    }
                )

    return candidates


def _calculate_radiant_altitudes(observer, candidates, times_vec, sun_lons):
    """
    Calculates topocentric radiant altitudes with atmospheric refraction for all candidate times.
    """
    from ...utils.astronomy.refraction import calculate_refraction
    from ..visibility.culmination import _get_observer_coords

    lat_deg, lon_hours = _get_observer_coords(observer)
    lon_decimal = lon_hours * 15.0

    ra_h_list = []
    dec_d_list = []
    for i, c in enumerate(candidates):
        data = c["data"]
        peak_lon = data["peak_lon"]
        current_lon = sun_lons[i]
        ra_h, dec_d = _get_drifted_radiant(data, peak_lon, current_lon)
        ra_h_list.append(ra_h)
        dec_d_list.append(dec_d)

    ras = np.array(ra_h_list)
    decs = np.array(dec_d_list)

    check_times_gmst = times_vec.gmst
    lst_hours = cast(float, check_times_gmst) + lon_decimal / 15.0
    lat_rad = np.deg2rad(lat_deg)
    lst_rad = np.deg2rad(lst_hours * 15.0)

    sin_lat = np.sin(lat_rad)
    cos_lat = np.cos(lat_rad)

    ra_rad = np.deg2rad(ras * 15.0)
    dec_rad = np.deg2rad(decs)

    sin_dec = np.sin(dec_rad)
    cos_dec = np.cos(dec_rad)

    sin_lst = np.sin(lst_rad)
    cos_lst = np.cos(lst_rad)

    cd_cr = cos_dec * np.cos(ra_rad)
    cd_sr = cos_dec * np.sin(ra_rad)

    cd_ch = cos_lst * cd_cr + sin_lst * cd_sr

    sin_alt = sin_lat * sin_dec + cos_lat * cd_ch
    r_alts_geom = np.rad2deg(np.arcsin(np.clip(sin_alt, -1.0, 1.0)))
    r_alts_geom += calculate_refraction(r_alts_geom)

    return r_alts_geom
