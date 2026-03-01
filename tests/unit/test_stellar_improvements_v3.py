import unittest
from unittest.mock import MagicMock
from apts.optics import OpticalPath
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.camera.vendors.qhy import QhyCamera
from apts.units import get_unit_registry

class TestStellarImprovementsV3(unittest.TestCase):
    def test_sampling_diffraction_limited(self):
        # Setup: Small telescope (80mm) with extremely good seeing (0.5")
        # Dawes limit for 80mm is ~1.45", Rayleigh limit is ~1.7"
        t = MagicMock(spec=Telescope)
        t.focal_length = 400 * get_unit_registry().mm
        t.aperture = 80 * get_unit_registry().mm

        # Rayleigh limit = 1.22 * 550nm / 80mm ~ 1.702 arcsec
        t.rayleigh_limit.return_value = 1.702 * get_unit_registry().arcsecond

        c = MagicMock(spec=Camera)
        # Pixel scale = (3.76 / 400) * 206265 = 1.939 arcsec/pixel
        c.pixel_size.return_value = 3.76 * get_unit_registry().micrometer

        path = OpticalPath(t, [], [], [], [], c)

        # Case 1: Seeing (0.5") < Rayleigh (1.702")
        # Resolution limit = 1.702"
        # Ratio = 1.702 / 1.939 = 0.877 (< 1.5 -> Under-sampled)
        status = path.sampling(seeing=0.5)
        self.assertEqual(status, "Under-sampled")

        # Case 2: Seeing (5.0") > Rayleigh (1.702")
        # Resolution limit = 5.0"
        # Ratio = 5.0 / 1.939 = 2.578 (Well-sampled, 1.0 <= ratio <= 3.0)
        status_bad_seeing = path.sampling(seeing=5.0)
        self.assertEqual(status_bad_seeing, "Well-sampled")

        # Case 3: Extreme seeing
        # Ratio = 7.0 / 1.939 = 3.61 (> 3.0 -> Over-sampled)
        status_extreme_seeing = path.sampling(seeing=7.0)
        self.assertEqual(status_extreme_seeing, "Over-sampled")

    def test_sampling_nyquist_thresholds(self):
        t = MagicMock(spec=Telescope)
        t.rayleigh_limit.return_value = 2.0 * get_unit_registry().arcsecond

        c = MagicMock(spec=Camera)
        # Mock pixel_size and telescope.focal_length so pixel_scale() works
        t.focal_length = 100 * get_unit_registry().mm
        c.pixel_size.return_value = 1.0 * get_unit_registry().micrometer

        path = OpticalPath(t, [], [], [], [], c)

        # Resolution limit will be max(seeing=2.0, rayleigh=2.0) = 2.0

        # Ratio = 2.0 / pixel_scale
        # Ratio 0.8 (< 1.0) -> Under-sampled
        # pixel_scale = 2.5
        # (p_size / 100) * 206265 = 2.5 => p_size = 2.5 * 100 / 206265
        c.pixel_size.return_value = (2.5 * 100 / 206265) * get_unit_registry().mm
        self.assertEqual(path.sampling(seeing=2.0), "Under-sampled")

        # Ratio 1.5 (Well-sampled, 1.0-2.0)
        # pixel_scale = 2.0 / 1.5 = 1.333
        c.pixel_size.return_value = (1.3333 * 100 / 206265) * get_unit_registry().mm
        self.assertEqual(path.sampling(seeing=2.0), "Well-sampled")

        # Ratio 4.0 (> 2.0) -> Over-sampled
        # pixel_scale = 0.5
        c.pixel_size.return_value = (0.5 * 100 / 206265) * get_unit_registry().mm
        self.assertEqual(path.sampling(seeing=2.0), "Over-sampled")

    def test_zwo_duo_cameras(self):
        mc_duo = ZwoCamera.ZWO_ASI2600MC_DUO()
        self.assertEqual(mc_duo.vendor, "ZWO ASI2600MC Duo")
        self.assertEqual(mc_duo.mass, 800 * get_unit_registry().gram)
        self.assertEqual(mc_duo.backfocus, 17.5 * get_unit_registry().mm)
        self.assertEqual(mc_duo.quantum_efficiency, 80)

        mm_duo = ZwoCamera.ZWO_ASI2600MM_DUO()
        self.assertEqual(mm_duo.vendor, "ZWO ASI2600MM Duo")
        self.assertEqual(mm_duo.quantum_efficiency, 91)

    def test_zwo_updated_pro_cameras(self):
        mc_pro = ZwoCamera.ZWO_ASI2600MC_PRO()
        self.assertEqual(mc_pro.mass, 720 * get_unit_registry().gram)
        self.assertEqual(mc_pro.backfocus, 17.5 * get_unit_registry().mm)

        ff_pro = ZwoCamera.ZWO_ASI6200MM_PRO()
        self.assertEqual(ff_pro.mass, 1010 * get_unit_registry().gram)
        self.assertEqual(ff_pro.backfocus, 17.5 * get_unit_registry().mm)

    def test_qhy_new_cameras(self):
        q600m = QhyCamera.QHY_QHY_600M()
        self.assertEqual(q600m.vendor, "QHY QHY 600M")
        # For factory methods, pixel_size() is set explicitly
        self.assertAlmostEqual(q600m.pixel_size().to("micrometer").magnitude, 3.76, places=2)
        self.assertEqual(q600m.mass, 1050 * get_unit_registry().gram)

        q268c = QhyCamera.QHY_QHY_268C()
        self.assertEqual(q268c.vendor, "QHY QHY 268C")
        self.assertEqual(q268c.quantum_efficiency, 81)

if __name__ == "__main__":
    unittest.main()
