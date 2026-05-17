from skyfield.api import load
import numpy as np
from scipy.optimize import brentq


def find_extrema(f, t0, t1, num_points=1000):
    """
    Finds the extrema of a function f over the interval [t0, t1]
    by finding the roots of its derivative.
    Returns a list of tuples (time, value, is_max).
    """
    ts = load.timescale()
    times = ts.linspace(t0, t1, num_points)

    # Approximate derivative
    dt = (t1 - t0) / num_points
    values = f(times)
    deriv = np.gradient(values, dt)

    # Find roots of the derivative
    root_indices = np.where(np.diff(np.sign(deriv)))[0]

    extrema = []
    for i in root_indices:
        try:
            # Refine root location
            def deriv_at(t):
                # Ensure t is float
                t_val = float(t)
                return np.gradient(
                    f(ts.tt(jd=[t_val - 0.01, t_val, t_val + 0.01])), 0.01
                )[1]

            t_root = brentq(deriv_at, float(times[i].tt), float(times[i + 1].tt))
            t_extremum = ts.tt(jd=t_root)
            v_extremum = f(t_extremum)

            # Check second derivative to determine if max or min
            def second_deriv_at(t):
                t_val = float(t)
                return np.gradient(
                    np.gradient(f(ts.tt(jd=[t_val - 0.01, t_val, t_val + 0.01])), 0.01),
                    0.01,
                )[1]

            is_max = second_deriv_at(t_root) < 0

            extrema.append((t_extremum, v_extremum, is_max))
        except (RuntimeError, ValueError):
            # brentq can fail if the root is not bracketed
            continue

    return extrema


def find_highest_altitude(observer, planet, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def altitude(t):
        return observer.at(t).observe(planet).apparent().altaz()[0].degrees

    extrema = find_extrema(altitude, t0, t1)
    maxima = [e for e in extrema if e[2]]

    if not maxima:
        return None, 0

    highest = max(maxima, key=lambda x: x[1])
    return highest[0].utc_datetime(), highest[1]


def find_aphelion_perihelion(eph, planet_name, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    body = eph[planet_name]
    sun = eph["sun"]

    def distance_to_sun(t):
        return body.at(t).observe(sun).distance().km

    extrema = find_extrema(distance_to_sun, t0, t1)

    events = []
    for t, v, is_max in extrema:
        event_type = "Aphelion" if is_max else "Perihelion"
        events.append(
            {
                "date": t.utc_datetime(),
                "event": f"{planet_name.capitalize()} {event_type}",
            }
        )

    return events


def find_moon_apogee_perigee(eph, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    moon = eph["moon"]
    earth = eph["earth"]

    def distance_to_earth(t):
        return earth.at(t).observe(moon).distance().km

    extrema = find_extrema(distance_to_earth, t0, t1)

    events = []
    for t, v, is_max in extrema:
        event_type = "Apogee" if is_max else "Perigee"
        events.append({"date": t.utc_datetime(), "event": f"Moon {event_type}"})

    return events


def find_conjunctions(
    eph, p1_name, p2_name, start_date, end_date, threshold_degrees=None
):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = eph[p1_name]
    p2 = eph[p2_name]

    def separation(t):
        return p1.at(t).separation_from(p2.at(t)).degrees

    extrema = find_extrema(separation, t0, t1)

    events = []
    for t, v, is_max in extrema:
        if not is_max:
            separation_val = v
            if threshold_degrees is None or separation_val < threshold_degrees:
                events.append(
                    {
                        "date": t.utc_datetime(),
                        "event": f"{p1_name.capitalize()} conjunct {p2_name.capitalize()}",
                        "separation_degrees": separation_val,
                    }
                )

    return events


def find_mercury_inferior_conjunctions(
    eph, start_date, end_date, threshold_degrees=5.0
):
    return find_conjunctions(
        eph, "mercury", "sun", start_date, end_date, threshold_degrees
    )


def find_lunar_occultations(observer, eph, bright_stars, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = eph["moon"]
    earth = eph["earth"]

    # Optimization: Hourly check, vectorized over times
    num_hours = int((t1 - t0) * 24)
    if num_hours < 1:
        num_hours = 1
    times = ts.linspace(t0, t1, num_hours)

    # Pre-calculate Moon positions once for all stars
    mpos = earth.at(times).observe(moon)

    events = []

    # Optimization: Use pre-calculated float columns if available to avoid Pint overhead
    if "ra_hours" in bright_stars.columns and "dec_degrees" in bright_stars.columns:
        ra_hours = bright_stars["ra_hours"].values
        dec_degrees = bright_stars["dec_degrees"].values
        names = bright_stars["Name"].values
    else:
        # Fallback to slower extraction if columns are missing
        ra_hours = [
            star_data["RA"].to("hour").magnitude
            if hasattr(star_data["RA"], "to")
            else star_data["RA"]
            for _, star_data in bright_stars.iterrows()
        ]
        dec_degrees = [
            star_data["Dec"].to("degree").magnitude
            if hasattr(star_data["Dec"], "to")
            else star_data["Dec"]
            for _, star_data in bright_stars.iterrows()
        ]
        names = bright_stars["Name"].values

    from skyfield.api import Star

    # Optimization: Filter stars by ecliptic latitude to prune candidates.
    # The Moon stays within ~5.3 degrees of the ecliptic.
    stars_vector = Star(ra_hours=ra_hours, dec_degrees=dec_degrees)
    # Observe all stars at t0 for filtering
    spos_at_t0 = earth.at(t0).observe(stars_vector)
    lats, _, _ = spos_at_t0.ecliptic_latlon()
    # Using 10 degree margin for safety
    mask = np.abs(lats.degrees) < 10.0

    indices_to_check = np.where(mask)[0]

    for idx in indices_to_check:
        star = Star(ra_hours=ra_hours[idx], dec_degrees=dec_degrees[idx])
        name = names[idx]

        # Observe star at all times (vectorized over times)
        spos = earth.at(times).observe(star)

        # Vectorized separation calculation
        seps = mpos.separation_from(spos).degrees

        # Find indices where separation < 0.5 degrees
        occ_indices = np.where(seps < 0.5)[0]

        for occ_idx in occ_indices:
            events.append(
                {
                    "date": times[occ_idx].utc_datetime(),
                    "event": f"Moon occults {name}",
                }
            )

    return events
