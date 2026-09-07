import unittest
from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoASI678MCAudit(unittest.TestCase):

    def test_asi678mc_specs(self):
        cam = ZwoCamera.ZWO_ASI_678MC()

        # Mass: 126g
        self.assertEqual(cam.mass.to("gram").magnitude, 126)

        # Optical length / backfocus: 12.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)
        self.assertEqual(cam.backfocus, Quantity(12.5, "millimeter"))

        # Connection thread: CS
        self.assertEqual(cam.connection_type, ConnectionType.CS)

        # Resolution: 3840 x 2160 (4K UHD)
        self.assertEqual(cam.width, 3840)
        self.assertEqual(cam.height, 2160)

        # Sensor dimensions & pixel size: 2.0µm, 7.68mm x 4.32mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.0)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.68)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 4.32)

        # Full well capacity: 11270 e-
        self.assertEqual(cam.full_well, 11270)

        # Read noise: 0.6 e-
        self.assertEqual(cam.read_noise, 0.6)

        # Peak Quantum Efficiency: 83%
        self.assertEqual(cam.quantum_efficiency, 83)


if __name__ == "__main__":
    unittest.main()
