import unittest
from datetime import datetime, timedelta, timezone
import pandas as pd
import ephem # Required for place.date
import pint # Required for ureg and units
from apts.objects.planets import Planets
from apts.place import Place
from apts.conditions import Conditions
from apts.constants import ObjectTableLabels
from apts.utils import ureg

# Define a mock ephem object that can be used by Planets class
class MockEphemBody:
    def __init__(self, name, mag=0.0, earth_distance=1.0, size=1.0, elong=0.0, phase=0.0, ra=0.0, dec=0.0):
        self.name = name
        self.mag = mag # This is a float, will be wrapped with ureg.mag in the DataFrame
        self.earth_distance = earth_distance
        self.size = size
        self.elong = elong
        self.phase = phase
        self.ra = ra
        self.dec = dec

class TestPlanetsGetVisible(unittest.TestCase):
    def setUp(self):
        # Create a dummy place
        self.place = Place(lat=34.0522, lon=-118.2437, elevation=71, name="TestPlace")
        # Set a fixed date for observer for reproducible tests
        self.place.date = ephem.Date(datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc))

        # Instantiate Planets object. This will call self.planets.compute()
        # which tries to use ephem objects. We will overwrite self.planets.objects directly.
        self.planets = Planets(self.place)

        self.conditions = Conditions()
        # Ensure max_object_magnitude is high enough for test planets
        self.conditions.max_object_magnitude = 10.0 * ureg.mag

        # Define observation window
        self.start_time = datetime(2023, 1, 1, 22, 0, 0, tzinfo=timezone.utc)
        self.stop_time = datetime(2023, 1, 2, 2, 0, 0, tzinfo=timezone.utc) # Next day, 4 hour window

        # Create mock planet data
        self.mock_planets_data = [
            {
                ObjectTableLabels.EPHEM: MockEphemBody("PlanetInWindow", mag=1.0),
                ObjectTableLabels.NAME: "PlanetInWindow",
                ObjectTableLabels.TRANSIT: self.start_time + timedelta(hours=1), # 23:00 UTC
                ObjectTableLabels.RISING: self.start_time - timedelta(hours=2),
                ObjectTableLabels.SETTING: self.stop_time + timedelta(hours=2),
                ObjectTableLabels.MAGNITUDE: 1.0 * ureg.mag, # Magnitude with units
            },
            {
                ObjectTableLabels.EPHEM: MockEphemBody("PlanetInMarginBefore", mag=2.0),
                ObjectTableLabels.NAME: "PlanetInMarginBefore",
                ObjectTableLabels.TRANSIT: self.start_time - timedelta(minutes=15), # 21:45 UTC
                ObjectTableLabels.RISING: self.start_time - timedelta(hours=3),
                ObjectTableLabels.SETTING: self.stop_time + timedelta(hours=1),
                ObjectTableLabels.MAGNITUDE: 2.0 * ureg.mag,
            },
            {
                ObjectTableLabels.EPHEM: MockEphemBody("PlanetInMarginAfter", mag=3.0),
                ObjectTableLabels.NAME: "PlanetInMarginAfter",
                ObjectTableLabels.TRANSIT: self.stop_time + timedelta(minutes=15), # 02:15 UTC (next day)
                ObjectTableLabels.RISING: self.start_time - timedelta(hours=1),
                ObjectTableLabels.SETTING: self.stop_time + timedelta(hours=3),
                ObjectTableLabels.MAGNITUDE: 3.0 * ureg.mag,
            },
            {
                ObjectTableLabels.EPHEM: MockEphemBody("PlanetOutsideMarginBefore", mag=4.0),
                ObjectTableLabels.NAME: "PlanetOutsideMarginBefore",
                ObjectTableLabels.TRANSIT: self.start_time - timedelta(minutes=45), # 21:15 UTC
                ObjectTableLabels.RISING: self.start_time - timedelta(hours=4),
                ObjectTableLabels.SETTING: self.stop_time, # Sets exactly at observation stop
                ObjectTableLabels.MAGNITUDE: 4.0 * ureg.mag,
            },
            {
                ObjectTableLabels.EPHEM: MockEphemBody("PlanetOutsideMarginAfter", mag=5.0),
                ObjectTableLabels.NAME: "PlanetOutsideMarginAfter",
                ObjectTableLabels.TRANSIT: self.stop_time + timedelta(minutes=45), # 02:45 UTC (next day)
                ObjectTableLabels.RISING: self.start_time, # Rises exactly at observation start
                ObjectTableLabels.SETTING: self.stop_time + timedelta(hours=4),
                ObjectTableLabels.MAGNITUDE: 5.0 * ureg.mag,
            },
            {
                ObjectTableLabels.EPHEM: MockEphemBody("PlanetTooDim", mag=11.0),
                ObjectTableLabels.NAME: "PlanetTooDim",
                ObjectTableLabels.TRANSIT: self.start_time + timedelta(hours=2), # 00:00 UTC (next day)
                ObjectTableLabels.RISING: self.start_time - timedelta(hours=1),
                ObjectTableLabels.SETTING: self.stop_time + timedelta(hours=1),
                ObjectTableLabels.MAGNITUDE: (self.conditions.max_object_magnitude.magnitude + 1.0) * ureg.mag,
            },
        ]
        # Overwrite the .objects DataFrame with mock data
        self.planets.objects = pd.DataFrame(self.mock_planets_data)

        # Add other columns that Planets.compute would normally populate.
        # This ensures the DataFrame has the expected structure.
        default_angle = 0.0 * ureg.degree
        default_time = 0.0 * ureg.hour
        default_au = 0.0 * ureg.AU
        default_arcsec = 0.0 * ureg.arcsecond
        default_percent = 0.0 * ureg.percent # Changed from ureg.dimensionless to ureg.percent

        self.planets.objects[ObjectTableLabels.ALTITUDE] = default_angle
        self.planets.objects[ObjectTableLabels.RA] = default_time
        self.planets.objects[ObjectTableLabels.DEC] = default_angle
        self.planets.objects[ObjectTableLabels.DISTANCE] = default_au
        self.planets.objects[ObjectTableLabels.SIZE] = default_arcsec
        self.planets.objects[ObjectTableLabels.ELONGATION] = default_angle
        # Phase in Planets.compute() is: body.Ephem.phase * ureg.dimensionless
        # However, the column is often conceptually treated as percent.
        # Using ureg.percent here for consistency if any downstream code assumes it.
        # If it causes issues, ureg.dimensionless is the source.
        # For this test, it doesn't matter as phase is not used in get_visible.
        self.planets.objects[ObjectTableLabels.PHASE] = self.planets.objects[ObjectTableLabels.EPHEM].apply(lambda x: x.phase) * ureg.percent


    def test_get_visible_planets_with_margin(self):
        # Test with hours_margin = 0.5 (30 minutes)
        visible_planets_df = self.planets.get_visible(
            self.conditions, self.start_time, self.stop_time, hours_margin=0.5
        )
        visible_names = sorted(visible_planets_df[ObjectTableLabels.NAME].tolist())

        expected_visible = sorted(["PlanetInWindow", "PlanetInMarginBefore", "PlanetInMarginAfter", "PlanetOutsideMarginBefore", "PlanetOutsideMarginAfter"])
        self.assertEqual(visible_names, expected_visible,
                         f"Visible planets with margin do not match expected. Got: {visible_names}, Expected: {expected_visible}")

        self.assertIn("PlanetOutsideMarginBefore", visible_names, "PlanetOutsideMarginBefore SHOULD BE visible with margin due to rise/set overlap")
        self.assertIn("PlanetOutsideMarginAfter", visible_names, "PlanetOutsideMarginAfter SHOULD BE visible with margin due to rise/set overlap")
        self.assertNotIn("PlanetTooDim", visible_names, "PlanetTooDim should NOT be visible due to magnitude")
        self.assertEqual(len(visible_names), 5, f"Incorrect number of visible planets with margin. Got {len(visible_names)}, expected 5.")

    def test_get_visible_planets_without_margin(self):
        # Test with hours_margin = 0 (default)
        visible_planets_df = self.planets.get_visible(
            self.conditions, self.start_time, self.stop_time, hours_margin=0
        )
        visible_names = sorted(visible_planets_df[ObjectTableLabels.NAME].tolist())

        expected_visible = sorted(["PlanetInWindow", "PlanetInMarginBefore", "PlanetInMarginAfter", "PlanetOutsideMarginBefore", "PlanetOutsideMarginAfter"])
        self.assertEqual(visible_names, expected_visible,
                         f"Visible planets without margin do not match expected. Got: {visible_names}, Expected: {expected_visible}")

        self.assertIn("PlanetInMarginBefore", visible_names, "PlanetInMarginBefore SHOULD BE visible without margin due to rise/set overlap")
        self.assertIn("PlanetInMarginAfter", visible_names, "PlanetInMarginAfter SHOULD BE visible without margin due to rise/set overlap")
        self.assertIn("PlanetOutsideMarginBefore", visible_names, "PlanetOutsideMarginBefore SHOULD BE visible without margin due to rise/set overlap")
        self.assertIn("PlanetOutsideMarginAfter", visible_names, "PlanetOutsideMarginAfter SHOULD BE visible without margin due to rise/set overlap")
        self.assertNotIn("PlanetTooDim", visible_names, "PlanetTooDim should NOT be visible due to magnitude")
        self.assertEqual(len(visible_names), 5, f"Incorrect number of visible planets without margin. Got {len(visible_names)}, expected 5.")

if __name__ == '__main__':
    unittest.main()
