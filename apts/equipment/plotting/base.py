import logging
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import pandas as pd

from ...constants import EquipmentTableLabels, OpticalType
from ...constants.graphconstants import get_plot_colors, get_plot_style
from ...i18n import gettext_
from ...utils.plot import PlotUtils

if TYPE_CHECKING:
    import networkx as nx

logger = logging.getLogger(__name__)


class BaseEquipmentPlottingMixIn:
    if TYPE_CHECKING:

        def max_zoom(self) -> float: ...
        def _generate_data(self) -> pd.DataFrame: ...
        def _connect(self) -> None: ...

        connection_garph: "nx.DiGraph"

    def _plot(
        self,
        to_plot,
        title,
        x_label,
        y_label,
        dark_mode_enabled: bool,
        autolayout=False,
        multiline_labels=True,
        include_naked_eye=False,
        **args,
    ):
        style = get_plot_style(dark_mode_enabled)
        colors = get_plot_colors(dark_mode_enabled)
        data, legend_labels = self._filter_and_merge(
            to_plot, multiline_labels, include_naked_eye
        )

        if autolayout:
            plt.rcParams.update({"figure.autolayout": True})

        ax = args.get("ax")
        if not ax:
            subplot_args = {k: v for k, v in args.items() if k != "ax"}
            # Ensure correct background for the figure from the start
            fig, ax = plt.subplots(
                facecolor=style["FIGURE_FACE_COLOR"], edgecolor="none", **subplot_args
            )
            args["ax"] = ax

        if data.empty:
            return PlotUtils.plot_no_data(ax, title, dark_mode_enabled)

        # Pass title as None initially, then set it with color
        ax = data.plot(
            kind="bar",
            title=None,
            stacked=True,
            color=[colors.get(c, "#CCCCCC") for c in legend_labels],
            **args,
        )
        fig = ax.figure  # Get the figure object
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

        ax.set_title(title, color=style["TEXT_COLOR"])  # Set title color
        ax.set_xlabel(x_label, color=style["TEXT_COLOR"])
        ax.set_ylabel(y_label, color=style["TEXT_COLOR"])

        ax.tick_params(axis="x", colors=style["TICK_COLOR"])
        ax.tick_params(axis="y", colors=style["TICK_COLOR"])

        ax.spines["bottom"].set_color(style["AXIS_COLOR"])
        ax.spines["top"].set_color(style["AXIS_COLOR"])
        ax.spines["left"].set_color(style["AXIS_COLOR"])
        ax.spines["right"].set_color(style["AXIS_COLOR"])

        ax.legend(loc="upper right")
        PlotUtils.style_legend(ax, style)
        return ax

    def _filter_and_merge(self, to_plot, multiline_labels, include_naked_eye=False):
        """
        This methods filter data to plot and merge Visual and Image series together
        """
        # Filter only relevant data - by to_plot key
        all_data = self._generate_data()
        if not include_naked_eye:
            all_data = all_data[~all_data[EquipmentTableLabels.IS_NAKED_EYE]]

        data = all_data[
            [to_plot, EquipmentTableLabels.TYPE, EquipmentTableLabels.LABEL]
        ].sort_values(by=to_plot)  # pyright: ignore

        if len(data) <= 8:
            # Split label by ',' if multiline_labels is set to true
            labels = [
                label.replace(",", "\n") if multiline_labels else label
                for label in data[EquipmentTableLabels.LABEL].values
            ]
        else:
            # For more than 8 option display only ids
            labels = data.index

        # Prepare rows where keys are Enums
        rows_list = [{row[1]: row[0]} for row in data.values]
        # Create DataFrame with Enums as columns
        result_df = pd.DataFrame(rows_list, index=labels)  # pyright: ignore

        # Get the columns (Enums) to return for color mapping
        # Note: result_df.columns will be unique and sorted/ordered by pandas based on insertion
        columns_enums = result_df.columns.tolist()

        # Translate columns for display
        new_columns = [
            gettext_(c.name) if isinstance(c, OpticalType) else str(c)
            for c in columns_enums
        ]
        result_df.columns = new_columns  # pyright: ignore

        return result_df, columns_enums
