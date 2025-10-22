import pytest
from unittest.mock import patch, MagicMock
from apts.plot import plot_skymap, _plot_messier_on_skymap, _plot_planets_on_skymap, _plot_sun_on_skymap, _plot_moon_on_skymap, _plot_ngc_on_skymap
from apts.observations import Observation
from apts.equipment import Equipment
from apts.catalogs import Catalogs
from apts.place import Place
from apts.conditions import Conditions
from datetime import datetime
import pandas as pd
from matplotlib.patches import Ellipse
import pytz


@pytest.fixture
def mock_observation():
    place = Place(lat=34.0, lon=-118.0, elevation=0, name="LA")
    equipment = Equipment()
    utc = pytz.UTC
    # Use a nighttime start time for the observation in LA
    # 2023-01-02 04:00 UTC is 2023-01-01 20:00 PST (8 PM)
    conditions = Conditions(
        start_time=datetime(2023, 1, 2, 4, 0, tzinfo=utc),
    )
    observation = Observation(
        place=place, equipment=equipment, conditions=conditions
    )
    return observation


def test_plot_skymap_renders_messier_objects(mock_observation):
    # Mock the necessary methods and data to avoid actual plotting
    with patch("apts.plot.pyplot") as mock_pyplot, \
         patch.object(Observation, 'local_messier', MagicMock()) as mock_local_messier:
        # Mock the figure and axes objects
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (0, 360)
        mock_ax.get_ylim.return_value = (0, 90)
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        messier_data = {
            "Name": ["M31", "M42"],
            "Messier": ["M31", "M42"],
            "Width": [178.0, 85.0],
            "Height": [63.0, 60.0],
            "Angle": [35.0, 0.0],
        }
        mock_visible_messier = pd.DataFrame(messier_data)
        mock_observation.get_visible_messier = MagicMock(return_value=mock_visible_messier)

        # Create a mock Skyfield object that can be observed
        from skyfield.timelib import Time, Timescale
        from skyfield.units import Angle
        import numpy as np
        mock_skyfield_obj = MagicMock()
        mock_skyfield_obj.ra = Angle(hours=0.0)
        mock_skyfield_obj.dec = Angle(degrees=0.0)
        mock_ts = MagicMock(spec=Timescale)
        mock_time = MagicMock(spec=Time)
        mock_time.tdb = 2451545.0
        mock_time.whole = 2451545.0
        mock_time.tdb_fraction = 0.0
        mock_time.ts = mock_ts
        mock_ts.tdb.return_value = mock_time
        mock_skyfield_obj._observe_from_bcrs.return_value = (np.zeros(3), np.zeros(3), mock_time, 0)
        mock_local_messier.find_by_name.return_value = mock_skyfield_obj
        mock_local_messier.get_skyfield_object.return_value = mock_skyfield_obj
        mock_local_messier.objects = mock_visible_messier

        # Call the function to be tested
        plot_skymap(
            observation=mock_observation,
            target_name="M31",
            plot_messier=True,
            zoom_deg=10.0,
        )

        # Assert that the subplots function was called, indicating a plot was created
        mock_pyplot.subplots.assert_called_once()

        # Check that Ellipse patch was added
        assert mock_ax.add_patch.call_count > 0

def test_plot_messier_on_skymap_flips_orientation_correctly():
    # Create mock objects
    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Mock the visible Messier objects data
    messier_data = {
        "Messier": ["M31"],
        "Width": [178.0],
        "Height": [63.0],
        "Angle": [35.0],
    }
    mock_visible_messier = pd.DataFrame(messier_data)
    mock_observation.get_visible_messier.return_value = mock_visible_messier
    mock_observation.local_messier.find_by_name.return_value = MagicMock()
    mock_observer.observe.return_value.apparent.return_value.altaz.return_value = (
        MagicMock(degrees=45),
        MagicMock(degrees=180),
        MagicMock(),
    )

    # Call the function with horizontal flip
    _plot_messier_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        target_name="M42",
        flipped_horizontally=True,
        flipped_vertically=False,
    )

    # Check that the ellipse was created with the correct angle
    args, kwargs = mock_ax.add_patch.call_args
    ellipse = args[0]
    assert isinstance(ellipse, Ellipse)
    assert ellipse.angle == -35.0

    # Call the function with vertical flip
    _plot_messier_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        target_name="M42",
        flipped_horizontally=False,
        flipped_vertically=True,
    )

    # Check that the ellipse was created with the correct angle
    args, kwargs = mock_ax.add_patch.call_args
    ellipse = args[0]
    assert isinstance(ellipse, Ellipse)
    assert ellipse.angle == 145.0

def test_plot_planets_on_skymap_renders_planets_as_ellipses():
    # Create mock objects
    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Mock the visible planets data
    planets_data = {
        "Name": ["Mars"],
        "Size": [14.5],
    }
    mock_visible_planets = pd.DataFrame(planets_data)
    mock_observation.get_visible_planets.return_value = mock_visible_planets
    mock_observation.local_planets.find_by_name.return_value = MagicMock()
    mock_observer.observe.return_value.apparent.return_value.altaz.return_value = (
        MagicMock(degrees=45),
        MagicMock(degrees=180),
        MagicMock(),
    )
    style = {"TEXT_COLOR": "white"}
    # Call the function
    _plot_planets_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        effective_dark_mode=False,
        style=style,
    )

    # Check that the ellipse was created with the correct size
    args, kwargs = mock_ax.add_patch.call_args
    ellipse = args[0]
    assert isinstance(ellipse, Ellipse)
    assert ellipse.width == 14.5 / 3600.0
    assert ellipse.height == 14.5 / 3600.0

def test_plot_sun_on_skymap_renders_sun():
    # Create mock objects
    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Mock the sun's position
    mock_observer.observe.return_value.apparent.return_value.altaz.return_value = (
        MagicMock(degrees=45),
        MagicMock(degrees=180),
        MagicMock(),
    )
    style = {"TEXT_COLOR": "white"}
    # Call the function
    _plot_sun_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        style=style,
    )

    # Check that an ellipse was added
    assert mock_ax.add_patch.call_count > 0

def test_plot_moon_on_skymap_renders_moon():
    # Create mock objects
    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Mock the moon's position
    mock_observer.observe.return_value.apparent.return_value.altaz.return_value = (
        MagicMock(degrees=45),
        MagicMock(degrees=180),
        MagicMock(),
    )
    style = {"TEXT_COLOR": "white"}
    # Call the function
    _plot_moon_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        style=style,
    )

    # Check that an ellipse was added
    assert mock_ax.add_patch.call_count > 0

def test_plot_ngc_object_with_no_size(mock_observation):
    # Mock the necessary methods and data to avoid actual plotting
    with patch("apts.plot.pyplot") as mock_pyplot:
        # Mock the figure and axes objects
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (0, 360)
        mock_ax.get_ylim.return_value = (0, 90)
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        # Call the function to be tested
        plot_skymap(
            observation=mock_observation,
            target_name="IC0024",
            plot_ngc=True,
            zoom_deg=10.0,
        )

        # Assert that the subplots function was called, indicating a plot was created
        mock_pyplot.subplots.assert_called_once()

def test_plot_planet_with_no_size_polar(mock_observation):
    # Mock the necessary methods and data to avoid actual plotting
    with patch("apts.plot.pyplot") as mock_pyplot:
        # Mock the figure and axes objects
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        # Call the function to be tested
        plot_skymap(
            observation=mock_observation,
            target_name="Mars",
            plot_planets=True,
        )

        # Assert that the subplots function was called, indicating a plot was created
        mock_pyplot.subplots.assert_called_once()
