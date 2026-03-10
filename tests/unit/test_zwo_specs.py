import unittest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

class TestZwoUpdates(unittest.TestCase):
    def test_asi462_specs(self):
        # Test factory method
        cam = ZwoCamera.ZWO_ASI_462MC()
        self.assertEqual(cam.sensor_width.to('mm').magnitude, 5.6)
        self.assertEqual(cam.sensor_height.to('mm').magnitude, 3.2)
        self.assertEqual(cam.width, 1936)
        self.assertEqual(cam.height, 1096)
        self.assertEqual(cam.pixel_size().to('micrometer').magnitude, 2.9)
        self.assertEqual(cam.full_well, 11200)
        self.assertEqual(cam.read_noise, 0.5)
        self.assertEqual(cam.quantum_efficiency, 91)

        # Test MM version
        cam_mm = ZwoCamera.ZWO_ASI_462MM()
        self.assertEqual(cam_mm.sensor_width.to('mm').magnitude, 5.6)
        self.assertEqual(cam_mm.quantum_efficiency, 91)

    def test_asi585_specs(self):
        # Test legacy factory method (now consolidated)
        cam = ZwoCamera.ZWO_ASI585MC()
        self.assertEqual(cam.sensor_width.to('mm').magnitude, 11.13)
        self.assertEqual(cam.sensor_height.to('mm').magnitude, 6.26)
        self.assertEqual(cam.width, 3840)
        self.assertEqual(cam.height, 2160)
        self.assertEqual(cam.pixel_size().to('micrometer').magnitude, 2.9)
        self.assertEqual(cam.full_well, 40000)
        self.assertEqual(cam.read_noise, 0.6)
        self.assertEqual(cam.quantum_efficiency, 91)

        # Test V2 variant via from_database check indirectly
        cam_v2 = ZwoCamera.ZWO_ASI_585MC_V2()
        self.assertEqual(cam_v2.mass.to('gram').magnitude, 155)
        self.assertEqual(cam_v2.full_well, 40000)

    def test_asi678_specs(self):
        cam = ZwoCamera.ZWO_ASI_678MC()
        self.assertEqual(cam.sensor_width.to('mm').magnitude, 7.68)
        self.assertEqual(cam.sensor_height.to('mm').magnitude, 4.32)
        self.assertEqual(cam.width, 3840)
        self.assertEqual(cam.height, 2160)
        self.assertEqual(cam.pixel_size().to('micrometer').magnitude, 2.0)
        self.assertEqual(cam.full_well, 11270)
        self.assertEqual(cam.read_noise, 0.6)
        self.assertEqual(cam.quantum_efficiency, 83)

    def test_asi664_specs(self):
        cam = ZwoCamera.ZWO_ASI_664MC()
        self.assertEqual(cam.sensor_width.to('mm').magnitude, 7.841)
        self.assertEqual(cam.sensor_height.to('mm').magnitude, 4.454)
        self.assertEqual(cam.width, 2704)
        self.assertEqual(cam.height, 1536)
        self.assertEqual(cam.pixel_size().to('micrometer').magnitude, 2.9)
        self.assertEqual(cam.full_well, 36500)
        self.assertEqual(cam.read_noise, 0.46)
        self.assertEqual(cam.quantum_efficiency, 91)
        self.assertEqual(cam.optical_length.to('mm').magnitude, 12.5)

if __name__ == '__main__':
    unittest.main()
