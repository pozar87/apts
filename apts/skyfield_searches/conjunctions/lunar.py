import numpy as np
from ...cache import get_timescale
from ...constants import astronomy
from ...utils import planetary
from ..utils import _refine_conjunction

def find_lunar_planetary_occultations(observer, start_date, end_date):
    """
    Finds occultations of planets by the Moon for a specific observer.
    Provides precise ingress and egress times.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")

    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    events = []

    sun = planetary.get_skyfield_obj("sun")

    for p_name in planets:
        planet = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)

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

        from skyfield import almanac
        setattr(is_occulted, "step_days", 0.005)
        t_occ, y_occ = almanac.find_discrete(t0, t1, is_occulted)

        # Handle cases where the occultation starts before t0 or ends after t1
        t_list = list(t_occ)
        if is_occulted(t0):
            t_list.insert(0, t0)

        if len(t_list) % 2 != 0:
            t_list.append(t1)

        for i in range(0, len(t_list), 2):
            if i + 1 < len(t_list):
                ingress_t = t_list[i]
                egress_t = t_list[i + 1]
                # Mid-point for conjunction refinement if needed
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
