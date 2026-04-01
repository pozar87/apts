import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.reducer.vendors.askar import AskarReducer

class TestEquipmentUpdateV5(unittest.TestCase):
    def test_sky_watcher_130pds_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_130PDS_Newtonian()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher 130PDS Newtonian")
        self.assertEqual(scope.aperture.to('mm').magnitude, 130)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 650)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 4000)
        self.assertEqual(scope.focal_ratio().magnitude, 650/130)

    def test_askar_103apo_reducer_0_8x_specs(self):
        reducer = AskarReducer.Askar_103APO_Reducer_0_8x()
        self.assertEqual(reducer.get_vendor(), "Askar 103APO Reducer 0.8x")
        self.assertEqual(reducer.magnification, 0.8)
        self.assertEqual(reducer.mass.to('gram').magnitude, 480)
        self.assertEqual(reducer.required_backfocus.to('mm').magnitude, 55)

if __name__ == '__main__':
    unittest.main()
