import unittest
from apts.opticalequipment.telescope.vendors.takahashi import TakahashiTelescope
from apts.units import get_unit_registry

class TestTakahashiSpecs(unittest.TestCase):
    def test_takahashi_fsq_85edp(self):
        telescope = TakahashiTelescope.Takahashi_FSQ_85EDP()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 85)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 450)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 3600)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 0)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 5.29, places=2)

    def test_takahashi_fsq_106ed(self):
        telescope = TakahashiTelescope.Takahashi_FSQ_106ED()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 106)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 530)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 7000)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 0)
        self.assertEqual(telescope.focal_ratio().magnitude, 5.0)

    def test_takahashi_epsilon_130d(self):
        telescope = TakahashiTelescope.Takahashi_Epsilon_130D()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 130)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 430)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 63)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 3.31, places=2)

    def test_takahashi_epsilon_160ed(self):
        telescope = TakahashiTelescope.Takahashi_Epsilon_160ED()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 160)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 530)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 63)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 3.31, places=2)

    def test_takahashi_epsilon_180ed(self):
        telescope = TakahashiTelescope.Takahashi_Epsilon_180ED()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 180)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 500)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 10700)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 80)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 2.78, places=2)

    def test_takahashi_mewlon_210(self):
        telescope = TakahashiTelescope.Takahashi_Mewlon_210()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 210)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 2415)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 65)
        self.assertEqual(telescope.focal_ratio().magnitude, 11.5)

if __name__ == "__main__":
    unittest.main()
