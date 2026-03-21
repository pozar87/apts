import unittest
from apts.utils import planetary
from apts.cache import get_timescale

class TestPlanetarySurfaceBrightness(unittest.TestCase):
    def setUp(self):
        self.ts = get_timescale()
        # Near Full Moon for benchmark (approx May 23, 2024 12:00 UTC)
        self.t = self.ts.utc(2024, 5, 23, 12, 0)

    def test_sun_surface_brightness(self):
        """Verify Sun surface brightness is approx -10.6 mag/arcsec^2."""
        sb = planetary.get_planet_surface_brightness("sun", self.t)
        self.assertAlmostEqual(sb, -10.6, delta=0.5)

    def test_moon_surface_brightness(self):
        """Verify Moon surface brightness is approx 3.4 mag/arcsec^2 (Near Full)."""
        sb = planetary.get_planet_surface_brightness("moon", self.t)
        self.assertAlmostEqual(sb, 3.4, delta=0.5)

    def test_jupiter_surface_brightness(self):
        """Verify Jupiter surface brightness is approx 5.5 mag/arcsec^2."""
        sb = planetary.get_planet_surface_brightness("jupiter", self.t)
        self.assertAlmostEqual(sb, 5.5, delta=0.5)

if __name__ == "__main__":
    unittest.main()
