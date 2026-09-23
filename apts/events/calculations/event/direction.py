import math
from dataclasses import dataclass
from typing import Any


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


def get_sky_brightness(
    sun_alt_deg: float | None,
    moon_alt_deg: float | None = None,
    moon_phase_frac: float = 0.0,
) -> str:
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
