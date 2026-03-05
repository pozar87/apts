import unittest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

class TestStellarZwoCameras(unittest.TestCase):
    def test_asi676_specs(self):
        cam = ZwoCamera.ZWO_ASI_676MC()
        self.assertEqual(cam.width, 3552)
        self.assertEqual(cam.height, 3552)
        self.assertEqual(cam.full_well, 10550)
        self.assertEqual(cam.pixel_size().to('micrometer').magnitude, 2.0)

        cam_mm = ZwoCamera.ZWO_ASI_676MM()
        self.assertEqual(cam_mm.quantum_efficiency, 91)

    def test_asi482_specs(self):
        cam = ZwoCamera.ZWO_ASI_482MC()
        self.assertEqual(cam.width, 1920)
        self.assertEqual(cam.pixel_size().to('micrometer').magnitude, 5.8)
        self.assertEqual(cam.full_well, 51500)

    def test_asi485_specs(self):
        cam = ZwoCamera.ZWO_ASI_485MC()
        self.assertEqual(cam.width, 3840)
        self.assertEqual(cam.pixel_size().to('micrometer').magnitude, 2.9)
        self.assertEqual(cam.full_well, 13000)

    def test_asi662_specs(self):
        cam = ZwoCamera.ZWO_ASI_662MM()
        self.assertEqual(cam.width, 1920)
        self.assertEqual(cam.quantum_efficiency, 91)
        self.assertEqual(cam.full_well, 38200)

    def test_asi585_pro_specs(self):
        cam = ZwoCamera.ZWO_ASI_585MC_Pro()
        self.assertEqual(cam.width, 3840)
        self.assertEqual(cam.full_well, 40000)
        self.assertEqual(cam.mass.to('gram').magnitude, 470)
        self.assertEqual(cam.optical_length.to('mm').magnitude, 6.5)

if __name__ == '__main__':
    unittest.main()
