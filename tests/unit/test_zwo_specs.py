import unittest

from pint import Quantity

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils.equipment import ConnectionType


class TestZwoUpdates(unittest.TestCase):
    def test_asi462_specs(self):
        # Test factory method
        cam = ZwoCamera.ZWO_ASI_462MC()
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 5.6)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 3.2)
        self.assertEqual(cam.width, 1936)
        self.assertEqual(cam.height, 1096)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.9)
        self.assertEqual(cam.full_well, 11200)
        self.assertEqual(cam.read_noise, 0.5)
        # Audited to 89% peak QE
        self.assertEqual(cam.quantum_efficiency, 89)

        # Test MM version
        cam_mm = ZwoCamera.ZWO_ASI_462MM()
        self.assertEqual(
            cam_mm.sensor_width.to("mm").magnitude, 5.57
        )  # Verified for IMX462
        # Use existing QE for now or update if verified for MM too (usually same for IMX462)
        self.assertEqual(cam_mm.quantum_efficiency, 91)

    def test_asi585_specs(self):
        # Test legacy factory method (now consolidated)
        cam = ZwoCamera.ZWO_ASI585MC()
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 11.13)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 6.26)
        self.assertEqual(cam.width, 3840)
        self.assertEqual(cam.height, 2160)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.9)
        self.assertEqual(cam.full_well, 40000)
        self.assertEqual(cam.read_noise, 0.6)
        self.assertEqual(cam.quantum_efficiency, 91)

        # Test mass standardization
        self.assertEqual(cam.mass.to("gram").magnitude, 126)

    def test_asi678_specs(self):
        cam = ZwoCamera.ZWO_ASI_678MC()
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.68)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 4.32)
        self.assertEqual(cam.width, 3840)
        self.assertEqual(cam.height, 2160)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.0)
        self.assertEqual(cam.full_well, 11270)
        self.assertEqual(cam.read_noise, 0.6)
        self.assertEqual(cam.quantum_efficiency, 83)

    def test_asi664_specs(self):
        cam = ZwoCamera.ZWO_ASI_664MC()
        self.assertEqual(cam.sensor_width.to("mm").magnitude, 7.84)
        self.assertEqual(cam.sensor_height.to("mm").magnitude, 4.45)
        self.assertEqual(cam.width, 2704)
        self.assertEqual(cam.height, 1536)
        self.assertEqual(cam.pixel_size().to("micrometer").magnitude, 2.9)
        self.assertEqual(cam.full_well, 38500)
        self.assertEqual(cam.read_noise, 0.46)
        self.assertEqual(cam.quantum_efficiency, 91)
        self.assertEqual(cam.optical_length.to("mm").magnitude, 12.5)

    def test_asi224_specs(self):
        cam = ZwoCamera.ZWO_ASI_224MC()
        self.assertEqual(cam.mass.to("gram").magnitude, 120)
        self.assertEqual(cam.read_noise, 0.8)
        self.assertEqual(cam.quantum_efficiency, 80)
        self.assertEqual(cam.full_well, 19200)

    def test_asi174mm_specs(self):
        cam = ZwoCamera.ZWO_ASI_174MM()
        self.assertEqual(cam.mass.to("gram").magnitude, 140)
        self.assertEqual(cam.read_noise, 3.5)
        self.assertEqual(cam.quantum_efficiency, 78)
        self.assertEqual(cam.connection_type, ConnectionType.CS)
        self.assertEqual(cam.backfocus, Quantity(6.5, "millimeter"))


    def test_asi120_specs(self):
        # Test the classic USB2.0 models (Mono and Color)
        cam_mm = ZwoCamera.ZWO_ASI_120MM()
        self.assertEqual(cam_mm.mass.to('gram').magnitude, 100)

        cam_mc = ZwoCamera.ZWO_ASI_120MC()
        self.assertEqual(cam_mc.mass.to('gram').magnitude, 100)

        # Test the USB3.0 'S' model
        cam_mcs = ZwoCamera.ZWO_ASI_120MC_S()
        self.assertEqual(cam_mcs.mass.to('gram').magnitude, 100)

        # Test the special ASIAir variant
        cam_air = ZwoCamera.ZWO_ASI_120MM_S_for_ASIAir()
        self.assertEqual(cam_air.mass.to('gram').magnitude, 100)

if __name__ == '__main__':
    unittest.main()
