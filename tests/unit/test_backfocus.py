import unittest
from typing import Any, cast
from apts.opticalequipment import Telescope, Camera, Reducer, Spacer, Focuser
from apts.equipment import Equipment
from apts.utils import ConnectionType, Gender
from apts.constants import GraphConstants


class TestBackfocus(unittest.TestCase):
    def test_backfocus_gap_with_reducer(self):
        # Setup: Telescope -> Reducer (55mm req) -> 20mm Spacer -> Camera (17.5mm depth)
        # Using default genders where possible
        t = Telescope(
            80, 480, vendor="Test Scope", connection_type=ConnectionType.M42
        )  # Default Female

        # Reducer: Input M42 Male, Output M42 Female (Defaults)
        r = Reducer(
            "Test Reducer",
            magnification=0.8,
            optical_length=10,
            required_backfocus=55,
            in_connection_type=ConnectionType.M42,
            out_connection_type=ConnectionType.M42,
        )

        # Spacer: Input M42 Male, Output M42 Female
        s = Spacer(
            "Test Spacer",
            optical_length=20,
            in_connection_type=ConnectionType.M42,
            out_connection_type=ConnectionType.M42,
            in_gender=Gender.MALE,
            out_gender=Gender.FEMALE,
        )

        # Camera: Input M42 Male (override default Female if needed, but actually Camera input is Female usually... wait)
        # In my code: Camera(connection_gender=Gender.FEMALE) by default.
        # If Telescope is Female, it needs a Male input.
        # Let's re-check the logic. Telescope OUT is Female. Reducer IN is Male. Correct.
        # Reducer OUT is Female. Spacer IN is Male. Correct.
        # Spacer OUT is Female. Camera IN is Male? Usually Camera has a Female thread, but let's see.

        c = Camera(
            23.5,
            15.7,
            6000,
            4000,
            vendor="Test Cam",
            connection_type=ConnectionType.M42,
            connection_gender=Gender.MALE,
            backfocus=17.5,
        )

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
        self.assertEqual(cast(Any, path.backfocus_gap()).magnitude, 17.5)

    def test_total_mass(self):
        t = Telescope(
            80, 480, vendor="Test Scope", mass=2000, connection_type=ConnectionType.M42
        )
        c = Camera(
            23.5,
            15.7,
            6000,
            4000,
            vendor="Test Cam",
            mass=500,
            connection_type=ConnectionType.M42,
            connection_gender=Gender.MALE,
        )

        eq = Equipment()
        eq.register(t)
        eq.register(c)

        paths = eq._get_paths(GraphConstants.IMAGE_ID)
        self.assertTrue(len(paths) > 0)
        path = paths[0]

        # Total mass: 2000 (scope) + 500 (cam) = 2500g
        self.assertEqual(cast(Any, path.total_mass()).magnitude, 2500)

    def test_total_mass_with_attached(self):
        t = Telescope(80, 480, mass=2000, connection_type=ConnectionType.M42)
        # Attach a focuser motor
        f = Focuser("EAF", mass=500)
        t.attach(f)

        c = Camera(23.5, 15.7, 6000, 4000, mass=300, connection_type=ConnectionType.M42, connection_gender=Gender.MALE)

        from apts.optics import OpticalPath
        path = OpticalPath.from_path([t, c])

        # Total mass: 2000 (scope) + 500 (focuser) + 300 (cam) = 2800g
        self.assertEqual(cast(Any, path.total_mass()).magnitude, 2800)

    def test_registry(self):
        from apts.equipment_registry import EquipmentRegistry

        reg = EquipmentRegistry()
        featured = reg.get_featured()
        self.assertIn("Camera", featured)

        # Test preset creation
        cam = reg.create("preset:Camera:ZWO_ASI2600MC_PRO")
        self.assertIsInstance(cam, Camera)
        self.assertEqual(cam.vendor, "ZWO ASI2600MC Pro")

        # Test database creation (using a name we know is in featured)
        scope = reg.create("db:80ED")
        self.assertIsInstance(scope, Telescope)
