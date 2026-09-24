CATEGORY_RULES = [
    ("occultation", None, "OCCULTATION"),
    (None, "occultation", "OCCULTATION"),
    ("conjunction", None, "CONJUNCTION"),
    (None, "conjunction", "CONJUNCTION"),
    ("lunar eclipse", None, "LUNAR_ECLIPSE"),
    ("solar eclipse", None, "SOLAR_ECLIPSE"),
    ("eclipse", None, "SOLAR_ECLIPSE"),
    ("meteor shower", None, "METEOR_SHOWER"),
    ("shower", None, "METEOR_SHOWER"),
    (None, "meteor", "METEOR_SHOWER"),
    ("opposition", None, "OPPOSITION"),
    ("transit", None, "TRANSIT"),
    ("alignment", None, "PLANET_ALIGNMENT"),
    ("flyby", None, "FLYBY"),
    ("iss", None, "FLYBY"),
    ("tiangong", None, "FLYBY"),
    ("launch", None, "ROCKET_LAUNCH"),
    ("rocket", None, "ROCKET_LAUNCH"),
    ("start kosmiczny", None, "ROCKET_LAUNCH"),
    ("start", None, "ROCKET_LAUNCH"),
    ("falcon", None, "ROCKET_LAUNCH"),
    ("vega", None, "ROCKET_LAUNCH"),
    ("sentinel", None, "ROCKET_LAUNCH"),
    ("crew-", None, "ROCKET_LAUNCH"),
    (None, "launch", "ROCKET_LAUNCH"),
    (None, "rocket", "ROCKET_LAUNCH"),
    ("solstice", None, "EQUINOX_SOLSTICE"),
    ("equinox", None, "EQUINOX_SOLSTICE"),
    ("season", None, "EQUINOX_SOLSTICE"),
    ("moon phase", None, "MOON_PHASE"),
    (None, "moon phase", "MOON_PHASE"),
    (None, "moon_phases", "MOON_PHASE"),
    ("first quarter", None, "MOON_PHASE"),
    ("third quarter", None, "MOON_PHASE"),
    ("last quarter", None, "MOON_PHASE"),
    ("new moon", None, "MOON_PHASE"),
    ("full moon", None, "MOON_PHASE"),
    ("supermoon", None, "SUPERMOON"),
    ("libration", None, "MOON_LIBRATION"),
    ("lunar feature", None, "LUNAR_FEATURE"),
]


def get_event_category(event_name: str, event_type: str = "") -> str:
    """Infers standard uppercase event category from event name and type."""
    name_lower = str(event_name).lower()
    type_lower = str(event_type).lower()

    for name_kw, type_kw, category in CATEGORY_RULES:
        if name_kw and name_kw in name_lower:
            return category
        if type_kw and type_kw in type_lower:
            return category

    return "CELESTIAL_EVENT"
