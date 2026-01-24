
import pytest
import pandas as pd
from datetime import datetime
import pytz
from unittest.mock import MagicMock, patch
from apts.place import Place
from apts.equipment import Equipment
from apts.conditions import Conditions
from apts.observations import Observation
from apts.plotting.utils import get_object_angular_size_deg
from apts.i18n import language_context

@pytest.fixture
def mock_observation():
    place = Place(lat=52.0, lon=21.0, elevation=100, name="Warsaw")
    equipment = Equipment()
    target_date = datetime(2023, 11, 1, 22, 0, tzinfo=pytz.UTC)
    conditions = Conditions()
    observation = Observation(place=place, equipment=equipment, conditions=conditions, target_date=target_date)
    return observation

def test_get_object_angular_size_deg_i18n(mock_observation):
    # Test English context
    with language_context("en"):
        size_en = get_object_angular_size_deg(mock_observation, "Jupiter")
        assert size_en > 0
        assert abs(size_en * 3600 - 49.4) < 1.0 # Jupiter is around 49 arcsec

    # Test Polish context
    with language_context("pl"):
        # Even if we pass "Jupiter" (English name), it should work because of technical name matching
        size_pl = get_object_angular_size_deg(mock_observation, "Jupiter")
        assert size_pl == size_en

        # Test with Polish name
        size_pl_translated = get_object_angular_size_deg(mock_observation, "Jowisz")
        assert size_pl_translated == size_en

def test_get_object_angular_size_deg_technical_name(mock_observation):
    size = get_object_angular_size_deg(mock_observation, "jupiter barycenter")
    assert size > 0
    assert abs(size * 3600 - 49.4) < 1.0

def test_planet_visual_size_on_polar_plot(mock_observation):
    from apts.plotting.skymap_objects import _plot_solar_system_object_on_skymap

    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Mock observer to return some valid altaz/radec
    from skyfield.units import Angle
    mock_observed = MagicMock()
    mock_observed.apparent.return_value.altaz.return_value = (Angle(degrees=45), Angle(degrees=180), None)
    mock_observed.apparent.return_value.radec.return_value = (Angle(hours=12), Angle(degrees=0), None)
    mock_observer.observe.return_value = mock_observed

    style = {"EMPHASIS_COLOR": "yellow"}

    with patch("apts.plotting.skymap_objects.get_dark_mode", return_value=True):
        _plot_solar_system_object_on_skymap(
            mock_observation,
            mock_ax,
            mock_observer,
            is_polar=True,
            style=style,
            object_name="Jupiter"
        )

    # Check that scatter was called
    mock_ax.scatter.assert_called_once()
    args, kwargs = mock_ax.scatter.call_args
    size = kwargs.get('s')

    # Jupiter mag is around -2.7.
    # visual_size = (4.5 + 1 - (-2.7)) * 5 = 8.2 * 5 = 41
    # size_deg * 200 = 0.0137 * 200 = 2.74
    # max(2.74, 41) = 41
    assert size >= 40
