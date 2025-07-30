import unittest
from datetime import datetime, timezone
import pandas as pd
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
            self.solar_objects.objects[ObjectTableLabels.NAME] == "Moon"
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
            self.solar_objects.objects[ObjectTableLabels.NAME] == "Mars"
        ].iloc[0]

        # Plausibility checks for Mars
        # Phase should be between 0 and 100
        self.assertGreaterEqual(mars_data[ObjectTableLabels.PHASE], 0)
        self.assertLessEqual(mars_data[ObjectTableLabels.PHASE], 100)

        # Size (apparent diameter) should be a positive value
        self.assertGreater(mars_data[ObjectTableLabels.SIZE], 0)


if __name__ == "__main__":
    unittest.main()
