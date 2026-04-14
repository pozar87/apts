
import unittest
from apts.constants import DSOType, FilterStrategy
from apts.scoring import SuitabilityScorer
from apts.place import Place
from apts.equipment import Equipment
from apts.catalogs import Catalogs
from apts.discovery import DiscoveryService, TimelineGenerator
import datetime

class TestScoring(unittest.TestCase):
    def setUp(self):
        self.place = Place(52.2297, 21.0122) # Warsaw
        self.equipment = Equipment()
        # Add some basic equipment to have a path
        from apts.opticalequipment.telescope.vendors.william_optics import William_opticsTelescope
        from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
        self.equipment.register(William_opticsTelescope.William_Optics_RedCat_61())
        self.equipment.register(ZwoCamera.ZWO_ASI_2600MC_Pro())
        self.path = self.equipment._get_paths("Image")[0]
        self.catalogs = Catalogs()

    def test_suitability_scorer(self):
        scorer = SuitabilityScorer(self.place, self.path)
        # Test altitude scoring
        self.assertEqual(scorer.score_altitude(70), 30)
        self.assertEqual(scorer.score_altitude(60), 25)
        self.assertEqual(scorer.score_altitude(40), 18)
        self.assertEqual(scorer.score_altitude(25), 10)
        self.assertEqual(scorer.score_altitude(10), 0)

        # Test imaging window scoring
        self.assertEqual(scorer.score_imaging_window(300), 20)
        self.assertEqual(scorer.score_imaging_window(180), 16)
        self.assertEqual(scorer.score_imaging_window(120), 12)
        self.assertEqual(scorer.score_imaging_window(60), 8)
        self.assertEqual(scorer.score_imaging_window(30), 0)

        # Test FOV fit scoring
        self.assertEqual(scorer.score_fov_fit(50), 30)
        self.assertEqual(scorer.score_fov_fit(150), 18)
        self.assertEqual(scorer.score_fov_fit(5), 0)

    def test_discovery_service(self):
        # This will actually score objects, might be slow so we limit
        top_picks = DiscoveryService.get_top_picks(self.place, self.path, self.catalogs, limit=5)
        self.assertEqual(len(top_picks), 5)
        self.assertTrue("Score" in top_picks[0])
        self.assertTrue(top_picks[0]["Score"] > 0)

    def test_timeline_generator(self):
        timeline = TimelineGenerator.generate_timeline(self.place)
        self.assertIn("twilight_events", timeline)
        self.assertIn("moon_events", timeline)

if __name__ == "__main__":
    unittest.main()
