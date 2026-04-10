import unittest
from apts.opticalequipment.camera.vendors.player_one import Player_oneCamera
from apts.opticalequipment.telescope.vendors.william_optics import William_opticsTelescope
from apts.optics import OpticalPath
from apts.units import get_unit_registry
from apts.constants.astronomy import RAD_TO_ARCSEC

class TestPlayerOneV2(unittest.TestCase):
    def test_poseidon_c_pro_v2_specs(self):
        camera = Player_oneCamera.Player_One_Poseidon_C_Pro_v2()
        self.assertEqual(camera.vendor, "Player One Poseidon-C Pro v2")
        self.assertEqual(camera.pixel_size().to('micrometer').magnitude, 3.76)
        self.assertEqual(camera.mass.to('gram').magnitude, 510)
        self.assertEqual(camera.full_well, 71700)
        self.assertEqual(camera.quantum_efficiency, 81)

    def test_pixel_scale_precision(self):
        # Using a WO RedCat 51 (250mm) and Poseidon (3.76um)
        # Pixel scale = (3.76 / 250) * RAD_TO_ARCSEC = 3.102172...
        telescope = William_opticsTelescope.William_Optics_RedCat_51()
        camera = Player_oneCamera.Player_One_Poseidon_C_Pro_v2()
        path = OpticalPath.from_path([telescope, camera])

        scale = path.pixel_scale().to('arcsecond').magnitude
        expected = (0.00376 / 250.0) * RAD_TO_ARCSEC
        self.assertAlmostEqual(scale, expected, places=10)

        # Verify it's more precise than the old 206265 constant
        old_expected = (0.00376 / 250.0) * 206265
        self.assertNotAlmostEqual(scale, old_expected, places=10)

    def test_zeus_m_pro_v2_specs(self):
        camera = Player_oneCamera.Player_One_Zeus_M_Pro_v2()
        self.assertEqual(camera.vendor, "Player One Zeus-M Pro v2")
        self.assertEqual(camera.pixel_size().to('micrometer').magnitude, 3.76)
        self.assertEqual(camera.mass.to('gram').magnitude, 550)
        self.assertEqual(camera.full_well, 51000)
        self.assertEqual(camera.quantum_efficiency, 91)

if __name__ == "__main__":
    unittest.main()
