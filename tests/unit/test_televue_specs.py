import unittest
from apts.opticalequipment.telescope.vendors.televue import TelevueTelescope

class TestTelevueSpecs(unittest.TestCase):
    def test_tv60_specs(self):
        scope = TelevueTelescope.TeleVue_TV_60()
        self.assertEqual(scope.aperture.to('mm').magnitude, 60)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 360)
        self.assertEqual(scope.mass.to('gram').magnitude, 1360)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_tv76_specs(self):
        scope = TelevueTelescope.TeleVue_TV_76()
        self.assertEqual(scope.aperture.to('mm').magnitude, 76)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 480)
        self.assertEqual(scope.mass.to('gram').magnitude, 2310)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_tv85_specs(self):
        scope = TelevueTelescope.TeleVue_TV_85()
        self.assertEqual(scope.aperture.to('mm').magnitude, 85)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 600)
        self.assertEqual(scope.mass.to('gram').magnitude, 2770)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_tv102_specs(self):
        scope = TelevueTelescope.TeleVue_TV_102()
        self.assertEqual(scope.aperture.to('mm').magnitude, 102)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 880)
        self.assertEqual(scope.mass.to('gram').magnitude, 4000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_np101_specs(self):
        scope = TelevueTelescope.TeleVue_TV_NP101()
        self.assertEqual(scope.aperture.to('mm').magnitude, 101)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 540)
        self.assertEqual(scope.mass.to('gram').magnitude, 4220)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_np101is_specs(self):
        scope = TelevueTelescope.TeleVue_NP101is()
        self.assertEqual(scope.aperture.to('mm').magnitude, 101)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 540)
        self.assertEqual(scope.mass.to('gram').magnitude, 4850)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_np127is_specs(self):
        scope = TelevueTelescope.TeleVue_TV_NP127is()
        self.assertEqual(scope.aperture.to('mm').magnitude, 127)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 660)
        self.assertEqual(scope.mass.to('gram').magnitude, 6580)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_np127fli_specs(self):
        scope = TelevueTelescope.TeleVue_NP127fli()
        self.assertEqual(scope.aperture.to('mm').magnitude, 127)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 660)
        self.assertEqual(scope.mass.to('gram').magnitude, 6500)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

if __name__ == '__main__':
    unittest.main()
