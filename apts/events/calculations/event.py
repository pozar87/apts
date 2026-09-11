import logging
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

logger = logging.getLogger(__name__)
utc = timezone.utc


@dataclass
class DirectionData:
    """Represents cardinal/ordinal direction details for an event."""
    code: str  # e.g., "E"
    name: str  # e.g., "Look East"
    azimuth_deg: float  # e.g., 90.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "name": self.name,
            "azimuth_deg": round(float(self.azimuth_deg), 1),
        }


def get_sky_brightness(sun_alt_deg: float | None, moon_alt_deg: float | None = None, moon_phase_frac: float = 0.0) -> str:
    """
    Infers sky brightness classification state based on Sun and Moon altitude.

    Returns:
        One of 'DAY', 'CIVIL_TWILIGHT', 'NAUTICAL_TWILIGHT', 'ASTRONOMICAL_TWILIGHT',
        'NIGHT_MOONLIT', 'NIGHT_DARK'.
    """
    if sun_alt_deg is None:
        return "NIGHT_DARK"

    alt = float(sun_alt_deg)
    if alt >= -0.833:
        return "DAY"
    elif alt >= -6.0:
        return "CIVIL_TWILIGHT"
    elif alt >= -12.0:
        return "NAUTICAL_TWILIGHT"
    elif alt >= -18.0:
        return "ASTRONOMICAL_TWILIGHT"

    # Deep night: check Moon influence
    if moon_alt_deg is not None and moon_alt_deg > 0.0 and moon_phase_frac >= 0.2:
        return "NIGHT_MOONLIT"

    return "NIGHT_DARK"


def get_direction_data(azimuth_deg: float | None) -> DirectionData:
    """Converts an azimuth in degrees into cardinal direction code and description."""
    from apts.i18n import gettext_

    if azimuth_deg is None or math.isnan(azimuth_deg):
        return DirectionData(code="E", name=gettext_("Look East"), azimuth_deg=90.0)

    az = float(azimuth_deg) % 360.0

    directions = [
        (11.25, 33.75, "NNE", gettext_("Look North-Northeast")),
        (33.75, 56.25, "NE", gettext_("Look Northeast")),
        (56.25, 78.75, "ENE", gettext_("Look East-Northeast")),
        (78.75, 101.25, "E", gettext_("Look East")),
        (101.25, 123.75, "ESE", gettext_("Look East-Southeast")),
        (123.75, 146.25, "SE", gettext_("Look Southeast")),
        (146.25, 168.75, "SSE", gettext_("Look South-Southeast")),
        (168.75, 191.25, "S", gettext_("Look South")),
        (191.25, 213.75, "SSW", gettext_("Look South-Southwest")),
        (213.75, 236.25, "SW", gettext_("Look Southwest")),
        (236.25, 258.75, "WSW", gettext_("Look West-Southwest")),
        (258.75, 281.25, "W", gettext_("Look West")),
        (281.25, 303.75, "WNW", gettext_("Look West-Northwest")),
        (303.75, 326.25, "NW", gettext_("Look Northwest")),
        (326.25, 348.75, "NNW", gettext_("Look North-Northwest")),
    ]

    for low, high, code, name in directions:
        if low <= az < high:
            return DirectionData(code=code, name=name, azimuth_deg=az)

    # Wrap-around for North (348.75 to 360 / 0 to 11.25)
    return DirectionData(code="N", name=gettext_("Look North"), azimuth_deg=az)


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


def _get_flyby_or_launch_guide(cat: str, title_lower: str) -> list[str] | None:
    from apts.i18n import gettext_

    if cat in ("FLYBY", "ISS_FLYBY", "TIANGONG_FLYBY") or "flyby" in title_lower or "iss" in title_lower:
        return [
            gettext_("Find an open viewing location with a clear view of the sky in the pass direction."),
            gettext_("Check the exact rise time and direction before heading outside."),
            gettext_("Watch the horizon for a bright, steady, non-blinking point of light moving across the sky."),
            gettext_("Track the satellite visually with naked eye or wide-field binoculars."),
            gettext_("Note the time and peak altitude as it passes overhead."),
        ]
    if cat in ("ROCKET_LAUNCH", "SPACE_LAUNCH") or "launch" in title_lower or "rocket" in title_lower:
        return [
            gettext_("Confirm the launch schedule and trajectory azimuth prior to liftoff."),
            gettext_("Find an elevated or unobstructed location facing the launch direction."),
            gettext_("Look low near the horizon at T+2 to T+3 minutes for the rising exhaust plume."),
            gettext_("Use binoculars to spot stage separation or twilight expansion effects."),
        ]
    return None


