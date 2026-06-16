import logging
from typing import Optional

import networkx as nx
import pandas as pd

from ..constants import GraphConstants, NodeLabels, OpticalType
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
        from .exporter import EquipmentExporter

        return EquipmentExporter(self).data(language)

    def _generate_data(self) -> pd.DataFrame:
        from .exporter import EquipmentExporter

        return EquipmentExporter(self)._generate_data()

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
