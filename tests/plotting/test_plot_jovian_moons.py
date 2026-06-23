import matplotlib
matplotlib.use("Agg")
import pytest
import pandas as pd
from unittest.mock import MagicMock, patch
from datetime import datetime
import pytz
import numpy as np

from apts.plotting.jovian_moons import generate_plot_jovian_moons, plot_jovian_moons
from apts.observations import Observation
from apts.place import Place
from apts.equipment import Equipment
from skyfield.api import load

@pytest.fixture
def mock_observation():
    place = Place(lat=50.0, lon=20.0, elevation=200, name="Krakow")
    equipment = Equipment()
    observation = Observation(place=place, equipment=equipment)
    # Use a real Time object from skyfield
    ts = load.timescale()
    observation.effective_date = ts.utc(2025, 2, 18)
    return observation

def test_generate_plot_jovian_moons_flipping(mock_observation):
    with patch("apts.plotting.jovian_moons.pyplot.subplots") as mock_subplots:
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)

        # Mock other dependencies to avoid errors
        with patch("apts.plotting.jovian_moons.get_jovian_ephemeris"), \
             patch("apts.plotting.jovian_moons.JovianSearchContext") as mock_ctx_cls, \
             patch("apts.plotting.jovian_moons.JovianMoonState"):

            mock_ctx = mock_ctx_cls.return_value
            mock_ctx.moon_map = {}
            mock_ctx.jupiter = MagicMock()

            # Mock the observer.at(t).observe(jupiter) chain
            mock_j_obs = MagicMock()
            mock_j_obs.radec.return_value = (MagicMock(radians=0), MagicMock(degrees=0), MagicMock(km=700000000))

            # Since observer is an object, we need to mock its methods
            mock_observer = MagicMock()
            mock_observation.place.observer = mock_observer
            mock_observer.at.return_value.observe.return_value.apparent.return_value = mock_j_obs

            # 1. Test no flipping
            generate_plot_jovian_moons(mock_observation, flipped_horizontally=False, flipped_vertically=False)
            mock_ax.invert_xaxis.assert_not_called()
            mock_ax.invert_yaxis.assert_not_called()

            mock_ax.reset_mock()

            # 2. Test horizontal flipping
            generate_plot_jovian_moons(mock_observation, flipped_horizontally=True, flipped_vertically=False)
            mock_ax.invert_xaxis.assert_called_once()
            mock_ax.invert_yaxis.assert_not_called()

            mock_ax.reset_mock()

            # 3. Test vertical flipping
            generate_plot_jovian_moons(mock_observation, flipped_horizontally=False, flipped_vertically=True)
            mock_ax.invert_xaxis.assert_not_called()
            mock_ax.invert_yaxis.assert_called_once()

            mock_ax.reset_mock()

            # 4. Test both flips
            generate_plot_jovian_moons(mock_observation, flipped_horizontally=True, flipped_vertically=True)
            mock_ax.invert_xaxis.assert_called_once()
            mock_ax.invert_yaxis.assert_called_once()

def test_plot_jovian_moons_equipment_detection(mock_observation):
    # Mock equipment data
    equipment_data = pd.DataFrame([
        {"ID": 1, "Flipped Horizontally": True, "Flipped Vertically": False},
        {"ID": 2, "Flipped Horizontally": False, "Flipped Vertically": True}
    ])

    with patch.object(mock_observation.equipment, "data", return_value=equipment_data), \
         patch("apts.plotting.jovian_moons.generate_plot_jovian_moons") as mock_generate:

        # 1. Detect ID 1
        plot_jovian_moons(mock_observation, equipment_id=1)
        args, kwargs = mock_generate.call_args
        assert bool(kwargs["flipped_horizontally"]) == True
        assert bool(kwargs["flipped_vertically"]) == False

        # 2. Detect ID 2
        plot_jovian_moons(mock_observation, equipment_id=2)
        args, kwargs = mock_generate.call_args
        assert bool(kwargs["flipped_horizontally"]) == False
        assert bool(kwargs["flipped_vertically"]) == True

        # 3. Explicit override should take precedence (flip_horizontally=False)
        plot_jovian_moons(mock_observation, equipment_id=1, flip_horizontally=False)
        args, kwargs = mock_generate.call_args
        assert bool(kwargs["flipped_horizontally"]) == False
        # Flipped Vertically should still be taken from equipment if not overridden,
        # but here it is False in equipment ID 1 anyway.
        assert bool(kwargs["flipped_vertically"]) == False

        # 4. Explicit override should take precedence (flip_vertically=True)
        plot_jovian_moons(mock_observation, equipment_id=1, flip_vertically=True)
        args, kwargs = mock_generate.call_args
        assert bool(kwargs["flipped_horizontally"]) == True
        assert bool(kwargs["flipped_vertically"]) == True
