import unittest

from apts.equipment import Equipment
from apts.opticalequipment.smart_telescope import SmartTelescope
from apts.constants import GraphConstants


class SmartTelescopeTest(unittest.TestCase):
    def test_smart_telescope_registration(self):
        # Given
        eq = Equipment()
        st = SmartTelescope(
            aperture=50,
            focal_length=200,
            sensor_width=1.2,
            sensor_height=1.2,
            width=1920,
            height=1080,
            vendor="Dwarf II",
        )

        # When
        eq.register(st)
        paths = eq._get_paths(GraphConstants.IMAGE_ID)

        # Then
        self.assertEqual(len(paths), 1, "There should be exactly one path to the image node.")
        path = paths[0]
        self.assertEqual(path.telescope, st, "The telescope in the path should be the smart telescope.")
        # New accurate formula: 2 * atan(1.2 / (2 * 200)) = 0.34377...
        self.assertAlmostEqual(path.fov().magnitude, 0.34377, places=5)

    def test_smart_telescope_no_visual_path(self):
        # Given
        eq = Equipment()
        st = SmartTelescope(
            aperture=50,
            focal_length=200,
            sensor_width=1.2,
            sensor_height=1.2,
            width=1920,
            height=1080,
            vendor="Dwarf II",
        )

        # When
        eq.register(st)
        paths = eq._get_paths(GraphConstants.EYE_ID)

        # Then
        # NakedEye path is always present
        self.assertEqual(len(paths), 1, "There should be no new visual paths for a smart telescope.")


if __name__ == "__main__":
    unittest.main()
