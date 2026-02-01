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


def generate_plot_weather(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)
    eff_conditions = conditions or observation.conditions

    if observation.place.weather is None:
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
        ax_err.set_title(
            gettext_("Weather Plot Information"), color=style["TEXT_COLOR"]
        )
        return fig_err
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

        plt_clouds_ax = observation.place.weather.plot_clouds(
            ax=axes[0, 0], dark_mode_override=effective_dark_mode
        )
        if plt_clouds_ax:
            mark_observation(observation, plt_clouds_ax, effective_dark_mode, style)
            mark_good_conditions(
                observation,
                plt_clouds_ax,
                0,
                eff_conditions.max_clouds,
                effective_dark_mode,
                style,
            )

        observation.place.weather.plot_clouds_summary(
            ax=axes[0, 1], dark_mode_override=effective_dark_mode
        )

        plt_precip_ax = observation.place.weather.plot_precipitation(
            ax=axes[1, 0], dark_mode_override=effective_dark_mode
        )
        if plt_precip_ax:
            mark_observation(observation, plt_precip_ax, effective_dark_mode, style)
            mark_good_conditions(
                observation,
                plt_precip_ax,
                0,
                eff_conditions.max_precipitation_probability,
                effective_dark_mode,
                style,
            )

        observation.place.weather.plot_precipitation_type_summary(
            ax=axes[1, 1], dark_mode_override=effective_dark_mode
        )

        plt_temp_ax = observation.place.weather.plot_temperature(
            ax=axes[2, 0], dark_mode_override=effective_dark_mode
        )
        if plt_temp_ax:
            mark_observation(observation, plt_temp_ax, effective_dark_mode, style)
            mark_good_conditions(
                observation,
                plt_temp_ax,
                eff_conditions.min_temperature,
                eff_conditions.max_temperature,
                effective_dark_mode,
                style,
            )

        plt_wind_ax = observation.place.weather.plot_wind(
            ax=axes[2, 1], dark_mode_override=effective_dark_mode
        )
        if plt_wind_ax:
            mark_observation(observation, plt_wind_ax, effective_dark_mode, style)
            mark_good_conditions(
                observation,
                plt_wind_ax,
                0,
                eff_conditions.max_wind,
                effective_dark_mode,
                style,
            )

        plt_pressure_ax = observation.place.weather.plot_pressure_and_ozone(
            ax=axes[3, 0], dark_mode_override=effective_dark_mode
        )
        if plt_pressure_ax:
            mark_observation(observation, plt_pressure_ax, effective_dark_mode, style)

        plt_visibility_ax = observation.place.weather.plot_visibility(
            ax=axes[3, 1], dark_mode_override=effective_dark_mode
        )
        if plt_visibility_ax:
            mark_observation(
                observation, plt_visibility_ax, effective_dark_mode, style
            )
            mark_good_conditions(
                observation,
                plt_visibility_ax,
                eff_conditions.min_visibility,
                100,  # Arbitrary large value for max visibility
                effective_dark_mode,
                style,
            )

        plt_moon_illumination_ax = observation.place.weather.plot_moon_illumination(
            ax=axes[4, 0], dark_mode_override=effective_dark_mode
        )
        if plt_moon_illumination_ax:
            mark_observation(
                observation, plt_moon_illumination_ax, effective_dark_mode, style
            )
            mark_good_conditions(
                observation,
                plt_moon_illumination_ax,
                0,
                eff_conditions.max_moon_illumination,
                effective_dark_mode,
                style,
            )

        plt_fog_ax = observation.place.weather.plot_fog(
            ax=axes[4, 1], dark_mode_override=effective_dark_mode
        )
        if plt_fog_ax:
            mark_observation(observation, plt_fog_ax, effective_dark_mode, style)
            mark_good_conditions(
                observation,
                plt_fog_ax,
                0,
                eff_conditions.max_fog,
                effective_dark_mode,
                style,
            )

        if "aurora" in observation.place.weather.data.columns:
            plt_aurora_ax = observation.place.weather.plot_aurora(
                ax=axes[5, 0], dark_mode_override=effective_dark_mode
            )
            if plt_aurora_ax:
                mark_observation(observation, plt_aurora_ax, effective_dark_mode, style)
                mark_good_conditions(
                    observation,
                    plt_aurora_ax,
                    eff_conditions.min_aurora,
                    100,
                    effective_dark_mode,
                    style,
                )
        else:
            # If the aurora column doesn't exist, you can hide the subplot
            axes[5, 0].set_visible(False)

        # Hide the unused subplot
        axes[5, 1].set_visible(False)

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
