import unittest
from apts.equipment import Equipment
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.barlow import Barlow
from apts.opticalequipment.diagonal import Diagonal
from apts.opticalequipment.eyepiece import Eyepiece
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.oag import OAG
from apts.utils import ConnectionType, Gender
from apts.constants import GraphConstants

class TestEquipmentConnections(unittest.TestCase):
    def test_telescope_t2_output(self):
        # Telescope with both 1.25" and T2 output
        t = Telescope(80, 600, "Test Telescope", connection_type=ConnectionType.F_1_25, t2_output=True)
        e = Equipment()
        e.register(t)

        # Verify both outputs are registered in the graph
        out_125 = t.out_id(ConnectionType.F_1_25)
        out_t2 = t.out_id(ConnectionType.T2)

        self.assertTrue(e.connection_garph.has_node(out_125))
        self.assertTrue(e.connection_garph.has_node(out_t2))

        # Verify connections from telescope to outputs
        self.assertTrue(e.connection_garph.has_edge(t.id(), out_125))
        self.assertTrue(e.connection_garph.has_edge(t.id(), out_t2))

    def test_oag_multiple_outputs(self):
        # OAG has a main output and a guide output
        oag = OAG("Test OAG", in_connection_type=ConnectionType.T2, out_connection_type=ConnectionType.T2,
                  guide_connection_type=ConnectionType.M42)
        e = Equipment()
        e.register(oag)

        # Verify all ports
        in_t2 = oag.in_id(ConnectionType.T2)
        out_t2 = oag.out_id(ConnectionType.T2)
        out_m42 = oag.out_id(ConnectionType.M42)

        self.assertTrue(e.connection_garph.has_node(in_t2))
        self.assertTrue(e.connection_garph.has_node(out_t2))
        self.assertTrue(e.connection_garph.has_node(out_m42))

        self.assertTrue(e.connection_garph.has_edge(in_t2, oag.id()))
        self.assertTrue(e.connection_garph.has_edge(oag.id(), out_t2))
        self.assertTrue(e.connection_garph.has_edge(oag.id(), out_m42))

    def test_path_finding_multiple_outputs(self):
        # Setup: Telescope (1.25" and T2) -> Barlow (1.25") -> Eyepiece (1.25")
        #                                  -> Camera (T2)
        t = Telescope(80, 600, "Test Telescope", connection_type=ConnectionType.F_1_25, t2_output=True)
        b = Barlow(2, "Test Barlow", connection_type=ConnectionType.F_1_25)
        ep = Eyepiece(20, "Test Eyepiece", connection_type=ConnectionType.F_1_25)
        cam = Camera(36, 24, 6000, 4000, "Test Camera", connection_type=ConnectionType.T2)

        e = Equipment()
        e.register(t)
        e.register(b)
        e.register(ep)
        e.register(cam)

        # Visual paths
        visual_paths = e._get_paths(GraphConstants.EYE_ID)
        # 3 paths: NakedEye, Telescope -> Eyepiece and Telescope -> Barlow -> Eyepiece
        self.assertEqual(len(visual_paths), 3)

        # Imaging paths
        imaging_paths = e._get_paths(GraphConstants.IMAGE_ID)
        self.assertEqual(len(imaging_paths), 1) # Telescope (T2) -> Camera
        self.assertEqual(imaging_paths[0].output, cam)
        self.assertEqual(imaging_paths[0].telescope, t)

if __name__ == "__main__":
    unittest.main()
