import unittest
from unittest.mock import MagicMock
import numpy as np
import pandas as pd
from apts.objects.calculations.visibility import (
    calculate_visible_stars_mask,
    filter_objects_by_magnitude,
)


class TestVisibilityCalculations(unittest.TestCase):
    def test_filter_objects_by_magnitude_scalar(self):
        df = pd.DataFrame({
            "Name": ["Obj1", "Obj2", "Obj3"],
            "Magnitude": [2.0, 5.0, 8.0],
        })
        conditions = MagicMock()
        conditions.max_object_magnitude = 6.0

        filtered = filter_objects_by_magnitude(df, conditions)
        self.assertEqual(len(filtered), 2)
        self.assertListEqual(list(filtered["Name"]), ["Obj1", "Obj2"])

    def test_filter_objects_by_magnitude_float_column(self):
        df = pd.DataFrame({
            "Name": ["Obj1", "Obj2", "Obj3"],
            "Magnitude": [2.0, 5.0, 8.0],
            "Magnitude_float": [2.0, 5.0, 8.0],
        })
        conditions = MagicMock()
        conditions.max_object_magnitude = 4.0

        filtered = filter_objects_by_magnitude(df, conditions)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]["Name"], "Obj1")

    def test_calculate_visible_stars_mask_basic(self):
        # Observer at lat 52.0, lon 21.0
        lat_decimal = 52.0
        lon_decimal = 21.0

        # Star 1: Circumpolar high altitude star (Dec 80)
        # Star 2: Deep southern star unreachable at lat 52 (Dec -80)
        stars_ras = np.array([0.0, 12.0])
        stars_decs = np.array([80.0, -80.0])
        check_times_gmst = np.array([0.0, 6.0, 12.0, 18.0])

        conditions = MagicMock()
        conditions.horizon_content = False
        conditions.horizon_file = False
        conditions.min_object_azimuth = 0
        conditions.max_object_azimuth = 360
        conditions.min_object_altitude = 10.0
        conditions.horizon.get_min_altitude.return_value = 10.0

        mask = calculate_visible_stars_mask(
            lat_decimal,
            lon_decimal,
            stars_ras,
            stars_decs,
            check_times_gmst,
            conditions,
        )

        self.assertTrue(mask[0])
        self.assertFalse(mask[1])


if __name__ == "__main__":
    unittest.main()
