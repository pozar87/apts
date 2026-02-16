import unittest
from typing import Any, cast
from unittest.mock import MagicMock
from apts.optics import OpticsUtils, OpticalPath
from apts.opticalequipment.binoculars import Binoculars

# We need the real classes to use them with isinstance in OpticsUtils.expand
from apts.opticalequipment.barlow import Barlow
from apts.opticalequipment.diagonal import Diagonal
from apts.opticalequipment.filter import Filter
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.eyepiece import Eyepiece

class TestOptics(unittest.TestCase):
    def test_expand_binoculars(self):
        binos = MagicMock(spec=Binoculars)
        path = [binos]
        telescope, barlows, diagonals, filters, output = OpticsUtils.expand(path)
        self.assertEqual(telescope, binos)
        self.assertEqual(barlows, [])
        self.assertEqual(diagonals, [])
        self.assertEqual(filters, [])
        self.assertEqual(output, binos)

    def test_expand_telescope(self):
        t = MagicMock(spec=Telescope)
        b = MagicMock(spec=Barlow)
        d = MagicMock(spec=Diagonal)
        f = MagicMock(spec=Filter)
        e = MagicMock(spec=Eyepiece)

        path = [t, b, d, f, e]
        telescope, barlows, diagonals, filters, output = OpticsUtils.expand(path)

        self.assertEqual(telescope, t)
        self.assertEqual(barlows, [b])
        self.assertEqual(diagonals, [d])
        self.assertEqual(filters, [f])
        self.assertEqual(output, e)

    def test_barlows_multiplications(self):
        b1 = MagicMock()
        b1.magnification = 2
        b2 = MagicMock()
        b2.magnification = 3

        self.assertEqual(OpticsUtils.barlows_multiplications([b1, b2]), 6)
        self.assertEqual(OpticsUtils.barlows_multiplications([]), 1)

    def test_optical_path_zoom_binos(self):
        binos = MagicMock(spec=Binoculars)
        binos.magnification = 10
        path = OpticalPath(binos, [], [], [], binos)

        zoom = path.zoom()
        self.assertEqual(cast(Any, zoom).magnitude, 10)

    def test_optical_path_elements(self):
        t = MagicMock()
        e = MagicMock()
        b = MagicMock()
        path = OpticalPath(t, [b], [], [], e)

        elements = path.elements()
        self.assertEqual(elements, frozenset({t, e, b}))

    def test_get_image_orientation_binos(self):
        binos = MagicMock(spec=Binoculars)
        path = OpticalPath(binos, [], [], [], binos)
        self.assertEqual(path.get_image_orientation(), (False, False))

    def test_get_image_orientation_telescope(self):
        t = MagicMock(spec=Telescope)
        e = MagicMock()

        # Default telescope (inverted)
        path = OpticalPath(t, [], [], [], e)
        self.assertEqual(path.get_image_orientation(), (True, True))

        # With standard diagonal (vertical flip)
        d = MagicMock(spec=Diagonal)
        d.is_erecting = False
        path_d = OpticalPath(t, [], [d], [], e)
        # (True, True) + vertical flip -> (True, False)
        self.assertEqual(path_d.get_image_orientation(), (True, False))

        # With erecting diagonal (horizontal and vertical flip)
        de = MagicMock(spec=Diagonal)
        de.is_erecting = True
        path_de = OpticalPath(t, [], [de], [], e)
        # (True, True) + (True, True) -> (False, False)
        self.assertEqual(path_de.get_image_orientation(), (False, False))

if __name__ == "__main__":
    unittest.main()
