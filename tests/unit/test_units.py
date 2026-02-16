import unittest
from typing import Any, cast
from apts.units import get_unit_registry, set_unit_registry

class TestUnits(unittest.TestCase):
    def test_unit_definitions(self):
        ureg = get_unit_registry()

        # Test custom units
        self.assertIn("mag", ureg)
        self.assertIn("arcsecond", ureg)
        self.assertIn("AU", ureg)
        self.assertIn("hour", ureg)

        # Test conversions or properties
        self.assertEqual(ureg.hour, 60 * ureg.minute)
        self.assertAlmostEqual(
            cast(Any, 1 * ureg.arcsecond).to(ureg.degree).magnitude, 1 / 3600
        )

    def test_set_unit_registry(self):
        original_ureg = get_unit_registry()
        new_ureg = "MockRegistry"
        try:
            set_unit_registry(new_ureg)
            self.assertEqual(get_unit_registry(), "MockRegistry")
        finally:
            # Restore
            set_unit_registry(original_ureg)

if __name__ == "__main__":
    unittest.main()
