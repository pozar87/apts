import unittest
from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType, Gender


class TestZwoASI1600Audit(unittest.TestCase):

    def test_asi1600mm_pro_specs(self):
        """Audit test for ZWO ASI1600MM Pro based on official ZWO documentation."""
        cam = ZwoCamera.ZWO_ASI_1600MM_Pro()

        # Vendor name
        self.assertEqual(cam.vendor, "ZWO ASI1600MM Pro")

        # Mass & backfocus / optical length
        self.assertEqual(cam.mass.to("gram").magnitude, 410)
        self.assertEqual(cam.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(cam.backfocus, Quantity(17.5, "millimeter"))

        # Connection type & gender
        self.assertEqual(cam.connection_type, ConnectionType.M42)
        self.assertEqual(cam.connection_gender, Gender.FEMALE)

        # Resolution (4656 x 3520)
        self.assertEqual(cam.width, 4656)
        self.assertEqual(cam.height, 3520)

        # Sensor dimensions & pixel size (3.8µm, 17.7mm x 13.4mm)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 3.8)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 17.7)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 13.4)

        # Sensor performance parameters
        self.assertEqual(cam.full_well, 20000)
        self.assertEqual(cam.read_noise, 1.2)
        self.assertEqual(cam.quantum_efficiency, 60)

    def test_asi1600mc_pro_specs(self):
        """Audit test for ZWO ASI1600MC Pro based on official ZWO documentation."""
        cam = ZwoCamera.ZWO_ASI_1600MC_Pro()

        # Vendor name
        self.assertEqual(cam.vendor, "ZWO ASI1600MC Pro")

        # Mass & backfocus / optical length
        self.assertEqual(cam.mass.to("gram").magnitude, 410)
        self.assertEqual(cam.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(cam.backfocus, Quantity(17.5, "millimeter"))

        # Connection type & gender
        self.assertEqual(cam.connection_type, ConnectionType.M42)
        self.assertEqual(cam.connection_gender, Gender.FEMALE)

        # Resolution (4656 x 3520)
        self.assertEqual(cam.width, 4656)
        self.assertEqual(cam.height, 3520)

        # Sensor dimensions & pixel size (3.8µm, 17.7mm x 13.4mm)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 3.8)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 17.7)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 13.4)

        # Sensor performance parameters
        self.assertEqual(cam.full_well, 20000)
        self.assertEqual(cam.read_noise, 1.2)
        self.assertEqual(cam.quantum_efficiency, 60)


if __name__ == "__main__":
    unittest.main()
