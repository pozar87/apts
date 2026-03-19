import unittest
from datetime import datetime, timezone
from apts.utils import planetary
from apts.cache import get_timescale

class TestPlanetaryMagnitude(unittest.TestCase):
    def setUp(self):
        self.ts = get_timescale()
        # 2024-03-25 is a Full Moon
        self.full_moon_date = datetime(2024, 3, 25, 7, 0, 0, tzinfo=timezone.utc)
        self.full_moon_t = self.ts.from_datetime(self.full_moon_date)

        # 2024-04-01 is around Last Quarter
        self.quarter_moon_date = datetime(2024, 4, 1, 3, 0, 0, tzinfo=timezone.utc)
        self.quarter_moon_t = self.ts.from_datetime(self.quarter_moon_date)

    def test_sun_magnitude(self):
        """Verify Sun magnitude is around -26.7."""
        mag = planetary.get_planet_magnitude("sun", self.full_moon_t)
        # Should be very close to -26.74 at ~1 AU
        self.assertAlmostEqual(mag, -26.74, delta=0.5)

    def test_moon_magnitude(self):
        """Verify Moon magnitude for Full and Quarter phases."""
        mag_full = planetary.get_planet_magnitude("moon", self.full_moon_t)
        # Full Moon should be around -12.7
        self.assertAlmostEqual(mag_full, -12.7, delta=1.0)

        mag_quarter = planetary.get_planet_magnitude("moon", self.quarter_moon_t)
        # Quarter Moon should be around -10.0 (about 2.5-3 mags fainter than full)
        self.assertLess(mag_quarter, -9.0)
        self.assertGreater(mag_quarter, -11.0)

    def test_major_planets_magnitude(self):
        """Verify magnitude calculation for major planets."""
        # Venus is usually the brightest planet
        mag_venus = planetary.get_planet_magnitude("venus", self.full_moon_t)
        self.assertLess(mag_venus, -3.0)
        self.assertGreater(mag_venus, -5.0)

        # Jupiter
        mag_jupiter = planetary.get_planet_magnitude("jupiter", self.full_moon_t)
        self.assertLess(mag_jupiter, -1.5)
        self.assertGreater(mag_jupiter, -3.0)

        # Mars (varies a lot, but usually > -3.0)
        mag_mars = planetary.get_planet_magnitude("mars", self.full_moon_t)
        self.assertGreater(mag_mars, -3.0)

    def test_invalid_planet(self):
        """Test handling of unknown objects."""
        with self.assertRaises(ValueError):
            planetary.get_planet_magnitude("Krypton", self.full_moon_t)

if __name__ == "__main__":
    unittest.main()
