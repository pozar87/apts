import unittest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

class TestZwo385Audit(unittest.TestCase):
    def test_asi385mc_specs(self):
        cam = ZwoCamera.ZWO_ASI_385MC()
        self.assertEqual(cam.vendor, "ZWO ASI385MC")
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.26)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 4.11)
        self.assertEqual(cam.width, 1936)
        self.assertEqual(cam.height, 1096)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 3.75)
        self.assertEqual(cam.full_well, 18700)
        self.assertEqual(cam.read_noise, 0.75)
        self.assertEqual(cam.quantum_efficiency, 80)
        self.assertEqual(cam.mass.to("gram").magnitude, 120)
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)

    def test_asi385mm_specs(self):
        cam = ZwoCamera.ZWO_ASI_385MM()
        self.assertEqual(cam.vendor, "ZWO ASI385MM")
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.26)
        self.assertEqual(cam.mass.to("gram").magnitude, 120)
        self.assertEqual(cam.quantum_efficiency, 80)

if __name__ == "__main__":
    unittest.main()
