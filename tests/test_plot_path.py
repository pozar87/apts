from unittest.mock import MagicMock, patch

from apts.plot import plot_sun_and_moon_path


def test_plot_sun_and_moon_path_sun():
    mock_observation = MagicMock()
    mock_observation.sun_observation = True
    with patch.object(
        mock_observation.place, "plot_sun_path"
    ) as mock_plot_sun_path:
        plot_sun_and_moon_path(mock_observation)
        mock_plot_sun_path.assert_called_once()


def test_plot_sun_and_moon_path_moon():
    mock_observation = MagicMock()
    mock_observation.sun_observation = False
    with patch.object(
        mock_observation.place, "plot_moon_path"
    ) as mock_plot_moon_path:
        plot_sun_and_moon_path(mock_observation)
        mock_plot_moon_path.assert_called_once()
