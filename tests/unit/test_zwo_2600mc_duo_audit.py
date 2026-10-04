import unittest

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils import ConnectionType, Gender


class TestZwo2600MCDuoAudit(unittest.TestCase):
    def test_zwo_2600mc_duo_audit(self):
        # Test both factory methods
        camera_1 = ZwoCamera.ZWO_ASI2600MC_DUO()
        camera_2 = ZwoCamera.ZWO_ASI_2600MC_Duo()

        for camera in [camera_1, camera_2]:
            # Assert vendor name and physical specifications
            self.assertEqual(camera.vendor, "ZWO ASI2600MC Duo")
            self.assertEqual(camera.mass.to("gram").magnitude, 800)
            self.assertEqual(camera.optical_length.to("mm").magnitude, 17.5)

            # Assert sensor and optical specifications
            self.assertEqual(camera.full_well, 50000)
            self.assertEqual(camera.pixel_size().to("micrometer").magnitude, 3.76)
            self.assertEqual(camera.quantum_efficiency, 80)
            self.assertEqual(camera.read_noise, 1.0)
            self.assertEqual(camera.width, 6248)
            self.assertEqual(camera.height, 4176)
            self.assertEqual(camera.sensor_width.to("mm").magnitude, 23.5)
            self.assertEqual(camera.sensor_height.to("mm").magnitude, 15.7)

            # Assert M54 female connection (verified via ZWO official specs)
            self.assertEqual(camera.connection_type, ConnectionType.M54)
            self.assertEqual(camera.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
