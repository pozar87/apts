import unittest

from apts.cache import get_timescale
from apts.opticalequipment.camera.vendors.qhy import QhyCamera
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.optics import OpticalPath
from apts.utils import planetary


class TestStellarV6(unittest.TestCase):
    def test_saturn_ring_tilt_2025(self):
        ts = get_timescale()
        # Saturn rings are nearly edge-on in March 2025
        t = ts.utc(2025, 3, 23)
        details = planetary.get_saturn_ring_details(t)
        # Expected tilt is very small, < 1 degree
        self.assertLess(abs(details["tilt_degrees"]), 1.0)
        self.assertGreater(details["major_axis_arcsec"], 35.0)
        self.assertLess(details["minor_axis_arcsec"], 1.0)

    def test_saturn_ring_tilt_2017(self):
        ts = get_timescale()
        # Saturn rings were at maximum tilt in 2017 (~27 deg)
        t = ts.utc(2017, 10, 1)
        details = planetary.get_saturn_ring_details(t)
        self.assertAlmostEqual(details["tilt_degrees"], 26.9, delta=1.0)
        self.assertGreater(details["minor_axis_arcsec"], 15.0)

    def test_optical_path_saturn_rings(self):
        ts = get_timescale()
        t = ts.utc(2024, 9, 1)  # ~3.6 deg tilt
        telescope = Sky_watcherTelescope.Sky_Watcher_Explorer_130P()
        camera = ZwoCamera.ZWO_ASI_664MC()
        path = OpticalPath.from_path([telescope, camera])

        rings_px = path.saturn_ring_size_in_pixels(t)
        self.assertIsNotNone(rings_px)
        assert rings_px is not None
        major, minor = rings_px
        self.assertGreater(major, 40.0)
        self.assertGreater(minor, 2.0)

    def test_camera_664_specs(self):
        zwo_mc = ZwoCamera.ZWO_ASI_664MC()
        zwo_mm = ZwoCamera.ZWO_ASI_664MM()
        qhy_c = QhyCamera.QHY_QHY_5III_664C()

        for cam in [zwo_mc, zwo_mm, qhy_c]:
            self.assertEqual(cam.width, 2704)
            self.assertEqual(cam.height, 1536)
            self.assertEqual(cam.pixel_size().magnitude, 2.9)
            if "ZWO" in cam.vendor:
                self.assertEqual(cam.full_well, 36500)
            else:
                self.assertEqual(cam.full_well, 38500)


if __name__ == "__main__":
    unittest.main()
