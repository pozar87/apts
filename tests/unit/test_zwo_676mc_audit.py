import unittest
from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoASI676MCAudit(unittest.TestCase):

    def test_asi676mc_specs(self):
        cam = ZwoCamera.ZWO_ASI_676MC()

        # Mass: 126g
        self.assertEqual(cam.mass.to("gram").magnitude, 126)

        # Optical length / backfocus: 12.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)
        self.assertEqual(cam.backfocus, Quantity(12.5, "millimeter"))

        # Connection thread: CS
        self.assertEqual(cam.connection_type, ConnectionType.CS)

        # Resolution: 3552 x 3552
        self.assertEqual(cam.width, 3552)
        self.assertEqual(cam.height, 3552)

        # Sensor dimensions & pixel size: 2.0µm, 7.1mm x 7.1mm (3552 * 2.0µm)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.0)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.1)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 7.1)

        # Full well capacity: 10550 e-
        self.assertEqual(cam.full_well, 10550)

        # Read noise: 0.56 e-
        self.assertEqual(cam.read_noise, 0.56)

        # Peak Quantum Efficiency: 83%
        self.assertEqual(cam.quantum_efficiency, 83)


if __name__ == "__main__":
    unittest.main()
