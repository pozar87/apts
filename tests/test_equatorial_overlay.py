from typing import Any, cast
from unittest.mock import MagicMock, PropertyMock, patch

import numpy as np
import pandas as pd
import pytest
from skyfield.api import Star as SkyfieldStar
from skyfield.units import Angle

from apts.conditions import Conditions
from apts.constants.plot import CoordinateSystem
from apts.equipment import Equipment
from apts.observations import Observation
from apts.place import Place
from apts.plot import _generate_plot_skymap


@pytest.fixture
def mock_obs_and_target():
    """Fixture to create a mock observation and target object."""
    with (
        patch.object(
            Observation, "local_stars", new_callable=PropertyMock
        ) as mock_local_stars,
        patch.object(
            Observation, "local_messier", new_callable=PropertyMock
        ) as mock_local_messier,
        patch.object(
            Observation, "local_ngc", new_callable=PropertyMock
        ) as mock_local_ngc,
        patch.object(
            Observation, "local_planets", new_callable=PropertyMock
        ) as mock_local_planets,
    ):
        place = Place(lat=34.0, lon=-118.0, elevation=0, name="LA")
        equipment = Equipment()
        conditions = Conditions(
            min_object_altitude=30.0,
            min_object_azimuth=90.0,
            max_object_azimuth=270.0,
        )
        obs = Observation(place=place, equipment=equipment, conditions=conditions)

        target_name = "Vega"
        mock_target_object = MagicMock()
        # To satisfy hasattr checks in the code for deep sky objects
        type(mock_target_object).ra = MagicMock(spec=Angle)
        type(mock_target_object).dec = MagicMock(spec=Angle)

        # Configure the mocks to return instances that have the methods/properties needed
        mock_stars_instance = MagicMock()
        mock_stars_instance.objects = pd.DataFrame([{"Name": target_name}])
        mock_stars_instance.get_skyfield_object.return_value = mock_target_object
        mock_local_stars.return_value = mock_stars_instance

        mock_messier_instance = MagicMock()
        mock_messier_instance.objects = pd.DataFrame(
            columns=cast(Any, ["Messier", "Name"])
        )
        mock_local_messier.return_value = mock_messier_instance

        mock_ngc_instance = MagicMock()
        mock_ngc_instance.objects = pd.DataFrame(columns=cast(Any, ["NGC", "Name"]))
        mock_local_ngc.return_value = mock_ngc_instance

        mock_planets_instance = MagicMock()
        mock_planets_instance.find_by_name.return_value = None
        mock_local_planets.return_value = mock_planets_instance

        yield obs, target_name, mock_target_object


def test_equatorial_skymap_overlay_normal_azimuth(mock_obs_and_target):
    """
    Tests that the available sky overlay is correctly calculated for a normal
    azimuth range (e.g., 90-270 degrees).
    """
    obs, target_name, mock_target_object = mock_obs_and_target
    # Conditions are already set in the fixture for normal azimuth

    # Mock the observer and coordinate transformation
    mock_observer = MagicMock()
    obs.place.observer.at = MagicMock(return_value=mock_observer)

    # Create a predictable alt/az grid to be returned by the mocked observer
    # Grid shape is (num_dec, num_ra) = (30, 120)
    alt_grid = np.full((30, 120), 45.0)  # All are above the 30 deg min_altitude
    az_grid = np.zeros((30, 120))
    # First half of the grid is within the good azimuth range [90, 270]
    az_grid[:, :60] = 180.0
    # Second half is outside the good azimuth range
    az_grid[:, 60:] = 0.0

    mock_alt = Angle(degrees=alt_grid.ravel())
    mock_az = Angle(degrees=az_grid.ravel())

    # This mock will be returned when observing the grid of stars
    mock_grid_observation = MagicMock()
    mock_grid_observation.apparent.return_value.altaz.return_value = (
        mock_alt,
        mock_az,
        MagicMock(),
    )

    # This mock will be returned when observing the single target object
    mock_target_observation = MagicMock()
    mock_target_observation.apparent.return_value.altaz.return_value = (
        Angle(degrees=60),
        Angle(degrees=180),
        MagicMock(),
    )
    mock_target_observation.apparent.return_value.radec.return_value = (
        mock_target_object.ra,
        mock_target_object.dec,
        MagicMock(),
    )

    def observe_side_effect(target):
        # SkyfieldStar is used for both single stars and grids of stars
        if isinstance(target, SkyfieldStar):
            # Check if it's the grid by looking at the number of stars
            if isinstance(target.ra.hours, np.ndarray) and len(target.ra.hours) > 1:
                return mock_grid_observation
        return mock_target_observation  # The single target object or other types

    mock_observer.observe.side_effect = observe_side_effect

    with patch("apts.plot.pyplot") as mock_pyplot:
        mock_fig, mock_ax = MagicMock(), MagicMock()
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        # Call the function being tested
        _generate_plot_skymap(
            observation=obs,
            target_name=target_name,
            coordinate_system=cast(Any, CoordinateSystem.EQUATORIAL),
            plot_stars=False,
        )

        # Assert that the overlay was drawn
        mock_ax.contourf.assert_called_once()
        args, _ = mock_ax.contourf.call_args

        # Verify the mask passed to contourf is correct
        plotted_mask = args[2]
        expected_alt_mask = alt_grid >= obs.conditions.min_object_altitude
        expected_az_mask = (az_grid >= obs.conditions.min_object_azimuth) & (
            az_grid <= obs.conditions.max_object_azimuth
        )
        expected_good_mask = expected_alt_mask & expected_az_mask

        np.testing.assert_array_equal(plotted_mask, expected_good_mask.astype(int))


