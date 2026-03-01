import unittest
from apts.opticalequipment.camera import Camera

class TestCameraHeuristics(unittest.TestCase):
    def test_full_frame_heuristic(self):
        # Case: "full frame" in name
        entry = {'brand': 'Test', 'name': 'Generic Full Frame Camera', 'optical_length': 10, 'mass': 500}
        cam = Camera.from_database(entry)
        self.assertAlmostEqual(cam.sensor_width.to('mm').magnitude, 35.9, places=1)
        self.assertAlmostEqual(cam.sensor_height.to('mm').magnitude, 23.9, places=1)

        # Case: "36x24" in name
        entry2 = {'brand': 'Test', 'name': 'Camera 36x24 Sensor', 'optical_length': 10, 'mass': 500}
        cam2 = Camera.from_database(entry2)
        self.assertAlmostEqual(cam2.sensor_width.to('mm').magnitude, 35.9, places=1)
        self.assertAlmostEqual(cam2.sensor_height.to('mm').magnitude, 23.9, places=1)

    def test_four_thirds_heuristic(self):
        # Case: "4/3" in name
        entry = {'brand': 'Test', 'name': 'ASI 4/3 Camera', 'optical_length': 10, 'mass': 500}
        cam = Camera.from_database(entry)
        self.assertAlmostEqual(cam.sensor_width.to('mm').magnitude, 17.3, places=1)
        self.assertAlmostEqual(cam.sensor_height.to('mm').magnitude, 13.0, places=1)

        # Case: "micro four thirds" in name
        entry2 = {'brand': 'Test', 'name': 'Micro Four Thirds Sensor', 'optical_length': 10, 'mass': 500}
        cam2 = Camera.from_database(entry2)
        self.assertAlmostEqual(cam2.sensor_width.to('mm').magnitude, 17.3, places=1)
        self.assertAlmostEqual(cam2.sensor_height.to('mm').magnitude, 13.0, places=1)

    def test_default_aps_c_heuristic(self):
        # Default case (APS-C)
        entry = {'brand': 'Test', 'name': 'ASI2600MC Pro', 'optical_length': 10, 'mass': 500}
        cam = Camera.from_database(entry)
        self.assertAlmostEqual(cam.sensor_width.to('mm').magnitude, 23.5, places=1)
        self.assertAlmostEqual(cam.sensor_height.to('mm').magnitude, 15.7, places=1)

if __name__ == '__main__':
    unittest.main()
