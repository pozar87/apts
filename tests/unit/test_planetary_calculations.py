import unittest
import numpy as np

from apts.utils.planetary.calculations import (
    calculate_sub_observer_latitude,
    calculate_apparent_polar_radius,
    calculate_angular_diameter,
    calculate_illuminated_fraction,
    calculate_illuminated_disk_area,
    calculate_surface_brightness,
    calculate_sun_magnitude,
    calculate_moon_magnitude_krisciunas,
)


class TestPlanetaryCalculations(unittest.TestCase):
    def test_calculate_sub_observer_latitude_scalar(self):
        # Test zero declination and same RA/Dec
        res = calculate_sub_observer_latitude(
            alpha_rad=0.0,
            delta_rad=0.0,
            alpha0_rad=0.0,
            delta0_rad=np.radians(90.0),  # North pole at Dec=90
        )
        self.assertIsInstance(res, float)
        self.assertAlmostEqual(res, 0.0, places=5)

    def test_calculate_sub_observer_latitude_array(self):
        alpha_rad = np.array([0.0, np.pi / 2])
        delta_rad = np.array([0.0, 0.0])
        alpha0_rad = np.array([0.0, 0.0])
        delta0_rad = np.array([np.pi / 2, np.pi / 2])
        res = calculate_sub_observer_latitude(
            alpha_rad, delta_rad, alpha0_rad, delta0_rad
        )
        self.assertIsInstance(res, np.ndarray)
        self.assertEqual(len(res), 2)

    def test_calculate_apparent_polar_radius(self):
        # Jupiter: r_eq ~ 71492 km, r_pol ~ 66854 km
        r_eq = 71492.0
        r_pol = 66854.0

        # At tilt = 0 deg (equator-on view), apparent polar radius = r_pol
        res_0 = calculate_apparent_polar_radius(r_eq, r_pol, De_deg=0.0)
        self.assertAlmostEqual(res_0, r_pol, places=2)

        # At tilt = 90 deg (pole-on view), apparent polar radius = r_eq
        res_90 = calculate_apparent_polar_radius(r_eq, r_pol, De_deg=90.0)
        self.assertAlmostEqual(res_90, r_eq, places=2)

    def test_calculate_angular_diameter(self):
        # Jupiter ~ 71492 km radius at ~ 778.5e6 km distance
        r_km = 71492.0
        dist_km = 778.5e6
        ang_diam = calculate_angular_diameter(r_km, dist_km)
        self.assertIsInstance(ang_diam, float)
        self.assertGreater(ang_diam, 30.0)
        self.assertLess(ang_diam, 50.0)

    def test_calculate_illuminated_fraction(self):
        # Phase angle = 0 rad (full disk) -> fraction = 1.0
        self.assertAlmostEqual(calculate_illuminated_fraction(0.0), 1.0)
        # Phase angle = pi/2 rad (half disk) -> fraction = 0.5
        self.assertAlmostEqual(calculate_illuminated_fraction(np.pi / 2), 0.5)
        # Phase angle = pi rad (new/dark disk) -> fraction = 0.0
        self.assertAlmostEqual(calculate_illuminated_fraction(np.pi), 0.0)

    def test_calculate_illuminated_disk_area(self):
        # Diameter = 10 arcsec, fraction = 1.0 -> pi * 5^2 = ~78.5398 arcsec2
        area = calculate_illuminated_disk_area(10.0, 1.0)
        self.assertAlmostEqual(area, np.pi * 25.0, places=5)

    def test_calculate_surface_brightness(self):
        # V = 5.0, Area = 100 arcsec2 -> 5.0 + 2.5 * log10(100) = 5.0 + 5.0 = 10.0
        sb = calculate_surface_brightness(5.0, 100.0)
        self.assertAlmostEqual(sb, 10.0, places=5)

        # Zero or negative area -> float('inf')
        self.assertEqual(calculate_surface_brightness(5.0, 0.0), float("inf"))
        self.assertEqual(calculate_surface_brightness(5.0, -10.0), float("inf"))

        # Array input
        areas = np.array([100.0, 0.0, 10.0])
        sb_arr = calculate_surface_brightness(5.0, areas)
        self.assertIsInstance(sb_arr, np.ndarray)
        self.assertAlmostEqual(sb_arr[0], 10.0, places=5)
        self.assertTrue(np.isinf(sb_arr[1]))

    def test_calculate_sun_magnitude(self):
        # At 1.0 AU, Sun magnitude = -26.74
        m1 = calculate_sun_magnitude(1.0)
        self.assertAlmostEqual(m1, -26.74, places=5)

        # At 2.0 AU, magnitude increases by 5 * log10(2) ~ 1.505
        m2 = calculate_sun_magnitude(2.0)
        self.assertAlmostEqual(m2, -26.74 + 5 * np.log10(2.0), places=5)

    def test_calculate_moon_magnitude_krisciunas(self):
        # At phase = 0 deg and mean distance 384400 km
        m0 = calculate_moon_magnitude_krisciunas(0.0, 384400.0)
        self.assertAlmostEqual(m0, -12.73, places=5)


if __name__ == "__main__":
    unittest.main()
