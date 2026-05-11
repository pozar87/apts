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

    # Optimized filtering: avoid iterative ra/dec extraction
    v_ra_hours = catalogs.BRIGHT_STARS["ra_hours"].to_numpy()
    v_dec_degrees = catalogs.BRIGHT_STARS["dec_degrees"].to_numpy()
    star_names_all = catalogs.BRIGHT_STARS["Name"].to_numpy()

    stars_vector_all = Star(ra_hours=v_ra_hours, dec_degrees=v_dec_degrees)
    spos_at_t_ref = observer.at(t_ref).observe(stars_vector_all)
    lats, _, _ = spos_at_t_ref.ecliptic_latlon()

    # Planets stay within ~7 degrees of the ecliptic (except Pluto, which is not in this list)
    mask = np.abs(lats.degrees) < 7.0

    # Filtered vectorized Star object
    star_data_filtered = Star(
        ra_hours=v_ra_hours[mask], dec_degrees=v_dec_degrees[mask]
    )
    star_names_filtered = star_names_all[mask]

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            star_data=star_data_filtered,
            start_date=start_date,
            end_date=end_date,
            threshold_degrees=threshold_degrees,
            precomputed_positions=precomputed_positions,
            star_names=star_names_filtered,
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

    # Optimized path: avoid iterative Star object conversion and coordinate extraction.
    # We use pre-calculated float coordinates to create a single vectorized Star object.
    messier_names = catalogs.MESSIER["Messier"].to_numpy()
    messier_vector = Star(
        ra_hours=catalogs.MESSIER["ra_hours"].to_numpy(),
        dec_degrees=catalogs.MESSIER["dec_degrees"].to_numpy(),
    )

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        # 3.0 degrees threshold for planet-DSO conjunctions
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            star_data=messier_vector,
            start_date=start_date,
            end_date=end_date,
            threshold_degrees=3.0,
            precomputed_positions=precomputed_positions,
            star_names=messier_names,
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
