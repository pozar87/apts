import logging
from typing import TYPE_CHECKING, Optional, Any

import numpy
import pandas as pd
from matplotlib import pyplot

from apts.i18n import gettext_
from apts.plotting.utils import mark_good_conditions, mark_observation
from .utils import get_plot_setup, apply_colors

if TYPE_CHECKING:
    from apts.observations import Observation
    from apts.conditions import Conditions

logger = logging.getLogger(__name__)


def _handle_no_weather(title: str, effective_dark_mode: bool, style: dict):
    fig_err, ax_err = pyplot.subplots(figsize=(10, 6))
    fig_err.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax_err.set_facecolor(style["AXES_FACE_COLOR"])
    warning_color = "#FFCC00" if effective_dark_mode else "orange"
    ax_err.text(
        0.5,
        0.5,
        gettext_("Weather data not available for plotting."),
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=12,
        color=warning_color,
        wrap=True,
        transform=ax_err.transAxes,
    )
    ax_err.set_xticks([])
    ax_err.set_yticks([])
    ax_err.set_title(title, color=style["TEXT_COLOR"])
    return fig_err


def _generate_observation_weather_plot(
    observation: "Observation",
    plot_func_name: str,
    title: str,
    min_val: float,
    max_val: float,
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    """
    Private helper to generate a weather plot for an observation.
    """
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(title, effective_dark_mode, style)

    plot_func = getattr(observation.place.weather, plot_func_name)
    ax = plot_func(dark_mode_override=effective_dark_mode, **args)
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            min_val,
            max_val,
            effective_dark_mode,
            style,
        )
    return ax


def generate_plot_clouds(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_clouds",
        gettext_("Clouds"),
        0,
        eff_conditions.max_clouds,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_clouds_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    if observation.place.weather is None:
        return _handle_no_weather(gettext_("Cloud summary"), effective_dark_mode, style)

    return observation.place.weather.plot_clouds_summary(
        dark_mode_override=effective_dark_mode, **args
    )


def generate_plot_precipitation(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_precipitation",
        gettext_("Precipitation intensity and probability"),
        0,
        min(
            eff_conditions.max_precipitation_probability,
            eff_conditions.max_precipitation_intensity,
        ),
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_precipitation_type_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    if observation.place.weather is None:
        return _handle_no_weather(
            gettext_("Precipitation type summary"), effective_dark_mode, style
        )

    return observation.place.weather.plot_precipitation_type_summary(
        dark_mode_override=effective_dark_mode, **args
    )


def generate_plot_temperature(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_temperature",
        gettext_("Temperatures"),
        eff_conditions.min_temperature,
        eff_conditions.max_temperature,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_wind(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_wind",
        gettext_("Wind speed"),
        0,
        eff_conditions.max_wind,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_pressure_and_ozone(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    if observation.place.weather is None:
        return _handle_no_weather(
            gettext_("Pressure and Ozone"), effective_dark_mode, style
        )

    ax = observation.place.weather.plot_pressure_and_ozone(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
    return ax


def generate_plot_visibility(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_visibility",
        gettext_("Visibility"),
        eff_conditions.min_visibility,
        100,  # Arbitrary large value for max visibility
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_moon_illumination(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_moon_illumination",
        gettext_("Moon Illumination"),
        0,
        eff_conditions.max_moon_illumination,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_fog(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_fog",
        gettext_("Fog"),
        0,
        eff_conditions.max_fog,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_aurora(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions

    if (
        observation.place.weather is not None
        and "aurora" in observation.place.weather.data.columns
    ):
        return _generate_observation_weather_plot(
            observation,
            "plot_aurora",
            gettext_("Aurora"),
            eff_conditions.min_aurora,
            100,
            dark_mode_override=dark_mode_override,
            conditions=conditions,
            **args,
        )
    elif observation.place.weather is None:
        effective_dark_mode, style = get_plot_setup(dark_mode_override)
        return _handle_no_weather(gettext_("Aurora"), effective_dark_mode, style)

    return None


def generate_plot_seeing(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_seeing",
        gettext_("Seeing"),
        0,
        eff_conditions.max_seeing,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_sqm(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    return _generate_observation_weather_plot(
        observation,
        "plot_sqm",
        gettext_("Sky brightness"),
        eff_conditions.min_sqm,
        22.0,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_weather_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    eff_conditions = conditions or observation.conditions

    if observation.place.weather is None:
        return _handle_no_weather(
            gettext_("Weather summary"), effective_dark_mode, style
        )

    analysis = observation.get_weather_analysis(conditions=eff_conditions)
    if not analysis:
        return _handle_no_weather(
            gettext_("Weather summary"), effective_dark_mode, style
        )

    df = pd.DataFrame(analysis)
    ax = args.pop("ax", None)

    # Pie chart of good vs bad hours
    good_count = df[df.is_good_hour].shape[0]
    bad_count = df.shape[0] - good_count

    if good_count == 0 and bad_count == 0:
        return _handle_no_weather(
            gettext_("Weather summary"), effective_dark_mode, style
        )

    summary_data = pd.Series(
        [good_count, bad_count],
        index=[gettext_("Good hours"), gettext_("Bad hours")],
    )

    # Use the same style as other summary plots
    plot_ax = summary_data.plot(
        kind="pie",
        ax=ax,
        autopct="%1.1f%%",
        colors=["#90EE90", "#FF6B6B"]
        if not effective_dark_mode
        else ["#00FF7F", "#FF5252"],
        **args,
    )

    if not ax:
        ax = plot_ax
        fig = ax.figure
    else:
        fig = ax.figure

    apply_colors(ax, fig, style)

    ax.set_title(gettext_("Weather goodness summary"), color=style["TEXT_COLOR"])
    ax.set_ylabel("")  # Remove default ylabel

    for text_obj in ax.texts:
        text_obj.set_color(style["TEXT_COLOR"])

    return ax


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
