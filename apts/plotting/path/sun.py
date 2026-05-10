import logging
from math import copysign
from typing import TYPE_CHECKING, Optional

from ...config import get_dark_mode
from ...constants.graphconstants import get_plot_style
from ...i18n import gettext_
from ...utils.plot import PlotUtils
from .utils import is_southern_hemisphere, setup_cardinal_markers

if TYPE_CHECKING:
    from ...place import Place

logger = logging.getLogger(__name__)

def generate_plot_sun_path(
    place: "Place", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    data = place.sun_path()
    is_southern = is_southern_hemisphere(place)

    if is_southern:
        data["Azimuth"] = (data["Azimuth"] + 180) % 360 - 180

    passed_ax = args.pop("ax", None)

    plot_kwargs = {
        "x": "Azimuth",
        "y": "Sun altitude",
        "title": "Sun altitude",
        "style": ".-",
        **args,
    }

    if passed_ax is not None:
        plot_kwargs["ax"] = passed_ax
        data.plot(**plot_kwargs)
        ax = passed_ax
        fig = ax.figure
    else:
        ax = data.plot(**plot_kwargs)
        fig = ax.figure

    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    if ax.lines:
        ax.lines[0].set_color(style["TEXT_COLOR"])

    ax.set_title(
        gettext_("Sun Path on {date}").format(
            date=place.date.utc_datetime().strftime("%Y-%m-%d")
        ),
        color=style["TEXT_COLOR"],
    )

    setup_cardinal_markers(ax, is_southern, style)

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
