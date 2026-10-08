import unittest

from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType, Gender


class TestZwoASI071MCProAudit(unittest.TestCase):

    def test_asi071mc_pro_specs(self):
        """Audit test for ZWO ASI071MC Pro based on official ZWO documentation."""
        cam = ZwoCamera.ZWO_ASI_071MC_Pro()

        # Vendor name
        self.assertEqual(cam.vendor, "ZWO ASI071MC Pro")

        # Mass & backfocus / optical length
        self.assertEqual(cam.mass.to("gram").magnitude, 640)
        self.assertEqual(cam.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(cam.backfocus, Quantity(17.5, "millimeter"))

        # Connection type & gender
        self.assertEqual(cam.connection_type, ConnectionType.M42)
        self.assertEqual(cam.connection_gender, Gender.FEMALE)

        # Resolution (4944 x 3284)
        self.assertEqual(cam.width, 4944)
        self.assertEqual(cam.height, 3284)

        # Sensor dimensions & pixel size (4.78µm, 23.6mm x 15.6mm)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 4.78)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 23.6)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 15.6)

        # Sensor performance parameters
        self.assertEqual(cam.full_well, 46000)
        self.assertEqual(cam.read_noise, 2.3)
        self.assertEqual(cam.quantum_efficiency, 50)


if __name__ == "__main__":
    unittest.main()
