import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from apts.place import Place

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


def get_direction_data(azimuth_deg: float | None) -> DirectionData:
    """Converts an azimuth in degrees into cardinal direction code and description."""
    if azimuth_deg is None or math.isnan(azimuth_deg):
        return DirectionData(code="E", name="Look East", azimuth_deg=90.0)

    az = float(azimuth_deg) % 360.0

    directions = [
        (11.25, 33.75, "NNE", "Look North-Northeast"),
        (33.75, 56.25, "NE", "Look Northeast"),
        (56.25, 78.75, "ENE", "Look East-Northeast"),
        (78.75, 101.25, "E", "Look East"),
        (101.25, 123.75, "ESE", "Look East-Southeast"),
        (123.75, 146.25, "SE", "Look Southeast"),
        (146.25, 168.75, "SSE", "Look South-Southeast"),
        (168.75, 191.25, "S", "Look South"),
        (191.25, 213.75, "SSW", "Look South-Southwest"),
        (213.75, 236.25, "SW", "Look Southwest"),
        (236.25, 258.75, "WSW", "Look West-Southwest"),
        (258.75, 281.25, "W", "Look West"),
        (281.25, 303.75, "WNW", "Look West-Northwest"),
        (303.75, 326.25, "NW", "Look Northwest"),
        (326.25, 348.75, "NNW", "Look North-Northwest"),
    ]

    for low, high, code, name in directions:
        if low <= az < high:
            return DirectionData(code=code, name=name, azimuth_deg=az)

    # Wrap-around for North (348.75 to 360 / 0 to 11.25)
    return DirectionData(code="N", name="Look North", azimuth_deg=az)


def get_event_category(event_name: str, event_type: str = "") -> str:
    """Infers standard uppercase event category from event name and type."""
    name_lower = str(event_name).lower()
    type_lower = str(event_type).lower()

    if "occultation" in name_lower or "occultation" in type_lower:
        return "OCCULTATION"
    if "conjunction" in name_lower or "conjunction" in type_lower:
        return "CONJUNCTION"
    if "lunar eclipse" in name_lower:
        return "LUNAR_ECLIPSE"
    if "solar eclipse" in name_lower or "eclipse" in name_lower:
        return "SOLAR_ECLIPSE"
    if "meteor shower" in name_lower or "shower" in name_lower or "meteor" in type_lower:
        return "METEOR_SHOWER"
    if "opposition" in name_lower:
        return "OPPOSITION"
    if "transit" in name_lower:
        return "TRANSIT"
    if "alignment" in name_lower:
        return "PLANET_ALIGNMENT"
    if "flyby" in name_lower or "iss" in name_lower or "tiangong" in name_lower or "launch" in name_lower:
        return "FLYBY"
    if "solstice" in name_lower or "equinox" in name_lower or "season" in name_lower:
        return "EQUINOX_SOLSTICE"

    return "CELESTIAL_EVENT"


