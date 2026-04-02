from unittest.mock import MagicMock, patch

from apts.plot import plot_sun_and_moon_path


@patch("apts.plotting.path.generate_plot_sun_path")
def test_plot_sun_and_moon_path_sun(mock_generate_plot_sun_path):
    mock_observation = MagicMock()
    mock_observation.sun_observation = True
    plot_sun_and_moon_path(mock_observation)
    mock_generate_plot_sun_path.assert_called_once_with(mock_observation.place, None)


@patch("apts.plotting.path.generate_plot_moon_path")
def test_plot_sun_and_moon_path_moon(mock_generate_plot_moon_path):
    mock_observation = MagicMock()
    mock_observation.sun_observation = False
    plot_sun_and_moon_path(mock_observation)
    mock_generate_plot_moon_path.assert_called_once_with(mock_observation.place, None)
