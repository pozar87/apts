import logging
from typing import Optional

import networkx as nx
import numpy
import pandas as pd

from ..constants import EquipmentTableLabels, GraphConstants, NodeLabels, OpticalType
from ..i18n import gettext_, language_context
from ..opticalequipment import (
    NakedEye,
    OpticalEquipment,
)
from ..optics import OpticalPath
from ..utils import ConnectionType
from ..utils import find_all_paths
from .plotting import EquipmentPlottingMixIn

logger = logging.getLogger(__name__)


class Equipment(EquipmentPlottingMixIn):
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

    def _get_paths(self, output_ids):
        """
        Find all unique optical paths to the given output IDs.
        """
        # Connect all outputs with inputs
        self._connect()

        if not isinstance(output_ids, list):
            output_ids = [output_ids]

        # Find input and output nodes
        results = []
        # Store frozenset of equipment to avoid redundant path creation
        seen_equipment_sets = set()

        logger.debug(f"Space {GraphConstants.SPACE_ID}, Outputs {output_ids}")
        for optical_path in find_all_paths(
            self.connection_garph, GraphConstants.SPACE_ID, output_ids
        ):
            logger.debug(f"Optical Path: {optical_path}")
            # Get equipment objects in the path
            equipment_list: list[OpticalEquipment] = [
                self.connection_garph.nodes[node_id][NodeLabels.EQUIPMENT]
                for node_id in optical_path
                if self.connection_garph.nodes[node_id][NodeLabels.EQUIPMENT] is not None
            ]

            # Use frozenset for early uniqueness check
            equipment_set = frozenset(equipment_list)
            if equipment_set not in seen_equipment_sets:
                seen_equipment_sets.add(equipment_set)
                # Only create OpticalPath if it's unique
                op = OpticalPath.from_path(equipment_list)
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
            # Translate Type column using vectorized mapping
            # Get unique types to minimize gettext calls
            unique_types = result[EquipmentTableLabels.TYPE].unique()
            translation_map = {
                t: (gettext_(t.name) if isinstance(t, OpticalType) else t)
                for t in unique_types
            }
            result[EquipmentTableLabels.TYPE] = result[EquipmentTableLabels.TYPE].map(
                translation_map.get
            )

            # Remove internal columns
            if EquipmentTableLabels.IS_NAKED_EYE in result.columns:
                result = result.drop(columns=[EquipmentTableLabels.IS_NAKED_EYE])
        return result

    def _extract_path_row(self, path: OpticalPath) -> list:
        """
        Extract technical parameters for a single optical path.
        """
        # Determine if the main optic is Binoculars or NakedEye
        is_naked_eye = isinstance(path.telescope, NakedEye)

        # Calculate useful_zoom
        useful_zoom_value = path.is_magnification_useful()

        # Get output type
        output_type_value = path.output.output_type()

        # Calculate Exit Pupil
        exit_pupil_value = path.exit_pupil().to("mm").magnitude
        if exit_pupil_value < 0:
            exit_pupil_value = 0

        flipped_horizontally, flipped_vertically = path.get_image_orientation()

        # Pixel Scale
        pixel_scale_value = path.pixel_scale()
        pixel_scale_magnitude = (
            pixel_scale_value.magnitude if pixel_scale_value is not None else numpy.nan
        )

        # NPF Rule
        npf_value = path.npf_rule()
        npf_magnitude = npf_value.magnitude if npf_value is not None else numpy.nan

        # Rule of 500
        r500_value = path.rule_of_500()
        r500_magnitude = r500_value.magnitude if r500_value is not None else numpy.nan

        # Sampling status (default seeing 2.0")
        sampling_value = path.sampling_status(seeing=2.0)

        # Critical Focus Zone
        cfz_value = path.critical_focus_zone()
        cfz_magnitude = cfz_value.magnitude if cfz_value is not None else numpy.nan

        # Backfocus Gap
        bf_gap_value = path.backfocus_gap()
        bf_gap_magnitude = (
            bf_gap_value.to("mm").magnitude if bf_gap_value is not None else numpy.nan
        )

        # Total Mass
        total_mass_value = path.total_mass()
        total_mass_magnitude = total_mass_value.to("gram").magnitude

        dawes = path.dawes_limit()
        rayleigh = path.rayleigh_limit()

        return [
            path.label(),
            output_type_value,
            path.zoom().magnitude,
            useful_zoom_value,
            path.fov().magnitude,
            path.fov_width().magnitude,
            path.fov_height().magnitude,
            path.fov_diagonal().magnitude,
            exit_pupil_value,
            dawes.magnitude if dawes is not None else numpy.nan,
            rayleigh.magnitude if rayleigh is not None else numpy.nan,
            path.ideal_planetary_focal_ratio() or numpy.nan,
            path.telescope.limiting_magnitude(),
            path.brightness().magnitude,
            path.length(),
            path.component_list(),
            flipped_horizontally,
            flipped_vertically,
            pixel_scale_magnitude,
            sampling_value,
            npf_magnitude,
            r500_magnitude,
            cfz_magnitude,
            bf_gap_magnitude,
            total_mass_magnitude,
            is_naked_eye,
        ]

    def _merge_path_data(
        self, result_data: pd.DataFrame, rows: list, columns: list
    ) -> pd.DataFrame:
        """
        Merge extracted rows into a DataFrame and align dtypes.
        """
        if not rows:
            return result_data

        new_data = pd.DataFrame(rows, columns=columns)  # pyright: ignore
        if result_data.empty:
            return new_data

        for col in result_data.columns:
            if result_data[col].dtype != new_data[col].dtype:
                try:
                    new_data[col] = new_data[col].astype(result_data[col].dtype)
                except Exception as e:
                    logging.warning(
                        f"Could not align dtype for column {col}: {e}. This might lead to concat issues."
                    )
        return pd.concat([result_data, new_data], ignore_index=True)  # pyright: ignore

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
            EquipmentTableLabels.RAYLEIGH_LIMIT,
            EquipmentTableLabels.IDEAL_PLANETARY_FOCAL_RATIO,
            EquipmentTableLabels.RANGE,
            EquipmentTableLabels.BRIGHTNESS,
            EquipmentTableLabels.ELEMENTS,
            EquipmentTableLabels.COMPONENTS,
            EquipmentTableLabels.FLIPPED_HORIZONTALLY,
            EquipmentTableLabels.FLIPPED_VERTICALLY,
            EquipmentTableLabels.PIXEL_SCALE,
            EquipmentTableLabels.SAMPLING,
            EquipmentTableLabels.NPF_RULE,
            EquipmentTableLabels.RULE_OF_500,
            EquipmentTableLabels.CRITICAL_FOCUS_ZONE,
            EquipmentTableLabels.BACKFOCUS_GAP,
            EquipmentTableLabels.TOTAL_MASS,
            EquipmentTableLabels.IS_NAKED_EYE,
        ]

        # Get unique paths from both visual and image outputs in a single pass
        all_paths = self._get_paths([GraphConstants.EYE_ID, GraphConstants.IMAGE_ID])

        rows = [self._extract_path_row(path) for path in all_paths]
        result = pd.DataFrame(columns=columns)  # pyright: ignore
        result = self._merge_path_data(result, rows, columns)

        # Add ID column as first
        if not result.empty:
            result["ID"] = result.index
            result = result[["ID"] + columns]
        else:
            result["ID"] = []
            result = result[["ID"] + columns]

        return result  # pyright: ignore

    def max_zoom(self):
        """
        Max useful zoom due to atmosphere
        """
        return 350

    def _connect(self):
        if self._connected:
            return
        logger.debug("Connecting nodes")

        for out_node_id, out_node_data in self.connection_garph.nodes(data=True):
            if out_node_data.get(NodeLabels.TYPE) == OpticalType.OUTPUT:
                # Get output type and gender
                connection_type = out_node_data[NodeLabels.CONNECTION_TYPE]
                connection_gender = out_node_data.get(NodeLabels.CONNECTION_GENDER)

                for in_node_id, in_node_data in self.connection_garph.nodes(data=True):
                    if (
                        in_node_data.get(NodeLabels.TYPE) == OpticalType.INPUT
                        and in_node_data.get(NodeLabels.CONNECTION_TYPE)
                        == connection_type
                    ):
                        # Match genders - only different genders can connect
                        in_gender = in_node_data.get(NodeLabels.CONNECTION_GENDER)

                        # If both genders are specified, they must be different
                        if connection_gender is not None and in_gender is not None:
                            if connection_gender == in_gender:
                                continue
                        # If either gender is missing and it's NOT a push-fit (1.25" or 2"),
                        # we cannot assume they connect.
                        elif connection_type not in [
                            ConnectionType.F_1_25,
                            ConnectionType.F_2,
                        ]:
                            continue

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
        connection_gender=None,
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
            node_label = (
                str(connection_type)
                + (str(connection_gender) if connection_gender else "")
                + " "
                + OpticalEquipment.IN
            )
        elif node_type == OpticalType.OUTPUT:
            node_label = (
                str(connection_type)
                + (str(connection_gender) if connection_gender else "")
                + " "
                + OpticalEquipment.OUT
            )
        else:
            node_label = ""

        node[NodeLabels.TYPE] = node_type
        node[NodeLabels.LABEL] = node_label
        node[NodeLabels.EQUIPMENT] = equipment
        node[NodeLabels.CONNECTION_TYPE] = connection_type
        node[NodeLabels.CONNECTION_GENDER] = connection_gender
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
        self._connected = False
        optical_eqipment.register(self)