def get_step_by_step_guide(category: str, title: str = "", objects: list[str] | None = None) -> list[str]:
    """Generates step-by-step observational guide instructions for an event."""
    cat = category.upper()
    obj_str = " or ".join(objects) if objects else "target"

    if cat == "OCCULTATION":
        return [
            "Verify that the occultation is visible from your location.",
            "Arrive and set up equipment at least 15–30 minutes before the event.",
            "Focus carefully before the occultation begins.",
            "Watch continuously near the predicted disappearance time.",
            "If possible, record the event with a camera or video setup.",
        ]
    elif cat == "CONJUNCTION":
        return [
            "Find an observing location with an unobstructed horizon in the specified direction.",
            "Set up binoculars or a telescope 15–20 minutes before peak alignment.",
            "Locate the brighter object first, then scan near it to find the companion.",
            "Observe both objects together within the same field of view.",
            "Capture wide-field photographs during twilight or dark sky hours.",
        ]
    elif cat == "METEOR_SHOWER":
        return [
            "Choose a dark location away from city lights.",
            "Allow 20–30 minutes for your eyes to fully adapt to darkness.",
            "Lie back comfortably on a reclining chair facing the radiant direction.",
            "Observe with the naked eye for the widest field of view.",
            "Keep warm and count the number of meteors per hour.",
        ]
    elif cat == "SOLAR_ECLIPSE":
        return [
            "Ensure you have ISO-certified solar viewing glasses or solar filters.",
            "Inspect all solar filters for damage before looking at the Sun.",
            "Set up your viewing area in advance with a clear line of sight.",
            "Observe the progression of solar coverage safely.",
            "Never look directly at the Sun without approved solar filtration.",
        ]
    elif cat == "LUNAR_ECLIPSE":
        return [
            "Find a comfortable viewing spot with a clear view of the Moon.",
            "No special eye protection is needed; binoculars or small telescopes enhance the view.",
            "Observe the gradual darkening and copper-red color shift during totality.",
            "Take long-exposure photographs as the Moon passes through Earth's umbra.",
        ]
    elif cat == "OPPOSITION":
        return [
            "Plan your observation around midnight when the planet reaches its highest altitude.",
            "Use a telescope with moderate to high magnification for fine surface details.",
            "Allow your telescope to thermally acclimate to outdoor temperatures.",
            "Observe during periods of steady atmospheric seeing.",
        ]
    elif cat == "TRANSIT":
        return [
            "Equip your optical setup with safe, dedicated solar filters.",
            "Track the ingress and egress times of the transit carefully.",
            "Use high magnification to resolve the silhouette against the solar disk.",
            "Record timestamped images throughout the transit progression.",
        ]
    else:
        return [
            "Check local weather and cloud cover prior to the event.",
            f"Locate {obj_str} in the sky using cardinal directions and altitude.",
            "Use appropriate optical aid (naked eye, binoculars, or telescope).",
            "Observe near the predicted peak viewing time for the best view.",
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
    sep_text = f" with an angular separation of {angular_separation}" if angular_separation else ""

    if category == "OCCULTATION" and len(objects) >= 2:
        return (
            f"The {objects[0]} will pass directly in front of {objects[1]}, creating a lunar occultation "
            f"visible from {location_name} at {datetime_utc_str}."
        )
    elif category == "CONJUNCTION" and len(objects) >= 2:
        return (
            f"{objects[0]} and {objects[1]} will share a close celestial conjunction{sep_text}, "
            f"visible in the sky from {location_name}."
        )
    elif category == "METEOR_SHOWER":
        shower_name = objects[0] if objects else title
        return (
            f"Peak activity for the {shower_name} meteor shower, offering optimal viewing conditions "
            f"from {location_name}."
        )
    else:
        return f"{title} occurring on {datetime_utc_str}, visible from {location_name}."


@dataclass
class EventExportData:
    """DTO matching the Stargazer Earth JSON schema specification."""
    category: str
    title: str
    datetime_utc: str
    best_viewing_time_local: str
    location_name: str
    description: str
    angular_separation: str | None
    direction: DirectionData
    step_by_step_guide: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "category": self.category,
            "title": self.title,
            "datetime_utc": self.datetime_utc,
            "best_viewing_time_local": self.best_viewing_time_local,
            "location_name": self.location_name,
            "description": self.description,
            "angular_separation": self.angular_separation,
            "direction": self.direction.to_dict() if isinstance(self.direction, DirectionData) else self.direction,
            "step_by_step_guide": self.step_by_step_guide,
        }


