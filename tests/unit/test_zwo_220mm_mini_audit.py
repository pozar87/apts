import unittest
from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoASI220MMMiniAudit(unittest.TestCase):

    def test_asi220mm_mini_specs(self):
        cam_std = ZwoCamera.ZWO_ASI_220MM_Mini()
        cam_air = ZwoCamera.ZWO_ASI_220MM_Mini_for_ASIAir()

        for cam in [cam_std, cam_air]:
            # Mass: 60g
            self.assertEqual(cam.mass.to("gram").magnitude, 60)

            # Optical length / backfocus: 8.5mm
            self.assertEqual(cam.optical_length.to("mm").magnitude, 8.5)
            self.assertEqual(cam.backfocus, Quantity(8.5, "millimeter"))

            # Connection thread: CS female / 1.25" male
            self.assertEqual(cam.connection_type, ConnectionType.CS)

            # Resolution: 1920 x 1080 (2.07 MP)
            self.assertEqual(cam.width, 1920)
            self.assertEqual(cam.height, 1080)

            # Sensor dimensions & pixel size: 4.0µm, 7.68mm x 4.32mm
            self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 4.0)
            self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.68)
            self.assertEqual(cam.sensor_height.to("mm").magnitude, 4.32)

            # Full well capacity: 8780 e-
            self.assertEqual(cam.full_well, 8780)

            # Read noise: 0.6 e-
            self.assertEqual(cam.read_noise, 0.6)

            # Peak Quantum Efficiency: 92%
            self.assertEqual(cam.quantum_efficiency, 92)


if __name__ == "__main__":
    unittest.main()
