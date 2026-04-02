from datetime import datetime
from skyfield.api import load, Star
from ..cache import get_ephemeris, get_timescale
from ..utils import planetary
from .utils import find_solar_longitude_time

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
    utc = start_date.tzinfo
    eph = get_ephemeris()
    sun = eph["sun"]
    moon = eph["moon"]

    showers = {
        "Quadrantids": {
            "start": (1, 1),
            "peak_lon": 283.16,
            "end": (1, 5),
            "radiant": (15.3, 49.0),
        },
        "Lyrids": {
            "start": (4, 14),
            "peak_lon": 32.32,
            "end": (4, 30),
            "radiant": (18.1, 34.0),
        },
        "Eta Aquarids": {
            "start": (4, 19),
            "peak_lon": 45.5,
            "end": (5, 28),
            "radiant": (22.5, -1.0),
        },
        "Delta Aquarids": {
            "start": (7, 12),
            "peak_lon": 127.0,
            "end": (8, 23),
            "radiant": (22.6, -16.0),
        },
        "Perseids": {
            "start": (7, 17),
            "peak_lon": 140.0,
            "end": (8, 24),
            "radiant": (3.1, 58.0),
        },
        "Orionids": {
            "start": (10, 2),
            "peak_lon": 208.0,
            "end": (11, 7),
            "radiant": (6.3, 16.0),
        },
        "Leonids": {
            "start": (11, 6),
            "peak_lon": 235.27,
            "end": (11, 30),
            "radiant": (10.2, 22.0),
        },
        "Geminids": {
            "start": (12, 4),
            "peak_lon": 262.2,
            "end": (12, 17),
            "radiant": (7.5, 33.0),
        },
        "Ursids": {
            "start": (12, 17),
            "peak_lon": 270.7,
            "end": (12, 26),
            "radiant": (14.5, 76.0),
        },
    }

    events = []
    peak_candidates = []

    for year in range(start_date.year, end_date.year + 1):
        for shower, data in showers.items():
            s_date = datetime(year, data["start"][0], data["start"][1], tzinfo=utc)
            e_date = datetime(year, data["end"][0], data["end"][1], tzinfo=utc)

            # Handle showers crossing year boundary
            t_s = ts.utc(year, data["start"][0], data["start"][1])
            t_e = ts.utc(year, data["end"][0], data["end"][1])
            if t_e < t_s:
                t_e = ts.utc(year + 1, data["end"][0], data["end"][1])

            peak_t = find_solar_longitude_time(t_s, t_e, data["peak_lon"])
            peak_date = peak_t.utc_datetime() if peak_t is not None else None

            if start_date <= s_date <= end_date:
                events.append({
                    "date": s_date,
                    "event": f"{shower} Start",
                    "shower_name": shower,
                    "phase": "Start",
                    "type": "Meteor Shower",
                })

            if peak_date and start_date <= peak_date <= end_date:
                peak_candidates.append({
                    "peak_t": peak_t,
                    "peak_date": peak_date,
                    "shower_name": shower,
                    "radiant": data["radiant"]
                })

            if start_date <= e_date <= end_date:
                events.append({
                    "date": e_date,
                    "event": f"{shower} End",
                    "shower_name": shower,
                    "phase": "End",
                    "type": "Meteor Shower",
                })

    if peak_candidates:
        # Calculate Sun and Moon data in bulk for efficiency
        peak_times = ts.from_datetimes([p["peak_date"] for p in peak_candidates])

        sun_alts = (
            observer.at(peak_times)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

        moon_alts = (
            observer.at(peak_times)
            .observe(moon)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

        moon_illums = planetary.get_moon_illumination(peak_times)

        for i, p in enumerate(peak_candidates):
            # For radiants, we observe individually to avoid pairwise N-to-N vectorization
            # issues in Skyfield for Star objects.
            radiant_ra, radiant_dec = p["radiant"]
            radiant_obj = Star(ra_hours=radiant_ra, dec_degrees=radiant_dec)

            r_alt, _, _ = (
                observer.at(p["peak_t"])
                .observe(radiant_obj)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)
            )

            s_alt = sun_alts[i]
            is_visible = r_alt.degrees > 0 and s_alt <= -6

            events.append({
                "date": p["peak_date"],
                "event": f"{p['shower_name']} Peak",
                "shower_name": p["shower_name"],
                "phase": "Peak",
                "type": "Meteor Shower",
                "altitude": float(r_alt.degrees),
                "sun_altitude": float(s_alt),
                "moon_altitude": float(moon_alts[i]),
                "moon_illumination": float(moon_illums[i]),
                "is_visible": bool(is_visible),
            })

    return events
