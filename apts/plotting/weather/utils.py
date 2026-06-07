import logging
from typing import Any, Optional, cast, TYPE_CHECKING

import pandas as pd
from matplotlib import pyplot

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style
from apts.i18n import gettext_
from apts.plotting.utils import mark_good_conditions, mark_observation
from apts.utils.plot import PlotUtils

if TYPE_CHECKING:
    from apts.observations import Observation
    from apts.conditions import Conditions

logger = logging.getLogger(__name__)

# Re-export for consistency and easier patching in tests
__all__ = ["mark_good_conditions", "mark_observation"]


def get_plot_setup(dark_mode_override: Optional[bool] = None):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()
    style = get_plot_style(effective_dark_mode)
    return effective_dark_mode, style


def finalize_plot(ax, fig, style, title, y_label, effective_dark_mode, local_timezone):
    ax.set_title(title, color=style["TEXT_COLOR"])
    PlotUtils.style_legend(ax, style)
    PlotUtils.annotate_plot(ax, y_label, effective_dark_mode, local_timezone)
    return ax


def apply_colors(ax, fig, style):
    if ax:
        ax.set_facecolor(style["AXES_FACE_COLOR"])
    if fig:
        cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])


def handle_no_weather(title: str, effective_dark_mode: bool, style: dict):
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


def generate_observation_weather_plot(
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
    Helper to generate a weather plot for an observation.
    """
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    if observation.place.weather is None:
        return handle_no_weather(title, effective_dark_mode, style)

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


def generic_line_plot(
    data: pd.DataFrame,
    title: str,
    y_label: str,
    local_timezone: Any,
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    ax = args.pop("ax", None)
    if data.empty:
        return PlotUtils.plot_no_data(ax, title, effective_dark_mode)

    fig = ax.figure if ax else None

    plot_kwargs = args.copy()
    plot_ax = data.plot(
        x="time",
        ax=ax,
        x_compat=True,
        **plot_kwargs,
    )

    if ax is None:
        ax = plot_ax
        fig = ax.figure

    apply_colors(ax, fig, style)
    return finalize_plot(
        ax,
        fig,
        style,
        ax.get_title() or title,
        y_label,
        effective_dark_mode,
        local_timezone,
    )


def generic_pie_plot(
    data: pd.DataFrame,
    group_by_col: str,
    label: str,
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    ax = args.pop("ax", None)
    if data.empty:
        return PlotUtils.plot_no_data(ax, label, effective_dark_mode)

    fig = ax.figure if ax else None
    plot_kwargs = args.copy()

    plot_ax = (
        data.groupby(group_by_col)
        .size()
        .plot(kind="pie", label=label, ax=ax, **plot_kwargs)
    )

    if ax is None:
        ax = plot_ax
        fig = ax.figure

    apply_colors(ax, fig, style)

    title_text = ax.get_title() or plot_kwargs.get("label") or label
    ax.set_title(title_text, color=style["TEXT_COLOR"])
    ax.set_ylabel(ax.get_ylabel(), color=style["TEXT_COLOR"])

    for text_obj in ax.texts:
        text_obj.set_color(style["TEXT_COLOR"])

    return ax
