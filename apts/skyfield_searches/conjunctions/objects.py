import numpy as np
from skyfield.api import Star
from ...cache import get_timescale
from ...utils import planetary
from .base import find_conjunctions_with_stars

def find_planet_star_conjunctions(
    observer,
    start_date,
    end_date,
    threshold_degrees=2.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between major planets and bright stars.
    Vectorized over stars for each planet for high performance.
    """
    from ...catalogs import Catalogs

    catalogs = Catalogs()
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    # Filter stars close to the ecliptic (within 10 degrees)
    # The planets stay close to the ecliptic (mostly within 7 degrees)
    ts = get_timescale()
    t_ref = ts.utc(start_date)

    star_objs_all = catalogs.BRIGHT_STARS["skyfield_object"].tolist()
    star_names_all = catalogs.BRIGHT_STARS["Name"].tolist()

    stars_vector = Star(
        ra_hours=np.array([s.ra.hours for s in star_objs_all]),
        dec_degrees=np.array([s.dec.degrees for s in star_objs_all]),
    )
    spos_at_t_ref = observer.at(t_ref).observe(stars_vector)
    lats, _, _ = spos_at_t_ref.ecliptic_latlon()

    # Planets stay within ~7 degrees of the ecliptic (except Pluto, which is not in this list)
    mask = np.abs(lats.degrees) < 7.0
    star_data = [(star_names_all[i], star_objs_all[i]) for i in np.where(mask)[0]]

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            star_data,
            start_date,
            end_date,
            threshold_degrees=threshold_degrees,
            precomputed_positions=precomputed_positions,
        )
        for conj in conjunctions:
            events.append(
                {
                    "date": conj["date"],
                    "event": "Conjunction",
                    "object1": simple_name,
                    "object2": conj["object2"],
                    "separation_degrees": conj["separation_degrees"],
                    "type": "Planet-Star Conjunction",
                }
            )

    return events

def find_planet_messier_conjunctions(
    observer, start_date, end_date, precomputed_positions=None
):
    """Finds conjunctions between major planets and Messier objects."""
    from ...catalogs import Catalogs

    catalogs = Catalogs()
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    # Optimization: replace iterrows() with zip() for better performance
    messier_data = list(
        zip(catalogs.MESSIER["Messier"], catalogs.MESSIER["skyfield_object"])
    )

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        # 3.0 degrees threshold for planet-DSO conjunctions
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            messier_data,
            start_date,
            end_date,
            threshold_degrees=3.0,
            precomputed_positions=precomputed_positions,
        )
        for conj in conjunctions:
            events.append(
                {
                    "date": conj["date"],
                    "event": "Conjunction",
                    "object1": simple_name,
                    "object2": conj["object2"],
                    "separation_degrees": conj["separation_degrees"],
                    "type": "Planet-Messier Conjunction",
                }
            )
    return events