def test_equatorial_skymap_overlay_wrapping_azimuth(mock_obs_and_target):
    """
    Tests that the available sky overlay is correctly calculated for a wrapping
    azimuth range (e.g., 270-90 degrees).
    """
    obs, target_name, mock_target_object = mock_obs_and_target
    # Override conditions for a wrapping azimuth range
    obs.conditions.min_object_azimuth = 270.0
    obs.conditions.max_object_azimuth = 90.0

    # Mock the observer and coordinate transformation
    mock_observer = MagicMock()
    obs.place.observer.at = MagicMock(return_value=mock_observer)

    # Create a predictable alt/az grid
    alt_grid = np.full((30, 120), 45.0)  # All above min_altitude
    az_grid = np.zeros((30, 120))
    # Part of the grid is in the good range (>= 270)
    az_grid[:, :30] = 300.0
    # Part is in the good range (<= 90)
    az_grid[:, 30:60] = 45.0
    # Part is outside the good range
    az_grid[:, 60:] = 180.0

    mock_alt = Angle(degrees=alt_grid.ravel())
    mock_az = Angle(degrees=az_grid.ravel())
    mock_grid_observation = MagicMock()
    mock_grid_observation.apparent.return_value.altaz.return_value = (
        mock_alt,
        mock_az,
        MagicMock(),
    )

    mock_target_observation = MagicMock()
    mock_target_observation.apparent.return_value.altaz.return_value = (
        Angle(degrees=60),
        Angle(degrees=180),
        MagicMock(),
    )
    mock_target_observation.apparent.return_value.radec.return_value = (
        mock_target_object.ra,
        mock_target_object.dec,
        MagicMock(),
    )

    def observe_side_effect(target):
        if isinstance(target, SkyfieldStar):
            if isinstance(target.ra.hours, np.ndarray) and len(target.ra.hours) > 1:
                return mock_grid_observation
        return mock_target_observation

    mock_observer.observe.side_effect = observe_side_effect

    with patch("apts.plot.pyplot") as mock_pyplot:
        mock_fig, mock_ax = MagicMock(), MagicMock()
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        # Call the function
        _generate_plot_skymap(
            observation=obs,
            target_name=target_name,
            coordinate_system=cast(Any, CoordinateSystem.EQUATORIAL),
            plot_stars=False,
        )

        # Assertions
        mock_ax.contourf.assert_called_once()
        args, _ = mock_ax.contourf.call_args
        plotted_mask = args[2]

        expected_alt_mask = alt_grid >= obs.conditions.min_object_altitude
        expected_az_mask = (az_grid >= obs.conditions.min_object_azimuth) | (
            az_grid <= obs.conditions.max_object_azimuth
        )
        expected_good_mask = expected_alt_mask & expected_az_mask

        np.testing.assert_array_equal(plotted_mask, expected_good_mask.astype(int))
