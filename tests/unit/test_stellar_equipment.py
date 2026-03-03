import unittest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

class TestNewEquipment(unittest.TestCase):
    def test_asi432mm_specs(self):
        cam = ZwoCamera.ZWO_ASI_432MM()
        self.assertEqual(cam.get_vendor(), "ZWO ASI432MM")
        self.assertEqual(cam.sensor_width.to('mm').magnitude, 14.5)
        self.assertEqual(cam.sensor_height.to('mm').magnitude, 9.9)
        self.assertEqual(cam.width, 1608)
        self.assertEqual(cam.height, 1104)
        self.assertEqual(cam.pixel_size().to('micrometer').magnitude, 9.0)
        self.assertEqual(cam.full_well, 97000)
        self.assertEqual(cam.read_noise, 2.4)
        self.assertEqual(cam.quantum_efficiency, 79)
        self.assertEqual(cam.mass.to('gram').magnitude, 126)

    def test_evolux_62ed_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Evolux_62ED()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Evolux 62ED")
        self.assertEqual(scope.aperture.to('mm').magnitude, 62)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 400)
        self.assertEqual(scope.mass.to('gram').magnitude, 2500)

    def test_evolux_82ed_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Evolux_82ED()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Evolux 82ED")
        self.assertEqual(scope.aperture.to('mm').magnitude, 82)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 530)
        self.assertEqual(scope.mass.to('gram').magnitude, 2920)

if __name__ == '__main__':
    unittest.main()