class Event:
    """
    Represents an astronomical event in apts, encapsulating both metadata and
    visualization capabilities for Stargazer integration.
    """

    def __init__(
        self,
        category: str,
        title: str,
        datetime_utc: datetime | str,
        best_viewing_time_local: str,
        location_name: str = "Observer Location",
        description: str = "",
        angular_separation: str | None = None,
        direction: DirectionData | dict[str, Any] | None = None,
        azimuth_deg: float | None = None,
        altitude_deg: float | None = None,
        step_by_step_guide: list[str] | None = None,
        objects: list[str] | None = None,
        place: Optional["Place"] = None,
        extra_data: dict[str, Any] | None = None,
    ):
        if isinstance(datetime_utc, datetime):
            if datetime_utc.tzinfo is None:
                datetime_utc = datetime_utc.replace(tzinfo=utc)
            self.dt_utc = datetime_utc.astimezone(utc)
            self.datetime_utc = self.dt_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            self.datetime_utc = str(datetime_utc)
            try:
                # Parse ISO timestamp
                clean_ts = self.datetime_utc.replace("Z", "+00:00")
                self.dt_utc = datetime.fromisoformat(clean_ts).astimezone(utc)
            except ValueError:
                self.dt_utc = datetime.now(utc)

        self.category = category
        self.title = title
        self.best_viewing_time_local = best_viewing_time_local
        self.location_name = location_name
        self.objects = objects or []
        self.angular_separation = angular_separation
        self.altitude_deg = altitude_deg
        self.azimuth_deg = azimuth_deg
        self.place = place
        self.extra_data = extra_data or {}

        # Handle Direction
        if isinstance(direction, DirectionData):
            self.direction = direction
        elif isinstance(direction, dict):
            self.direction = DirectionData(
                code=direction.get("code", "E"),
                name=direction.get("name", "Look East"),
                azimuth_deg=float(direction.get("azimuth_deg", azimuth_deg if azimuth_deg is not None else 90.0)),
            )
        else:
            self.direction = get_direction_data(azimuth_deg)

        # Handle Step-by-step guide
        if step_by_step_guide:
            self.step_by_step_guide = step_by_step_guide
        else:
            self.step_by_step_guide = get_step_by_step_guide(self.category, self.title, self.objects)

        # Handle Description
        if description:
            self.description = description
        else:
            self.description = build_event_description(
                self.category,
                self.title,
                self.objects,
                self.datetime_utc,
                self.location_name,
                self.angular_separation,
            )

    def to_export_data(self) -> EventExportData:
        return EventExportData(
            category=self.category,
            title=self.title,
            datetime_utc=self.datetime_utc,
            best_viewing_time_local=self.best_viewing_time_local,
            location_name=self.location_name,
            description=self.description,
            angular_separation=self.angular_separation,
            direction=self.direction,
            step_by_step_guide=self.step_by_step_guide,
        )

    def to_dict(self) -> dict[str, Any]:
        """Returns dictionary formatted strictly for Stargazer Earth DTO integration."""
        return self.to_export_data().to_dict()

    def to_json(self, indent: int = 2) -> str:
        """Returns JSON string matching the Stargazer schema."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def generate_finder_chart(
        self,
        format: str = "png",
        theme: str = "stargazer_dark",
        figsize: tuple = (10, 8),
        dpi: int = 150,
        **kwargs,
    ) -> bytes | str:
        """
        Generates a clean sky finder chart at the moment of the event.

        Returns:
            bytes for 'png', or str/bytes for 'svg'.
        """
        from apts.visualization.finder_chart import generate_finder_chart

        return generate_finder_chart(
            self,
            format=format,
            theme=theme,
            figsize=figsize,
            dpi=dpi,
            **kwargs,
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any], place: Optional["Place"] = None) -> "Event":
        """Instantiates an Event from a dictionary (e.g. calculated event record)."""
        event_name = data.get("event", data.get("title", "Astronomical Event"))
        event_type = data.get("type", "")
        category = data.get("category") or get_event_category(event_name, event_type)

        # Date handling
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

        dt_utc = dt.astimezone(utc)

        # Best viewing local time
        if place and hasattr(place, "local_timezone") and place.local_timezone:
            local_dt = dt_utc.astimezone(place.local_timezone)
        else:
            local_dt = dt_utc

        best_viewing_time_local = local_dt.strftime("%H:%M")
        location_name = getattr(place, "name", None) or data.get("location_name") or "Observer Location"

        # Objects extraction
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

        # Title construction
        title = data.get("title")
        if not title:
            if len(objs) >= 2 and category == "OCCULTATION":
                title = f"{objs[0].title()} occultation of {objs[1].title()}"
            elif len(objs) >= 2 and category == "CONJUNCTION":
                title = f"Conjunction of {objs[0].title()} and {objs[1].title()}"
            elif objs and category == "METEOR_SHOWER":
                title = f"{objs[0]} Meteor Shower Peak"
            else:
                title = str(event_name)

        # Separation formatting
        angular_sep = data.get("angular_separation")
        if not angular_sep and "separation_degrees" in data and data["separation_degrees"] is not None:
            sep_val = float(data["separation_degrees"])
            if sep_val < 1.0:
                angular_sep = f"{round(sep_val * 60.0, 1)}'"
            else:
                angular_sep = f"{round(sep_val, 1)}°"

        azimuth_deg = data.get("azimuth") or data.get("azimuth_deg")
        if azimuth_deg is not None:
            azimuth_deg = float(azimuth_deg)

        altitude_deg = data.get("altitude") or data.get("altitude_deg")
        if altitude_deg is not None:
            altitude_deg = float(altitude_deg)

        return cls(
            category=category,
            title=title,
            datetime_utc=dt_utc,
            best_viewing_time_local=best_viewing_time_local,
            location_name=location_name,
            description=data.get("description", ""),
            angular_separation=angular_sep,
            azimuth_deg=azimuth_deg,
            altitude_deg=altitude_deg,
            direction=data.get("direction"),
            step_by_step_guide=data.get("step_by_step_guide"),
            objects=objs,
            place=place,
            extra_data=data,
        )

    @classmethod
    def from_row(cls, row: Any, place: Optional["Place"] = None) -> "Event":
        """Instantiates an Event from a pandas Series or dict-like row."""
        if hasattr(row, "to_dict"):
            d = row.to_dict()
        else:
            d = dict(row)
        return cls.from_dict(d, place=place)
