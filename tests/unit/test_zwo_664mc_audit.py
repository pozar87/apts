import unittest

from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoASI664MCAudit(unittest.TestCase):

    def test_asi664mc_specs(self):
        cam = ZwoCamera.ZWO_ASI_664MC()

        # Mass: 126g
        self.assertEqual(cam.mass.to("gram").magnitude, 126)

        # Optical length / backfocus: 12.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)
        self.assertEqual(cam.backfocus, Quantity(12.5, "millimeter"))

        # Connection thread: CS
        self.assertEqual(cam.connection_type, ConnectionType.CS)

        # Resolution: 2704 x 1536 (4.15MP)
        self.assertEqual(cam.width, 2704)
        self.assertEqual(cam.height, 1536)

        # Sensor dimensions & pixel size: 2.9µm, 7.84mm x 4.45mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.9)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.84)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 4.45)

        # Full well capacity: 38500 e-
        self.assertEqual(cam.full_well, 38500)

        # Read noise: 0.46 e-
        self.assertEqual(cam.read_noise, 0.46)

        # Peak Quantum Efficiency: 91%
        self.assertEqual(cam.quantum_efficiency, 91)


if __name__ == "__main__":
    unittest.main()
