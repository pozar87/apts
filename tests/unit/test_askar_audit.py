import unittest
from apts.opticalequipment.telescope.vendors.askar import AskarTelescope
from apts.utils import ConnectionType

class TestAskarAudit(unittest.TestCase):
    def test_fma180_pro_specs(self):
        # Official specs: 40mm aperture, 180mm focal length, 800g mass, M48 camera thread
        scope = AskarTelescope.Askar_FMA_180_Pro()
        self.assertEqual(scope.aperture.to('mm').magnitude, 40)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 180)
        self.assertEqual(scope.mass.to('gram').magnitude, 800)
        self.assertEqual(scope.connection_type, ConnectionType.M48)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_50p_specs(self):
        # Official specs: 50mm aperture, 190mm focal length, 1400g mass, M48 camera thread
        scope = AskarTelescope.Askar_50P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 50)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 190)
        self.assertEqual(scope.mass.to('gram').magnitude, 1400)
        self.assertEqual(scope.connection_type, ConnectionType.M48)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.get_vendor(), "Askar 50P")

if __name__ == '__main__':
    unittest.main()
