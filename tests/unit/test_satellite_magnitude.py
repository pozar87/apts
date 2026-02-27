import unittest

import numpy as np

from apts.skyfield_searches import calculate_satellite_magnitude


class TestSatelliteMagnitude(unittest.TestCase):
    def test_iss_magnitude_zenith_full_phase(self):
        """
        Test ISS magnitude at 400km (near zenith) with 0 phase angle (fully sunlit).
        ISS standard magnitude is -1.8 at 1000km.
        Calculation: -1.8 + 5 * log10(400/1000) - 2.5 * log10(1)
        -1.8 + 5 * (-0.3979) = -1.8 - 1.989 = -3.789
        """
        # Satellite is at [400, 0, 0]
        # Sun is at [1000, 0, 0] (infinite distance effectively, but vector sat->sun is [1, 0, 0])
        # Observer is at [0, 0, 0]
        # Vector sat_to_sun = [600, 0, 0] -> normalized [1, 0, 0]
        # Vector sat_to_obs = [-400, 0, 0] -> normalized [-1, 0, 0]
        # Wait, phase angle beta is angle between sat->sun and sat->observer.
        # For "fully sunlit" (phase=0), the sun must be behind the observer's back.

        sat_pos = np.array([400.0, 0.0, 0.0])
        sun_pos = np.array([-1000.0, 0.0, 0.0])  # Sun is far away in -X
        obs_pos = np.array([0.0, 0.0, 0.0])  # Observer is at origin
        distance = 400.0

        # sat_to_sun = [-1400, 0, 0] -> dir [-1, 0, 0]
        # sat_to_obs = [-400, 0, 0]  -> dir [-1, 0, 0]
        # angle = 0

        mag = calculate_satellite_magnitude(
            "ISS (ZARYA)", sat_pos, sun_pos, obs_pos, distance
        )
        self.assertAlmostEqual(mag, -3.789, places=2)

    def test_iss_magnitude_high_altitude_half_phase(self):
        """
        Test ISS at 1000km with 90 degree phase angle.
        Phi(pi/2) = (sin(pi/2) + (pi - pi/2)*cos(pi/2)) / pi = 1/pi
        Calculation: -1.8 + 5 * log10(1) - 2.5 * log10(1/pi)
        -1.8 + 0 - 2.5 * (-0.497) = -1.8 + 1.24 = -0.56
        """
        sat_pos = np.array([0.0, 0.0, 0.0])
        sun_pos = np.array([10000.0, 0.0, 0.0])  # Sun in +X
        obs_pos = np.array([0.0, 1000.0, 0.0])  # Observer in +Y
        distance = 1000.0

        # sat_to_sun = [1, 0, 0]
        # sat_to_obs = [0, 1, 0]
        # angle = 90 deg (pi/2)

        mag = calculate_satellite_magnitude(
            "ISS (ZARYA)", sat_pos, sun_pos, obs_pos, distance
        )
        self.assertAlmostEqual(mag, -0.557, places=2)

    def test_tiangong_magnitude_standard(self):
        """
        Test Tiangong at standard 1000km distance, 0 phase.
        Should equal its standard magnitude 0.0.
        """
        sat_pos = np.array([1000.0, 0.0, 0.0])
        sun_pos = np.array([-2000.0, 0.0, 0.0])
        obs_pos = np.array([0.0, 0.0, 0.0])
        distance = 1000.0

        mag = calculate_satellite_magnitude(
            "CSS (TIANHE)", sat_pos, sun_pos, obs_pos, distance
        )
        self.assertAlmostEqual(mag, 0.0, places=2)

    def test_magnitude_fallback(self):
        """Test handling of zero vectors or invalid distances."""
        sat_pos = np.array([0.0, 0.0, 0.0])
        sun_pos = np.array([0.0, 0.0, 0.0])
        obs_pos = np.array([0.0, 0.0, 0.0])
        distance = 1000.0

        mag = calculate_satellite_magnitude("ISS", sat_pos, sun_pos, obs_pos, distance)
        self.assertEqual(mag, 5.0)

    def test_extreme_phase_angle(self):
        """Test magnitude when satellite is almost between observer and sun (crescent)."""
        # 170 degree phase angle (almost 180, which would be 0 illumination)
        sat_pos = np.array([0.0, 0.0, 0.0])
        sun_pos = np.array([100.0, 0.0, 0.0])

        # Observer looking almost towards the sun (170 degrees from sun-sat vector)
        angle = np.radians(170)
        obs_pos = np.array([1000.0 * np.cos(angle), 1000.0 * np.sin(angle), 0.0])
        distance = 1000.0

        mag = calculate_satellite_magnitude(
            "ISS (ZARYA)", sat_pos, sun_pos, obs_pos, distance
        )
        # Standard magnitude is -1.8 at 0 phase. At 170 phase, it should be much fainter.
        self.assertGreater(mag, 5.0)


if __name__ == "__main__":
    unittest.main()
