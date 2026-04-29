import logging
from datetime import timedelta
from typing import TYPE_CHECKING, Any, Optional, cast

import pandas as pd
from matplotlib import lines, pyplot

from apts.config import get_dark_mode
from apts.constants.graphconstants import (
    get_messier_color,
    get_plot_style,
)
from apts.i18n import gettext_
from apts.plotting.utils import mark_good_conditions, mark_observation
from apts.utils.plot import Utils as PlotUtils
from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation

logger = logging.getLogger(__name__)


def generate_plot_messier(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    ax = args.pop("ax", None)
    fig = None
    if ax:
        fig = ax.figure
    else:
        fig, ax = pyplot.subplots(figsize=(18, 12), **args)

    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    try:
        messier_df = observation.get_visible_messier().copy()

        if len(messier_df) == 0:
            return _generate_empty_messier_plot(
                observation, fig, ax, effective_dark_mode, style
            )

        # Vectorized property extraction to avoid slow iterrows()
        # Ensure numeric columns are floats to avoid Pint/Quantity overhead
        for col in [
            ObjectTableLabels.ALTITUDE,
            ObjectTableLabels.SIZE_MAJOR,
            ObjectTableLabels.SIZE_MINOR,
        ]:
            if col in messier_df.columns:
                messier_df[col] = [
                    getattr(x, "magnitude", x) for x in messier_df[col].values
                ]

        # Vectorized marker size: marker area (s) as width * height
        messier_df["marker_size"] = (
            messier_df[ObjectTableLabels.SIZE_MAJOR]
            * messier_df[ObjectTableLabels.SIZE_MINOR]
        )

        # Determine colors (Type is often already translated in get_visible_messier)
        types = (
            messier_df["Type"].fillna("Other")
            if "Type" in messier_df.columns
            else pd.Series("Other", index=messier_df.index)
        )
        messier_df["TranslatedType"] = [gettext_(t) for t in types]
        messier_df["color"] = [
            get_messier_color(t, effective_dark_mode)
            for t in messier_df["TranslatedType"]
        ]

        # Filter out objects without a valid transit time in the window
        plot_df = messier_df[messier_df[ObjectTableLabels.TRANSIT].notna()].copy()

        plotted_types = {}
        if not plot_df.empty:
            # Single vectorized scatter call for all objects
            ax.scatter(
                plot_df[ObjectTableLabels.TRANSIT],
                plot_df[ObjectTableLabels.ALTITUDE],
                s=plot_df["marker_size"],
                marker="o",
                c=plot_df["color"],
            )

            # Annotation loop optimized to avoid iterrows()
            for text, x, y in zip(
                plot_df[ObjectTableLabels.MESSIER],
                plot_df[ObjectTableLabels.TRANSIT],
                plot_df[ObjectTableLabels.ALTITUDE],
            ):
                ax.annotate(
                    text,
                    (x, y),
                    xytext=(5, 5),
                    textcoords="offset points",
                    color=style["TEXT_COLOR"],
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

        _add_messier_legend(ax, plotted_types, style)

        ax.set_title(gettext_("Messier Objects Altitude"), color=style["TEXT_COLOR"])
        logger.info(gettext_("Successfully generated Messier plot."))
        return fig

    except Exception as e:
        return _handle_messier_plot_error(fig, ax, e, effective_dark_mode, style)


def _generate_empty_messier_plot(observation, fig, ax, effective_dark_mode, style):
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
    ax.set_title(gettext_("Messier Objects Altitude"), color=style["TEXT_COLOR"])
    logger.info(gettext_("Generated empty Messier plot as no objects are visible."))
    return fig


def _add_messier_legend(ax, plotted_types, style):
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
    ax.legend(handles=legend_handles, title=gettext_("Object Types"))
    PlotUtils.style_legend(ax, style)


def _handle_messier_plot_error(fig, ax, e, effective_dark_mode, style):
    logger.error(f"Error generating Messier plot: {e}", exc_info=True)
    ax.clear()
    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    error_text_color = "#FF6B6B" if effective_dark_mode else "red"
    ax.text(
        0.5,
        0.5,
        gettext_("Error generating Messier plot.\nSee logs for details."),
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=12,
        color=error_text_color,
        wrap=True,
        transform=ax.transAxes,
    )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(gettext_("Messier Plot Error"), color=style["TEXT_COLOR"])
    return fig
