import unittest
from apts.opticalequipment.telescope.vendors.televue import TelevueTelescope

class TestTelevueSpecs(unittest.TestCase):
<<<<<<< HEAD
    def test_tv_60_specs(self):
        scope = TelevueTelescope.TeleVue_TV_60()
        self.assertEqual(scope.aperture.magnitude, 60)
        self.assertEqual(scope.focal_length.magnitude, 360)
        self.assertEqual(scope.mass.magnitude, 1361)
        self.assertEqual(scope.central_obstruction.magnitude, 0)

    def test_tv_76_specs(self):
        scope = TelevueTelescope.TeleVue_TV_76()
        self.assertEqual(scope.aperture.magnitude, 76)
        self.assertEqual(scope.focal_length.magnitude, 480)
        self.assertEqual(scope.mass.magnitude, 2313)
        self.assertEqual(scope.central_obstruction.magnitude, 0)

    def test_tv_85_specs(self):
        scope = TelevueTelescope.TeleVue_TV_85()
        self.assertEqual(scope.aperture.magnitude, 85)
        self.assertEqual(scope.focal_length.magnitude, 600)
        self.assertEqual(scope.mass.magnitude, 2767)
        self.assertEqual(scope.central_obstruction.magnitude, 0)

    def test_tv_102_specs(self):
        scope = TelevueTelescope.TeleVue_TV_102()
        self.assertEqual(scope.aperture.magnitude, 102)
        self.assertEqual(scope.focal_length.magnitude, 880)
        self.assertEqual(scope.mass.magnitude, 4173)
        self.assertEqual(scope.central_obstruction.magnitude, 0)

    def test_np101_specs(self):
        scope = TelevueTelescope.TeleVue_TV_NP101()
        self.assertEqual(scope.aperture.magnitude, 101)
        self.assertEqual(scope.focal_length.magnitude, 540)
        self.assertEqual(scope.mass.magnitude, 4853)
        self.assertEqual(scope.central_obstruction.magnitude, 0)

    def test_np101is_specs(self):
        scope = TelevueTelescope.TeleVue_NP101is()
        self.assertEqual(scope.aperture.magnitude, 101)
        self.assertEqual(scope.focal_length.magnitude, 540)
        self.assertEqual(scope.mass.magnitude, 4853)
        self.assertEqual(scope.central_obstruction.magnitude, 0)

    def test_np127is_specs(self):
        scope = TelevueTelescope.TeleVue_TV_NP127is()
        self.assertEqual(scope.aperture.magnitude, 127)
        self.assertEqual(scope.focal_length.magnitude, 660)
        self.assertEqual(scope.mass.magnitude, 6577)
        self.assertEqual(scope.central_obstruction.magnitude, 0)

    def test_np127fli_specs(self):
        scope = TelevueTelescope.TeleVue_NP127fli()
        self.assertEqual(scope.aperture.magnitude, 127)
        self.assertEqual(scope.focal_length.magnitude, 660)
        self.assertEqual(scope.mass.magnitude, 6577)
        self.assertEqual(scope.central_obstruction.magnitude, 0)
=======
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
>>>>>>> origin/master

if __name__ == '__main__':
    unittest.main()
