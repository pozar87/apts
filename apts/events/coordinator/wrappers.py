
from ...catalogs.messier import get_messier_raw
from ...catalogs.stars import get_bright_stars_raw
from ..calculations import lunar, sky, space
from ..calculations import planetary as planetary_calc


class EventCalculationWrappers:
    """
    Mixin providing calculation delegation wrapper methods for AstronomicalEvents.
    Maintained for backward compatibility and clean dispatching.
    """

    def calculate_venus_greatest_brilliancy(self):
        return planetary_calc.calculate_venus_greatest_brilliancy(
            self.observer, self.start_date, self.end_date
        )

    def calculate_space_launches(self):
        return space.calculate_space_launches(self.start_date, self.end_date)

    def calculate_space_events(self):
        return space.calculate_space_events(self.start_date, self.end_date)

    def calculate_iss_flybys(self):
        return space.calculate_iss_flybys(
            self.place, self.observer, self.start_date, self.end_date
        )

    def calculate_tiangong_flybys(self):
        return space.calculate_tiangong_flybys(
            self.place, self.observer, self.start_date, self.end_date
        )

    def calculate_solar_eclipses(self):
        return sky.calculate_solar_eclipses(
            self.observer, self.start_date, self.end_date
        )

    def calculate_lunar_eclipses(self):
        return lunar.calculate_lunar_eclipses(
            self.observer, self.start_date, self.end_date
        )

    def calculate_moon_phases(self):
        return lunar.calculate_moon_phases(
            self.ts, self.start_date, self.end_date, self.eph
        )

    def calculate_conjunctions(self, precomputed_positions=None):
        return planetary_calc.calculate_conjunctions(
            self.ts,
            self.observer,
            self.start_date,
            self.end_date,
            self.executor,
            precomputed_positions,
        )

    def calculate_oppositions(self):
        return planetary_calc.calculate_oppositions(
            self.observer, self.start_date, self.end_date, self.executor
        )

    def calculate_meteor_showers(self):
        return sky.calculate_meteor_showers(
            self.observer, self.start_date, self.end_date
        )

    def calculate_highest_altitudes(self):
        return planetary_calc.calculate_highest_altitudes(
            self.observer, self.start_date, self.end_date, self.executor
        )

    def calculate_lunar_occultations(self):
        return lunar.calculate_lunar_occultations(
            self.observer, self.start_date, self.end_date, get_bright_stars_raw()
        )

    def calculate_lunar_planetary_occultations(self):
        return lunar.calculate_lunar_planetary_occultations(
            self.observer, self.start_date, self.end_date
        )

    def calculate_aphelion_perihelion(self):
        return planetary_calc.calculate_aphelion_perihelion(
            self.start_date, self.end_date, self.executor
        )

    def calculate_moon_apogee_perigee(self):
        return lunar.calculate_moon_apogee_perigee(self.start_date, self.end_date)

    def calculate_mercury_inferior_conjunctions(self):
        return planetary_calc.calculate_mercury_inferior_conjunctions(
            self.observer, self.start_date, self.end_date
        )

    def calculate_moon_messier_conjunctions(self, precomputed_positions=None):
        return lunar.calculate_moon_messier_conjunctions(
            self.observer,
            self.start_date,
            self.end_date,
            get_messier_raw(),
            precomputed_positions,
        )

    def calculate_moon_star_conjunctions(self, precomputed_positions=None):
        return lunar.calculate_moon_star_conjunctions(
            self.ts,
            self.observer,
            self.start_date,
            self.end_date,
            get_bright_stars_raw(),
            precomputed_positions,
        )

    def calculate_nasa_comets(self):
        return sky.calculate_nasa_comets(self.start_date, self.end_date)

    def calculate_planet_alignments(self):
        return planetary_calc.calculate_planet_alignments(
            self.observer, self.start_date, self.end_date
        )

    def calculate_golden_blue_hours(self):
        return sky.calculate_golden_blue_hours(
            self.observer, self.start_date, self.end_date, self.event_settings
        )

    def calculate_culminations(self):
        return sky.calculate_culminations(
            self.observer, self.start_date, self.end_date
        )

    def calculate_messier_culminations(self):
        return sky.calculate_messier_culminations(
            self.observer, self.start_date, self.end_date, get_messier_raw()
        )

    def calculate_jovian_moon_events(self):
        return planetary_calc.calculate_jovian_moon_events(
            self.observer, self.start_date, self.end_date
        )

    def calculate_saturn_ring_crossings(self):
        return planetary_calc.calculate_saturn_ring_crossings(
            self.start_date, self.end_date
        )

    def calculate_greatest_elongations(self):
        return planetary_calc.calculate_greatest_elongations(
            self.observer, self.start_date, self.end_date
        )

    def calculate_planetary_dichotomy(self, precomputed_positions=None):
        return planetary_calc.calculate_planetary_dichotomy(
            self.observer, self.start_date, self.end_date, precomputed_positions
        )

    def calculate_seasons(self):
        return sky.calculate_seasons(self.start_date, self.end_date)

    def calculate_planet_messier_conjunctions(self, precomputed_positions=None):
        return planetary_calc.calculate_planet_messier_conjunctions(
            self.observer, self.start_date, self.end_date, precomputed_positions
        )

    def calculate_jupiter_grs_transits(self, grs_longitude: float | None = None):
        return planetary_calc.calculate_jupiter_grs_transits(
            self.observer, self.start_date, self.end_date, grs_longitude
        )

    def calculate_planet_star_conjunctions(self, precomputed_positions=None):
        return planetary_calc.calculate_planet_star_conjunctions(
            self.observer, self.start_date, self.end_date, precomputed_positions
        )

    def calculate_planet_stationary_points(self):
        return planetary_calc.calculate_planet_stationary_points(
            self.observer, self.start_date, self.end_date, self.executor
        )

    def calculate_planet_solar_conjunctions(self):
        return planetary_calc.calculate_planet_solar_conjunctions(
            self.observer, self.start_date, self.end_date
        )

    def calculate_lunar_features(self):
        return lunar.calculate_lunar_features(
            self.observer, self.start_date, self.end_date
        )

    def calculate_moon_libration_maxima(self):
        return lunar.calculate_moon_libration_maxima(
            self.observer, self.start_date, self.end_date
        )

    def calculate_planet_planet_occultations(self):
        return planetary_calc.calculate_planet_planet_occultations(
            self.observer, self.start_date, self.end_date
        )

    def calculate_supermoons(self):
        return lunar.calculate_supermoons(self.start_date, self.end_date)

    def calculate_mars_closest_approach(self):
        return planetary_calc.calculate_mars_closest_approach(
            self.observer, self.start_date, self.end_date
        )

    def calculate_jovian_mutual_events(self):
        return planetary_calc.calculate_jovian_mutual_events(
            self.observer, self.start_date, self.end_date
        )

    def calculate_celestial_configurations(self):
        return planetary_calc.calculate_celestial_configurations(
            self.observer, self.start_date, self.end_date
        )
