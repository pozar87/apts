import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

class TestOmniXLTSpecs(unittest.TestCase):
    def test_omni_xlt_102_specs(self):
        scope = CelestronTelescope.Celestron_Omni_XLT_102()
        self.assertEqual(scope.get_vendor(), "Celestron Omni XLT 102")
        self.assertEqual(scope.aperture.to('mm').magnitude, 102)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 4310)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1000/102, places=2)

    def test_omni_xlt_120_specs(self):
        scope = CelestronTelescope.Celestron_Omni_XLT_120()
        self.assertEqual(scope.get_vendor(), "Celestron Omni XLT 120")
        self.assertEqual(scope.aperture.to('mm').magnitude, 120)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 5670)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1000/120, places=2)

    def test_omni_xlt_127_sct_specs(self):
        scope = CelestronTelescope.Celestron_Omni_XLT_127_SCT()
        self.assertEqual(scope.get_vendor(), "Celestron Omni XLT 127 SCT")
        self.assertEqual(scope.aperture.to('mm').magnitude, 127)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1250)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 40)
        self.assertEqual(scope.mass.to('gram').magnitude, 2950)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1250/127, places=2)

    def test_omni_xlt_150_specs(self):
        scope = CelestronTelescope.Celestron_Omni_XLT_150()
        self.assertEqual(scope.get_vendor(), "Celestron Omni XLT 150")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 5440)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 750/150, places=2)

    def test_omni_xlt_150r_specs(self):
        scope = CelestronTelescope.Celestron_Omni_XLT_150R()
        self.assertEqual(scope.get_vendor(), "Celestron Omni XLT 150R")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 7260)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 750/150, places=2)

if __name__ == '__main__':
    unittest.main()
