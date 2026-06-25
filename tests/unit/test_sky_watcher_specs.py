import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

class TestSkyWatcherSpecs(unittest.TestCase):
    def test_az_eq5_gt_8_newton_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_AZ_EQ5_GT_8_Newton()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher AZ-EQ5 GT 8\" Newton")
        self.assertEqual(scope.aperture.to('mm').magnitude, 200)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 52)
        self.assertEqual(scope.mass.to('gram').magnitude, 8500)

    def test_az_eq6_pro_8_newton_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_AZ_EQ6_Pro_8_Newton()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher AZ-EQ6 Pro 8\" Newton")
        self.assertEqual(scope.aperture.to('mm').magnitude, 200)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 52)
        self.assertEqual(scope.mass.to('gram').magnitude, 8600)

    def test_black_diamond_ed100_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Black_Diamond_ED100()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Black Diamond ED100")
        self.assertEqual(scope.aperture.to('mm').magnitude, 100)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 900)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 3000)

    def test_black_diamond_ed120_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Black_Diamond_ED120()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Black Diamond ED120")
        self.assertEqual(scope.aperture.to('mm').magnitude, 120)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 900)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 5130)

    def test_black_diamond_ed80_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Black_Diamond_ED80()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Black Diamond ED80")
        self.assertEqual(scope.aperture.to('mm').magnitude, 80)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 600)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2470)

    def test_equinox_100_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Equinox_100()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Equinox 100")
        self.assertEqual(scope.aperture.to('mm').magnitude, 100)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 900)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 4500)

    def test_equinox_120_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Equinox_120()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Equinox 120")
        self.assertEqual(scope.aperture.to('mm').magnitude, 120)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 900)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 6200)

    def test_equinox_80_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Equinox_80()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Equinox 80")
        self.assertEqual(scope.aperture.to('mm').magnitude, 80)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 500)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2900)

    def test_heritage_100p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Heritage_100P()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Heritage 100P")
        self.assertEqual(scope.aperture.to('mm').magnitude, 100)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 400)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 34)
        self.assertEqual(scope.mass.to('gram').magnitude, 1100)

    def test_heritage_76_mini_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Heritage_76_Mini()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Heritage 76 Mini")
        self.assertEqual(scope.aperture.to('mm').magnitude, 76)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 300)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 28)
        self.assertEqual(scope.mass.to('gram').magnitude, 600)

    def test_skymax_90_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_SkyMax_90()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher SkyMax 90")
        self.assertEqual(scope.aperture.to('mm').magnitude, 90)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1250)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 29)
        self.assertEqual(scope.mass.to('gram').magnitude, 1370)

    def test_skymax_102_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_SkyMax_102()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher SkyMax 102")
        self.assertEqual(scope.aperture.to('mm').magnitude, 102)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1300)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 31)
        self.assertEqual(scope.mass.to('gram').magnitude, 2200)

    def test_skymax_102_az_gti_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_SkyMax_102_AZ_GTi()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher SkyMax 102 AZ-GTi")
        self.assertEqual(scope.aperture.to('mm').magnitude, 102)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1300)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 31)
        self.assertEqual(scope.mass.to('gram').magnitude, 2200)

    def test_skymax_127_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_SkyMax_127()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher SkyMax 127")
        self.assertEqual(scope.aperture.to('mm').magnitude, 127)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1500)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 39)
        self.assertEqual(scope.mass.to('gram').magnitude, 3400)

    def test_skymax_127_az_gti_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_SkyMax_127_AZ_GTi()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher SkyMax 127 AZ-GTi")
        self.assertEqual(scope.aperture.to('mm').magnitude, 127)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1500)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 39)
        self.assertEqual(scope.mass.to('gram').magnitude, 3400)

    def test_skymax_150_pro_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_SkyMax_150_Pro()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher SkyMax 150 Pro")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1800)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 5600)

    def test_skymax_180_pro_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_SkyMax_180_Pro()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher SkyMax 180 Pro")
        self.assertEqual(scope.aperture.to('mm').magnitude, 180)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2700)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 41)
        self.assertEqual(scope.mass.to('gram').magnitude, 7800)

    def test_star_discovery_150p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Star_Discovery_150P()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Star Discovery 150P")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 4900)

    def test_star_discovery_150i_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Star_Discovery_150i()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Star Discovery 150i")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 4900)

    def test_star_discovery_200p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Star_Discovery_200P()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Star Discovery 200P")
        self.assertEqual(scope.aperture.to('mm').magnitude, 200)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 52)
        self.assertEqual(scope.mass.to('gram').magnitude, 8200)

    def test_stargate_450p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Stargate_450P_Truss_Dob()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Stargate 450P Truss Dob")
        self.assertEqual(scope.aperture.to('mm').magnitude, 458)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1900)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 120)
        self.assertEqual(scope.mass.to('gram').magnitude, 50000)

    def test_stargate_500p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Stargate_500P_Truss_Dob()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Stargate 500P Truss Dob")
        self.assertEqual(scope.aperture.to('mm').magnitude, 508)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 136)
        self.assertEqual(scope.mass.to('gram').magnitude, 65000)

    def test_starquest_80mc_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Starquest_80MC()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Starquest 80MC")
        self.assertEqual(scope.aperture.to('mm').magnitude, 80)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 26)
        self.assertEqual(scope.mass.to('gram').magnitude, 1200)

    def test_250pds_newtonian_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_250PDS_Newtonian()
        self.assertEqual(scope.aperture.to('mm').magnitude, 254)
        self.assertEqual(scope.mass.to('gram').magnitude, 14380)

    def test_explorer_250p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Explorer_250P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 254)
        self.assertEqual(scope.mass.to('gram').magnitude, 14380)

    def test_heritage_150p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Heritage_150P()
        self.assertEqual(scope.mass.to('gram').magnitude, 3700)

    def test_star_adventurer_gti_80ed_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Star_Adventurer_GTi_80ED()
        self.assertEqual(scope.aperture.to('mm').magnitude, 80)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 600)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2600)

    def test_explorer_150p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Explorer_150P()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Explorer 150P")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 4930)

    def test_evostar_150ed_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Evostar_150ED()
        self.assertEqual(scope.mass.to('gram').magnitude, 9500)

    def test_evostar_150dx_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Evostar_150DX()
        self.assertEqual(scope.mass.to('gram').magnitude, 9980)

if __name__ == '__main__':
    unittest.main()
