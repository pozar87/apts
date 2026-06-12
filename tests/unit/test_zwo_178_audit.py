import unittest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

class TestZwo178Audit(unittest.TestCase):
    def test_asi178mc_specs(self):
        cam = ZwoCamera.ZWO_ASI_178MC()
        self.assertEqual(cam.vendor, "ZWO ASI178MC")
        self.assertEqual(cam.mass.to("gram").magnitude, 120)
        self.assertEqual(cam.width, 3096)
        self.assertEqual(cam.height, 2080)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.4)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.4)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 5.0)
        self.assertEqual(cam.full_well, 15000)
        self.assertEqual(cam.read_noise, 2.2)
        self.assertEqual(cam.quantum_efficiency, 81)
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)

    def test_asi178mm_specs(self):
        cam = ZwoCamera.ZWO_ASI_178MM()
        self.assertEqual(cam.vendor, "ZWO ASI178MM")
        self.assertEqual(cam.mass.to("gram").magnitude, 120)
        self.assertEqual(cam.width, 3096)
        self.assertEqual(cam.height, 2080)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.4)
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.4)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 5.0)
        self.assertEqual(cam.full_well, 15000)
        self.assertEqual(cam.read_noise, 2.2)
        self.assertEqual(cam.quantum_efficiency, 81)
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)

if __name__ == '__main__':
    unittest.main()
