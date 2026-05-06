from typing import Any, Optional, cast
import pandas as pd
from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style
from apts.utils.plot import PlotUtils

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

def generic_line_plot(
    data: pd.DataFrame,
    title: str,
    y_label: str,
    local_timezone: Any,
    dark_mode_override: Optional[bool] = None,
    **args
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
    return finalize_plot(ax, fig, style, ax.get_title() or title, y_label, effective_dark_mode, local_timezone)

def generic_pie_plot(
    data: pd.DataFrame,
    group_by_col: str,
    label: str,
    dark_mode_override: Optional[bool] = None,
    **args
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
