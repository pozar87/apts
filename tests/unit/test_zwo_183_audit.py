import unittest

from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType, Gender


class TestZwoASI183Audit(unittest.TestCase):

    def test_asi183mm_pro_specs(self):
        cam = ZwoCamera.ZWO_ASI_183MM_Pro()

        # Vendor name
        self.assertEqual(cam.vendor, "ZWO ASI183MM Pro")

        # Mass: 410g
        self.assertEqual(cam.mass.to("gram").magnitude, 410)

        # Optical length / backfocus: 17.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(cam.backfocus, Quantity(17.5, "millimeter"))

        # Connection thread: M42 Female
        self.assertEqual(cam.connection_type, ConnectionType.M42)
        self.assertEqual(cam.connection_gender, Gender.FEMALE)

        # Resolution: 5496 x 3672 (20.1MP)
        self.assertEqual(cam.width, 5496)
        self.assertEqual(cam.height, 3672)

        # Sensor dimensions & pixel size: 2.4µm, 13.2mm x 8.8mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.4)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 13.2)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 8.8)

        # Full well capacity: 15000 e-
        self.assertEqual(cam.full_well, 15000)

        # Read noise: 1.6 e-
        self.assertEqual(cam.read_noise, 1.6)

        # Peak Quantum Efficiency: 84%
        self.assertEqual(cam.quantum_efficiency, 84)

    def test_asi183mc_pro_specs(self):
        cam = ZwoCamera.ZWO_ASI_183MC_Pro()

        # Vendor name
        self.assertEqual(cam.vendor, "ZWO ASI183MC Pro")

        # Mass: 410g
        self.assertEqual(cam.mass.to("gram").magnitude, 410)

        # Optical length / backfocus: 17.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(cam.backfocus, Quantity(17.5, "millimeter"))

        # Connection thread: M42 Female
        self.assertEqual(cam.connection_type, ConnectionType.M42)
        self.assertEqual(cam.connection_gender, Gender.FEMALE)

        # Resolution: 5496 x 3672 (20.1MP)
        self.assertEqual(cam.width, 5496)
        self.assertEqual(cam.height, 3672)

        # Sensor dimensions & pixel size: 2.4µm, 13.2mm x 8.8mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.4)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 13.2)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 8.8)

        # Full well capacity: 15000 e-
        self.assertEqual(cam.full_well, 15000)

        # Read noise: 1.6 e-
        self.assertEqual(cam.read_noise, 1.6)

        # Peak Quantum Efficiency: 84%
        self.assertEqual(cam.quantum_efficiency, 84)


if __name__ == "__main__":
    unittest.main()
