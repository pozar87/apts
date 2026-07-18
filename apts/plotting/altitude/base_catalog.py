import logging
from datetime import timedelta
from typing import TYPE_CHECKING, Any, Callable, Dict, Optional, cast

import pandas as pd
from matplotlib import lines

from apts.constants.graphconstants import (
    get_messier_color,
    get_plot_style,
)
from apts.i18n import gettext_
from apts.plotting.utils import mark_good_conditions, mark_observation
from apts.utils.plot import PlotUtils
from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation

logger = logging.getLogger(__name__)


def generate_catalog_altitude_plot(
    observation: "Observation",
    get_df_func: Callable[[], pd.DataFrame],
    label_column: str,
    title: str,
    legend_title: str,
    logger_msg: str,
    error_title: str,
    error_text: str,
    logger_error_msg: str,
    clip_lower: Optional[float] = None,
    dark_mode_override: Optional[bool] = None,
    scatter_kwargs: Optional[Dict[str, Any]] = None,
    annotate_kwargs: Optional[Dict[str, Any]] = None,
    pyplot_module: Any = None,
    get_dark_mode_func: Optional[Callable[[], bool]] = None,
    **args,
):
    if pyplot_module is None:
        from matplotlib import pyplot as pyplot_module

    if get_dark_mode_func is None:
        from apts.config import get_dark_mode as get_dark_mode_func

    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode_func()

    style = get_plot_style(effective_dark_mode)

    ax = args.pop("ax", None)
    fig = None
    if ax:
        fig = ax.figure
    else:
        fig, ax = pyplot_module.subplots(figsize=(18, 12), **args)

    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    try:
        df = get_df_func().copy()

        if len(df) == 0:
            return _generate_empty_plot(
                observation, fig, ax, effective_dark_mode, style, title, logger_msg
            )

        # Vectorized property extraction to avoid slow iterrows()
        # Ensure numeric columns are floats to avoid Pint/Quantity overhead
        for col in [
            ObjectTableLabels.ALTITUDE,
            ObjectTableLabels.SIZE_MAJOR,
            ObjectTableLabels.SIZE_MINOR,
        ]:
            if col in df.columns:
                df[col] = [
                    getattr(x, "magnitude", x) for x in df[col].values
                ]

        # Vectorized marker size: marker area (s) as width * height
        marker_size = (
            df[ObjectTableLabels.SIZE_MAJOR]
            * df[ObjectTableLabels.SIZE_MINOR]
        )
        if clip_lower is not None:
            marker_size = marker_size.clip(lower=clip_lower)
        df["marker_size"] = marker_size

        # Determine colors
        # Optimization: use unique-value mapping for colors to avoid redundant O(N) overhead.
        from ...i18n import bulk_gettext

        types = (
            df["Type"].fillna("Other")
            if "Type" in df.columns
            else pd.Series("Other", index=df.index)
        )

        # Ensure types are translated for correct color matching and display
        translated_types = cast(pd.Series, bulk_gettext(types))
        unique_types = translated_types.unique()
        color_map = {
            t: get_messier_color(t, effective_dark_mode) for t in unique_types
        }
        df["color"] = translated_types.map(color_map)
        df["TranslatedType"] = translated_types
        df["Type"] = translated_types

        # Filter out objects without a valid transit time in the window
        plot_df = df[df[ObjectTableLabels.TRANSIT].notna()].copy()

        plotted_types = {}
        if not plot_df.empty:
            # Single vectorized scatter call for all objects
            s_kwargs = scatter_kwargs or {}
            ax.scatter(
                plot_df[ObjectTableLabels.TRANSIT],
                plot_df[ObjectTableLabels.ALTITUDE],
                s=plot_df["marker_size"],
                marker="o",
                c=plot_df["color"],
                **s_kwargs,
            )

            # Annotation loop optimized to avoid iterrows()
            a_kwargs = annotate_kwargs or {}
            for text, x, y in zip(
                plot_df[label_column],
                plot_df[ObjectTableLabels.TRANSIT],
                plot_df[ObjectTableLabels.ALTITUDE],
            ):
                ax.annotate(
                    text,
                    (x, y),
                    xytext=(5, 5),
                    textcoords="offset points",
                    color=style["TEXT_COLOR"],
                    **a_kwargs,
                )

            # Collect unique types for legend
            # Using casting on the method itself to bypass Pyright's overload resolution issues with Pandas
            unique_rows = cast(Any, plot_df).drop_duplicates(subset=["TranslatedType"])
            plotted_types = dict(
                zip(unique_rows["TranslatedType"], unique_rows["color"])
            )

        if observation.start is not None and observation.time_limit is not None:
            ax.set_xlim(
                [
                    observation.start - timedelta(minutes=15),
                    observation.time_limit + timedelta(minutes=15),
                ]
            )
        ax.set_ylim(0, 90)
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            observation.conditions.min_object_altitude,
            90,
            effective_dark_mode,
            style,
        )
        PlotUtils.annotate_plot(
            ax,
            gettext_("Altitude [°]"),
            effective_dark_mode,
            observation.place.local_timezone,
        )

        _add_legend(ax, plotted_types, style, legend_title)

        ax.set_title(title, color=style["TEXT_COLOR"])
        logger.info(logger_msg)
        return fig

    except Exception as e:
        return _handle_plot_error(
            fig, ax, e, effective_dark_mode, style, error_title, error_text, logger_error_msg
        )


def _generate_empty_plot(observation, fig, ax, effective_dark_mode, style, title, logger_msg):
    if observation.start is not None and observation.time_limit is not None:
        ax.set_xlim(
            [
                observation.start - timedelta(minutes=15),
                observation.time_limit + timedelta(minutes=15),
            ]
        )
    ax.set_ylim(0, 90)
    mark_observation(observation, ax, effective_dark_mode, style)
    mark_good_conditions(
        observation,
        ax,
        observation.conditions.min_object_altitude,
        90,
        effective_dark_mode,
        style,
    )
    PlotUtils.annotate_plot(
        ax,
        gettext_("Altitude [°]"),
        effective_dark_mode,
        observation.place.local_timezone,
    )
    ax.set_title(title, color=style["TEXT_COLOR"])
    logger.info(logger_msg)
    return fig


def _add_legend(ax, plotted_types, style, legend_title):
    legend_handles = [
        lines.Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            label=obj_type,
            markerfacecolor=color,
            markersize=10,
        )
        for obj_type, color in plotted_types.items()
    ]
    ax.legend(handles=legend_handles, title=legend_title)
    PlotUtils.style_legend(ax, style)


def _handle_plot_error(
    fig, ax, e, effective_dark_mode, style, error_title, error_text, logger_error_msg
):
    logger.error(f"{logger_error_msg}: {e}", exc_info=True)
    ax.clear()
    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    error_text_color = "#FF6B6B" if effective_dark_mode else "red"
    ax.text(
        0.5,
        0.5,
        error_text,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=12,
        color=error_text_color,
        wrap=True,
        transform=ax.transAxes,
    )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(error_title, color=style["TEXT_COLOR"])
    return fig
