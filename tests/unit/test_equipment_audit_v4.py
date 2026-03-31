import unittest
import sys
from unittest.mock import MagicMock

# Mock complex dependencies before importing apts
mock_modules = [
    'pandas', 'seaborn', 'timezonefinder', 'skyfield', 'skyfield.api',
    'skyfield.almanac', 'skyfield.data', 'skyfield.constants', 'ephem',
    'matplotlib', 'matplotlib.pyplot', 'matplotlib.font_manager',
    'matplotlib.ticker', 'matplotlib.axes', 'pytz', 'dateutil', 'dateutil.tz',
    'networkx', 'scipy', 'scipy.optimize', 'scipy.interpolate', 'svgwrite',
    'PIL', 'PIL.Image', 'PIL.ImageDraw', 'PIL.ImageFont'
]
for module in mock_modules:
    sys.modules[module] = MagicMock()

from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.reducer.vendors.askar import AskarReducer

class TestEquipmentAuditV4(unittest.TestCase):
    def test_sky_watcher_130pds(self):
        scope = Sky_watcherTelescope.Sky_Watcher_130PDS_Newtonian()
        self.assertEqual(scope.aperture.to('mm').magnitude, 130)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 650)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 4000)

    def test_sky_watcher_quattro_200p_correction(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Quattro_200P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 200)

    def test_askar_103apo_reducer(self):
        reducer = AskarReducer.Askar_103APO_Reducer_0_8x()
        self.assertEqual(reducer.magnification, 0.8)
        self.assertEqual(reducer.mass.to('gram').magnitude, 480)
        self.assertEqual(reducer.required_backfocus.to('mm').magnitude, 55)

if __name__ == '__main__':
    unittest.main()
