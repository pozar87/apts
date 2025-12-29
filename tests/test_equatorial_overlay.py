import unittest
from unittest.mock import Mock, patch
import numpy as np

from apts.plot import _generate_plot_skymap
from apts.conditions import Conditions
from apts.constants.plot import CoordinateSystem
from skyfield.timelib import Time

class EquatorialOverlayTest(unittest.TestCase):
    @patch('matplotlib.pyplot.subplots')
    def test_plot_skymap_equatorial_overlay_is_drawn(self, mock_subplots):
        """
        Tests that the "available sky" overlay is drawn on polar equatorial skymaps.
        """
        # 1. Setup Mocks
        # Create a mock for the Axes object that has the methods we expect to be called
        mock_ax = Mock(spec=[
            'contourf', 'set_rlim', 'set_theta_zero_location',
            'set_theta_direction', 'set_yticks', 'set_yticklabels',
            'set_rlabel_position', 'set_xticklabels', 'grid', 'text',
            'scatter', 'annotate', 'set_title', 'get_facecolor'
        ])
        mock_fig = Mock()
        mock_subplots.return_value = (mock_fig, mock_ax)

        mock_observation = Mock()

        # Mock place and time attributes
        mock_ts = Mock()
        # The internal logic needs a valid Time object to do comparisons
        mock_ts.tt = 2451545.0  # J2000.0
        mock_time = Time(mock_ts)
        mock_ts.now.return_value = mock_time
        mock_observation.place = Mock()
        mock_observation.place.local_timezone = 'UTC'
        mock_observation.place.lat = 50.0
        mock_observation.place.ts = mock_ts
        mock_observation.start = None
        mock_observation.stop = None
        mock_observation.effective_date = mock_ts.now.return_value


        # Mock the observer chain to return mock coordinates
        # The grid created inside the function is 30x120
        mock_alt = Mock()
        mock_alt.degrees = np.full((30, 120), 45.0)
        mock_az = Mock()
        mock_az.degrees = np.full((30, 120), 90.0)

        # Mocks for the single target object
        mock_target_alt = Mock(degrees=45.0)
        mock_target_az = Mock(degrees=90.0)
        mock_target_ra = Mock(hours=6.0, radians=np.pi/2)
        mock_target_dec = Mock(degrees=30.0)

        def observe_side_effect(target):
            # Returns different coordinates depending on whether we are observing
            # the grid of stars or the single target object.
            mock_apparent = Mock()
            if hasattr(target, 'ra_hours'): # This is the grid
                mock_apparent.altaz.return_value = (mock_alt, mock_az, Mock())
            else: # This is the target
                mock_apparent.altaz.return_value = (mock_target_alt, mock_target_az, Mock())
                mock_apparent.radec.return_value = (mock_target_ra, mock_target_dec, Mock())

            mock_observed = Mock()
            mock_observed.apparent.return_value = mock_apparent
            return mock_observed

        mock_observer = Mock()
        mock_observer.at.return_value.observe.side_effect = observe_side_effect
        mock_observation.place.observer = mock_observer


        # Set observation conditions that will create a visible overlay
        mock_observation.conditions = Conditions(
            min_object_altitude=30,
            min_object_azimuth=0,
            max_object_azimuth=180
        )

        # Mock the catalog lookups to return a valid target
        mock_target = Mock()
        mock_observation.local_messier.objects = Mock(**{'[].empty': True})
        mock_observation.local_ngc.objects = Mock(**{'[].empty': True})
        mock_observation.local_stars.objects = Mock(**{'[].empty': True})
        mock_observation.local_planets.find_by_name.return_value = mock_target

        # 2. Call the function under test
        _generate_plot_skymap(
            observation=mock_observation,
            target_name="Jupiter",
            coordinate_system=CoordinateSystem.EQUATORIAL,
            plot_stars=False # Disable other plotting to isolate the overlay
        )

        # 3. Assert that the overlay was drawn
        mock_ax.contourf.assert_called_once()

        # Verify some of the arguments to ensure it's our call
        args, kwargs = mock_ax.contourf.call_args
        self.assertEqual(args[2].shape, (30, 120)) # Check mask shape
        self.assertEqual(args[2].dtype, int)      # Check mask dtype
        self.assertIn('colors', kwargs)
        self.assertIn('alpha', kwargs)
        self.assertIn('levels', kwargs)
