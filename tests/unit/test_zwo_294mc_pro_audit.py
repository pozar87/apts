import unittest

from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType, Gender


class TestZwoASI294MCProAudit(unittest.TestCase):

    def test_asi294mc_pro_specs(self):
        cam = ZwoCamera.ZWO_ASI_294MC_Pro()

        # Vendor name
        self.assertEqual(cam.vendor, "ZWO ASI294MC Pro")

        # Mass: 410g
        self.assertEqual(cam.mass.to("gram").magnitude, 410)

        # Optical length / backfocus: 17.5mm
        self.assertEqual(cam.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(cam.backfocus, Quantity(17.5, "millimeter"))

        # Connection thread: M42 Female
        self.assertEqual(cam.connection_type, ConnectionType.M42)
        self.assertEqual(cam.connection_gender, Gender.FEMALE)

        # Resolution: 4144 x 2822 (11.7MP)
        self.assertEqual(cam.width, 4144)
        self.assertEqual(cam.height, 2822)

        # Sensor dimensions & pixel size: 4.63µm, 19.1mm x 13.0mm
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 4.63)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 19.1)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 13.0)

        # Full well capacity: 63,700 e-
        self.assertEqual(cam.full_well, 63700)

        # Read noise: 1.2 e-
        self.assertEqual(cam.read_noise, 1.2)

        # Peak Quantum Efficiency: 75%
        self.assertEqual(cam.quantum_efficiency, 75)


if __name__ == "__main__":
    unittest.main()
