import unittest

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.optics import OpticalPath


class TestStellarUpdates(unittest.TestCase):
    def test_seestar_s30_pro_specs(self):
        s30_pro = ZwoTelescope.ZWO_Seestar_S30_Pro()
        self.assertEqual(s30_pro.aperture.magnitude, 30)
        self.assertEqual(s30_pro.focal_length.magnitude, 150)
        self.assertEqual(s30_pro.sensor_width.magnitude, 7.68)
        self.assertEqual(s30_pro.sensor_height.magnitude, 4.32)
        # Pixel size for IMX678 (3840x2160 on 7.68x4.32mm) is 2.0um
        self.assertAlmostEqual(s30_pro.pixel_size().magnitude, 2.0, places=1)
        self.assertEqual(s30_pro.full_well, 11270)
        self.assertEqual(s30_pro.quantum_efficiency, 83)

    def test_asi585mm_pro_specs(self):
        cam = ZwoCamera.ZWO_ASI_585MM_Pro()
        self.assertEqual(cam.sensor_width.magnitude, 11.13)
        self.assertEqual(cam.sensor_height.magnitude, 6.26)
        self.assertAlmostEqual(cam.pixel_size().magnitude, 2.9, places=1)
        self.assertEqual(cam.full_well, 40000)
        self.assertEqual(cam.quantum_efficiency, 91)
        self.assertEqual(cam.mass.magnitude, 470)

    def test_asi585mc_pro_specs(self):
        cam = ZwoCamera.ZWO_ASI_585MC_Pro()
        self.assertEqual(cam.sensor_width.magnitude, 11.13)
        self.assertEqual(cam.sensor_height.magnitude, 6.26)
        self.assertAlmostEqual(cam.pixel_size().magnitude, 2.9, places=1)
        self.assertEqual(cam.full_well, 40000)
        self.assertEqual(cam.quantum_efficiency, 80)
        self.assertEqual(cam.mass.magnitude, 470)

    def test_estimated_star_trailing(self):
        # Setup: 500mm focal length, 3.76um pixels
        # Pixel scale = (3.76 / 500) * 206265 = 1.551 arcsec/pixel
        from apts.opticalequipment.camera import Camera
        from apts.opticalequipment.telescope import Telescope

        tele = Telescope(80, 500, vendor="Test Scope")
        cam = Camera(23.5, 15.7, 6248, 4176, vendor="Test Cam", pixel_size=3.76)
        path = OpticalPath.from_path([tele, cam])

        # At Dec 0, sidereal rate is 15.041 "/s
        # In 10 seconds, movement is 150.41"
        # Trailing in pixels = 150.41 / 1.551 = 96.97 pixels
        trailing = path.estimated_star_trailing(exposure_time=10, declination=0)
        self.assertIsNotNone(trailing)
        self.assertAlmostEqual(trailing, 96.97, places=1)  # type: ignore

        # At Dec 60, cos(60) = 0.5, movement is 75.205"
        # Trailing = 75.205 / 1.551 = 48.48 pixels
        trailing_60 = path.estimated_star_trailing(exposure_time=10, declination=60)
        self.assertIsNotNone(trailing_60)
        self.assertAlmostEqual(trailing_60, 48.48, places=1)  # type: ignore

    def test_optimum_sub_exposure_with_swamp(self):
        from apts.opticalequipment.camera import Camera
        from apts.opticalequipment.telescope import Telescope

        tele = Telescope(80, 500, vendor="Test Scope")
        # Read noise 1.0e-, QE 80%
        cam = Camera(
            23.5,
            15.7,
            6248,
            4176,
            vendor="Test Cam",
            pixel_size=3.76,
            read_noise=1.0,
            quantum_efficiency=80.0,
        )
        path = OpticalPath.from_path([tele, cam])

        sqm = 21.0

        t10 = path.optimum_sub_exposure(sqm, swamp_factor=10.0)
        t20 = path.optimum_sub_exposure(sqm, swamp_factor=20.0)

        # Strengthen assertion: ensure results are not None and correctly scaled
        self.assertIsNotNone(t10)
        self.assertIsNotNone(t20)
        self.assertAlmostEqual(t20.magnitude, 2.0 * t10.magnitude, places=4)  # type: ignore


if __name__ == "__main__":
    unittest.main()
