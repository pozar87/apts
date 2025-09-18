from enum import Enum


class EventType(str, Enum):
    """
    An enumeration of the types of astronomical events that can be calculated.
    """

    MOON_PHASES = "moon_phases"
    CONJUNCTIONS = "conjunctions"
    OPPOSITIONS = "oppositions"
    METEOR_SHOWERS = "meteor_showers"
    HIGHEST_ALTITUDES = "highest_altitudes"
    LUNAR_OCCULTATIONS = "lunar_occultations"
    APHELION_PERIHELION = "aphelion_perihelion"
    MOON_APOGEE_PERIGEE = "moon_apogee_perigee"
    MERCURY_INFERIOR_CONJUNCTIONS = "mercury_inferior_conjunctions"
    MOON_MESSIER_CONJUNCTIONS = "moon_messier_conjunctions"
    SOLAR_ECLIPSES = "solar_eclipses"
    LUNAR_ECLIPSES = "lunar_eclipses"
    SPACE_LAUNCHES = "space_launches"
    SPACE_EVENTS = "space_events"
    ISS_FLYBYS = "iss_flybys"
    TIANGONG_FLYBYS = "tiangong_flybys"

    def __str__(self):
        return self.value
