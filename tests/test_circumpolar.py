
import unittest
from datetime import datetime, timezone
from apts.place import Place
from apts.conditions import Conditions
from apts.observations import Observation
from apts.equipment import Equipment

class TestCircumpolarObjects(unittest.TestCase):
    def test_circumpolar_messier_object_visibility(self):
        """
        Test that a circumpolar Messier object (e.g., M81) is correctly identified as visible
        from a high-latitude location where it never sets.
        """
        # Tromsø, Norway (approx. 69.6° N)
        place = Place(lat=69.6, lon=18.9, date=datetime(2025, 3, 20, 22, 0, 0, tzinfo=timezone.utc))
        equipment = Equipment()
        conditions = Conditions()

        # Create an observation for a night in March
        obs = Observation(place, equipment, conditions, target_date=datetime(2025, 3, 20).date())

        # M81 is circumpolar from this latitude and should be visible.
        # Its declination is ~+69°, so it should always be above the horizon.
        visible_messier = obs.get_visible_messier()

        m81_is_visible = "M81" in visible_messier["Messier"].values

        self.assertTrue(m81_is_visible, "M81 should be visible as a circumpolar object from Tromsø.")

    def test_circumpolar_below_horizon_messier_object_is_not_visible(self):
        """
        Test that a Messier object that is always below the horizon (circumpolar-below)
        is correctly identified as not visible.
        """
        # Tromsø, Norway (approx. 69.6° N)
        place = Place(lat=69.6, lon=18.9, date=datetime(2025, 6, 20, 22, 0, 0, tzinfo=timezone.utc))
        equipment = Equipment()
        conditions = Conditions()

        # Create an observation for a night in June
        obs = Observation(place, equipment, conditions, target_date=datetime(2025, 6, 20).date())

        # M7 (Ptolemy's Cluster) has a declination of approx -34.8°.
        # From Tromsø (69.6° N), an object needs a declination greater than
        # -(90 - 69.6) = -20.4° to ever rise. M7 will never be visible.
        visible_messier = obs.get_visible_messier()

        m7_is_visible = "M7" in visible_messier["Messier"].values

        self.assertFalse(m7_is_visible, "M7 should not be visible from Tromsø as it is always below the horizon.")


if __name__ == "__main__":
    unittest.main()
