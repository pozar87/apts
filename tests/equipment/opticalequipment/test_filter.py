import unittest

from apts.constants import GraphConstants
from apts.equipment import Equipment
from apts.opticalequipment.eyepiece import Eyepiece
from apts.opticalequipment.filter import Filter
from apts.opticalequipment.telescope import Telescope


class FilterTest(unittest.TestCase):
    def test_filter_registration(self):
        # Given
        eq = Equipment()
        t = Telescope(aperture=150, focal_length=750, vendor="SkyWatcher")
        f = Filter(name="OIII", vendor="Astronomik")
        e = Eyepiece(focal_length=10, vendor="Celestron")

        eq.register(t)
        eq.register(f)
        eq.register(e)

        # When
        paths = eq._get_paths(GraphConstants.EYE_ID)

        # Then
        # We expect 3 paths: NakedEye, Telescope->Eyepiece, Telescope->Filter->Eyepiece
        self.assertEqual(len(paths), 3)

        # Find the path with the filter
        filtered_path = None
        for path in paths:
            if f in path.elements():
                filtered_path = path
                break

        self.assertIsNotNone(filtered_path, "Could not find a path with the filter.")
        assert filtered_path is not None
        self.assertIn(f, filtered_path.elements())
        self.assertIn(t, filtered_path.elements())
        self.assertIn(e, filtered_path.elements())


if __name__ == "__main__":
    unittest.main()
