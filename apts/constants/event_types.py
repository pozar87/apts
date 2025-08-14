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

    def __str__(self):
        return self.value
