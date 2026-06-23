import logging
from typing import TYPE_CHECKING, Optional

import matplotlib.pyplot as plt
import networkx as nx

from ...config import get_dark_mode
from ...constants import GraphConstants, NodeLabels, OpticalType
from ...constants.graphconstants import get_plot_colors, get_plot_style
from ...i18n import language_context
from ..models import MatplotlibSVGWrapper
from .base import BaseEquipmentPlottingMixIn

if TYPE_CHECKING:
    import networkx as nx

logger = logging.getLogger(__name__)


class GraphEquipmentPlottingMixIn(BaseEquipmentPlottingMixIn):
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

            for node_id, data in node_data:
                equipment = data.get(NodeLabels.EQUIPMENT)

                if node_id == GraphConstants.SPACE_ID:
                    layers[node_id] = 0
                elif node_id in [GraphConstants.EYE_ID, GraphConstants.IMAGE_ID]:
                    layers[node_id] = 6  # Final sinks - own column
                elif equipment is not None:
                    # Use polymorphic path_layer attribute if available
                    layers[node_id] = getattr(equipment, "path_layer", 3)
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

        return (
            fig,
            ax,
            current_node_colors,
            text_color,
            edge_color_val,
            figure_face_color,
            axes_face_color,
        )

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
                figure_face_color,
                axes_face_color,
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

            # Note: nx.draw might reset the figure facecolor, so we re-apply it here
            fig.patch.set_facecolor(figure_face_color)
            ax.set_facecolor(axes_face_color)

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
