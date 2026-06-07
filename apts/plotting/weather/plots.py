import logging
from typing import TYPE_CHECKING, Optional, Any

import numpy
from matplotlib import pyplot

from apts.i18n import gettext_
from .utils import (
    get_plot_setup,
    handle_no_weather as _handle_no_weather,
)

from .params import (
    generate_plot_clouds,
    generate_plot_precipitation,
    generate_plot_temperature,
    generate_plot_wind,
    generate_plot_pressure_and_ozone,
    generate_plot_visibility,
    generate_plot_moon_illumination,
    generate_plot_fog,
    generate_plot_aurora,
    generate_plot_seeing,
    generate_plot_sqm,
)

from .summary import (
    generate_plot_clouds_summary,
    generate_plot_precipitation_type_summary,
    generate_plot_weather_summary,
)

if TYPE_CHECKING:
    from apts.observations import Observation
    from apts.conditions import Conditions

logger = logging.getLogger(__name__)


def _create_weather_figure_and_axes(style: dict, **args) -> tuple[Any, Any]:
    """
    Creates the figure and axes for the main weather plot.
    """
    axes_arg = args.pop("ax", None)
    if (
        axes_arg is not None
        and isinstance(axes_arg, numpy.ndarray)
        and axes_arg.shape == (7, 2)
    ):
        axes_out = axes_arg
        fig = axes_out[0, 0].figure
    else:
        fig, axes_out = pyplot.subplots(nrows=7, ncols=2, figsize=(13, 30), **args)

    if fig:
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

    return fig, axes_out


def _plot_all_weather_subplots(
    observation: "Observation",
    axes_in: Any,
    effective_dark_mode: bool,
    conditions: Optional["Conditions"] = None,
):
    """
    Plots all weather subplots on the provided axes.
    """
    generate_plot_clouds(
        observation,
        ax=axes_in[0, 0],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )
    generate_plot_clouds_summary(
        observation, ax=axes_in[0, 1], dark_mode_override=effective_dark_mode
    )

    generate_plot_precipitation(
        observation,
        ax=axes_in[1, 0],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )
    generate_plot_precipitation_type_summary(
        observation, ax=axes_in[1, 1], dark_mode_override=effective_dark_mode
    )

    generate_plot_temperature(
        observation,
        ax=axes_in[2, 0],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )
    generate_plot_wind(
        observation,
        ax=axes_in[2, 1],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )

    generate_plot_pressure_and_ozone(
        observation, ax=axes_in[3, 0], dark_mode_override=effective_dark_mode
    )
    generate_plot_visibility(
        observation,
        ax=axes_in[3, 1],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )

    generate_plot_moon_illumination(
        observation,
        ax=axes_in[4, 0],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )
    generate_plot_fog(
        observation,
        ax=axes_in[4, 1],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )

    generate_plot_seeing(
        observation,
        ax=axes_in[5, 0],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )
    generate_plot_sqm(
        observation,
        ax=axes_in[5, 1],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )

    plt_aurora_ax = generate_plot_aurora(
        observation,
        ax=axes_in[6, 0],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )
    if plt_aurora_ax is None:
        axes_in[6, 0].set_visible(False)

    generate_plot_weather_summary(
        observation,
        ax=axes_in[6, 1],
        dark_mode_override=effective_dark_mode,
        conditions=conditions,
    )


def generate_plot_weather(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)

    if observation.place.weather is None:
        return _handle_no_weather(
            gettext_("Weather Plot Information"), effective_dark_mode, style
        )

    fig = None
    try:
        fig, axes_out = _create_weather_figure_and_axes(style, **args)
        _plot_all_weather_subplots(
            observation, axes_out, effective_dark_mode, conditions=conditions
        )

        if fig:
            fig.tight_layout()
        return fig

    except Exception as e:
        logger.error(f"Error generating Weather plot details: {e}", exc_info=True)
        if fig is not None:
            try:
                pyplot.close(fig)
            except Exception as close_exc:
                logger.error(
                    f"Error closing figure during weather plot error handling: {close_exc}"
                )

        fig_err, ax_err = pyplot.subplots(figsize=(10, 6))
        fig_err.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax_err.set_facecolor(style["AXES_FACE_COLOR"])
        error_color = "#FF6B6B" if effective_dark_mode else "red"
        ax_err.text(
            0.5,
            0.5,
            gettext_("Error generating Weather plot details.\nSee logs for specifics."),
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
            color=error_color,
            wrap=True,
            transform=ax_err.transAxes,
        )
        ax_err.set_xticks([])
        ax_err.set_yticks([])
        ax_err.set_title(gettext_("Weather Plot Error"), color=style["TEXT_COLOR"])
        return fig_err


__all__ = [
    "generate_plot_weather",
    "generate_plot_clouds",
    "generate_plot_clouds_summary",
    "generate_plot_precipitation",
    "generate_plot_precipitation_type_summary",
    "generate_plot_temperature",
    "generate_plot_wind",
    "generate_plot_pressure_and_ozone",
    "generate_plot_visibility",
    "generate_plot_moon_illumination",
    "generate_plot_fog",
    "generate_plot_aurora",
    "generate_plot_seeing",
    "generate_plot_sqm",
    "generate_plot_weather_summary",
]
