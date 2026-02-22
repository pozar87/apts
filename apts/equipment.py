import io
import logging
from typing import Optional

import numpy
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from matplotlib.ticker import FuncFormatter

from .config import get_dark_mode
from .constants import EquipmentTableLabels, GraphConstants, NodeLabels, OpticalType
from .constants.graphconstants import get_plot_colors, get_plot_style
from .i18n import gettext_, language_context
from .opticalequipment import (
    NakedEye,
    OpticalEquipment,
)
from .optics import OpticalPath
from .utils import Utils as GenericUtils
from .utils.plot import Utils as PlotUtils

logger = logging.getLogger(__name__)


class MatplotlibSVGWrapper:
    def __init__(self, fig):
        self.fig = fig

    def _repr_svg_(self):
        output = io.StringIO()
        self.fig.savefig(
            output,
            format="svg",
            facecolor=self.fig.get_facecolor(),
            edgecolor="none",
            transparent=False,
        )
        plt.close(self.fig)
        return (output.getvalue(),)


class Equipment:
    """
    This class represents all possessed astronomical equipment. Allows to compute all possible
    hardware configuration. It uses directed graph for internal processing.
    """

    def __init__(self):
        self.connection_garph = nx.DiGraph()
        # Register standard input and outputs
        self.add_vertex(GraphConstants.SPACE_ID)
        self.add_vertex(GraphConstants.EYE_ID, node_type=OpticalType.VISUAL)
        self.add_vertex(GraphConstants.IMAGE_ID, node_type=OpticalType.IMAGE)
        self.register(NakedEye())
        self._connected = False

    def _get_paths(self, output_id):
        # Connect all outputs with inputs
        self._connect()
        # Find input and output nodes
        results = []
        results_set = set()
        logger.debug(f"Space {GraphConstants.SPACE_ID}, Output {output_id}")
        for optical_path in GenericUtils.find_all_paths(
            self.connection_garph, GraphConstants.SPACE_ID, output_id
        ):
            logger.debug(f"Optical Path: {optical_path}")
            result: list[Optional[OpticalEquipment]] = [
                self.connection_garph.nodes[node_id][NodeLabels.EQUIPMENT]
                for node_id in optical_path
            ]
            op = OpticalPath.from_path([item for item in result if item is not None])  # pyright: ignore
            if op.elements() not in results_set:
                results_set.add(op.elements())
                results.append(op)
        return results

    def get_zooms(self, node_id) -> list[float]:
        """
        Compute all possible zooms
        :param node_id:
        :return: sorted list of zooms
        """
        result = [path.zoom().magnitude for path in self._get_paths(node_id)]
        result.sort()
        return result

    def data(self, language: Optional[str] = None) -> pd.DataFrame:
        with language_context(language):
            result = self._generate_data()
            # Translate Type column
            result[EquipmentTableLabels.TYPE] = result[EquipmentTableLabels.TYPE].apply(
                lambda x: gettext_(x.name) if isinstance(x, OpticalType) else x
            )
            # Remove internal columns
            if EquipmentTableLabels.IS_NAKED_EYE in result.columns:
                result = result.drop(columns=[EquipmentTableLabels.IS_NAKED_EYE])
        return result

    def _generate_data(self) -> pd.DataFrame:
        columns = [
            EquipmentTableLabels.LABEL,
            EquipmentTableLabels.TYPE,
            EquipmentTableLabels.ZOOM,
            EquipmentTableLabels.USEFUL_ZOOM,
            EquipmentTableLabels.FOV,
            EquipmentTableLabels.FOV_W,
            EquipmentTableLabels.FOV_H,
            EquipmentTableLabels.FOV_D,
            EquipmentTableLabels.EXIT_PUPIL,
            EquipmentTableLabels.DAWES_LIMIT,
            EquipmentTableLabels.RANGE,
            EquipmentTableLabels.BRIGHTNESS,
            EquipmentTableLabels.ELEMENTS,
            EquipmentTableLabels.FLIPPED_HORIZONTALLY,
            EquipmentTableLabels.FLIPPED_VERTICALLY,
            EquipmentTableLabels.PIXEL_SCALE,
            EquipmentTableLabels.SAMPLING,
            EquipmentTableLabels.NPF_RULE,
            EquipmentTableLabels.RULE_OF_500,
            EquipmentTableLabels.CRITICAL_FOCUS_ZONE,
            EquipmentTableLabels.IS_NAKED_EYE,
        ]

        # Import Binoculars here to keep it local to where it's used for isinstance
        # and avoid potential circular imports if Binoculars ever needed Equipment.
        from .opticalequipment.binoculars import Binoculars

        def append(result_data, paths):
            rows = []
            logging.debug(f"Appending paths {paths}")
            for path in paths:
                # path.telescope is the main optic (telescope or binoculars)
                # path.output is the final element (eyepiece, camera, or binoculars itself)

                # Determine if the main optic is Binoculars or NakedEye
                is_naked_eye = isinstance(path.telescope, NakedEye)
                is_binoculars = isinstance(path.telescope, Binoculars) or is_naked_eye

                # Calculate useful_zoom
                useful_zoom_value = True  # Default for binoculars and naked eye
                if not is_binoculars:
                    if hasattr(path.telescope, "max_useful_zoom"):
                        # max_useful_zoom() on Telescope returns a float, zoom() is a Quantity
                        useful_zoom_value = (
                            path.zoom().magnitude < path.telescope.max_useful_zoom()
                        )
                    else:
                        useful_zoom_value = (
                            False  # Should not happen for Telescope objects
                        )

                # Get output type. For Binoculars, path.output is the Binocular instance.
                output_type_value = path.output.output_type()

                # Calculate Exit Pupil
                # path.exit_pupil() now returns a Quantity (e.g., mm)
                exit_pupil_value = path.exit_pupil().to("mm").magnitude
                if exit_pupil_value < 0:  # Guard against potential negative values
                    exit_pupil_value = 0

                flipped_horizontally, flipped_vertically = path.get_image_orientation()

                # Pixel Scale
                pixel_scale_value = path.pixel_scale()
                if pixel_scale_value is not None:
                    pixel_scale_magnitude = pixel_scale_value.magnitude
                else:
                    pixel_scale_magnitude = numpy.nan

                # NPF Rule
                npf_value = path.npf_rule()
                if npf_value is not None:
                    npf_magnitude = npf_value.magnitude
                else:
                    npf_magnitude = numpy.nan

                # Rule of 500
                r500_value = path.rule_of_500()
                if r500_value is not None:
                    r500_magnitude = r500_value.magnitude
                else:
                    r500_magnitude = numpy.nan

                # Sampling status (default seeing 2.0")
                sampling_value = path.sampling_status(seeing=2.0)

                # Critical Focus Zone
                cfz_value = path.critical_focus_zone()
                if cfz_value is not None:
                    cfz_magnitude = cfz_value.magnitude
                else:
                    cfz_magnitude = numpy.nan

                rows.append(
                    [
                        path.label(),
                        output_type_value,
                        path.zoom().magnitude,
                        useful_zoom_value,
                        path.fov().magnitude,
                        path.fov_width().magnitude,
                        path.fov_height().magnitude,
                        path.fov_diagonal().magnitude,
                        exit_pupil_value,
                        path.telescope.dawes_limit().magnitude,  # dawes_limit() in Binoculars/Telescope returns Quantity
                        path.telescope.limiting_magnitude(),  # limiting_magnitude() in Binoculars/Telescope returns float/int
                        path.brightness().magnitude,  # brightness() in OpticalPath returns Quantity
                        path.length(),  # length() in OpticalPath returns int
                        flipped_horizontally,
                        flipped_vertically,
                        pixel_scale_magnitude,
                        sampling_value,
                        npf_magnitude,
                        r500_magnitude,
                        cfz_magnitude,
                        is_naked_eye,
                    ]
                )

            if rows:
                new_data = pd.DataFrame(rows, columns=columns)  # pyright: ignore
                if result_data.empty:
                    result_data = new_data
                else:
                    for col in result_data.columns:
                        if result_data[col].dtype != new_data[col].dtype:
                            # Try to convert new_data's column to result_data's dtype if they are compatible
                            try:
                                new_data[col] = new_data[col].astype(
                                    result_data[col].dtype
                                )
                            except Exception as e:
                                logging.warning(
                                    f"Could not align dtype for column {col}: {e}. This might lead to concat issues."
                                )
                    result_data = pd.concat([result_data, new_data], ignore_index=True)  # pyright: ignore
            return result_data

        result = pd.DataFrame(columns=columns)  # pyright: ignore
        # Get paths from both visual and image outputs
        visual_paths = self._get_paths(GraphConstants.EYE_ID)
        image_paths = self._get_paths(GraphConstants.IMAGE_ID)

        # Combine paths and remove duplicates across both visual and image paths
        # Use path elements as the uniqueness criterion to avoid duplicates
        all_paths = []
        seen_elements = set()

        # First add image paths (these include smart telescopes)
        for path in image_paths:
            if path.elements() not in seen_elements:
                seen_elements.add(path.elements())
                all_paths.append(path)

        # Then add visual paths, but skip any that have elements already seen
        for path in visual_paths:
            if path.elements() not in seen_elements:
                seen_elements.add(path.elements())
                all_paths.append(path)

        result = append(result, all_paths)

        # Add ID column as first
        if not result.empty:  # Only add ID if DataFrame is not empty
            result["ID"] = result.index
            result = result[["ID"] + columns]
        else:  # If empty, ensure ID column exists for consistency if expected by other code
            result[
                "ID"
            ] = []  # Initialize with empty list or appropriate empty type for ID
            result = result[["ID"] + columns]

        return result  # pyright: ignore

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

    def max_zoom(self):
        """
        Max useful zoom due to atmosphere
        """
        return 350

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
                return GenericUtils.decdeg2dms(tick, pretty=True)

            def add_line(description, position):
                position = GenericUtils.dms2decdeg(position)
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
        import matplotlib.pyplot as plt

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

    def plot_connection_graph(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            # Connect all outputs with inputs
            self._connect()

            effective_dark_mode = dark_mode_override if dark_mode_override is not None else get_dark_mode()
            current_plot_style = get_plot_style(effective_dark_mode)
            current_node_colors = get_plot_colors(effective_dark_mode)

            logger.debug(
                f"plot_connection_graph: effective_dark_mode = {effective_dark_mode}"
            )
            logger.debug(
                f"plot_connection_graph: current_plot_style = {current_plot_style}"
            )
            logger.debug(
                f"plot_connection_graph: current_node_colors = {current_node_colors}"
            )

            # Create a simplified graph for visualization by removing technical IN/OUT nodes
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

            node_data = plot_graph.nodes(data=True)

            # Calculate vertex colors with a default for missing types
            vertex_colors_list = [
                current_node_colors.get(data.get(NodeLabels.TYPE), "#FF00FF")
                for _, data in node_data
            ]
            logger.debug(
                f"plot_connection_graph: Calculated vertex_colors_list = {vertex_colors_list}"
            )

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

            try:
                # Calculate layers for multipartite layout
                # Categorize nodes into logical steps of the optical path
                layers = {}

                # Import equipment classes locally to avoid circular dependencies
                from .opticalequipment.barlow import Barlow
                from .opticalequipment.binoculars import Binoculars
                from .opticalequipment.camera import Camera
                from .opticalequipment.diagonal import Diagonal
                from .opticalequipment.eyepiece import Eyepiece
                from .opticalequipment.filter import Filter
                from .opticalequipment.naked_eye import NakedEye
                from .opticalequipment.smart_telescope import SmartTelescope
                from .opticalequipment.telescope import Telescope

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

                pos = nx.multipartite_layout(plot_graph, subset_key="layer")
            except Exception as e:
                logger.warning(f"Failed to calculate multipartite layout: {e}")
                pos = nx.kamada_kawai_layout(plot_graph)

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

            fig.patch.set_facecolor(figure_face_color)
            ax.set_facecolor(axes_face_color)

            return MatplotlibSVGWrapper(fig)

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

    def _connect(self):
        if self._connected:
            return
        logger.debug("Connecting nodes")
        for out_node_id, out_node_data in self.connection_garph.nodes(data=True):
            if out_node_data.get(NodeLabels.TYPE) == OpticalType.OUTPUT:
                # Get output type
                connection_type = out_node_data[NodeLabels.CONNECTION_TYPE]
                for in_node_id, in_node_data in self.connection_garph.nodes(data=True):
                    if (
                        in_node_data.get(NodeLabels.TYPE) == OpticalType.INPUT
                        and in_node_data.get(NodeLabels.CONNECTION_TYPE)
                        == connection_type
                    ):
                        # Connect all outputs with all inputs, excluding connecting part to itself
                        out_id = OpticalEquipment.get_parent_id(
                            out_node_data[NodeLabels.NAME]
                        )
                        in_id = OpticalEquipment.get_parent_id(
                            in_node_data[NodeLabels.NAME]
                        )
                        if out_id != in_id:
                            self.add_edge(out_node_id, in_node_id)
        logger.debug(self.connection_garph)
        self._connected = True

    def add_vertex(
        self,
        node_name,
        equipment=None,
        node_type=OpticalType.GENERIC,
        connection_type=None,
    ):
        """
        Add single node to graph. Return new vertex.
        """
        logger.debug(f"Adding vertex {node_name}")
        self.connection_garph.add_node(node_name, label_dist=1.5)
        node = self.connection_garph.nodes[node_name]

        if equipment is not None:
            node_type = equipment.type()
            node_label = "\n".join([equipment.get_name(), equipment.label()])
        elif (
            node_type == OpticalType.GENERIC
            or node_type == OpticalType.VISUAL
            or node_type == OpticalType.IMAGE
        ):
            node_label = node_name
        elif node_type == OpticalType.INPUT:
            node_label = str(connection_type) + " " + OpticalEquipment.IN
        elif node_type == OpticalType.OUTPUT:
            node_label = str(connection_type) + " " + OpticalEquipment.OUT
        else:
            node_label = ""

        node[NodeLabels.TYPE] = node_type
        node[NodeLabels.LABEL] = node_label
        node[NodeLabels.EQUIPMENT] = equipment
        node[NodeLabels.CONNECTION_TYPE] = connection_type
        node[NodeLabels.NAME] = node_name

        return node

    def add_edge(self, node_from, node_to):
        logger.debug(f"Adding edge {node_from} -> {node_to}")
        # Add edge if only it doesn't exist

        source_id = (
            node_from if isinstance(node_from, str) else node_from[NodeLabels.NAME]
        )
        target_id = node_to if isinstance(node_to, str) else node_to[NodeLabels.NAME]

        if not self.connection_garph.has_edge(source_id, target_id):
            self.connection_garph.add_edge(source_id, target_id)

    def register(self, optical_eqipment):
        """
        Register any optical equipment in a optical graph.
        """
        optical_eqipment.register(self)
