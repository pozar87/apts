import unittest
from apts.opticalequipment.camera.vendors.celestron import CelestronCamera
from apts.utils import ConnectionType

class TestCelestronNexImage10Audit(unittest.TestCase):
    def test_neximage_10_specs(self):
        cam = CelestronCamera.Celestron_NexImage_10()
        self.assertEqual(cam.get_vendor(), "Celestron NexImage 10")
        self.assertEqual(cam.width, 3856)
        self.assertEqual(cam.height, 2764)
        self.assertAlmostEqual(cam.sensor_width.to('mm').magnitude, 6.4)
        self.assertAlmostEqual(cam.sensor_height.to('mm').magnitude, 4.6)
        self.assertAlmostEqual(cam.pixel_size().to('micrometer').magnitude, 1.67)
        self.assertAlmostEqual(cam.mass.to('gram').magnitude, 57)
        self.assertAlmostEqual(cam.optical_length.to('mm').magnitude, 10.6)
        self.assertEqual(cam.connection_type, ConnectionType.CS)

if __name__ == '__main__':
    unittest.main()
