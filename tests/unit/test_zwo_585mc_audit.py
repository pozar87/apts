import unittest

from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoASI585MCAudit(unittest.TestCase):

    def test_asi585mc_specs(self):
        cam = ZwoCamera.ZWO_ASI_585MC()

        # Mass: 126g
        self.assertEqual(cam.mass.to("gram").magnitude, 126)

        # Optical length / backfocus: 12.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)
        self.assertEqual(cam.backfocus, Quantity(12.5, "millimeter"))

        # Connection thread: CS
        self.assertEqual(cam.connection_type, ConnectionType.CS)

        # Resolution: 3840 x 2160 (8.29MP)
        self.assertEqual(cam.width, 3840)
        self.assertEqual(cam.height, 2160)

        # Sensor dimensions & pixel size: 2.9µm, 11.13mm x 6.26mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.9)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 11.13)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 6.26)

        # Full well capacity: 40000 e-
        self.assertEqual(cam.full_well, 40000)

        # Read noise: 0.6 e-
        self.assertEqual(cam.read_noise, 0.6)

        # Peak Quantum Efficiency: 91%
        self.assertEqual(cam.quantum_efficiency, 91)

    def test_asi585mc_alias_factory_method(self):
        cam = ZwoCamera.ZWO_ASI585MC()
        self.assertEqual(cam.vendor, "ZWO ASI585MC")
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)


if __name__ == "__main__":
    unittest.main()