def _get_observation_event_guide(cat: str, title_lower: str, obj_str: str) -> list[str] | None:
    from apts.i18n import gettext_

    if cat == "METEOR_SHOWER" or "shower" in title_lower or "meteor" in title_lower:
        return [
            gettext_("Choose a dark location away from city lights."),
            gettext_("Allow 20–30 minutes for your eyes to fully adapt to darkness."),
            gettext_("Lie back comfortably on a reclining chair facing the radiant direction."),
            gettext_("Observe with the naked eye for the widest field of view."),
            gettext_("Keep warm and count the number of meteors per hour."),
        ]
    if cat == "OCCULTATION":
        return [
            gettext_("Verify that the occultation is visible from your location."),
            gettext_("Arrive and set up equipment at least 15–30 minutes before the event."),
            gettext_("Focus carefully before the occultation begins."),
            gettext_("Watch continuously near the predicted disappearance time."),
            gettext_("If possible, record the event with a camera or video setup."),
        ]
    if cat == "CONJUNCTION":
        return [
            gettext_("Find an observing location with an unobstructed horizon in the specified direction."),
            gettext_("Set up binoculars or a telescope 15–20 minutes before peak alignment."),
            gettext_("Locate the brighter object first, then scan near it to find the companion."),
            gettext_("Observe both objects together within the same field of view."),
            gettext_("Capture wide-field photographs during twilight or dark sky hours."),
        ]
    if cat in ("PLANET_ALIGNMENT", "CELESTIAL_CONFIGURATION") or "alignment" in title_lower:
        return [
            gettext_("Find a site with a clear view spanning East to West along the ecliptic arc."),
            gettext_("Begin observing during early twilight as the brightest planets emerge."),
            gettext_("Scan along the ecliptic line to identify all participating planets."),
            gettext_("Use wide-angle camera gear or binoculars to capture the full parade."),
        ]
    return None


def _get_planetary_or_solar_guide(cat: str, title_lower: str) -> list[str] | None:
    from apts.i18n import gettext_

    if "jovian" in cat.lower() or "jovian" in title_lower or "grs" in title_lower or "jupiter" in title_lower:
        return [
            gettext_("Set up a telescope with medium-to-high magnification (100x–200x)."),
            gettext_("Allow your optical tube time to thermally stabilize outdoors."),
            gettext_("Locate Jupiter and identify the equatorial dark cloud bands."),
            gettext_("Observe the positions of the four Galilean moons (Io, Europa, Ganymede, Callisto)."),
            gettext_("Look for moon shadow transits or the Great Red Spot during peak visibility."),
        ]
    if cat == "SOLAR_ECLIPSE":
        return [
            gettext_("Ensure you have ISO-certified solar viewing glasses or solar filters."),
            gettext_("Inspect all solar filters for damage before looking at the Sun."),
            gettext_("Set up your viewing area in advance with a clear line of sight."),
            gettext_("Observe the progression of solar coverage safely."),
            gettext_("Never look directly at the Sun without approved solar filtration."),
        ]
    if cat == "LUNAR_ECLIPSE":
        return [
            gettext_("Find a comfortable viewing spot with a clear view of the Moon."),
            gettext_("No special eye protection is needed; binoculars or small telescopes enhance the view."),
            gettext_("Observe the gradual darkening and copper-red color shift during totality."),
            gettext_("Take long-exposure photographs as the Moon passes through Earth's umbra."),
        ]
    if cat == "OPPOSITION":
        return [
            gettext_("Plan your observation around midnight when the planet reaches its highest altitude."),
            gettext_("Use a telescope with moderate to high magnification for fine surface details."),
            gettext_("Allow your telescope to thermally acclimate to outdoor temperatures."),
            gettext_("Observe during periods of steady atmospheric seeing."),
        ]
    if cat == "TRANSIT":
        return [
            gettext_("Equip your optical setup with safe, dedicated solar filters."),
            gettext_("Track the ingress and egress times of the transit carefully."),
            gettext_("Use high magnification to resolve the silhouette against the solar disk."),
            gettext_("Record timestamped images throughout the transit progression."),
        ]
    if cat in ("GREATEST_ELONGATION", "VENUS_GREAT_BRILLIANCY"):
        return [
            gettext_("Locate the planet low near the horizon in early morning or evening twilight."),
            gettext_("Use binoculars or a small telescope to observe its crescent or gibbous phase."),
            gettext_("Observe before sunrise or after sunset when contrast is optimal."),
        ]
    if cat in ("MOON_PHASE", "SUPERMOON", "MOON_LIBRATION", "LUNAR_FEATURE"):
        return [
            gettext_("Choose a viewing spot with clear sky access toward the Moon."),
            gettext_("Use binoculars or a telescope along the lunar terminator line for shadow details."),
            gettext_("Observe prominent craters, mountain ranges, and maria surface features."),
        ]
    return None


