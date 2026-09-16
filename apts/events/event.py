import json
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Optional

from apts.events.calculations.event import (
    CATEGORY_RULES,
    DirectionData,
    _build_event_title,
    _extract_coordinates,
    _extract_event_objects,
    _format_angular_separation,
    _parse_event_datetime,
    build_event_description,
    get_direction_data,
    get_event_category,
    get_sky_brightness,
    get_step_by_step_guide,
    parse_event_datetime,
    resolve_direction_data,
    resolve_horizon_and_chart_metadata,
    resolve_topocentric_state,
)

if TYPE_CHECKING:
    from apts.place import Place

logger = logging.getLogger(__name__)
utc = timezone.utc

__all__ = [
    "CATEGORY_RULES",
    "DirectionData",
    "Event",
    "EventExportData",
    "build_event_description",
    "get_direction_data",
    "get_event_category",
    "get_sky_brightness",
    "get_step_by_step_guide",
    "parse_event_datetime",
    "resolve_topocentric_state",
    "resolve_horizon_and_chart_metadata",
    "resolve_direction_data",
]


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
    sky_brightness: str = "NIGHT_DARK"
    is_below_horizon: bool = False
    chart_datetime_utc: str | None = None
    chart_time_note: str | None = None
    target_altitude_deg: float | None = None

    def to_dict(self) -> dict[str, Any]:
        d = {
            "category": self.category,
            "title": self.title,
            "datetime_utc": self.datetime_utc,
            "best_viewing_time_local": self.best_viewing_time_local,
            "location_name": self.location_name,
            "description": self.description,
            "angular_separation": self.angular_separation,
            "direction": self.direction.to_dict() if isinstance(self.direction, DirectionData) else self.direction,
            "step_by_step_guide": self.step_by_step_guide,
            "sky_brightness": self.sky_brightness,
        }
        if self.is_below_horizon:
            d["is_below_horizon"] = self.is_below_horizon
        if self.chart_datetime_utc:
            d["chart_datetime_utc"] = self.chart_datetime_utc
        if self.chart_time_note:
            d["chart_time_note"] = self.chart_time_note
        if self.target_altitude_deg is not None:
            d["target_altitude_deg"] = round(float(self.target_altitude_deg), 1)
        return d


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
        self.dt_utc, self.datetime_utc = parse_event_datetime(datetime_utc)
        self.category = category
        self.title = title
        self.best_viewing_time_local = best_viewing_time_local
        self.location_name = location_name
        self.objects = objects or []
        self.angular_separation = angular_separation
        self.place = place
        self.extra_data = extra_data or {}

        # Resolve topocentric position and sky brightness
        self.azimuth_deg, self.altitude_deg, self.sky_brightness = resolve_topocentric_state(
            place, self.dt_utc, self.objects, azimuth_deg, altitude_deg, self.extra_data
        )

        # Initialize horizon and chart metadata
        (
            self.is_below_horizon,
            self.chart_datetime_utc,
            self.chart_time_note,
            self.target_altitude_deg,
        ) = resolve_horizon_and_chart_metadata(self.altitude_deg, self.extra_data)

        # Resolve Direction
        self.direction = resolve_direction_data(direction, self.azimuth_deg)

        # Resolve Step-by-step guide
        self.step_by_step_guide = (
            step_by_step_guide
            if step_by_step_guide
            else get_step_by_step_guide(self.category, self.title, self.objects)
        )

        # Resolve Description
        self.description = (
            description
            if description
            else build_event_description(
                self.category,
                self.title,
                self.objects,
                self.datetime_utc,
                self.location_name,
                self.angular_separation,
            )
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
            sky_brightness=getattr(self, "sky_brightness", "NIGHT_DARK"),
            is_below_horizon=getattr(self, "is_below_horizon", False),
            chart_datetime_utc=getattr(self, "chart_datetime_utc", None),
            chart_time_note=getattr(self, "chart_time_note", None),
            target_altitude_deg=getattr(self, "target_altitude_deg", self.altitude_deg),
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

        res = generate_finder_chart(
            self,
            format=format,
            theme=theme,
            figsize=figsize,
            dpi=dpi,
            **kwargs,
        )
        return res if res is not None else b"" if format == "png" else ""

    @classmethod
    def from_dict(cls, data: dict[str, Any], place: Optional["Place"] = None) -> "Event":
        """Instantiates an Event from a dictionary (e.g. calculated event record)."""
        event_name = data.get("event", data.get("title", "Astronomical Event"))
        event_type = data.get("type", "")
        category = data.get("category") or get_event_category(event_name, event_type)

        dt_utc = _parse_event_datetime(data)

        # Best viewing local time
        if place and hasattr(place, "local_timezone") and place.local_timezone:
            local_dt = dt_utc.astimezone(place.local_timezone)
        else:
            local_dt = dt_utc

        best_viewing_time_local = local_dt.strftime("%H:%M")
        location_name = getattr(place, "name", None) or data.get("location_name") or "Observer Location"

        objs = _extract_event_objects(data)
        title = _build_event_title(data, objs, category, str(event_name))
        angular_sep = _format_angular_separation(data)
        azimuth_deg, altitude_deg = _extract_coordinates(data)

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
