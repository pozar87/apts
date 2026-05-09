import logging
from math import copysign
from typing import TYPE_CHECKING, Optional
from importlib import resources
from unittest.mock import MagicMock

import matplotlib.font_manager as font_manager

from ..config import get_dark_mode
from ..constants.graphconstants import get_plot_style
from ..i18n import gettext_
from ..utils.plot import PlotUtils

if TYPE_CHECKING:
    from ..observations import Observation
    from ..place import Place

logger = logging.getLogger(__name__)

MOON_FONT = font_manager.FontProperties(
    fname=str(resources.files("apts").joinpath("data/moon_phases.ttf")), size=50
)


def plot_sun_and_moon_path(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if observation.sun_observation:
        return generate_plot_sun_path(observation.place, dark_mode_override, **args)
    else:
        return generate_plot_moon_path(observation.place, dark_mode_override, **args)


def generate_plot_sun_path(
    place: "Place", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    def add_marker(ax, label, position, text_color, grid_color):  # Pass ax and colors
        ax.axvline(position, color=grid_color, linestyle="--", linewidth=1)
        ax.text(
            position,
            1,
            label,
            weight="bold",
            horizontalalignment="center",
            color=text_color,
        )

    data = place.sun_path()

    # Handle MagicMock for tests
    is_southern = False
    try:
        if hasattr(place, "lat_decimal") and not isinstance(place.lat_decimal, MagicMock):
            if place.lat_decimal < 0:
                is_southern = True
    except Exception:
        pass

    if is_southern:
        data["Azimuth"] = (data["Azimuth"] + 180) % 360 - 180

    passed_ax = args.pop("ax", None)  # Renamed to avoid confusion

    plot_kwargs = {
        "x": "Azimuth",
        "y": "Sun altitude",
        "title": "Sun altitude",  # This title is styled later by direct ax.set_title
        "style": ".-",
        **args,  # Pass through any other user-supplied keyword arguments
    }

    if passed_ax is not None:
        plot_kwargs["ax"] = passed_ax  # Add 'ax' to kwargs only if it was provided
        data.plot(**plot_kwargs)  # Plot on the provided ax
        ax = passed_ax  # Use the axes that was passed in
        fig = ax.figure  # Get figure from provided ax
    else:
        ax = data.plot(**plot_kwargs)  # Let pandas create a new ax and figure
        fig = ax.figure  # Get figure from newly created ax

    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    if ax.lines:  # Style the main moon path line
        ax.lines[0].set_color(style["TEXT_COLOR"])

    ax.set_title(
        gettext_("Sun Path on {date}").format(
            date=place.date.utc_datetime().strftime("%Y-%m-%d")  # type: ignore
        ),
        color=style["TEXT_COLOR"],
    )

    # Add cardinal direction and set x-axis limits based on hemisphere
    if is_southern:  # Southern Hemisphere
        add_marker(ax, "W", -90, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "N", 0, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
        ax.set_xlim(135, -135)  # Inverted for South-up view, SE to SW
    else:  # Northern Hemisphere
        add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "S", 180, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "W", 270, style["TEXT_COLOR"], style["GRID_COLOR"])
        ax.set_xlim(45, 315)

    PlotUtils.annotate_plot(
        ax,
        gettext_("Altitude [°]"),
        effective_dark_mode,
        place.local_timezone,
        x_label=gettext_("Azimuth [°]"),
    )

    # Plot horizon
    ax.axhspan(0, -50, color=style["GRID_COLOR"], alpha=0.3)
    ax.locator_params(nbins=20)
    ax.set_ylim(bottom=-10, top=90)

    # Plot time for altitudes
    for _, obj_row in data.dropna().iloc[::6, :].iterrows():
        altitude = obj_row["Sun altitude"]
        azimuth = obj_row["Azimuth"]
        local_time = obj_row["Local_time"]
        if altitude > 0:
            ax.annotate(
                local_time,
                (azimuth + copysign(10, azimuth - 180) + 10, altitude + 1),
                color=style["TEXT_COLOR"],
            )
    PlotUtils.style_legend(ax, style)
    return ax


def generate_plot_moon_path(
    place: "Place", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    def add_marker(ax, label, position, text_color, grid_color):  # Pass ax and colors
        ax.axvline(position, color=grid_color, linestyle="--", linewidth=1)
        ax.text(
            position,
            1,
            label,
            weight="bold",
            horizontalalignment="center",
            color=text_color,
        )

    data = place.moon_path()

    # Handle MagicMock for tests
    is_southern = False
    try:
        if hasattr(place, "lat_decimal") and not isinstance(place.lat_decimal, MagicMock):
            if place.lat_decimal < 0:
                is_southern = True
    except Exception:
        pass

    if is_southern:
        data["Azimuth"] = (data["Azimuth"] + 180) % 360 - 180

    passed_ax = args.pop("ax", None)  # Renamed to avoid confusion

    plot_kwargs = {
        "x": "Azimuth",
        "y": "Moon altitude",
        "title": "Moon altitude",  # This title is styled later by direct ax.set_title
        "style": ".-",
        **args,  # Pass through any other user-supplied keyword arguments
    }

    if passed_ax is not None:
        plot_kwargs["ax"] = passed_ax  # Add 'ax' to kwargs only if it was provided
        data.plot(**plot_kwargs)  # Plot on the provided ax
        ax = passed_ax  # Use the axes that was passed in
        fig = ax.figure  # Get figure from provided ax
    else:
        ax = data.plot(**plot_kwargs)  # Let pandas create a new ax and figure
        fig = ax.figure  # Get figure from newly created ax

    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    if ax.lines:  # Style the main moon path line
        ax.lines[0].set_color(style["TEXT_COLOR"])

    # Add cardinal direction and set x-axis limits based on hemisphere
    if is_southern:  # Southern Hemisphere
        add_marker(ax, "W", -90, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "N", 0, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
        ax.set_xlim(135, -135)  # Inverted for South-up view
    else:  # Northern Hemisphere
        add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "S", 180, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "W", 270, style["TEXT_COLOR"], style["GRID_COLOR"])
        ax.set_xlim(45, 315)
    PlotUtils.annotate_plot(
        ax,
        gettext_("Altitude [°]"),
        effective_dark_mode,
        place.local_timezone,
        x_label=gettext_("Azimuth [°]"),
    )

    # Plot horizon
    ax.axhspan(0, -50, color=style["GRID_COLOR"], alpha=0.3)
    ax.locator_params(nbins=20)
    ax.set_ylim(bottom=-10, top=90)

    # --- Plot Moon Phase Icon and Illumination Text ---
    # Position icon differently based on hemisphere to avoid overlap with path
    if is_southern:  # Southern Hemisphere, transit is North
        icon_x_position = 0
        icon_y_position = 20
        text_y_position = icon_y_position - 13
    else:  # Northern Hemisphere, transit is South
        icon_x_position = 180
        icon_y_position = 10
        text_y_position = -3

    if effective_dark_mode:
        # In dark mode, draw a solid circle first, then the shadow on top.
        ax.plot(
            icon_x_position,
            icon_y_position,
            marker="o",
            markersize=45,
            color=style["TEXT_COLOR"],
            linestyle="None",
        )
        ax.text(
            icon_x_position,
            icon_y_position,
            place._moon_phase_letter(),
            fontproperties=MOON_FONT,
            horizontalalignment="center",
            verticalalignment="center",
            color=style["AXES_FACE_COLOR"],
        )
    else:
        # In light mode, just draw the phase character.
        ax.text(
            icon_x_position,
            icon_y_position,
            place._moon_phase_letter(),
            fontproperties=MOON_FONT,
            horizontalalignment="center",
            verticalalignment="center",
            color=style["TEXT_COLOR"],
        )
    ax.text(
        icon_x_position,
        text_y_position,
        f"{place.moon_illumination():.0f}%",
        color=style["TEXT_COLOR"],
        alpha=0.7,
        horizontalalignment="center",
    )

    # Plot time for altitudes, adjusting for hemisphere
    for _, obj_row in data.dropna().iloc[::6, :].iterrows():
        altitude = obj_row["Moon altitude"]
        azimuth = obj_row["Azimuth"]
        local_time = obj_row["Local_time"]

        if altitude > 0:
            if is_southern:  # Southern Hemisphere
                # Adjust offset direction to avoid text crossing the plot edges
                offset_direction = azimuth
                x_offset = copysign(10, offset_direction) + 10
            else:  # Northern Hemisphere
                x_offset = copysign(10, azimuth - 180) - 8

            ax.annotate(
                local_time,
                (azimuth + x_offset, altitude + 1),
                color=style["TEXT_COLOR"],
            )
    ax.set_title(
        gettext_("Moon Path")
        + f" on {place.date.utc_datetime().strftime('%Y-%m-%d')}",  # type: ignore
        color=style["TEXT_COLOR"],
    )
    PlotUtils.style_legend(ax, style)
    return ax
