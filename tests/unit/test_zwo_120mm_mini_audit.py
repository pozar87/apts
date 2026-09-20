import unittest
from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoASI120MMMiniAudit(unittest.TestCase):

    def test_asi120mm_mini_specs(self):
        cam = ZwoCamera.ZWO_ASI_120MM_Mini()

        # Mass: 60g
        self.assertEqual(cam.mass.to("gram").magnitude, 60)

        # Optical length / backfocus: 8.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 8.5)
        self.assertEqual(cam.backfocus, Quantity(8.5, "millimeter"))

        # Connection type: CS female thread / 1.25" male barrel
        self.assertEqual(cam.connection_type, ConnectionType.CS)

        # Resolution: 1280 x 960 (1.2 MP)
        self.assertEqual(cam.width, 1280)
        self.assertEqual(cam.height, 960)

        # Sensor dimensions & pixel size: 3.75µm, 4.8mm x 3.6mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 3.75)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 4.8)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 3.6)

        # Full well capacity: 13,000 e-
        self.assertEqual(cam.full_well, 13000)

        # Read noise: 4.0 e-
        self.assertEqual(cam.read_noise, 4.0)

        # Peak Quantum Efficiency: 80%
        self.assertEqual(cam.quantum_efficiency, 80)


if __name__ == "__main__":
    unittest.main()
