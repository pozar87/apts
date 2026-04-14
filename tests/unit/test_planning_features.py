
import unittest
from apts.constants import DSOType, FilterStrategy
from apts.scoring import SuitabilityScorer
from apts.place import Place
from apts.catalogs import Catalogs
from apts.discovery import DiscoveryService, TimelineGenerator
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.william_optics import William_opticsTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
import datetime

class TestNewPlanningFeatures(unittest.TestCase):
    def setUp(self):
        self.place = Place(52.2297, 21.0122) # Warsaw
        telescope = William_opticsTelescope.William_Optics_RedCat_61()
        camera = ZwoCamera.ZWO_ASI_2600MC_Pro()
        self.path = OpticalPath(telescope, [], [], [], [], camera)
        self.catalogs = Catalogs()

    def test_suitability_scorer_metrics(self):
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

    def test_discovery_top_picks(self):
        # This will score Messier objects
        top_picks = DiscoveryService.get_top_picks(self.place, self.path, self.catalogs, limit=5)
        self.assertEqual(len(top_picks), 5)
        self.assertIn("Score", top_picks[0])
        self.assertGreater(top_picks[0]["Score"], 0)
        self.assertIn("Details", top_picks[0])

    def test_timeline_generation(self):
        timeline = TimelineGenerator.generate_timeline(self.place)
        self.assertIn("twilight_events", timeline)
        self.assertIn("moon_events", timeline)
        self.assertIsInstance(timeline["twilight_events"], list)
        if timeline["twilight_events"]:
            self.assertIn("phase", timeline["twilight_events"][0])

if __name__ == "__main__":
    unittest.main()
