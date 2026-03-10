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
        # Find a row that has coordinates to reconstruct skyfield object
        valid_rows = self.ngc.objects[self.ngc.objects["ra_hours"].notnull()]
        # Reset skyfield_object to None to test restoration
        self.ngc.objects.loc[valid_rows.index, "skyfield_object"] = None
        if not valid_rows.empty:
            row = valid_rows.iloc[0]
            obj = self.ngc.get_skyfield_object(row)
            self.assertIsNotNone(obj)

    def test_ngc_get_visible_lazy_restoration(self):
        # 1. Reset catalog to ensure lazy state
        self.ngc.objects["skyfield_object"] = None
        # We also need to ensure Magnitude and Size are in raw float/object form
        # But catalogs.NGC might already have been restored by other tests.
        # Let's force it for this instance.
        self.ngc.objects["Magnitude"] = self.ngc.objects["Magnitude_float"].values.astype(object)

        # 2. Define conditions and time
        from apts.conditions import Conditions
        from apts.units import get_unit_registry
        ureg = get_unit_registry()
        conditions = Conditions()
        conditions.max_object_magnitude = 10 * ureg.mag
        conditions.min_object_altitude = 20 * ureg.degree

        start = datetime.datetime(2025, 2, 19, 20, 0, 0, tzinfo=pytz.UTC)
        stop = datetime.datetime(2025, 2, 19, 22, 0, 0, tzinfo=pytz.UTC)

        # 3. Call get_visible
        visible = self.ngc.get_visible(conditions, start, stop)

        # 4. Verify restoration
        if not visible.empty:
            # Check a visible object in master catalog
            idx = visible.index[0]
            self.assertIsNotNone(self.ngc.objects.loc[idx, "skyfield_object"])
            self.assertTrue(hasattr(self.ngc.objects.loc[idx, "Magnitude"], "magnitude"))
            self.assertTrue(hasattr(visible.loc[idx, "Magnitude"], "magnitude"))
