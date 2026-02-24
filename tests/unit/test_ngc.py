import datetime
import unittest

import pytz

from apts import catalogs
from apts.objects.ngc import NGC
from apts.constants import ObjectTableLabels
from tests import setup_place


class TestNGC(unittest.TestCase):
    def setUp(self):
        self.place = setup_place()
        self.ngc = NGC(self.place, catalogs)

    def test_ngc_initialization(self):
        self.assertIsNotNone(self.ngc.objects)
        self.assertIn(ObjectTableLabels.TRANSIT, self.ngc.objects.columns)
        self.assertIn(ObjectTableLabels.ALTITUDE, self.ngc.objects.columns)

    def test_ngc_compute(self):
        # Initial compute
        df = self.ngc.compute()
        self.assertIsNotNone(df)
        self.assertFalse(df[ObjectTableLabels.TRANSIT].isnull().all())

    def test_ngc_compute_with_date(self):
        # Compute with a specific date
        new_date = datetime.datetime(2025, 2, 19, tzinfo=pytz.UTC)
        df = self.ngc.compute(calculation_date=new_date)
        self.assertIsNotNone(df)

    def test_find_by_name(self):
        # Find a well-known NGC object
        # We search by both NGC number and Name if available.
        # Names in the catalog are like 'NGC0224'
        obj = self.ngc.find_by_name("NGC0224")
        if obj is None and not self.ngc.objects.empty:
            # Fallback to the first available name if NGC0224 is not found
            name = self.ngc.objects["Name"].iloc[0]
            obj = self.ngc.find_by_name(name)

        self.assertIsNotNone(obj)

        # Find a non-existent object
        none_obj = self.ngc.find_by_name("NGC 999999")
        self.assertIsNone(none_obj)

    def test_get_skyfield_object(self):
        # Find a row that has a skyfield object
        valid_rows = self.ngc.objects[self.ngc.objects["skyfield_object"].notnull()]
        if not valid_rows.empty:
            row = valid_rows.iloc[0]
            obj = self.ngc.get_skyfield_object(row)
            self.assertIsNotNone(obj)
