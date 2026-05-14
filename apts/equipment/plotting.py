import logging
from typing import Optional, TYPE_CHECKING

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from matplotlib.ticker import FuncFormatter

if TYPE_CHECKING:
    import networkx as nx

from ..config import get_dark_mode
from ..constants import EquipmentTableLabels, GraphConstants, NodeLabels, OpticalType
from ..constants.graphconstants import get_plot_colors, get_plot_style
from ..i18n import gettext_, language_context
from ..utils import decdeg2dms, dms2decdeg
from ..utils.plot import PlotUtils
from .models import MatplotlibSVGWrapper

logger = logging.getLogger(__name__)

class EquipmentPlottingMixIn:
    if TYPE_CHECKING:
        def max_zoom(self) -> float: ...
        def _generate_data(self) -> pd.DataFrame: ...
        def _connect(self) -> None: ...
        connection_garph: "nx.DiGraph"

    def plot_zoom(
        self,
        dark_mode_override: Optional[bool] = None,
        include_naked_eye: bool = False,
        language: Optional[str] = None,
        **args,
    ):
        """
        Plot available magnification
        """
        with language_context(language):
            if dark_mode_override is not None:
                effective_dark_mode = dark_mode_override
            else:
                effective_dark_mode = get_dark_mode()
            plot = self._plot(
                EquipmentTableLabels.ZOOM,
                gettext_("Available zoom"),
                gettext_("Used equipment"),
                gettext_("Magnification"),
                dark_mode_enabled=effective_dark_mode,
                include_naked_eye=include_naked_eye,
                **args,
            )
            # Add marker for maximal useful zoom
            style = get_plot_style(effective_dark_mode)  # Get style for the annotations
            max_zoom = self.max_zoom()
            plot.axhline(max_zoom, color=style["TEXT_COLOR"], linestyle="--", alpha=0.7)
            plot.annotate(
                gettext_("Max useful zoom due to atmosphere"),
                (-0.4, max_zoom + 2),
                alpha=0.7,
                color=style["TEXT_COLOR"],
            )

    def plot_fov(
        self,
        dark_mode_override: Optional[bool] = None,
        include_naked_eye: bool = False,
        language: Optional[str] = None,
        **args,
    ):
        """
        Plot available fields of view
        """
        with language_context(language):
            if dark_mode_override is not None:
                effective_dark_mode = dark_mode_override
            else:
                effective_dark_mode = get_dark_mode()

            style = get_plot_style(effective_dark_mode)

            def formatter(tick, pos):
                return decdeg2dms(tick, pretty=True)

            def add_line(description, position):
                position = dms2decdeg(position)
                plot.axhline(
                    position, color=style["TEXT_COLOR"], linestyle="--", alpha=0.7
                )
                plot.annotate(
                    description,
                    (-0.4, position + 0.03),
                    alpha=0.7,
                    color=style["TEXT_COLOR"],
                )

            plot = self._plot(
                EquipmentTableLabels.FOV,
                gettext_("Available fields of view"),
                gettext_("Used equipment"),
                gettext_("Field of view [°]"),
                dark_mode_enabled=effective_dark_mode,
                include_naked_eye=include_naked_eye,
                **args,
            )
            plot.yaxis.set_major_formatter(FuncFormatter(formatter))
            # Pleiades width is 1°50'
            add_line(gettext_("Pleiades size"), (1, 50, 0))
            # Average moon size is 0°31'42"
            add_line(gettext_("Moon size"), (0, 31, 42))
            # M51 width is 0°11'
            add_line(gettext_("M51 size"), (0, 11, 0))

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

    def _get_simplified_connection_graph(self) -> "nx.DiGraph":
        """
        Create a simplified graph for visualization by removing technical IN/OUT nodes
        """
        plot_graph = self.connection_garph.copy()
        nodes_to_remove = [
            n
            for n, d in plot_graph.nodes(data=True)
            if d.get(NodeLabels.TYPE) in [OpticalType.INPUT, OpticalType.OUTPUT]
        ]
        for n in nodes_to_remove:
            preds = list(plot_graph.predecessors(n))
            succs = list(plot_graph.successors(n))
            for p in preds:
                for s in succs:
                    plot_graph.add_edge(p, s)
            plot_graph.remove_node(n)
        return plot_graph

    def _calculate_graph_layout(self, plot_graph: "nx.DiGraph") -> dict:
        """
        Calculate layers for multipartite layout
        """
        node_data = plot_graph.nodes(data=True)
        try:
            # Categorize nodes into logical steps of the optical path
            layers = {}

            # Import equipment classes locally to avoid circular dependencies
            from ..opticalequipment.barlow import Barlow
            from ..opticalequipment.binoculars import Binoculars
            from ..opticalequipment.camera import Camera
            from ..opticalequipment.diagonal import Diagonal
            from ..opticalequipment.eyepiece import Eyepiece
            from ..opticalequipment.filter import Filter
            from ..opticalequipment.naked_eye import NakedEye
            from ..opticalequipment.smart_telescope import SmartTelescope
            from ..opticalequipment.telescope import Telescope

            for node_id, data in node_data:
                equipment = data.get(NodeLabels.EQUIPMENT)

                if node_id == GraphConstants.SPACE_ID:
                    layers[node_id] = 0
                elif node_id in [GraphConstants.EYE_ID, GraphConstants.IMAGE_ID]:
                    layers[node_id] = 4  # Final sinks
                elif equipment is not None:
                    # Main equipment nodes
                    if isinstance(
                        equipment, (Telescope, Binoculars, NakedEye, SmartTelescope)
                    ):
                        layers[node_id] = 1
                    elif isinstance(equipment, (Barlow, Diagonal, Filter)):
                        layers[node_id] = 2
                    elif isinstance(equipment, (Eyepiece, Camera)):
                        layers[node_id] = 3
                    else:
                        layers[node_id] = 2
                else:
                    layers[node_id] = 2

            # Assign layer attribute to nodes (must be integer for multipartite_layout)
            for node_id, layer in layers.items():
                plot_graph.nodes[node_id]["layer"] = int(layer)

            return nx.multipartite_layout(plot_graph, subset_key="layer")
        except Exception as e:
            logger.warning(f"Failed to calculate multipartite layout: {e}")
            return nx.kamada_kawai_layout(plot_graph)

    def _setup_graph_axes(self, dark_mode_enabled: bool):
        """
        Create the Matplotlib figure and axes for the connection graph
        """
        current_plot_style = get_plot_style(dark_mode_enabled)
        current_node_colors = get_plot_colors(dark_mode_enabled)

        # Determine general colors from style
        text_color = current_plot_style.get("TEXT_COLOR", "#000000")
        figure_face_color = current_plot_style.get("FIGURE_FACE_COLOR", "#D3D3D3")
        axes_face_color = current_plot_style.get("AXES_FACE_COLOR", figure_face_color)
        edge_color_val = current_plot_style.get("AXIS_COLOR", "#A9A9A9")

        fig, ax = plt.subplots(
            figsize=(10, 8), facecolor=figure_face_color, edgecolor="none"
        )
        fig.patch.set_facecolor(figure_face_color)
        ax.set_facecolor(axes_face_color)
        ax.axis("off")

        return fig, ax, current_node_colors, text_color, edge_color_val

    def plot_connection_graph(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            # Connect all outputs with inputs
            self._connect()

            effective_dark_mode = (
                dark_mode_override
                if dark_mode_override is not None
                else get_dark_mode()
            )

            # 1. Create a simplified graph for visualization
            plot_graph = self._get_simplified_connection_graph()
            node_data = plot_graph.nodes(data=True)

            # 2. Setup figure and axes with appropriate styles
            (
                fig,
                ax,
                current_node_colors,
                text_color,
                edge_color_val,
            ) = self._setup_graph_axes(effective_dark_mode)

            # 3. Calculate vertex colors
            vertex_colors_list = [
                current_node_colors.get(data.get(NodeLabels.TYPE), "#FF00FF")
                for _, data in node_data
            ]

            # 4. Calculate layout
            pos = self._calculate_graph_layout(plot_graph)

            # 5. Draw the graph
            nx.draw(
                plot_graph,
                pos,
                ax=ax,
                with_labels=True,
                labels={
                    node_id: data.get(NodeLabels.LABEL, "")
                    for node_id, data in node_data
                },
                node_color=vertex_colors_list,
                node_size=2000,
                edge_color=edge_color_val,
                font_color=text_color,
                font_size=8,
            )

            return MatplotlibSVGWrapper(fig)

    def plot_connection_graph_svg(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        # Pass dark_mode_override to the plot_connection_graph call
        plot = self.plot_connection_graph(
            dark_mode_override=dark_mode_override,
            language=language,
            **args,
        )
        return plot._repr_svg_()[0]  # SVG string is first in tuple
