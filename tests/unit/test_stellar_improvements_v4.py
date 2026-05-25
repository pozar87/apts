import unittest
from apts.opticalequipment.binoculars import Binoculars
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.camera import Camera
from apts.optics import OpticalPath

class TestStellarImprovementsV4(unittest.TestCase):
    def test_binoculars_rayleigh_limit_precision(self):
        # 10x50 Binoculars
        b = Binoculars(10, 50, "Nikon", 65)
        # 1.22 * 550nm / 50mm * 206265 = 2.768 arcsec
        limit = b.rayleigh_limit(wavelength_nm=550)
        self.assertAlmostEqual(limit.magnitude, 2.768, places=3)

        # H-alpha (656.3nm)
        # 1.22 * 656.3nm / 50mm * 206265 = 3.303 arcsec
        limit_ha = b.rayleigh_limit(wavelength_nm=656.3)
        self.assertAlmostEqual(limit_ha.magnitude, 3.303, places=3)

    def test_new_sampling_thresholds(self):
        # Setup path that will give specific ratios
        t = Telescope(aperture=100, focal_length=1000) # f/10
        c = Camera(36, 24, 6000, 4000) # pixel size = sqrt(36^2+24^2)/sqrt(6000^2+4000^2) ~ 0.006mm = 6um
        # scale = (6 / 1000) * 206265 = 1.23759 arcsec/pixel
        # Rayleigh limit (100mm) = 1.384 arcsec

        path = OpticalPath(t, [], [], [], [], c)

        # Case 1: Under-sampled (ratio < 1.0)
        # r_limit < 1.23759
        # Seeing 0.5, Rayleigh 1.384 => r_limit = 1.384
        # Ratio = 1.384 / 1.23759 = 1.118 (Well-sampled)

        # Let's force scale to be larger for under-sampled
        # focal_length = 500 => scale = 2.475
        t2 = Telescope(aperture=100, focal_length=500)
        path2 = OpticalPath(t2, [], [], [], [], c)
        # r_limit = max(seeing=1.0, Rayleigh=1.384) = 1.384
        # Ratio = 1.384 / 2.475 = 0.559 => Under-sampled
        self.assertEqual(path2.sampling(seeing=1.0), "Under-sampled")

        # Case 2: Well-sampled (1.0 <= ratio <= 3.0)
        # t1: scale = 1.23759, r_limit = 1.384 => Ratio = 1.118
        self.assertEqual(path.sampling(seeing=1.0), "Well-sampled")

        # Ratio 2.5
        # r_limit = 2.5 * 1.23759 = 3.0939
        self.assertEqual(path.sampling(seeing=3.0939), "Well-sampled")

        # Case 3: Over-sampled (ratio > 3.0)
        # Ratio 3.1 => r_limit = 3.1 * 1.23759 = 3.8365
        self.assertEqual(path.sampling(seeing=3.8365), "Over-sampled")

    def test_sky_watcher_verified_data(self):
        # Esprit 100ED: 100mm, 550mm, 6300g
        esprit100 = Sky_watcherTelescope.Sky_Watcher_Esprit_100ED()
        self.assertEqual(esprit100.aperture.to("mm").magnitude, 100)
        self.assertEqual(esprit100.focal_length.to("mm").magnitude, 550)
        self.assertEqual(esprit100.mass.to("gram").magnitude, 6300)

        # Evostar 72ED: 72mm, 420mm, 1950g
        evo72 = Sky_watcherTelescope.Sky_Watcher_Evostar_72ED()
        self.assertEqual(evo72.aperture.to("mm").magnitude, 72)
        self.assertEqual(evo72.focal_length.to("mm").magnitude, 420)
        self.assertEqual(evo72.mass.to("gram").magnitude, 1950)

        # Esprit 150ED: 150mm, 1050mm, 14520g
        esprit150 = Sky_watcherTelescope.Sky_Watcher_Esprit_150ED()
        self.assertEqual(esprit150.aperture.to("mm").magnitude, 150)
        self.assertEqual(esprit150.focal_length.to("mm").magnitude, 1050)
        self.assertEqual(esprit150.mass.to("gram").magnitude, 14520)

if __name__ == "__main__":
    unittest.main()
