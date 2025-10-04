import unittest
from datetime import datetime, timezone
from apts.objects.solar_objects import SolarObjects
from apts.place import Place
from apts.constants import ObjectTableLabels


class TestSolarObjects(unittest.TestCase):
    def setUp(self):
        # Use a fixed date and location for reproducible tests
        self.test_date = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        self.place = Place(lat=34.0, lon=-118.0, date=self.test_date)
        self.solar_objects = SolarObjects(self.place, calculation_date=self.test_date)

    def test_ephem_properties_are_calculated(self):
        """Test that magnitude, size, and phase are calculated and have plausible values."""
        self.assertIn(ObjectTableLabels.MAGNITUDE, self.solar_objects.objects.columns)
        self.assertIn(ObjectTableLabels.SIZE, self.solar_objects.objects.columns)
        self.assertIn(ObjectTableLabels.PHASE, self.solar_objects.objects.columns)

        # Check that the values are not null
        self.assertFalse(
            self.solar_objects.objects[ObjectTableLabels.MAGNITUDE].isnull().all()
        )
        self.assertFalse(self.solar_objects.objects[ObjectTableLabels.SIZE].isnull().all())
        self.assertFalse(self.solar_objects.objects[ObjectTableLabels.PHASE].isnull().all())

    def test_moon_properties(self):
        """Test the calculated properties for the Moon."""
        moon_data = self.solar_objects.objects[
            self.solar_objects.objects[ObjectTableLabels.NAME] == "moon"
        ].iloc[0]

        # Plausibility checks for the Moon on the given date
        # Phase should be between 0 and 100
        self.assertGreaterEqual(moon_data[ObjectTableLabels.PHASE], 0)
        self.assertLessEqual(moon_data[ObjectTableLabels.PHASE], 100)

        # Size (apparent diameter) should be a positive value (in arcseconds)
        self.assertGreater(moon_data[ObjectTableLabels.SIZE], 0)

    def test_mars_properties(self):
        """Test the calculated properties for Mars."""
        mars_data = self.solar_objects.objects[
            self.solar_objects.objects[ObjectTableLabels.NAME] == "mars barycenter"
        ].iloc[0]

        # Plausibility checks for Mars
        # Phase should be between 0 and 100
        self.assertGreaterEqual(mars_data[ObjectTableLabels.PHASE], 0)
        self.assertLessEqual(mars_data[ObjectTableLabels.PHASE], 100)

        # Size (apparent diameter) should be a positive value
        self.assertGreater(mars_data[ObjectTableLabels.SIZE], 0)


    def test_dwarf_planet_magnitude_and_filtering(self):
        """Test that dwarf planet magnitude is calculated and filtering works."""
        from types import SimpleNamespace
        from datetime import timedelta
        import pandas as pd

        # Find Ceres in the objects list
        ceres_data = self.solar_objects.objects[
            self.solar_objects.objects[ObjectTableLabels.NAME] == "(1) Ceres"
        ]

        # Check if Ceres data was found
        self.assertFalse(ceres_data.empty, "Ceres not found in solar objects.")
        ceres_data = ceres_data.iloc[0]

        # 1. Check that magnitude is a valid number
        self.assertTrue(
            pd.notna(ceres_data[ObjectTableLabels.MAGNITUDE]),
            "Ceres magnitude should not be NA.",
        )
        self.assertIsInstance(
            ceres_data[ObjectTableLabels.MAGNITUDE],
            float,
            "Ceres magnitude should be a float.",
        )

        # 2. Test filtering
        start = self.test_date
        stop = self.test_date + timedelta(days=1)
        ceres_mag = ceres_data[ObjectTableLabels.MAGNITUDE]

        # To make the test robust, we need to check if Ceres is actually visible during the test period.
        rising = ceres_data[ObjectTableLabels.RISING]
        setting = ceres_data[ObjectTableLabels.SETTING]
        is_up = False
        if rising <= setting:  # Doesn't cross midnight
            if not (rising > stop or setting < start):
                is_up = True
        else:  # Crosses midnight
            if not (setting < start and stop < rising):
                is_up = True

        if not is_up:
            self.skipTest(
                "Ceres is not visible during the test period, cannot test filtering."
            )

        # Case A: Magnitude limit is higher than Ceres' magnitude, so it should be visible
        conditions_high = SimpleNamespace(
            max_object_magnitude=ceres_mag + 1,
            min_object_altitude=0,  # No altitude constraint for simplicity
            min_object_azimuth=0,
            max_object_azimuth=360,
        )
        visible_planets_high = self.solar_objects.get_visible(
            conditions_high, start, stop
        )
        visible_planet_names_high = visible_planets_high["Name"].tolist()
        self.assertIn(
            "Ceres",
            visible_planet_names_high,
            "Ceres should be visible with a high magnitude limit.",
        )

        # Case B: Magnitude limit is lower than Ceres' magnitude, so it should be filtered out
        conditions_low = SimpleNamespace(
            max_object_magnitude=ceres_mag - 1,
            min_object_altitude=0,
            min_object_azimuth=0,
            max_object_azimuth=360,
        )
        visible_planets_low = self.solar_objects.get_visible(
            conditions_low, start, stop
        )
        visible_planet_names_low = visible_planets_low["Name"].tolist()
        self.assertNotIn(
            "Ceres",
            visible_planet_names_low,
            "Ceres should be filtered out with a low magnitude limit.",
        )


if __name__ == "__main__":
    unittest.main()
