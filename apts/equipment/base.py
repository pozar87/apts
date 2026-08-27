import logging
from typing import Optional

import networkx as nx
import pandas as pd

from ..constants import GraphConstants, NodeLabels, OpticalType
from ..opticalequipment import (
    NakedEye,
    OpticalEquipment,
)
from .calculations import can_connect_nodes, find_unique_optical_paths
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
        return find_unique_optical_paths(
            self.connection_garph, GraphConstants.SPACE_ID, output_ids
        )

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
            for in_node_id, in_node_data in self.connection_garph.nodes(data=True):
                if can_connect_nodes(out_node_data, in_node_data):
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