def get_step_by_step_guide(category: str, title: str = "", objects: list[str] | None = None) -> list[str]:
    """Generates step-by-step observational guide instructions for an event."""
    from apts.i18n import gettext_

    cat = category.upper()
    title_lower = str(title).lower()
    obj_str = " or ".join([gettext_(o) for o in objects]) if objects else gettext_("target")

    flyby_guide = _get_flyby_or_launch_guide(cat, title_lower)
    if flyby_guide:
        return flyby_guide

    obs_guide = _get_observation_event_guide(cat, title_lower, obj_str)
    if obs_guide:
        return obs_guide

    planetary_guide = _get_planetary_or_solar_guide(cat, title_lower)
    if planetary_guide:
        return planetary_guide

    return [
        gettext_("Check local weather and cloud cover prior to the event."),
        gettext_("Locate {target} in the sky using cardinal directions and altitude.").format(target=obj_str),
        gettext_("Use appropriate optical aid (naked eye, binoculars, or telescope)."),
        gettext_("Observe near the predicted peak viewing time for the best view."),
    ]


def build_event_description(
    category: str,
    title: str,
    objects: list[str],
    datetime_utc_str: str,
    location_name: str,
    angular_separation: str | None = None,
) -> str:
    """Generates a narrative description for the event."""
    from apts.i18n import gettext_

    sep_text = f" {gettext_('with an angular separation of')} {angular_separation}" if angular_separation else ""
    o1 = gettext_(objects[0]) if len(objects) >= 1 else gettext_("Target")
    o2 = gettext_(objects[1]) if len(objects) >= 2 else gettext_("Companion")
    loc = gettext_(location_name)

    if category == "OCCULTATION" and len(objects) >= 2:
        return gettext_("The {object1} will pass directly in front of {object2}, creating a lunar occultation visible from {location} at {time}.").format(
            object1=o1, object2=o2, location=loc, time=datetime_utc_str
        )
    elif category == "CONJUNCTION" and len(objects) >= 2:
        return gettext_("{object1} and {object2} will share a close celestial conjunction{separation}, visible in the sky from {location}.").format(
            object1=o1, object2=o2, separation=sep_text, location=loc
        )
    elif category == "METEOR_SHOWER":
        shower_name = o1 if objects else title
        return gettext_("Peak activity for the {shower} meteor shower, offering optimal viewing conditions from {location}.").format(
            shower=shower_name, location=loc
        )
    else:
        return gettext_("{title} occurring on {time}, visible from {location}.").format(
            title=title, time=datetime_utc_str, location=loc
        )


def parse_event_datetime(data: dict[str, Any]) -> datetime:
    """Parses event UTC datetime from data dictionary."""
    raw_date = data.get("date") or data.get("datetime_utc") or datetime.now(utc)
    if isinstance(raw_date, str):
        try:
            clean_ts = raw_date.replace("Z", "+00:00")
            dt = datetime.fromisoformat(clean_ts)
        except ValueError:
            dt = datetime.now(utc)
    elif isinstance(raw_date, datetime):
        dt = raw_date
    elif hasattr(raw_date, "to_pydatetime"):
        dt = raw_date.to_pydatetime()
    else:
        dt = datetime.now(utc)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=utc)

    return dt.astimezone(utc)


