import unittest
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

class TestZwoSeestarSpecs(unittest.TestCase):
    def test_seestar_s50_specs(self):
        s50 = ZwoTelescope.ZWO_Seestar_S50()
        self.assertEqual(s50.aperture.magnitude, 50)
        self.assertEqual(s50.focal_length.magnitude, 250)
        self.assertEqual(s50.full_well, 11200)
        self.assertEqual(s50.sensor_width.magnitude, 5.6)
        self.assertEqual(s50.pixel_size().magnitude, 2.9)

    def test_seestar_s30_specs(self):
        s30 = ZwoTelescope.ZWO_Seestar_S30()
        self.assertEqual(s30.aperture.magnitude, 30)
        self.assertEqual(s30.focal_length.magnitude, 150)
        self.assertEqual(s30.full_well, 38200)
        self.assertEqual(s30.sensor_width.magnitude, 5.57)
        self.assertEqual(s30.pixel_size().magnitude, 2.9)

    def test_seestar_s30_pro_specs(self):
        s30pro = ZwoTelescope.ZWO_Seestar_S30_Pro()
        self.assertEqual(s30pro.aperture.magnitude, 30)
        self.assertEqual(s30pro.focal_length.magnitude, 160)
        self.assertEqual(s30pro.full_well, 40000)
        self.assertEqual(s30pro.sensor_width.magnitude, 11.13)
        self.assertEqual(s30pro.pixel_size().magnitude, 2.9)
        self.assertAlmostEqual(s30pro.focal_ratio(), 5.33, places=2)

    def test_seestar_sensor_entries(self):
        s30pro_sensor = ZwoCamera.ZWO_Seestar_S30_Pro_Sensor()
        self.assertEqual(s30pro_sensor.full_well, 40000)
        self.assertEqual(s30pro_sensor.sensor_width.to('mm').magnitude, 11.13)
        self.assertEqual(s30pro_sensor.pixel_size().to('micrometer').magnitude, 2.9)

        s50_sensor = ZwoCamera.ZWO_Seestar_S50_Sensor()
        self.assertEqual(s50_sensor.full_well, 11200)
        self.assertEqual(s50_sensor.sensor_width.to('mm').magnitude, 5.6)

if __name__ == '__main__':
    unittest.main()
