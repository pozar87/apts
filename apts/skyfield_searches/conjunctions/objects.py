import numpy as np
from skyfield.api import Star

from ...cache import get_timescale
from ...catalogs.messier import get_messier_raw
from ...catalogs.stars import get_bright_stars_raw
from ...utils import planetary
from .stars import find_conjunctions_with_stars


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
    # Use the raw catalog (Catalogs.BRIGHT_STARS strips the technical columns)
    bright_stars = get_bright_stars_raw()
    v_ra_hours = bright_stars["ra_hours"].to_numpy()
    v_dec_degrees = bright_stars["dec_degrees"].to_numpy()
    star_names_all = bright_stars["Name"].to_numpy()

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
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    # Pre-filter Messier objects close to the ecliptic (within 10 degrees)
    # Planets stay within ~7 degrees of the ecliptic (e.g. Mercury), and threshold is 3.0 degrees.
    # Any object with absolute ecliptic latitude >= 10.0 degrees can never be in conjunction.
    ts = get_timescale()
    t_ref = ts.utc(start_date)

    # Use the raw catalog (Catalogs.MESSIER strips the technical columns)
    messier = get_messier_raw()
    v_ra_hours = messier["ra_hours"].to_numpy()
    v_dec_degrees = messier["dec_degrees"].to_numpy()
    messier_names_all = messier["Messier"].to_numpy()

    messier_vector_all = Star(ra_hours=v_ra_hours, dec_degrees=v_dec_degrees)
    spos_at_t_ref = observer.at(t_ref).observe(messier_vector_all)
    lats, _, _ = spos_at_t_ref.ecliptic_latlon()

    mask = np.abs(lats.degrees) < 10.0

    messier_names_filtered = messier_names_all[mask]
    messier_vector_filtered = Star(
        ra_hours=v_ra_hours[mask], dec_degrees=v_dec_degrees[mask]
    )

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        # 3.0 degrees threshold for planet-DSO conjunctions
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            star_data=messier_vector_filtered,
            start_date=start_date,
            end_date=end_date,
            threshold_degrees=3.0,
            precomputed_positions=precomputed_positions,
            star_names=messier_names_filtered,
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
