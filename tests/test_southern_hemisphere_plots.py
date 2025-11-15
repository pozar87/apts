import unittest
import numpy as np
from apts.place import Place

class TestSouthernHemispherePlots(unittest.TestCase):
    def test_sun_path_plot_for_southern_hemisphere(self):
        # Arrange
        # Use a real location in the Southern Hemisphere (Sydney)
        southern_place = Place(lat=-33.8688, lon=151.2093)

        # Act
        # Generate the actual plot Axes object
        ax = southern_place.plot_sun_path()

        # Assert
        # 1. Check if the x-axis limits are correctly inverted to center on North
        xlim = ax.get_xlim()
        self.assertEqual(xlim, (315, 45))

        # 2. Check that the plot is centered on North
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0, "No lines were plotted")

        # Combine data from all lines on the plot
        all_x_data = np.concatenate([line.get_xdata() for line in lines])
        all_y_data = np.concatenate([line.get_ydata() for line in lines])

        # Find the transit point (peak altitude)
        transit_index = np.argmax(all_y_data)
        transit_azimuth = all_x_data[transit_index]

        # The transit azimuth should be close to 0 or 360 degrees
        is_centered_on_north = transit_azimuth < 15 or transit_azimuth > 345
        self.assertTrue(is_centered_on_north, f"Plot not centered on North. Transit azimuth is {transit_azimuth}°")

    def test_moon_path_plot_for_southern_hemisphere(self):
        # Arrange
        # Use a real location in the Southern Hemisphere (Sydney)
        southern_place = Place(lat=-33.8688, lon=151.2093)

        # Act
        # Generate the actual plot Axes object
        ax = southern_place.plot_moon_path()

        # Assert
        # 1. Check if the x-axis limits are correctly inverted to center on North
        xlim = ax.get_xlim()
        self.assertEqual(xlim, (315, 45))

        # 2. Check that the plot is centered on North
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0, "No lines were plotted")

        # Combine data from all lines on the plot
        all_x_data = np.concatenate([line.get_xdata() for line in lines])
        all_y_data = np.concatenate([line.get_ydata() for line in lines])

        # Find the transit point (peak altitude)
        transit_index = np.argmax(all_y_data)
        transit_azimuth = all_x_data[transit_index]

        # The transit azimuth should be close to 0 or 360 degrees
        is_centered_on_north = transit_azimuth < 15 or transit_azimuth > 345
        self.assertTrue(is_centered_on_north, f"Plot not centered on North. Transit azimuth is {transit_azimuth}°")

if __name__ == "__main__":
    unittest.main()
