import unittest
from apts.opticalequipment.camera.vendors.celestron import CelestronCamera

class TestCelestronCameraAudit(unittest.TestCase):
    def test_neximage_burst_specs(self):
        camera = CelestronCamera.Celestron_NexImage_Burst()
        self.assertEqual(camera.get_vendor(), "Celestron NexImage Burst")
        self.assertEqual(camera.mass.to("gram").magnitude, 57)
        self.assertEqual(camera.optical_length.to("mm").magnitude, 10.6)
        self.assertEqual(camera.sensor_width.to("mm").magnitude, 4.8)
        self.assertEqual(camera.sensor_height.to("mm").magnitude, 3.6)
        self.assertEqual(camera.width, 1280)
        self.assertEqual(camera.height, 960)

    def test_neximage_5_specs(self):
        camera = CelestronCamera.Celestron_NexImage_5()
        self.assertEqual(camera.get_vendor(), "Celestron NexImage 5")
        self.assertEqual(camera.mass.to("gram").magnitude, 57)
        self.assertEqual(camera.optical_length.to("mm").magnitude, 10.6)
        self.assertEqual(camera.sensor_width.to("mm").magnitude, 5.7)
        self.assertEqual(camera.sensor_height.to("mm").magnitude, 4.28)
        self.assertEqual(camera.width, 2592)
        self.assertEqual(camera.height, 1944)

    def test_skyris_132m_specs(self):
        camera = CelestronCamera.Celestron_Skyris_132M()
        self.assertEqual(camera.get_vendor(), "Celestron Skyris 132M")
        self.assertEqual(camera.mass.to("gram").magnitude, 102)
        self.assertEqual(camera.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(camera.sensor_width.to("mm").magnitude, 4.8)
        self.assertEqual(camera.sensor_height.to("mm").magnitude, 3.6)

    def test_skyris_236m_specs(self):
        camera = CelestronCamera.Celestron_Skyris_236M()
        self.assertEqual(camera.get_vendor(), "Celestron Skyris 236M")
        self.assertEqual(camera.mass.to("gram").magnitude, 102)
        self.assertEqual(camera.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(camera.sensor_width.to("mm").magnitude, 5.4)
        self.assertEqual(camera.sensor_height.to("mm").magnitude, 3.4)

    def test_skyris_618m_specs(self):
        camera = CelestronCamera.Celestron_Skyris_618M()
        self.assertEqual(camera.get_vendor(), "Celestron Skyris 618M")
        self.assertEqual(camera.mass.to("gram").magnitude, 102)
        self.assertEqual(camera.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(camera.sensor_width.to("mm").magnitude, 3.6)
        self.assertEqual(camera.sensor_height.to("mm").magnitude, 2.7)

    def test_skyris_445m_specs(self):
        camera = CelestronCamera.Celestron_Skyris_445M()
        self.assertEqual(camera.get_vendor(), "Celestron Skyris 445M")
        self.assertEqual(camera.mass.to("gram").magnitude, 102)
        self.assertEqual(camera.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(camera.sensor_width.to("mm").magnitude, 4.8)
        self.assertEqual(camera.sensor_height.to("mm").magnitude, 3.6)

    def test_skyris_274m_specs(self):
        camera = CelestronCamera.Celestron_Skyris_274M()
        self.assertEqual(camera.get_vendor(), "Celestron Skyris 274M")
        self.assertEqual(camera.mass.to("gram").magnitude, 102)
        self.assertEqual(camera.optical_length.to("mm").magnitude, 17.5)
        self.assertEqual(camera.sensor_width.to("mm").magnitude, 8.5)
        self.assertEqual(camera.sensor_height.to("mm").magnitude, 6.8)

if __name__ == '__main__':
    unittest.main()
