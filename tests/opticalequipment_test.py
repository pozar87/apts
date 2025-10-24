import unittest

from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.barlow import Barlow
from apts.opticalequipment.eyepiece import Eyepiece
from apts.optics import OpticsUtils


class OpticalEquipmentTest(unittest.TestCase):

    def test_telescope(self):
        t = Telescope(aperture=150, focal_length=750)
        self.assertEqual(t.focal_ratio(), 5.0)
        self.assertEqual(t.dawes_limit().magnitude, 0.773)
        self.assertEqual(t.rayleigh_limit().magnitude, 0.92)
        self.assertAlmostEqual(t.limiting_magnitude(), 13.58, 2)
        self.assertAlmostEqual(t.light_grasp_ratio(7).magnitude, 459.18, 2)
        self.assertEqual(t.min_useful_zoom(), 25)
        self.assertEqual(t.max_useful_zoom(), 375)

    def test_barlow(self):
        b = Barlow(magnification=2)
        self.assertEqual(b.magnification, 2)

    def test_eyepiece(self):
        t = Telescope(aperture=150, focal_length=750)
        e = Eyepiece(focal_length=10, field_of_view=50)
        zoom = OpticsUtils.compute_zoom(t, [], e)
        self.assertEqual(zoom, 75)
        fov = e.field_of_view(t, zoom, 1)
        self.assertAlmostEqual(fov.magnitude, 0.67, 2)
