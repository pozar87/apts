import unittest

import networkx as nx

from apts.constants import NodeLabels, OpticalType
from apts.equipment.calculations import can_connect_nodes, find_unique_optical_paths
from apts.opticalequipment.eyepiece.vendors.sky_watcher import Sky_watcherEyepiece
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestEquipmentCalculations(unittest.TestCase):
    def test_can_connect_nodes_none(self):
        self.assertFalse(can_connect_nodes(None, None))
        self.assertFalse(can_connect_nodes({}, None))
        self.assertFalse(can_connect_nodes(None, {}))

    def test_can_connect_nodes_invalid_types(self):
        out_node = {NodeLabels.TYPE: OpticalType.INPUT}
        in_node = {NodeLabels.TYPE: OpticalType.INPUT}
        self.assertFalse(can_connect_nodes(out_node, in_node))

    def test_can_connect_nodes_mismatched_connection_types(self):
        out_node = {
            NodeLabels.TYPE: OpticalType.OUTPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.M42,
            NodeLabels.NAME: "eq1_out",
        }
        in_node = {
            NodeLabels.TYPE: OpticalType.INPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.M48,
            NodeLabels.NAME: "eq2_in",
        }
        self.assertFalse(can_connect_nodes(out_node, in_node))

    def test_can_connect_nodes_same_gender(self):
        out_node = {
            NodeLabels.TYPE: OpticalType.OUTPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.M42,
            NodeLabels.CONNECTION_GENDER: Gender.MALE,
            NodeLabels.NAME: "eq1_out",
        }
        in_node = {
            NodeLabels.TYPE: OpticalType.INPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.M42,
            NodeLabels.CONNECTION_GENDER: Gender.MALE,
            NodeLabels.NAME: "eq2_in",
        }
        self.assertFalse(can_connect_nodes(out_node, in_node))

    def test_can_connect_nodes_different_gender(self):
        out_node = {
            NodeLabels.TYPE: OpticalType.OUTPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.M42,
            NodeLabels.CONNECTION_GENDER: Gender.MALE,
            NodeLabels.NAME: "eq1_out",
        }
        in_node = {
            NodeLabels.TYPE: OpticalType.INPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.M42,
            NodeLabels.CONNECTION_GENDER: Gender.FEMALE,
            NodeLabels.NAME: "eq2_in",
        }
        self.assertTrue(can_connect_nodes(out_node, in_node))

    def test_can_connect_nodes_same_parent_equipment(self):
        out_node = {
            NodeLabels.TYPE: OpticalType.OUTPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.F_1_25,
            NodeLabels.CONNECTION_GENDER: Gender.FEMALE,
            NodeLabels.NAME: "eq1_out",
        }
        in_node = {
            NodeLabels.TYPE: OpticalType.INPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.F_1_25,
            NodeLabels.CONNECTION_GENDER: Gender.MALE,
            NodeLabels.NAME: "eq1_in",
        }
        self.assertFalse(can_connect_nodes(out_node, in_node))

    def test_can_connect_nodes_push_fit(self):
        out_node = {
            NodeLabels.TYPE: OpticalType.OUTPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.F_1_25,
            NodeLabels.CONNECTION_GENDER: None,
            NodeLabels.NAME: "eq1_out",
        }
        in_node = {
            NodeLabels.TYPE: OpticalType.INPUT,
            NodeLabels.CONNECTION_TYPE: ConnectionType.F_1_25,
            NodeLabels.CONNECTION_GENDER: None,
            NodeLabels.NAME: "eq2_in",
        }
        self.assertTrue(can_connect_nodes(out_node, in_node))

    def test_find_unique_optical_paths(self):
        tele = CelestronTelescope.Celestron_C8_OTA()
        eyepiece = Sky_watcherEyepiece.Sky_Watcher_Plossl_25mm()

        graph = nx.DiGraph()
        graph.add_node("SPACE", label_dist=1.5)
        graph.add_node("EYE", label_dist=1.5)

        graph.add_node(
            "tele_node",
            **{
                NodeLabels.EQUIPMENT: tele,
                NodeLabels.TYPE: OpticalType.GENERIC,
                NodeLabels.NAME: "tele_node",
            }
        )
        graph.add_node(
            "eye_node",
            **{
                NodeLabels.EQUIPMENT: eyepiece,
                NodeLabels.TYPE: OpticalType.GENERIC,
                NodeLabels.NAME: "eye_node",
            }
        )

        graph.add_edge("SPACE", "tele_node")
        graph.add_edge("tele_node", "eye_node")
        graph.add_edge("eye_node", "EYE")

        paths = find_unique_optical_paths(graph, "SPACE", "EYE")
        self.assertEqual(len(paths), 1)
        self.assertEqual(paths[0].telescope, tele)
        self.assertEqual(paths[0].output, eyepiece)


if __name__ == "__main__":
    unittest.main()
