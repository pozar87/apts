import unittest
from apts.opticalequipment import Telescope, Camera, Reducer, Spacer
from apts.equipment import Equipment
from apts.utils import ConnectionType, Gender
from apts.optics import OpticalPath
from apts.constants import GraphConstants

class TestBackfocus(unittest.TestCase):
    def test_backfocus_gap_with_reducer(self):
        # Setup: Telescope -> Reducer (55mm req) -> 20mm Spacer -> Camera (17.5mm depth)
        # We must use matching connections
        t = Telescope(80, 480, vendor="Test Scope", connection_type=ConnectionType.M42, connection_gender=Gender.FEMALE)

        # Reducer: Input M42 Male, Output M42 Female
        r = Reducer("Test Reducer", magnification=0.8, optical_length=10, required_backfocus=55,
                    in_connection_type=ConnectionType.M42, out_connection_type=ConnectionType.M42,
                    in_gender=Gender.MALE, out_gender=Gender.FEMALE)

        # Spacer: Input M42 Male, Output M42 Female
        s = Spacer("Test Spacer", optical_length=20,
                   in_connection_type=ConnectionType.M42, out_connection_type=ConnectionType.M42,
                   in_gender=Gender.MALE, out_gender=Gender.FEMALE)

        # Camera: Input M42 Male, sensor depth 17.5
        c = Camera(23.5, 15.7, 6000, 4000, vendor="Test Cam",
                   connection_type=ConnectionType.M42, connection_gender=Gender.MALE,
                   backfocus=17.5)

        eq = Equipment()
        eq.register(t)
        eq.register(r)
        eq.register(s)
        eq.register(c)

        # Get the path from space to image
        paths = eq._get_paths(GraphConstants.IMAGE_ID)
        self.assertTrue(len(paths) > 0, "No path found from Space to Image")

        path = paths[0]
        # Backfocus gap should be: 55 - (20 + 17.5) = 17.5mm
        # Wait, 20 (spacer) + 17.5 (camera sensor depth) = 37.5. 55 - 37.5 = 17.5.
        self.assertEqual(path.backfocus_gap().magnitude, 17.5)

    def test_total_mass(self):
        t = Telescope(80, 480, vendor="Test Scope", mass=2000, connection_type=ConnectionType.M42, connection_gender=Gender.FEMALE)
        c = Camera(23.5, 15.7, 6000, 4000, vendor="Test Cam", mass=500, connection_type=ConnectionType.M42, connection_gender=Gender.MALE)

        eq = Equipment()
        eq.register(t)
        eq.register(c)

        paths = eq._get_paths(GraphConstants.IMAGE_ID)
        self.assertTrue(len(paths) > 0)
        path = paths[0]

        # Total mass: 2000 (scope) + 500 (cam) = 2500g
        self.assertEqual(path.total_mass().magnitude, 2500)
