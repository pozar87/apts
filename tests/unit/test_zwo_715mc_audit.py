import unittest
from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoASI715MCAudit(unittest.TestCase):

    def test_asi715mc_specs(self):
        cam = ZwoCamera.ZWO_ASI_715MC()

        # Mass: 126g
        self.assertEqual(cam.mass.to("gram").magnitude, 126)

        # Optical length / backfocus: 12.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)
        self.assertEqual(cam.backfocus, Quantity(12.5, "millimeter"))

        # Connection thread: CS
        self.assertEqual(cam.connection_type, ConnectionType.CS)

        # Resolution: 3864 x 2192 (8.5MP)
        self.assertEqual(cam.width, 3864)
        self.assertEqual(cam.height, 2192)

        # Sensor dimensions & pixel size: 1.45µm, 5.6mm x 3.18mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 1.45)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 5.6)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 3.18)

        # Full well capacity: 6030 e-
        self.assertEqual(cam.full_well, 6030)

        # Read noise: 0.72 e-
        self.assertEqual(cam.read_noise, 0.72)

        # Peak Quantum Efficiency: 80%
        self.assertEqual(cam.quantum_efficiency, 80)


if __name__ == "__main__":
    unittest.main()