def extract_event_objects(data: dict[str, Any]) -> list[str]:
    """Extracts involved celestial object names from event record dictionary."""
    objs = []
    if data.get("object1"):
        objs.append(str(data["object1"]))
    if data.get("object2"):
        objs.append(str(data["object2"]))
    if not objs and "object" in data and data["object"]:
        objs.append(str(data["object"]))
    if not objs and "shower_name" in data and data["shower_name"]:
        objs.append(str(data["shower_name"]))
    if not objs and "planets" in data and data["planets"]:
        p_val = data["planets"]
        if isinstance(p_val, list):
            objs.extend([str(p) for p in p_val])
        elif isinstance(p_val, str):
            objs.append(p_val)

    if not objs:
        event_name = str(data.get("event") or data.get("title") or "").lower()
        event_type = str(data.get("type") or "").lower()
        category = str(data.get("category") or get_event_category(event_name, event_type)).upper()

        moon_kws = ["moon", "quarter", "crescent", "gibbous", "full moon", "new moon", "księżyc", "mond", "luna", "libration", "supermoon", "lunar"]
        sun_kws = ["sun", "solstice", "equinox", "słońce", "sonne", "sol", "autumnal", "vernal", "equinoccio", "solsticio", "tagundnachtgleiche", "równonoc", "przesilenie"]

        if category in ("MOON_PHASE", "SUPERMOON", "MOON_LIBRATION", "LUNAR_FEATURE", "LUNAR_ECLIPSE") or any(kw in event_name or kw in event_type for kw in moon_kws):
            objs.append("Moon")
        elif category in ("EQUINOX_SOLSTICE", "SOLAR_ECLIPSE") or any(kw in event_name or kw in event_type for kw in sun_kws):
            objs.append("Sun")

    return objs


def build_event_title(data: dict[str, Any], objs: list[str], category: str, event_name: str) -> str:
    """Constructs display title for the event if explicit title is absent."""
    title = data.get("title")
    if title:
        return title

    if len(objs) >= 2 and category == "OCCULTATION":
        return f"{objs[0].title()} occultation of {objs[1].title()}"
    if len(objs) >= 2 and category == "CONJUNCTION":
        return f"Conjunction of {objs[0].title()} and {objs[1].title()}"
    if objs and category == "METEOR_SHOWER":
        return f"{objs[0]} Meteor Shower Peak"

    return str(event_name)


def format_angular_separation(data: dict[str, Any]) -> str | None:
    """Formats angular separation string from event dictionary."""
    angular_sep = data.get("angular_separation")
    if not angular_sep and "separation_degrees" in data and data["separation_degrees"] is not None:
        sep_val = float(data["separation_degrees"])
        if sep_val < 1.0:
            return f"{round(sep_val * 60.0, 1)}'"
        return f"{round(sep_val, 1)}°"
    return angular_sep


def extract_coordinates(data: dict[str, Any]) -> tuple[float | None, float | None]:
    """Extracts float azimuth and altitude degrees from event dictionary."""
    azimuth_deg = data.get("azimuth") or data.get("azimuth_deg")
    altitude_deg = data.get("altitude") or data.get("altitude_deg")
    return (
        float(azimuth_deg) if azimuth_deg is not None else None,
        float(altitude_deg) if altitude_deg is not None else None,
    )


def resolve_event_topocentric_position(
    place: Any,
    dt_utc: datetime,
    objects: list[str],
    sun_alt: float | None = None,
    moon_alt: float | None = None,
    azimuth_deg: float | None = None,
    altitude_deg: float | None = None,
) -> tuple[float | None, float | None, float | None, float | None]:
    """
    Resolves sun altitude, moon altitude, primary object altitude, and primary object azimuth
    from place topocentric observer if available.
    Returns (sun_alt, moon_alt, altitude_deg, azimuth_deg).
    """
    if place is not None and hasattr(place, "get_altitude"):
        try:
            t_sf = place.ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)
            if sun_alt is None:
                sun_alt = place.get_altitude(place.sun, t_sf)
                moon_alt = place.get_altitude(place.moon, t_sf)
            if (azimuth_deg is None or altitude_deg is None) and objects:
                alt_primary = place.get_altitude(objects[0], t_sf)
                az_primary = place.get_azimuth(objects[0], t_sf)
                if not math.isnan(alt_primary) and not math.isnan(az_primary):
                    altitude_deg = float(alt_primary)
                    azimuth_deg = float(az_primary)
        except (ValueError, KeyError, AttributeError, TypeError) as e:
            logger.debug(f"Could not resolve topocentric position for primary object: {e}")

    return sun_alt, moon_alt, altitude_deg, azimuth_deg
