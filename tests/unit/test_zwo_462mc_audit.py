import unittest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType

class TestZwo462McAudit(unittest.TestCase):
    def test_asi462mc_audited_specs(self):
        """
        Verify the audited specifications for ZWO ASI462MC.
        Reference: https://astronomy-imaging-camera.com/product/asi462mc/
        """
        cam = ZwoCamera.ZWO_ASI_462MC()

        # Physical & Connection
        self.assertEqual(cam.vendor, "ZWO ASI462MC")
        self.assertEqual(cam.mass.to("gram").magnitude, 120)
        self.assertEqual(cam.connection_type, ConnectionType.CS)
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)

        # Sensor Dimensions & Resolution
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 5.6)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 3.2)
        self.assertEqual(cam.width, 1936)
        self.assertEqual(cam.height, 1096)

        # Sensor Performance
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.9)
        self.assertEqual(cam.full_well, 11200)
        self.assertEqual(cam.read_noise, 0.5)
        self.assertEqual(cam.quantum_efficiency, 89)

if __name__ == '__main__':
    unittest.main()
