import matplotlib

matplotlib.use("Agg")
from unittest.mock import MagicMock, patch
from typing import cast
import pandas as pd
import numpy as np
import pytest
from skyfield.units import Angle
from apts.constants.plot import CoordinateSystem
from apts.plotting.skymap_objects import _plot_ngc_on_skymap


@pytest.fixture
def mock_observation():
    observation = MagicMock()
    observation.place.lat = 34.0
    observation.place.lat_decimal = 34.0
    return observation


@pytest.fixture
def mock_ax():
    ax = MagicMock()
    ax.get_xlim.return_value = (0, 360)
    ax.get_ylim.return_value = (0, 90)
    return ax


@pytest.fixture
def mock_observer():
    observer = MagicMock()
    # Default observation returns
    mock_observed = MagicMock()
    mock_observed.apparent.return_value.altaz.return_value = (
        Angle(degrees=45),
        Angle(degrees=180),
        Angle(degrees=0),
    )
    mock_observed.apparent.return_value.radec.return_value = (
        Angle(hours=1.0),
        Angle(degrees=40.0),
        Angle(degrees=0),
    )
    # Mock position in AU for separation calculations
    mock_observed.position.au = np.array([1.0, 0.0, 0.0])
    observer.observe.return_value = mock_observed
    return observer


def test_plot_ngc_on_skymap_basic(mock_observation, mock_ax, mock_observer):
    # Mock NGC data
    ngc_data = pd.DataFrame(
        [
            {
                "NGC": "NGC 224",
                "Name": "Andromeda",
                "Size": 178.0,
                "MinAx": 63.0,
                "PosAng": 35.0,
                "Mag": 3.44,
                "Type": "Galaxy",
            },
            {
                "NGC": "NGC 1976",
                "Name": "M42",
                "Size": 85.0,
                "MinAx": 60.0,
                "PosAng": 0.0,
                "Mag": 4.0,
                "Type": "Nebula",
            },
        ]
    )
    mock_observation.get_visible_ngc.return_value = ngc_data

    mock_ngc_obj = MagicMock()
    # Ensure altaz and radec methods return expected objects
    mock_ngc_obj.dec = Angle(degrees=40.0)
    mock_observed = MagicMock()
    mock_observed.apparent.return_value.altaz.return_value = (
        Angle(degrees=45),
        Angle(degrees=180),
        Angle(degrees=0),
    )
    mock_observed.apparent.return_value.radec.return_value = (
        Angle(hours=1.0),
        Angle(degrees=40.0),
        Angle(degrees=0),
    )
    mock_observer.observe.return_value = mock_observed

    mock_observation.local_ngc.get_skyfield_object.return_value = mock_ngc_obj

    _plot_ngc_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        target_name="NGC 1976",  # Skip M42
    )

    # Should call add_patch once for NGC 224
    assert mock_ax.add_patch.call_count == 1
    assert mock_ax.annotate.call_count == 1


def test_plot_ngc_on_skymap_polar(mock_observation, mock_ax, mock_observer):
    ngc_data = pd.DataFrame(
        [
            {
                "NGC": "NGC 224",
                "Name": "Andromeda",
                "Size": 178.0,
                "MinAx": 63.0,
                "PosAng": 35.0,
                "Mag": 3.44,
                "Type": "Galaxy",
            }
        ]
    )
    mock_observation.get_visible_ngc.return_value = ngc_data
    mock_ngc_obj = MagicMock()
    mock_ngc_obj.dec = Angle(degrees=40.0)
    mock_observed = MagicMock()
    mock_observed.apparent.return_value.altaz.return_value = (
        Angle(degrees=45),
        Angle(degrees=180),
        Angle(degrees=0),
    )
    mock_observed.apparent.return_value.radec.return_value = (
        Angle(hours=1.0),
        Angle(degrees=40.0),
        Angle(degrees=0),
    )
    mock_observer.observe.return_value = mock_observed
    mock_observation.local_ngc.get_skyfield_object.return_value = mock_ngc_obj

    _plot_ngc_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=True,
        target_name="",
    )

    # In polar mode, it uses scatter and annotate
    assert mock_ax.scatter.call_count == 1
    assert mock_ax.annotate.call_count == 1


