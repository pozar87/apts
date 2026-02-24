import datetime
import unittest
import pytz
from apts import catalogs
from apts.objects.stars import Stars
from apts.constants import ObjectTableLabels
from tests import setup_place

INITIAL_DATE_STR = "2025/02/18 12:00:00"
INITIAL_DT = datetime.datetime.strptime(INITIAL_DATE_STR, "%Y/%m/%d %H:%M:%S").replace(
    tzinfo=pytz.UTC
)


class TestStars(unittest.TestCase):
    def setUp(self):
        self.place = setup_place()
        self.stars = Stars(self.place, catalogs)

    def test_stars_initialization(self):
        self.assertIsNotNone(self.stars.objects)
        self.assertIn(ObjectTableLabels.TRANSIT, self.stars.objects.columns)
        self.assertIn(ObjectTableLabels.ALTITUDE, self.stars.objects.columns)

    def test_stars_compute(self):
        # Initial compute
        df = self.stars.compute()
        self.assertIsNotNone(df)
        self.assertFalse(df[ObjectTableLabels.TRANSIT].isnull().all())
        self.assertFalse(df[ObjectTableLabels.ALTITUDE].isnull().all())
        self.assertFalse(df[ObjectTableLabels.RISING].isnull().all())
        self.assertFalse(df[ObjectTableLabels.SETTING].isnull().all())

    def test_stars_compute_with_date(self):
        # Compute with a specific date
        new_date = INITIAL_DT + datetime.timedelta(days=1)
        # Convert to local time as expected by compute logic for the date check
        local_new_date = new_date.astimezone(self.place.local_timezone)

        df = self.stars.compute(calculation_date=new_date)

        # Verify that transits are around the new date
        first_transit = df[ObjectTableLabels.TRANSIT].iloc[0]
        # Allow for some wiggle room because stars transit once per sidereal day
        self.assertLess(
            abs((first_transit - local_new_date).total_seconds()), 24 * 3600
        )

    def test_stars_compute_with_time_array(self):
        # Skyfield sometimes passes time arrays
        pass
