import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
import numpy as np
from datetime import datetime
from skyfield.api import utc

from apts.utils.polar_alignment import suggest_polar_alignment_stars, PolarAlignment
from apts.constants import ObjectTableLabels

class TestPolarAlignment(unittest.TestCase):
    def setUp(self):
        self.mock_observation = MagicMock()
        self.mock_observation.effective_date = datetime(2025, 1, 1, 20, 0, 0, tzinfo=utc)
        self.mock_observation.observation_local_time = self.mock_observation.effective_date
        self.mock_observation.place.lat_decimal = 52.2
        self.mock_observation.place.lon_decimal = 21.0
        self.mock_observation.place.ts.utc.return_value = self.mock_observation.effective_date

    def test_suggest_polar_alignment_stars(self):
        # Mock stars catalog
        mock_stars = pd.DataFrame({
            "Name": ["Polaris", "Vega", "Sirius"],
            ObjectTableLabels.ALTITUDE: [52.0, 45.0, 10.0],
            "Magnitude_float": [2.0, 0.0, -1.4],
            "ra_hours": [2.5, 18.5, 6.7],
            "dec_degrees": [89.2, 38.8, -16.7]
        })

        self.mock_observation.local_stars.get_visible.return_value = mock_stars

        candidates = suggest_polar_alignment_stars(self.mock_observation)

        self.assertFalse(candidates.empty)
        self.assertIn("Polaris", candidates["Name"].values)
        self.assertIn("Vega", candidates["Name"].values)
        self.assertNotIn("Sirius", candidates["Name"].values) # Altitude too low

        # Should be sorted by magnitude (Vega 0.0 before Polaris 2.0)
        self.assertEqual(candidates.iloc[0]["Name"], "Vega")

    def test_fit_circle_2_points(self):
        pa = PolarAlignment(self.mock_observation)
        # Simulate 2 points on a circle centered at (500, 500) with radius 100
        # p1 = (600, 500), p2 = (500, 600) => 90 degree rotation
        pa.frames = [
            {"target": {"x": 600, "y": 500}, "ra_rotation": 0},
            {"target": {"x": 500, "y": 600}, "ra_rotation": 90}
        ]

        center = pa._fit_circle()
        np.testing.assert_allclose(center, [500, 500], atol=1e-7)

    def test_fit_circle_3_points(self):
        pa = PolarAlignment(self.mock_observation)
        # 3 points on circle centered at (100, 100) with radius 50
        pa.frames = [
            {"target": {"x": 150, "y": 100}, "ra_rotation": 0},
            {"target": {"x": 100, "y": 150}, "ra_rotation": 90},
            {"target": {"x": 50, "y": 100}, "ra_rotation": 180}
        ]

        center = pa._fit_circle()
        np.testing.assert_allclose(center, [100, 100], atol=1e-7)

    @patch("apts.utils.polar_alignment.FitsAnalyzer")
    def test_add_frame_tracking(self, mock_fits):
        mock_analyzer = MagicMock()
        mock_fits.return_value = mock_analyzer
        mock_analyzer.data = np.zeros((1000, 1000))

        # First frame
        mock_analyzer.fitted_stars = [{"x": 100, "y": 100}, {"x": 500, "y": 500}]
        mock_analyzer.stars = [{"x": 100, "y": 100, "flux": 1000}, {"x": 500, "y": 500, "flux": 10}]

        pa = PolarAlignment(self.mock_observation)
        pa.add_frame("frame1.fits", 0)

        self.assertEqual(len(pa.frames), 1)
        self.assertEqual(pa.frames[0]["target"]["x"], 100) # Brightest selected

        # Second frame: target moved slightly
        mock_analyzer.fitted_stars = [{"x": 105, "y": 102}, {"x": 500, "y": 500}]
        pa.add_frame("frame2.fits", 10)

        self.assertEqual(len(pa.frames), 2)
        self.assertEqual(pa.frames[1]["target"]["x"], 105) # Tracked closest

    def test_calculate_correction_perfect_alignment(self):
        # Mock star
        mock_star = MagicMock()
        mock_star.ra.hours = 2.5
        mock_star.dec.degrees = 89.2
        self.mock_observation.local_stars.find_by_name.return_value = mock_star

        # Mock altaz
        mock_alt = MagicMock()
        mock_alt.degrees = 52.0
        mock_az = MagicMock()
        mock_az.degrees = 0.0
        mock_altaz_obj = MagicMock()
        mock_altaz_obj.altaz.return_value = (mock_alt, mock_az, None)
        self.mock_observation.place.observer.at().observe.return_value.apparent.return_value = mock_altaz_obj

        # Mock time object with gmst
        mock_time = MagicMock()
        mock_time.gmst = 2.5 # matching ra_hours for H=0
        self.mock_observation.place.ts.utc.return_value = mock_time

        pa = PolarAlignment(self.mock_observation, target_star_name="Polaris")
        pa.pixel_scale = 28.8

        pa.frames = [
            {"target": {"x": 600, "y": 500}, "ra_rotation": 0},
            {"target": {"x": 500, "y": 600}, "ra_rotation": 90}
        ]
        pa.mount_axis_image = np.array([500, 500])

        # Don't mock np.radians, let it run real math
        correction = pa.calculate_correction()
        self.assertIsNotNone(correction)
        self.assertIn("Altitude", correction["instructions"])

if __name__ == "__main__":
    unittest.main()
