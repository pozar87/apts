from typing import Any, Callable, Dict, Optional


def build_event_dispatch_map(
    events_obj: Any, precomputed: Optional[Dict[str, Any]] = None
) -> Dict[str, Callable[[], Any]]:
    """
    Builds the event calculation dispatch mapping for an AstronomicalEvents instance.
    """
    return {
        "moon_phases": events_obj.calculate_moon_phases,
        "conjunctions": lambda: events_obj.calculate_conjunctions(precomputed),
        "oppositions": events_obj.calculate_oppositions,
        "meteor_showers": events_obj.calculate_meteor_showers,
        "highest_altitudes": events_obj.calculate_highest_altitudes,
        "lunar_occultations": events_obj.calculate_lunar_occultations,
        "aphelion_perihelion": events_obj.calculate_aphelion_perihelion,
        "moon_apogee_perigee": events_obj.calculate_moon_apogee_perigee,
        "mercury_inferior_conjunctions": events_obj.calculate_mercury_inferior_conjunctions,
        "moon_messier_conjunctions": lambda: events_obj.calculate_moon_messier_conjunctions(
            precomputed
        ),
        "moon_star_conjunctions": lambda: events_obj.calculate_moon_star_conjunctions(
            precomputed
        ),
        "space_launches": events_obj.calculate_space_launches,
        "space_events": events_obj.calculate_space_events,
        "iss_flybys": events_obj.calculate_iss_flybys,
        "tiangong_flybys": events_obj.calculate_tiangong_flybys,
        "solar_eclipses": events_obj.calculate_solar_eclipses,
        "lunar_eclipses": events_obj.calculate_lunar_eclipses,
        "nasa_comets": events_obj.calculate_nasa_comets,
        "planet_alignments": events_obj.calculate_planet_alignments,
        "lunar_planetary_occultations": events_obj.calculate_lunar_planetary_occultations,
        "messier_culminations": events_obj.calculate_messier_culminations,
        "jovian_moon_events": events_obj.calculate_jovian_moon_events,
        "saturn_ring_crossings": events_obj.calculate_saturn_ring_crossings,
        "jupiter_grs_transits": events_obj.calculate_jupiter_grs_transits,
        "planet_messier_conjunctions": lambda: events_obj.calculate_planet_messier_conjunctions(
            precomputed
        ),
        "planet_star_conjunctions": lambda: events_obj.calculate_planet_star_conjunctions(
            precomputed
        ),
        "planet_stationary_points": events_obj.calculate_planet_stationary_points,
        "planet_solar_conjunctions": events_obj.calculate_planet_solar_conjunctions,
        "lunar_features": events_obj.calculate_lunar_features,
        "moon_libration_maxima": events_obj.calculate_moon_libration_maxima,
        "planet_planet_occultations": events_obj.calculate_planet_planet_occultations,
        "venus_great_brilliancy": events_obj.calculate_venus_greatest_brilliancy,
        "supermoons": events_obj.calculate_supermoons,
        "mars_closest_approach": events_obj.calculate_mars_closest_approach,
        "jovian_mutual_events": events_obj.calculate_jovian_mutual_events,
        "greatest_elongations": events_obj.calculate_greatest_elongations,
        "planetary_dichotomy": lambda: events_obj.calculate_planetary_dichotomy(
            precomputed
        ),
        "seasons": events_obj.calculate_seasons,
        "culminations": events_obj.calculate_culminations,
        "celestial_configurations": events_obj.calculate_celestial_configurations,
    }
