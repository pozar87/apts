import unittest
from unittest.mock import MagicMock
from apts.optics import OpticsUtils
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
        telescope, barlows, diagonals, filters, others, output = OpticsUtils.expand(
            path
        )
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
        telescope, barlows, diagonals, filters, others, output = OpticsUtils.expand(
            path
        )
