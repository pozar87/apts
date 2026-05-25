import numpy as np
from ...cache import get_timescale
from ...constants import astronomy
from ...utils import planetary
from ..utils import _refine_conjunction

def find_lunar_planetary_occultations(observer, start_date, end_date):
    """
    Finds occultations of planets by the Moon for a specific observer.
    Provides precise ingress and egress times.
    Optimized via vectorized coarse check followed by windowed refinement.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    sun = planetary.get_skyfield_obj("sun")

    planet_names = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    planet_objs = [planetary.get_skyfield_obj(p) for p in planet_names]
    simple_names = [planetary.get_simple_name(p) for p in planet_names]

    # Total days in range
    duration_days = t1 - t0
    # Check every 2 minutes for precision
    num_steps = int(duration_days * 24 * 30)
    if num_steps < 2:
        return []
    times = ts.linspace(t0, t1, num_steps)

    # Coarse check every 20 minutes (1 in 10 points)
    coarse_idx = np.arange(0, num_steps, 10)
    coarse_times = times[coarse_idx]

    # Observe Moon (coarse)
    mpos_coarse = observer.at(coarse_times).observe(moon).apparent()
    m_alt_coarse, _, m_dist_coarse = mpos_coarse.altaz()
    moon_rad_coarse = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist_coarse.km))

    # Sun altitude (coarse)
    sun_alts_coarse = (
        observer.at(coarse_times)
        .observe(sun)
        .apparent()
        .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
    )

    events = []

    from skyfield import almanac

    for p_idx, planet in enumerate(planet_objs):
        simple_name = simple_names[p_idx]

        # Observe Planet (coarse)
        ppos_coarse = observer.at(coarse_times).observe(planet).apparent()
        sep_coarse = mpos_coarse.separation_from(ppos_coarse).degrees

        # Potential: sep < rad + margin, Moon > 0, Sun <= -6
        potential_mask = (
            (sep_coarse < moon_rad_coarse + 0.2)
            & (m_alt_coarse.degrees > -1)
            & (sun_alts_coarse.degrees <= -5)
        )

        if not np.any(potential_mask):
            continue

        # Group potential coarse indices into contiguous windows
        potential_groups = np.split(
            np.where(potential_mask)[0], np.where(np.diff(np.where(potential_mask)[0]) > 1)[0] + 1
        )

        for group in potential_groups:
            # Create a time window around the coarse event
            w_start_idx = max(0, coarse_idx[group[0]] - 15)
            w_end_idx = min(num_steps - 1, coarse_idx[group[-1]] + 15)
            w_start_t = times[w_start_idx]
            w_end_t = times[w_end_idx]

            def is_occulted(t):
                m = observer.at(t).observe(moon).apparent()
                p = observer.at(t).observe(planet).apparent()
                sep = m.separation_from(p).degrees
                rad = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m.distance().km))
                alt, _, _ = m.altaz(temperature_C=10.0, pressure_mbar=1013.25)
                sun_alt = (
                    observer.at(t)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )
                return (sep < rad) & (alt.degrees > 0) & (sun_alt <= -6)

            setattr(is_occulted, "step_days", 0.005)
            t_occ, y_occ = almanac.find_discrete(w_start_t, w_end_t, is_occulted)

            t_list = list(t_occ)
            # If we started inside an occultation, add the window start
            if is_occulted(w_start_t):
                t_list.insert(0, w_start_t)
            # If we ended inside an occultation, add the window end
            if len(t_list) % 2 != 0:
                t_list.append(w_end_t)

            for i in range(0, len(t_list), 2):
                if i + 1 < len(t_list):
                    ingress_t = t_list[i]
                    egress_t = t_list[i + 1]
                    mid_t = ts.from_datetime(
                        ingress_t.utc_datetime()
                        + (egress_t.utc_datetime() - ingress_t.utc_datetime()) / 2
                    )
                    refined_t, _ = _refine_conjunction(observer, moon, planet, mid_t)

                    events.append(
                        {
                            "date": refined_t.utc_datetime(),
                            "object1": "Moon",
                            "object2": simple_name,
                            "ingress_time": ingress_t.utc_datetime(),
                            "egress_time": egress_t.utc_datetime(),
                            "type": "Lunar Planetary Occultation",
                            "event": "Lunar Planetary Occultation",
                        }
                    )
    return events
