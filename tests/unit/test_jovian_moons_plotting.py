import unittest
from datetime import datetime
import matplotlib.figure
from apts.place import Place
from apts.equipment import Equipment
from apts.observations import Observation

class TestJovianMoonsPlotting(unittest.TestCase):
    def test_plot_jovian_moons(self):
        place = Place(50.06, 19.94, "Krakow", 200)
        equipment = Equipment()
        obs = Observation(place, equipment)

        # Test plot generation for a specific date
        test_date = datetime(2024, 5, 20, 20, 0)
        fig = obs.plot_jovian_moons(plot_date=test_date)

        self.assertIsInstance(fig, matplotlib.figure.Figure)
        self.assertEqual(len(fig.axes), 1)

        ax = fig.axes[0]
        # Check title contains expected parts
        title = ax.get_title()
        self.assertIn("Jupiter", title)
        self.assertIn("Moons", title)

        # Check if Jupiter patch exists
        patches = ax.patches
        # There should be at least one patch for Jupiter
        self.assertTrue(any(hasattr(p, 'get_label') and p.get_label() == 'Jupiter' for p in patches))

if __name__ == "__main__":
    unittest.main()
