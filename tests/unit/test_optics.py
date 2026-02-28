import unittest
from typing import Any, cast
from unittest.mock import MagicMock
from apts.optics import OpticsUtils, OpticalPath
from apts.opticalequipment.binoculars import Binoculars
from apts.units import get_unit_registry

# We need the real classes to use them with isinstance in OpticsUtils.expand
from apts.opticalequipment.barlow import Barlow
from apts.opticalequipment.diagonal import Diagonal
from apts.opticalequipment.filter import Filter
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.eyepiece import Eyepiece
from apts.opticalequipment.camera import Camera


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
        self.assertEqual(others, [])
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

        self.assertEqual(telescope, t)
        self.assertEqual(barlows, [b])
        self.assertEqual(diagonals, [d])
        self.assertEqual(filters, [f])
        self.assertEqual(others, [])
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
        path = OpticalPath(binos, [], [], [], [], binos)

        zoom = path.zoom()
        self.assertEqual(cast(Any, zoom).magnitude, 10)

    def test_optical_path_elements(self):
        t = MagicMock()
        e = MagicMock()
        b = MagicMock()
        path = OpticalPath(t, [b], [], [], [], e)

        elements = path.elements()
        self.assertEqual(elements, frozenset({t, e, b}))

    def test_get_image_orientation_binos(self):
        binos = MagicMock(spec=Binoculars)
        path = OpticalPath(binos, [], [], [], [], binos)
        self.assertEqual(path.get_image_orientation(), (False, False))

    def test_get_image_orientation_telescope(self):
        t = MagicMock(spec=Telescope)
        e = MagicMock()

        # Default telescope (inverted)
        path = OpticalPath(t, [], [], [], [], e)
        self.assertEqual(path.get_image_orientation(), (True, True))

        # With standard diagonal (vertical flip)
        d = MagicMock(spec=Diagonal)
        d.is_erecting = False
        path_d = OpticalPath(t, [], [d], [], [], e)
        # (True, True) + vertical flip -> (True, False)
        self.assertEqual(path_d.get_image_orientation(), (True, False))

        # With erecting diagonal (horizontal and vertical flip)
        de = MagicMock(spec=Diagonal)
        de.is_erecting = True
        path_de = OpticalPath(t, [], [de], [], [], e)
        # (True, True) + (True, True) -> (False, False)
        self.assertEqual(path_de.get_image_orientation(), (False, False))

    def test_npf_rule(self):
        t = MagicMock(spec=Telescope)
        t.focal_length = 400 * get_unit_registry().mm
        t.focal_ratio.return_value = 5.6 * get_unit_registry().dimensionless

        c = MagicMock(spec=Camera)
        c.pixel_size.return_value = 3.76 * get_unit_registry().micrometer

        path = OpticalPath(t, [], [], [], [], c)

        # NPF = (35*5.6 + 30*3.76) / 400 = (196 + 112.8) / 400 = 308.8 / 400 = 0.772
        npf = path.npf_rule()
        self.assertAlmostEqual(cast(Any, npf).magnitude, 0.772, places=3)
        self.assertEqual(cast(Any, npf).units, get_unit_registry().second)

        # With declination 60 degrees (cos(60) = 0.5)
        # NPF = 0.772 / 0.5 = 1.544
        npf_60 = path.npf_rule(declination=60)
        self.assertAlmostEqual(cast(Any, npf_60).magnitude, 1.544, places=3)

    def test_rule_of_500(self):
        t = MagicMock(spec=Telescope)
        t.focal_length = 50 * get_unit_registry().mm

        c = MagicMock(spec=Camera)
        # APS-C Nikon: 23.5 x 15.7 -> diag ~ 28.26mm
        # crop_factor = 43.27 / 28.26 ~ 1.53
        c.sensor_width = 23.5 * get_unit_registry().mm
        c.sensor_height = 15.7 * get_unit_registry().mm

        path = OpticalPath(t, [], [], [], [], c)

        # 500 / (50 * 1.53) = 500 / 76.5 ~ 6.536
        r500 = path.rule_of_500()

        diagonal = (23.5**2 + 15.7**2) ** 0.5
        crop_factor = 43.27 / diagonal
        expected = 500 / (50 * crop_factor)

        self.assertAlmostEqual(cast(Any, r500).magnitude, expected, places=3)
        self.assertEqual(cast(Any, r500).units, get_unit_registry().second)

    def test_optical_path_fov_methods(self):
        t = MagicMock(spec=Telescope)
        t.focal_length = 1000 * get_unit_registry().mm

        c = MagicMock(spec=Camera)
        c.sensor_width = 36 * get_unit_registry().mm
        c.sensor_height = 24 * get_unit_registry().mm

        # Mock field_of_view_width etc. since we are testing OpticalPath's delegation
        c.field_of_view_width.return_value = 2.0 * get_unit_registry().deg
        c.field_of_view_height.return_value = 1.0 * get_unit_registry().deg
        c.field_of_view_diagonal.return_value = 2.2 * get_unit_registry().deg

        path = OpticalPath(t, [], [], [], [], c)

        self.assertEqual(cast(Any, path.fov_width()).magnitude, 2.0)
        self.assertEqual(cast(Any, path.fov_height()).magnitude, 1.0)
        self.assertEqual(cast(Any, path.fov_diagonal()).magnitude, 2.2)

        # Verify calls
        c.field_of_view_width.assert_called_once()
        c.field_of_view_height.assert_called_once()
        c.field_of_view_diagonal.assert_called_once()

    def test_atmospheric_dispersion(self):
        t = MagicMock(spec=Telescope)
        path = OpticalPath(t, [], [], [], [], MagicMock())

        # At zenith (90 degrees), dispersion should be 0
        disp_90 = path.atmospheric_dispersion(90)
        self.assertEqual(disp_90.magnitude, 0.0)

        # At 45 degrees, tan(z) = 1.
        # Manual calculation for 400nm and 700nm gives ~1.437 arcseconds
        disp_45 = path.atmospheric_dispersion(45)
        self.assertAlmostEqual(disp_45.magnitude, 1.437, places=3)
        self.assertEqual(disp_45.units, get_unit_registry().arcsecond)

        # At 30 degrees, tan(z) = sqrt(3) ~ 1.732.
        # 1.4368 * 1.732 ~ 2.4886
        disp_30 = path.atmospheric_dispersion(30)
        self.assertAlmostEqual(disp_30.magnitude, 2.489, places=3)


if __name__ == "__main__":
    unittest.main()
