import unittest

from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoASI6200Audit(unittest.TestCase):

    def test_asi6200mm_pro_specs(self):
        cam = ZwoCamera.ZWO_ASI_6200MM_Pro()

        # Mass: 700g
        self.assertEqual(cam.mass.to("gram").magnitude, 700)

        # Optical length / backfocus: 17.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(cam.backfocus, Quantity(17.5, "millimeter"))

        # Connection thread: M54 female
        self.assertEqual(cam.connection_type, ConnectionType.M54)

        # Resolution: 9576 x 6388 (61.17MP)
        self.assertEqual(cam.width, 9576)
        self.assertEqual(cam.height, 6388)

        # Sensor dimensions & pixel size: 3.76µm, 36.0mm x 24.0mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 3.76)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 36.0)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 24.0)

        # Full well capacity: 51400 e-
        self.assertEqual(cam.full_well, 51400)

        # Read noise: 1.2 e-
        self.assertEqual(cam.read_noise, 1.2)

        # Peak Quantum Efficiency: 91%
        self.assertEqual(cam.quantum_efficiency, 91)

    def test_asi6200mc_pro_specs(self):
        cam = ZwoCamera.ZWO_ASI_6200MC_Pro()

        # Mass: 700g
        self.assertEqual(cam.mass.to("gram").magnitude, 700)

        # Optical length / backfocus: 17.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(cam.backfocus, Quantity(17.5, "millimeter"))

        # Connection thread: M54 female
        self.assertEqual(cam.connection_type, ConnectionType.M54)

        # Resolution: 9576 x 6388 (61.17MP)
        self.assertEqual(cam.width, 9576)
        self.assertEqual(cam.height, 6388)

        # Sensor dimensions & pixel size: 3.76µm, 36.0mm x 24.0mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 3.76)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 36.0)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 24.0)

        # Full well capacity: 51400 e-
        self.assertEqual(cam.full_well, 51400)

        # Read noise: 1.2 e-
        self.assertEqual(cam.read_noise, 1.2)

        # Peak Quantum Efficiency: 80%
        self.assertEqual(cam.quantum_efficiency, 80)

    def test_asi6200mm_pro_alias(self):
        cam = ZwoCamera.ZWO_ASI6200MM_PRO()
        self.assertEqual(cam.vendor, "ZWO ASI6200MM Pro")
        self.assertEqual(cam.connection_type, ConnectionType.M54)


if __name__ == "__main__":
    unittest.main()
