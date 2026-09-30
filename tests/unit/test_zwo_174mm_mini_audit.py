import unittest

from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZWOASI174MMMiniAudit(unittest.TestCase):
    def test_zwo_asi_174mm_mini_specs(self):
        cam = ZwoCamera.ZWO_ASI_174MM_Mini()

        self.assertEqual(cam.get_vendor(), "ZWO ASI174MM Mini")
        self.assertEqual(cam.width, 1936)
        self.assertEqual(cam.height, 1216)
        self.assertAlmostEqual(cam.pixel_size().to("um").magnitude, 5.86, places=2)
        self.assertAlmostEqual(cam.sensor_width.to("mm").magnitude, 11.34, places=2)
        self.assertAlmostEqual(cam.sensor_height.to("mm").magnitude, 7.13, places=2)
        self.assertEqual(cam.quantum_efficiency, 77)
        self.assertEqual(cam.full_well, 32000)
        self.assertAlmostEqual(cam.read_noise, 3.5, places=1)
        self.assertAlmostEqual(cam.mass.to("gram").magnitude, 60.0, places=1)
        self.assertAlmostEqual(cam.optical_length.to("mm").magnitude, 8.5, places=1)
        self.assertEqual(cam.backfocus, Quantity(8.5, "millimeter"))
        self.assertEqual(cam.connection_type, ConnectionType.CS)

        # Inputs verification from _DATABASE
        inputs = cam._DATABASE["ZWO_ASI_174MM_Mini"]["inputs"]
        self.assertEqual(len(inputs), 2)
        self.assertEqual(inputs[0], ("CS", "Female"))
        self.assertEqual(inputs[1], ("1.25\"", "Male"))


if __name__ == "__main__":
    unittest.main()