def test_plot_ngc_on_skymap_zoom_horizontal(mock_observation, mock_ax, mock_observer):
    # Setup for zoom
    target_object = MagicMock()
    target_object.ra = Angle(hours=1.0)
    target_object.dec = Angle(degrees=40.0)

    ngc_data = pd.DataFrame(
        [
            {
                "NGC": "NGC 224",
                "Name": "Andromeda",
                "RA": "00:42:44",
                "Dec": "+41:16:09",
                "Size": 178.0,
                "MinAx": 63.0,
                "PosAng": 35.0,
                "Mag": 3.44,
            }
        ]
    )
    mock_observation.local_ngc.objects = ngc_data

    mock_ngc_obj = MagicMock()
    mock_ngc_obj.dec = Angle(degrees=40.0)
    # Mock apply for vectorized separation calculation
    mock_observed_ngc = MagicMock()
    mock_observed_ngc.position.au = np.array([1.0, 0.05, 0.0])  # Close to target
    mock_observed_ngc.apparent.return_value.altaz.return_value = (
        Angle(degrees=45),
        Angle(degrees=180),
        Angle(degrees=0),
    )
    mock_observed_ngc.apparent.return_value.radec.return_value = (
        Angle(hours=1.0),
        Angle(degrees=40.0),
        Angle(degrees=0),
    )

    # Mocking for separation calculation
    mock_vectors = MagicMock()
    mock_observation.local_ngc.get_skyfield_object.side_effect = (
        lambda x: mock_ngc_obj if isinstance(x, pd.Series) else mock_vectors
    )
    mock_vectors.apply.return_value = pd.Series([mock_observed_ngc])

    mock_observed_target = MagicMock()
    mock_observed_target.position.au = np.array([1.0, 0.0, 0.0])

    # We need to control what observer.observe returns for different calls
    def observe_side_effect(obj):
        from skyfield.api import Star as SkyfieldStar

        if isinstance(obj, SkyfieldStar):
            return mock_observed_target
        return mock_observed_ngc

    mock_observer.observe.side_effect = observe_side_effect

    mock_observed_ngc.xyz.au = np.array([1.0, 0.05, 0.0])

    _plot_ngc_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        target_name="",
        zoom_deg=10.0,
        target_object=target_object,
        coordinate_system=CoordinateSystem.HORIZONTAL,
    )

    assert mock_ax.add_patch.call_count >= 1


def test_plot_ngc_on_skymap_zoom_equatorial(mock_observation, mock_ax, mock_observer):
    # Setup for zoom equatorial
    target_object = MagicMock()
    target_object.ra = Angle(hours=1.0)
    target_object.dec = Angle(degrees=40.0)

    ngc_data = pd.DataFrame(
        [
            {
                "NGC": "NGC 224",
                "Name": "Andromeda",
                "RA": "00:42:44",
                "Dec": "+41:16:09",
                "Size": 178.0,
                "MinAx": 63.0,
                "PosAng": 35.0,
                "Mag": 3.44,
            }
        ]
    )
    mock_observation.local_ngc.objects = ngc_data

    mock_ngc_obj = MagicMock()
    mock_ngc_obj.dec = Angle(degrees=40.0)
    mock_observed_ngc = MagicMock()
    mock_observed_ngc.position.au = np.array([1.0, 0.01, 0.0])
    mock_observed_ngc.apparent.return_value.altaz.return_value = (
        Angle(degrees=45),
        Angle(degrees=180),
        Angle(degrees=0),
    )
    mock_observed_ngc.apparent.return_value.radec.return_value = (
        Angle(hours=1.0),
        Angle(degrees=40.0),
        Angle(degrees=0),
    )

    # Mocking for separation calculation
    mock_vectors = MagicMock()
    mock_observation.local_ngc.get_skyfield_object.side_effect = (
        lambda x: mock_ngc_obj if isinstance(x, pd.Series) else mock_vectors
    )
    mock_vectors.apply.return_value = pd.Series([mock_observed_ngc])

    mock_observed_target = MagicMock()
    mock_observed_target.position.au = np.array([1.0, 0.0, 0.0])

    def observe_side_effect(obj):
        from skyfield.api import Star as SkyfieldStar

        if isinstance(obj, SkyfieldStar):
            return mock_observed_target
        return mock_observed_ngc

    mock_observer.observe.side_effect = observe_side_effect

    mock_observed_ngc.xyz.au = np.array([1.0, 0.01, 0.0])

    _plot_ngc_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        target_name="",
        zoom_deg=5.0,
        target_object=target_object,
        coordinate_system=CoordinateSystem.EQUATORIAL,
    )

    assert mock_ax.add_patch.call_count >= 1


def test_plot_ngc_on_skymap_empty(mock_observation, mock_ax, mock_observer):
    mock_observation.get_visible_ngc.return_value = pd.DataFrame()

    _plot_ngc_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        target_name="",
    )

    assert mock_ax.add_patch.call_count == 0
