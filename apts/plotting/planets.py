import logging
from typing import TYPE_CHECKING, Optional

import svgwrite as svg

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_planet_color, get_plot_style
from apts.i18n import gettext_

if TYPE_CHECKING:
    from apts.observations import Observation

logger = logging.getLogger(__name__)


def plot_visible_planets_svg(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)
    default_fill_color = style["AXES_FACE_COLOR"]

    visible_planets = observation.get_visible_planets(**args)
    dwg = svg.Drawing(style={"background-color": style["BACKGROUND_COLOR"]})
    if not visible_planets.empty:
        max_size = visible_planets[["Size"]].max().iloc[0]
        max_size_val = (
            max_size.magnitude if hasattr(max_size, "magnitude") else max_size
        )
    else:
        max_size_val = 0
    y = int(max_size_val + 12)
    x = 20
    minimal_delta = 52
    last_radius = None
    for planet in visible_planets[["Name", "Size", "Phase", "TechnicalName"]].values:
        name = planet[0]
        radius_with_units = planet[1]
        radius = (
            radius_with_units.magnitude
            if hasattr(radius_with_units, "magnitude")
            else radius_with_units
        )
        phase_with_units = planet[2]
        phase = (
            phase_with_units.magnitude
            if hasattr(phase_with_units, "magnitude")
            else phase_with_units
        )
        phase_str = str(round(phase, 2))

        if last_radius is None:
            y += radius
            x += radius
        else:
            x += max(radius + last_radius + 10, minimal_delta)
        last_radius = radius
        dwg.add(
            dwg.circle(
                center=(x, y),
                r=radius,
                stroke=style["AXIS_COLOR"],
                stroke_width="1",
                fill=get_planet_color(name, effective_dark_mode, default_fill_color),
            )
        )
        dwg.add(
            dwg.text(
                name,
                insert=(x, y + radius + 15),
                text_anchor="middle",
                fill=style["TEXT_COLOR"],
            )
        )
        dwg.add(
            dwg.text(
                phase_str + "%",
                insert=(x, y - radius - 4),
                text_anchor="middle",
                fill=style["TEXT_COLOR"],
            )
        )
    return dwg.tostring()


def plot_visible_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    try:
        from IPython.display import SVG  # pyright: ignore
    except ImportError:
        logger.warning(gettext_("You can plot images only in Ipython notebook!"))
        return
    return SVG(plot_visible_planets_svg(observation, dark_mode_override, **args))
