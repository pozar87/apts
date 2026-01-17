import logging
from typing import Optional

import cairo as ca
import igraph as ig
import matplotlib.pyplot as plt
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


class Equipment:
    """
    This class represents all possessed astronomical equipment. Allows to compute all possible
    hardware configuration. It uses directed graph for internal processing.
    """

    def __init__(self):
        self.connection_garph = ig.Graph(directed=True)
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
        space_node = self.connection_garph.vs.find(name=GraphConstants.SPACE_ID)
        output_node = self.connection_garph.vs.find(name=output_id)
        results = []
        results_set = set()
        logger.debug(f"Space {space_node}, Output {output_node}")
        for optical_path in GenericUtils.find_all_paths(
            self.connection_garph, space_node.index, output_node.index
        ):
            logger.debug(f"Optical Path: {optical_path}")
            result: list[Optional[OpticalEquipment]] = [
                self.connection_garph.vs[id][NodeLabels.EQUIPMENT]
                for id in optical_path
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
        result = self._generate_data()
        if language is not None:
            with language_context(language):
                # Translate Type column
                result[EquipmentTableLabels.TYPE] = result[EquipmentTableLabels.TYPE].apply(
                    lambda x: gettext_(x.name) if isinstance(x, OpticalType) else x
                )
        else:
            # Default behavior (English/current context) - translate if needed or just convert to string
            result[EquipmentTableLabels.TYPE] = result[EquipmentTableLabels.TYPE].apply(
                lambda x: gettext_(x.name) if isinstance(x, OpticalType) else x
            )
        return result

    def _generate_data(self) -> pd.DataFrame:
        columns = [
            EquipmentTableLabels.LABEL,
            EquipmentTableLabels.TYPE,
            EquipmentTableLabels.ZOOM,
            EquipmentTableLabels.USEFUL_ZOOM,
            EquipmentTableLabels.FOV,
            EquipmentTableLabels.EXIT_PUPIL,
            EquipmentTableLabels.DAWES_LIMIT,
            EquipmentTableLabels.RANGE,
            EquipmentTableLabels.BRIGHTNESS,
            EquipmentTableLabels.ELEMENTS,
            EquipmentTableLabels.FLIPPED_HORIZONTALLY,
            EquipmentTableLabels.FLIPPED_VERTICALLY,
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
                is_binoculars = isinstance(path.telescope, (Binoculars, NakedEye))

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

                rows.append(
                    [
                        path.label(),
                        output_type_value,
                        path.zoom().magnitude,
                        useful_zoom_value,
                        path.fov().magnitude,
                        exit_pupil_value,
                        path.telescope.dawes_limit().magnitude,  # dawes_limit() in Binoculars/Telescope returns Quantity
                        path.telescope.limiting_magnitude(),  # limiting_magnitude() in Binoculars/Telescope returns float/int
                        path.brightness().magnitude,  # brightness() in OpticalPath returns Quantity
                        path.length(),  # length() in OpticalPath returns int
                        flipped_horizontally,
                        flipped_vertically,
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
            result["ID"] = []  # Initialize with empty list or appropriate empty type for ID
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
                plot.axhline(position, color=style["TEXT_COLOR"], linestyle="--", alpha=0.7)
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
        if data.empty:
            if not ax:
                subplot_args = {k: v for k, v in args.items() if k != "ax"}
                _, ax = plt.subplots(**subplot_args)
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

        legend = ax.legend(loc="upper right")
        if legend:  # Check if legend exists
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            if legend.get_title():  # Check if legend has a title
                legend.get_title().set_color(style["TEXT_COLOR"])
            for text, col in zip(legend.get_texts(), legend_labels):
                text.set_color(style["TEXT_COLOR"])
        return ax

    def _filter_and_merge(self, to_plot, multiline_labels, include_naked_eye=False):
        """
        This methods filter data to plot and merge Visual and Image series together
        """
        # Filter only relevant data - by to_plot key
        all_data = self._generate_data()
        if not include_naked_eye:
            all_data = all_data[all_data[EquipmentTableLabels.LABEL] != "Naked Eye 1x7"]

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

            if dark_mode_override is not None:
                effective_dark_mode = dark_mode_override
            else:
                effective_dark_mode = get_dark_mode()

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

            vertex_types = list(self.connection_garph.vs[NodeLabels.TYPE])  # Collect to log
            logger.debug(f"plot_connection_graph: Vertex NodeTypes = {vertex_types}")

            # Calculate vertex colors with a default for missing types (e.g., red to see if it's hit)
            # Using a distinct default like bright green (#00FF00) for debugging this specific issue
            # if the user reported "all red", this helps see if the default is hit.
            # The previous default was black. The user saw red. Let's use a new color for the default.
            vertex_colors_list = [
                current_node_colors.get(v_type, "#FF00FF") for v_type in vertex_types
            ]  # Magenta default
            logger.debug(
                f"plot_connection_graph: Calculated vertex_colors_list for direct assignment = {vertex_colors_list}"
            )

            # Determine general text color for labels
            text_color = current_plot_style.get(
                "TEXT_COLOR", "#000000"
            )  # Black default for text
            logger.debug(f"plot_connection_graph: text_color for labels = {text_color}")

            if len(self.connection_garph.vs) == len(vertex_colors_list):
                for i, color_val in enumerate(vertex_colors_list):
                    self.connection_garph.vs[i]["color"] = color_val
                    self.connection_garph.vs[i]["label_color"] = text_color
                    self.connection_garph.vs[i]["size"] = 20  # Default size
                    self.connection_garph.vs[i]["label_dist"] = (
                        1.5  # Default label distance
                    )
            else:
                logger.error(
                    "Mismatch between number of vertices and calculated colors. Skipping direct vertex property assignment."
                )

            background_color = current_plot_style.get(
                "BACKGROUND_COLOR", "#D3D3D3"
            )  # Light gray default for debugging background
            logger.debug(f"plot_connection_graph: background_color = {background_color}")

            edge_color_val = current_plot_style.get(
                "AXIS_COLOR", "#A9A9A9"
            )  # DarkGray default for debugging edges
            logger.debug(f"plot_connection_graph: edge_color_val = {edge_color_val}")

            # Call ig.plot(). Vertex-specific properties are now set on the graph itself.
            # Pass general styling for background and edges.
            return ig.plot(
                self.connection_garph,
                margin=80,
                background=background_color,
                edge_color=edge_color_val,
                # vertex_color, vertex_label_color, vertex_size, vertex_label_dist
                # are now set directly on graph.vs attributes.
                **args,
            )

    def plot_connection_graph_svg(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        surface = ca.ImageSurface(ca.FORMAT_ARGB32, 800, 600)
        # Pass dark_mode_override to the plot_connection_graph call
        plot = self.plot_connection_graph(
            target=surface,
            dark_mode_override=dark_mode_override,
            language=language,
            **args,
        )
        return plot._repr_svg_()[0]  # SVG string is first in tuple

    def _connect(self):
        if self._connected:
            return
        logger.debug("Connecting nodes")
        for out_node in self.connection_garph.vs.select(node_type=OpticalType.OUTPUT):
            # Get output type
            connection_type = out_node[NodeLabels.CONNECTION_TYPE]
            for in_node in self.connection_garph.vs.select(
                node_type=OpticalType.INPUT, connection_type=connection_type
            ):
                # Connect all outputs with all inputs, excluding connecting part to itself
                out_id = OpticalEquipment.get_parent_id(out_node[NodeLabels.NAME])
                in_id = OpticalEquipment.get_parent_id(in_node[NodeLabels.NAME])
                if out_id != in_id:
                    self.add_edge(out_node, in_node)
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
        self.connection_garph.add_vertex(node_name, label_dist=1.5)
        node = self.connection_garph.vs.find(name=node_name)

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

        return node

    def add_edge(self, node_from, node_to):
        logger.debug(f"Adding edge {node_from} -> {node_to}")
        # Add edge if only it doesn't exist
        # Check if an edge already exists. igraph's are_connected expects vertex IDs.
        # error=False ensures it returns a special value (like -1 or an invalid EID)
        # if no edge exists, instead of raising an error.
        # We consider directedness based on the graph type.

        source_id = node_from if isinstance(node_from, str) else node_from.index
        target_id = node_to if isinstance(node_to, str) else node_to.index

        existing_edge = self.connection_garph.get_eid(
            source_id, target_id, directed=True, error=False
        )
        if existing_edge < 0:  # An edge ID is non-negative if it exists
            self.connection_garph.add_edge(source_id, target_id)

    def register(self, optical_eqipment):
        """
        Register any optical equipment in a optical graph.
        """
        optical_eqipment.register(self)