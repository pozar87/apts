import logging
from typing import TYPE_CHECKING, Optional

import numpy
from matplotlib import pyplot

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style
from apts.i18n import gettext_
from apts.plotting.utils import mark_good_conditions, mark_observation

if TYPE_CHECKING:
    from apts.observations import Observation
    from apts.conditions import Conditions

logger = logging.getLogger(__name__)


def _get_plot_setup(observation: "Observation", dark_mode_override: Optional[bool]):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)
    return effective_dark_mode, style


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


def generate_plot_clouds(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(gettext_("Clouds"), effective_dark_mode, style)

    ax = observation.place.weather.plot_clouds(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            0,
            eff_conditions.max_clouds,
            effective_dark_mode,
            style,
        )
    return ax


def generate_plot_clouds_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
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
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(
            gettext_("Precipitation intensity and probability"),
            effective_dark_mode,
            style,
        )

    ax = observation.place.weather.plot_precipitation(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            0,
            min(
                eff_conditions.max_precipitation_probability,
                eff_conditions.max_precipitation_intensity,
            ),
            effective_dark_mode,
            style,
        )
    return ax


def generate_plot_precipitation_type_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
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
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(gettext_("Temperatures"), effective_dark_mode, style)

    ax = observation.place.weather.plot_temperature(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            eff_conditions.min_temperature,
            eff_conditions.max_temperature,
            effective_dark_mode,
            style,
        )
    return ax


def generate_plot_wind(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(gettext_("Wind speed"), effective_dark_mode, style)

    ax = observation.place.weather.plot_wind(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            0,
            eff_conditions.max_wind,
            effective_dark_mode,
            style,
        )
    return ax


def generate_plot_pressure_and_ozone(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
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
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(gettext_("Visibility"), effective_dark_mode, style)

    ax = observation.place.weather.plot_visibility(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            eff_conditions.min_visibility,
            100,  # Arbitrary large value for max visibility
            effective_dark_mode,
            style,
        )
    return ax


def generate_plot_moon_illumination(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(
            gettext_("Moon Illumination"), effective_dark_mode, style
        )

    ax = observation.place.weather.plot_moon_illumination(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            0,
            eff_conditions.max_moon_illumination,
            effective_dark_mode,
            style,
        )
    return ax


def generate_plot_fog(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(gettext_("Fog"), effective_dark_mode, style)

    ax = observation.place.weather.plot_fog(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            0,
            eff_conditions.max_fog,
            effective_dark_mode,
            style,
        )
    return ax


def generate_plot_aurora(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
    eff_conditions = conditions or observation.conditions
    if observation.place.weather is None:
        return _handle_no_weather(gettext_("Aurora"), effective_dark_mode, style)

    if "aurora" in observation.place.weather.data.columns:
        ax = observation.place.weather.plot_aurora(
            dark_mode_override=effective_dark_mode, **args
        )
        if ax:
            mark_observation(observation, ax, effective_dark_mode, style)
            mark_good_conditions(
                observation,
                ax,
                eff_conditions.min_aurora,
                100,
                effective_dark_mode,
                style,
            )
        return ax
    return None


def generate_plot_weather_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)
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

    import pandas as pd

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
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])
    else:
        ax.set_facecolor(style["AXES_FACE_COLOR"])
        ax.figure.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

    ax.set_title(gettext_("Weather goodness summary"), color=style["TEXT_COLOR"])
    ax.set_ylabel("")  # Remove default ylabel

    for text_obj in ax.texts:
        text_obj.set_color(style["TEXT_COLOR"])

    return ax


def generate_plot_weather(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = _get_plot_setup(observation, dark_mode_override)

    if observation.place.weather is None:
        return _handle_no_weather(
            gettext_("Weather Plot Information"), effective_dark_mode, style
        )

    try:
        axes_arg = args.pop("ax", None)
        fig = None
        axes = None

        if (
            axes_arg is not None
            and isinstance(axes_arg, numpy.ndarray)
            and axes_arg.shape == (6, 2)
        ):
            axes = axes_arg
            fig = axes[0, 0].figure
        else:
            fig, axes = pyplot.subplots(nrows=6, ncols=2, figsize=(13, 25), **args)

        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        generate_plot_clouds(
            observation,
            ax=axes[0, 0],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )
        generate_plot_clouds_summary(
            observation, ax=axes[0, 1], dark_mode_override=effective_dark_mode
        )

        generate_plot_precipitation(
            observation,
            ax=axes[1, 0],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )
        generate_plot_precipitation_type_summary(
            observation, ax=axes[1, 1], dark_mode_override=effective_dark_mode
        )

        generate_plot_temperature(
            observation,
            ax=axes[2, 0],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )
        generate_plot_wind(
            observation,
            ax=axes[2, 1],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )

        generate_plot_pressure_and_ozone(
            observation, ax=axes[3, 0], dark_mode_override=effective_dark_mode
        )
        generate_plot_visibility(
            observation,
            ax=axes[3, 1],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )

        generate_plot_moon_illumination(
            observation,
            ax=axes[4, 0],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )
        generate_plot_fog(
            observation,
            ax=axes[4, 1],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )

        plt_aurora_ax = generate_plot_aurora(
            observation,
            ax=axes[5, 0],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )
        if plt_aurora_ax is None:
            # If the aurora column doesn't exist, you can hide the subplot
            axes[5, 0].set_visible(False)

        generate_plot_weather_summary(
            observation,
            ax=axes[5, 1],
            dark_mode_override=effective_dark_mode,
            conditions=conditions,
        )

        fig.tight_layout()
        return fig

    except Exception as e:
        logger.error(f"Error generating Weather plot details: {e}", exc_info=True)
        current_fig = locals().get("fig", None)
        if current_fig is not None:
            try:
                pyplot.close(current_fig)
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
