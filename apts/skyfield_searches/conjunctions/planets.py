import numpy as np
from skyfield.searchlib import find_minima
from ...cache import get_timescale
from ...constants import astronomy
from ...utils import planetary
from ..utils import _refine_conjunction
from .base import find_conjunctions

def find_mercury_inferior_conjunctions(
    observer, start_date, end_date, threshold_degrees=1.0
):
    conjunctions = find_conjunctions(
        observer, "mercury", "sun", start_date, end_date, threshold_degrees
    )

    mercury = planetary.get_skyfield_obj("mercury")
    sun = planetary.get_skyfield_obj("sun")
    ts = get_timescale()

    inferior_events = []
    for event in conjunctions:
        t = ts.from_datetime(event["date"])
        mercury_obs = observer.at(t).observe(mercury)
        sun_obs = observer.at(t).observe(sun)

        mercury_dist = mercury_obs.distance().au
        sun_dist = sun_obs.distance().au

        if mercury_dist < sun_dist:
            # It is an inferior conjunction
            # Calculate angular radii
            mercury_angular_radius = np.degrees(
                np.arctan2(astronomy.MERCURY_RADIUS_KM / astronomy.AU_KM, mercury_dist)
            )
            sun_angular_radius = np.degrees(
                np.arctan2(astronomy.SUN_RADIUS_KM / astronomy.AU_KM, sun_dist)
            )

            event["is_transit"] = event["separation_degrees"] < (
                mercury_angular_radius + sun_angular_radius
            )
            inferior_events.append(event)

    return inferior_events

def find_planet_solar_conjunctions(observer, start_date, end_date, threshold_degrees=2.0):
    """
    Finds conjunctions between planets and the Sun.
    Distinguishes between inferior and superior conjunctions for inner planets.
    """
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    conjunctions = []
    for p_name in planets:
        planet_conjs = find_conjunctions(
            observer, p_name, "sun", start_date, end_date, threshold_degrees
        )
        simple_name = planetary.get_simple_name(p_name)

        for conj in planet_conjs:
            t = get_timescale().from_datetime(conj["date"])
            p_obj = planetary.get_skyfield_obj(p_name)
            sun_obj = planetary.get_skyfield_obj("sun")

            # Get distances to determine conjunction type
            p_dist = observer.at(t).observe(p_obj).distance().au
            sun_dist = observer.at(t).observe(sun_obj).distance().au

            if p_name in ["mercury", "venus"]:
                if p_dist < sun_dist:
                    kind = "Inferior Conjunction"
                    # Oracle: check for transit during inferior conjunction
                    p_rad = np.degrees(
                        np.arctan2(planetary.get_planet_radius_km(p_name) / astronomy.AU_KM, p_dist)
                    )
                    s_rad = np.degrees(
                        np.arctan2(astronomy.SUN_RADIUS_KM / astronomy.AU_KM, sun_dist)
                    )
                    is_transit = conj["separation_degrees"] < (p_rad + s_rad)
                else:
                    kind = "Superior Conjunction"
                    is_transit = False
            else:
                kind = "Conjunction"
                is_transit = False

            event_name = f"{simple_name} Solar {kind}"
            if is_transit:
                event_name += " (Transit)"

            conj.update(
                {
                    "event": event_name,
                    "object1": simple_name,
                    "object2": "Sun",
                    "type": "Planet Solar Conjunction",
                    "conjunction_kind": kind,
                    "is_transit": is_transit,
                }
            )
            conjunctions.append(conj)

    return conjunctions

def find_planet_planet_occultations(observer, start_date, end_date):
    """
    Finds occultations of one planet by another.
    Extremely rare events.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
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
    # Check all pairs of planets
    for i, p1_name in enumerate(planets):
        for p2_name in planets[i + 1 :]:
            p1_obj = planetary.get_skyfield_obj(p1_name)
            p2_obj = planetary.get_skyfield_obj(p2_name)

            def separation(t):
                # Use topocentric apparent positions
                # Optimization: for coarse search, we could use .observe()
                p1_obs = observer.at(t).observe(p1_obj).apparent()
                p2_obs = observer.at(t).observe(p2_obj).apparent()
                sep = p1_obs.separation_from(p2_obs).degrees

                # Calculate angular radii
                r1 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p1_name) / p1_obs.distance().km
                    )
                )
                r2 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p2_name) / p2_obs.distance().km
                    )
                )

                return sep - (r1 + r2)

            # Step of 0.5 days is safe for these slow events
            setattr(separation, "step_days", 0.5)
            times, _ = find_minima(t0, t1, separation)

            for t in times:
                # Refine
                refined_t, refined_sep = _refine_conjunction(observer, p1_obj, p2_obj, t)

                p1_obs = observer.at(refined_t).observe(p1_obj).apparent()
                p2_obs = observer.at(refined_t).observe(p2_obj).apparent()

                r1 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p1_name) / p1_obs.distance().km
                    )
                )
                r2 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p2_name) / p2_obs.distance().km
                    )
                )

                if refined_sep < (r1 + r2):
                    # Determine which planet is in front
                    if p1_obs.distance().km < p2_obs.distance().km:
                        occulting = planetary.get_simple_name(p1_name)
                        occulted = planetary.get_simple_name(p2_name)
                    else:
                        occulting = planetary.get_simple_name(p2_name)
                        occulted = planetary.get_simple_name(p1_name)

                    events.append(
                        {
                            "date": refined_t.utc_datetime(),
                            "event": f"{occulting} occults {occulted}",
                            "object1": occulting,
                            "object2": occulted,
                            "separation_degrees": float(refined_sep),
                            "type": "Planet-Planet Occultation",
                        }
                    )
    return events
