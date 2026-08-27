import logging
from typing import Any

from ..constants import NodeLabels, OpticalType
from ..opticalequipment import OpticalEquipment
from ..optics import OpticalPath
from ..utils import ConnectionType, find_all_paths

logger = logging.getLogger(__name__)


def can_connect_nodes(out_node_data: dict, in_node_data: dict) -> bool:
    """
    Determines whether an output optical node can connect to an input optical node.
    """
    if out_node_data is None or in_node_data is None:
        return False

    if out_node_data.get(NodeLabels.TYPE) != OpticalType.OUTPUT:
        return False

    if in_node_data.get(NodeLabels.TYPE) != OpticalType.INPUT:
        return False

    connection_type = out_node_data.get(NodeLabels.CONNECTION_TYPE)
    if in_node_data.get(NodeLabels.CONNECTION_TYPE) != connection_type:
        return False

    connection_gender = out_node_data.get(NodeLabels.CONNECTION_GENDER)
    in_gender = in_node_data.get(NodeLabels.CONNECTION_GENDER)

    if connection_gender is not None and in_gender is not None:
        if connection_gender == in_gender:
            return False
    elif connection_type not in [
        ConnectionType.F_1_25,
        ConnectionType.F_2,
    ]:
        return False

    out_id = OpticalEquipment.get_parent_id(out_node_data[NodeLabels.NAME])
    in_id = OpticalEquipment.get_parent_id(in_node_data[NodeLabels.NAME])
    return out_id != in_id


def find_unique_optical_paths(
    connection_graph: Any, space_id: str, output_ids: list[str] | str
) -> list[OpticalPath]:
    """
    Finds all unique optical paths from space_id to output_ids in the connection graph.
    """
    if not isinstance(output_ids, list):
        output_ids = [output_ids]

    results = []
    seen_equipment_sets = set()

    logger.debug(f"Space {space_id}, Outputs {output_ids}")
    for optical_path in find_all_paths(connection_graph, space_id, output_ids):
        logger.debug(f"Optical Path: {optical_path}")
        equipment_list: list[OpticalEquipment] = [
            connection_graph.nodes[node_id].get(NodeLabels.EQUIPMENT)
            for node_id in optical_path
            if connection_graph.nodes[node_id].get(NodeLabels.EQUIPMENT) is not None
        ]

        equipment_set = frozenset(equipment_list)
        if equipment_set not in seen_equipment_sets:
            seen_equipment_sets.add(equipment_set)
            op = OpticalPath.from_path(equipment_list)
            results.append(op)

    return results
