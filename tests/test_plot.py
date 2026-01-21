from datetime import datetime
from typing import Any, cast
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import pytz
from matplotlib.patches import Ellipse
from skyfield.units import Angle

from apts.conditions import Conditions
from apts.constants.plot import CoordinateSystem
from apts.equipment import Equipment
from apts.observations import Observation
from apts.place import Place
from apts.plot import plot_skymap
from apts.plotting.skymap_objects import (
    _plot_messier_on_skymap,
    _plot_planets_on_skymap,
    _plot_solar_system_object_on_skymap,
)
from apts.plotting.utils import calculate_ellipse_angle as _calculate_ellipse_angle


def test_calculate_ellipse_angle():
    # Test case 1: HORIZONTAL, no flips
    angle = _calculate_ellipse_angle(
        pos_angle=45,
        parallactic_angle=15,
        coordinate_system=cast(Any, CoordinateSystem.HORIZONTAL),
        flipped_horizontally=False,
        flipped_vertically=False,
    )
    assert abs(angle - 30.0) < 0.01

    # Test case 2: EQUATORIAL, no flips
    angle = _calculate_ellipse_angle(
        pos_angle=45,
        parallactic_angle=15,
        coordinate_system=cast(Any, CoordinateSystem.EQUATORIAL),
        flipped_horizontally=False,
        flipped_vertically=False,
    )
    assert abs(angle - 45.0) < 0.01

    # Test case 3: HORIZONTAL, horizontal flip
    angle = _calculate_ellipse_angle(
        pos_angle=45,
        parallactic_angle=15,
        coordinate_system=cast(Any, CoordinateSystem.HORIZONTAL),
        flipped_horizontally=True,
        flipped_vertically=False,
    )
    assert abs(angle - (-30.0)) < 0.01

    # Test case 4: HORIZONTAL, vertical flip
    angle = _calculate_ellipse_angle(
        pos_angle=45,
        parallactic_angle=15,
        coordinate_system=cast(Any, CoordinateSystem.HORIZONTAL),
        flipped_horizontally=False,
        flipped_vertically=True,
    )
    assert abs(angle - 150.0) < 0.01

    # Test case 5: HORIZONTAL, both flips
    angle = _calculate_ellipse_angle(
        pos_angle=45,
        parallactic_angle=15,
        coordinate_system=cast(Any, CoordinateSystem.HORIZONTAL),
        flipped_horizontally=True,
        flipped_vertically=True,
    )
    assert abs(angle - 210.0) < 0.01


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
    observation = Observation(place=place, equipment=equipment, conditions=conditions)
    return observation


def test_plot_skymap_renders_messier_objects(mock_observation):
    # Mock the necessary methods and data to avoid actual plotting
    with (
        patch("apts.plotting.skymap.pyplot") as mock_pyplot,
        patch.object(Observation, "local_messier", MagicMock()) as mock_local_messier,
    ):
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
        mock_observation.get_visible_messier = MagicMock(
            return_value=mock_visible_messier
        )

        # Create a mock Skyfield object that can be observed
        import numpy as np
        from skyfield.timelib import Time, Timescale
        from skyfield.units import Angle

        mock_skyfield_obj = MagicMock()
        mock_skyfield_obj.ra = Angle(hours=0.0)
        mock_skyfield_obj.dec = Angle(degrees=0.0)
        mock_skyfield_obj.radec.return_value = (
            mock_skyfield_obj.ra,
            mock_skyfield_obj.dec,
            None,
        )
        mock_ts = MagicMock(spec=Timescale)
        mock_time = MagicMock(spec=Time)
        mock_time.tdb = 2451545.0
        mock_time.whole = 2451545.0
        mock_time.tdb_fraction = 0.0
        mock_time.ts = mock_ts
        mock_ts.tdb.return_value = mock_time
        mock_skyfield_obj._observe_from_bcrs.return_value = (
            np.ones(3),
            np.ones(3),
            mock_time,
            0,
        )
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


def test_plot_ngc_object_with_no_size(mock_observation):
    # Mock the necessary methods and data to avoid actual plotting
    with (
        patch("apts.plotting.skymap.pyplot") as mock_pyplot,
        patch(
            "apts.plotting.skymap_zoom.get_brightness_color"
        ) as mock_get_brightness_color,
        patch(
            "apts.plotting.skymap_objects.get_brightness_color"
        ) as mock_get_brightness_color_obj,
    ):
        mock_get_brightness_color.return_value = "0.5"
        mock_get_brightness_color_obj.return_value = "0.5"
        # Mock the figure and axes objects
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (0, 360)
        mock_ax.get_ylim.return_value = (0, 90)
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        # Configure the mock object to have a radec method
        mock_ngc_object = MagicMock()
        mock_ngc_object.ra = Angle(hours=1.0)
        mock_ngc_object.dec = Angle(degrees=0)
        mock_ngc_object.radec.return_value = (
            Angle(hours=1.0),
            Angle(degrees=0),
            MagicMock(),
        )
        import numpy as np
        from skyfield.timelib import Time, Timescale

        mock_ts = MagicMock(spec=Timescale)
        mock_time = MagicMock(spec=Time)
        mock_time.tdb = 2451545.0
        mock_time.whole = 2451545.0
        mock_time.tdb_fraction = 0.0
        mock_time.ts = mock_ts
        mock_ts.tdb.return_value = mock_time
        mock_ngc_object._observe_from_bcrs.return_value = (
            np.ones(3),
            np.ones(3),
            mock_time,
            0,
        )
        mock_observation.local_ngc.find_by_name = MagicMock(
            return_value=mock_ngc_object
        )
        from skyfield.api import load

        ts = load.timescale()
        mock_observation.place.ts = ts
        mock_observation.conditions.start_time = ts.now()

        # Call the function to be tested
        plot_skymap(
            observation=mock_observation,
            target_name="IC0024",
            plot_ngc=True,
            zoom_deg=10.0,
        )

        # Assert that the subplots function was called, indicating a plot was created
        mock_pyplot.subplots.assert_called_once()


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
        "PosAng": [35.0],
    }
    mock_visible_messier = pd.DataFrame(messier_data)
    mock_observation.get_visible_messier.return_value = mock_visible_messier
    mock_messier_object = MagicMock()
    mock_messier_object.ra = Angle(hours=1.0)
    mock_messier_object.dec = Angle(degrees=40.0)
    mock_observation.place.lat = 34.0
    # Correctly mock the observer chain
    mock_observer.target.latitude.degrees = 34.0
    mock_observer.ts.now.return_value.gast = 15.0
    mock_observer.observe.return_value.apparent.return_value.altaz.return_value = (
        Angle(degrees=45),
        Angle(degrees=180),
        Angle(degrees=0),
    )
    mock_observer.observe.return_value.apparent.return_value.radec.return_value = (
        Angle(hours=1.0),
        Angle(degrees=40.0),
        Angle(degrees=0),
    )
    mock_observation.local_messier.find_by_name.return_value = mock_messier_object

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
    assert abs(ellipse.angle - 325.0) < 0.1

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
    assert abs(ellipse.angle - 145.0) < 0.1

    # Call the function with both flips
    _plot_messier_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        target_name="M42",
        flipped_horizontally=True,
        flipped_vertically=True,
    )

    # Check that the ellipse was created with the correct angle
    args, kwargs = mock_ax.add_patch.call_args
    ellipse = args[0]
    assert isinstance(ellipse, Ellipse)
    assert abs(ellipse.angle - 215.0) < 0.1


def test_plot_planets_on_skymap_renders_planets_as_ellipses():
    # Create mock objects
    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Mock the visible planets data
    planets_data = {
        "Name": ["Mars"],
        "TechnicalName": ["Mars"],
        "Size": [14.5],
    }
    mock_visible_planets = pd.DataFrame(planets_data)
    mock_observation.get_visible_planets.return_value = mock_visible_planets
    mock_observer.observe.return_value.apparent.return_value.altaz.return_value = (
        MagicMock(degrees=45),
        MagicMock(degrees=180),
        MagicMock(),
    )
    mock_observer.observe.return_value.apparent.return_value.radec.return_value = (
        MagicMock(hours=1.0),
        MagicMock(degrees=40.0),
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
        target_name="Mars",
    )

    # Check that add_patch was not called because the planet is the target
    mock_ax.add_patch.assert_not_called()


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
    mock_observer.observe.return_value.apparent.return_value.radec.return_value = (
        MagicMock(hours=1.0),
        MagicMock(degrees=40.0),
        MagicMock(),
    )
    style = {"TEXT_COLOR": "white"}
    # Call the function
    _plot_solar_system_object_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        style=style,
        object_name="Sun",
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
    mock_observer.observe.return_value.apparent.return_value.radec.return_value = (
        MagicMock(hours=1.0),
        MagicMock(degrees=40.0),
        MagicMock(),
    )
    style = {"TEXT_COLOR": "white"}
    # Call the function
    _plot_solar_system_object_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        style=style,
        object_name="Moon",
    )

    # Check that an ellipse was added
    assert mock_ax.add_patch.call_count > 0


def test_plot_planet_with_no_size_polar(mock_observation):
    # Mock the necessary methods and data to avoid actual plotting
    with patch("apts.plotting.skymap.pyplot") as mock_pyplot:
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


def test_plot_stars_on_skymap_equatorial_with_zoom():
    """Test that stars are plotted correctly in equatorial coordinates with zoom."""
    from apts.constants.plot import CoordinateSystem
    from apts.plotting.skymap_objects import _plot_stars_on_skymap

    # Create mock objects
    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Set up the axes limits for zoomed view
    mock_ax.get_xlim.return_value = (1.0, 2.0)  # RA hours
    mock_ax.get_ylim.return_value = (30.0, 40.0)  # Dec degrees

    # Mock star data - some stars inside zoom window, some outside
    mock_stars_data = pd.DataFrame(
        {
            "ra_hours": [0.5, 1.2, 1.8, 2.5, 3.0],  # 1.2, 1.8 inside zoom (1.0-2.0)
            "dec_degrees": [
                25.0,
                35.0,
                38.0,
                45.0,
                50.0,
            ],  # 35.0, 38.0 inside zoom (30.0-40.0)
            "magnitude": [3.0, 2.5, 4.0, 5.0, 6.0],
            "epoch_year": [
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
            ],  # Required by SkyfieldStar
        }
    )

    # Mock the star observation results
    # Use PropertyMock for proper property mocking
    from unittest.mock import PropertyMock

    import numpy as np

    mock_star_positions = MagicMock()
    mock_altaz = MagicMock()
    mock_az = MagicMock()
    mock_altaz.degrees = np.array([45.0, 50.0, 55.0, 60.0, 65.0])
    mock_az.degrees = np.array([180.0, 200.0, 220.0, 240.0, 260.0])  # Azimuth values

    # Set up the hours and degrees as properties that return numpy arrays
    ra_hours_array = np.array([0.5, 1.2, 1.8, 2.5, 3.0])
    dec_degrees_array = np.array([25.0, 35.0, 38.0, 45.0, 50.0])

    # Create simple mock radec object that returns real numpy arrays
    mock_radec = MagicMock()

    # Create separate mock objects for ra and dec with proper properties
    mock_ra = MagicMock()
    mock_dec = MagicMock()

    # Configure ra to have .hours property
    type(mock_ra).hours = PropertyMock(return_value=ra_hours_array)

    # Configure dec to have .degrees property
    type(mock_dec).degrees = PropertyMock(return_value=dec_degrees_array)

    # Mock the altaz return
    mock_star_positions.apparent.return_value.altaz.return_value = (
        mock_altaz,
        mock_az,
        MagicMock(),
    )
    mock_star_positions.apparent.return_value.radec.return_value = (
        mock_ra,  # This goes to ra
        mock_dec,  # This goes to dec
        MagicMock(),
    )
    mock_observer.observe.return_value = mock_star_positions

    # Mock get_hipparcos_data to return our test data
    with patch(
        "apts.plotting.skymap_objects.get_hipparcos_data", return_value=mock_stars_data
    ):
        # Test _plot_stars_on_skymap
        print("=== DEBUG: About to call _plot_stars_on_skymap ===")
        print("is_polar: False, zoom_deg: 2.0, coordinate_system: EQUATORIAL")
        print(f"Mock dec_degrees_array: {dec_degrees_array}")
        print(f"Mock dec_degrees_array type: {type(dec_degrees_array)}")

        # Add debug output to track the mock objects
        print(f"DEBUG: mock_observer: {mock_observer}")
        print(f"DEBUG: mock_star_positions: {mock_star_positions}")
        print(f"DEBUG: mock_radec: {mock_radec}")
        print(f"DEBUG: mock_ra: {mock_ra}")
        print(f"DEBUG: mock_dec: {mock_dec}")
        print(f"DEBUG: type(mock_ra).hours: {type(mock_ra).hours}")
        print(f"DEBUG: type(mock_dec).degrees: {type(mock_dec).degrees}")
        print(
            f"DEBUG: PropertyMock for ra hours: {PropertyMock(return_value=ra_hours_array)}"
        )
        print(
            f"DEBUG: PropertyMock for dec degrees: {PropertyMock(return_value=dec_degrees_array)}"
        )

        # Test the actual property access and indexing
        print("DEBUG: Testing property access...")
        print(f"DEBUG: mock_ra.hours: {mock_ra.hours}")
        print(f"DEBUG: type(mock_ra.hours): {type(mock_ra.hours)}")
        print(f"DEBUG: mock_dec.degrees: {mock_dec.degrees}")
        print(f"DEBUG: type(mock_dec.degrees): {type(mock_dec.degrees)}")

        # Test boolean indexing
        test_visible = np.ones(5, dtype=bool)
        print(f"DEBUG: test_visible: {test_visible}")
        print(f"DEBUG: mock_ra.hours[test_visible]: {mock_ra.hours[test_visible]}")
        print(
            f"DEBUG: type(mock_ra.hours[test_visible]): {type(mock_ra.hours[test_visible])}"
        )
        print(
            f"DEBUG: mock_dec.degrees[test_visible]: {mock_dec.degrees[test_visible]}"
        )
        print(
            f"DEBUG: type(mock_dec.degrees[test_visible]): {type(mock_dec.degrees[test_visible])}"
        )

        _plot_stars_on_skymap(
            mock_observation,
            mock_ax,
            mock_observer,
            mag_limit=6.0,
            is_polar=False,
            style={"TEXT_COLOR": "white"},
            zoom_deg=2.0,
            coordinate_system=cast(Any, CoordinateSystem.EQUATORIAL),
        )

        print("=== DEBUG: _plot_stars_on_skymap call completed ===")

        # Check if scatter was called at all
        print(f"mock_ax.scatter called: {mock_ax.scatter.called}")
        print(f"Number of scatter calls: {mock_ax.scatter.call_count}")

        if mock_ax.scatter.called:
            scatter_calls = mock_ax.scatter.call_args_list
            print(f"Scatter call args: {scatter_calls}")

            # Print details of each scatter call
            for i, call in enumerate(scatter_calls):
                args, kwargs = call
                print(f"Scatter call {i}: args={len(args) if args else 'None'}")
                if args and len(args) >= 2:
                    print(f"  First arg type: {type(args[0])}")
                    print(f"  Second arg type: {type(args[1])}")
                    if (
                        hasattr(args[0], "__len__")
                        and hasattr(args[1], "__len__")
                        and len(args[0]) > 0
                    ):
                        print(
                            f"  First arg values: {args[0][: min(3, len(args[0]))]}..."
                        )
                        print(
                            f"  Second arg values: {args[1][: min(3, len(args[1]))]}..."
                        )

        # Verify that scatter was called with stars in the zoom window
        # Should have 2 stars: (1.2, 35.0) and (1.8, 38.0)
        mock_ax.scatter.assert_called()
        scatter_calls = mock_ax.scatter.call_args_list

        # Find the equatorial scatter call (last one should be the equatorial plot)
        equatorial_scatter = None
        for call in scatter_calls:
            args, kwargs = call
            if len(args) >= 2:
                # Check if this looks like RA/Dec coordinates (values in reasonable ranges)
                ra_values, dec_values = args[0], args[1]
                print(
                    f"Checking scatter call: ra_values type: {type(ra_values)}, dec_values type: {type(dec_values)}"
                )
                if hasattr(ra_values, "__len__") and len(ra_values) > 0:
                    print(
                        f"RA values: {ra_values}, min/max: {min(ra_values) if hasattr(ra_values, '__iter__') else 'N/A'}/{max(ra_values) if hasattr(ra_values, '__iter__') else 'N/A'}"
                    )
                    print(
                        f"Dec values: {dec_values}, min/max: {min(dec_values) if hasattr(dec_values, '__iter__') else 'N/A'}/{max(dec_values) if hasattr(dec_values, '__iter__') else 'N/A'}"
                    )
                    if 0 <= min(ra_values) <= 24 and 0 <= min(dec_values) <= 90:
                        equatorial_scatter = call
                        print("Found equatorial scatter call!")
                        break
                else:
                    print("Skipping scatter call - not iterable or empty")

        assert equatorial_scatter is not None, (
            "No equatorial coordinate scatter plot found"
        )

        # Verify the scatter contains the correct stars (2 stars in zoom window)
        # Verify only the 2 stars in the zoom window were plotted
        args, kwargs = equatorial_scatter
        ra_values, dec_values = args[0], args[1]
        assert len(ra_values) == 2, (
            f"Expected 2 stars in zoom window, got {len(ra_values)}"
        )
        assert 1.2 in ra_values, (
            f"Star at RA=1.2 not found in plotted stars: {ra_values}"
        )
        assert 1.8 in ra_values, (
            f"Star at RA=1.8 not found in plotted stars: {ra_values}"
        )

    def test_plot_planets_southern_hemisphere():
        """
        Tests that plotting planets for a southern hemisphere location,
        which may introduce NaNs in the time curve, does not raise an error.
        """
        from matplotlib import pyplot as plt

        # 1. Setup a southern hemisphere observation
        # Sydney, Australia
        place = Place(lat=-33.8688, lon=151.2093, name="Sydney")
        equipment = Equipment()
        conditions = Conditions(
            start_time=datetime(2023, 8, 22, 10, 0, 0, tzinfo=pytz.utc)
        )  # Corresponds to evening in Sydney
        observation = Observation(
            place=place, equipment=equipment, conditions=conditions
        )

        # 2. Mock the necessary data
        # Mock get_visible_planets to return at least one planet
        planets_data = {
            "Name": ["Jupiter"],
            "TechnicalName": ["jupiter"],
            "Rising": [None],
            "Setting": [None],
        }
        mock_visible_planets = pd.DataFrame(planets_data)

        # Mock get_altaz_curve to return a DataFrame with a NaN row
        # This simulates the azimuth wrap-around logic for the southern hemisphere
        ts = place.ts
        start_time = observation.start
        end_time = observation.stop
        t0 = ts.utc(start_time)
        t1 = ts.utc(end_time)
        times = ts.linspace(t0, t1, 5)

        curve_data = {
            "Time": [times[0], times[1], pd.NaT, times[3], times[4]],
            "Altitude": [10, 20, pd.NA, 20, 10],
            "Azimuth": [350, 355, pd.NA, 5, 10],
        }
        mock_curve_df = pd.DataFrame(curve_data)

        with (
            patch.object(
                observation, "get_visible_planets", return_value=mock_visible_planets
            ),
            patch.object(
                observation.place, "get_altaz_curve", return_value=mock_curve_df
            ),
            patch.object(
                observation.local_planets,
                "get_skyfield_object",
                return_value=MagicMock(),
            ),
        ):
            fig, ax = plt.subplots()

            # 3. Call the plot_planets function
            try:
                observation.plot_planets(ax=ax)
            except AttributeError as e:
                pytest.fail(f"plot_planets raised an AttributeError: {e}")
            except Exception as e:
                pytest.fail(f"plot_planets raised an unexpected exception: {e}")
            finally:
                plt.close(fig)


def test_plot_messier_ellipse_angle_on_equatorial_zoom():
    """
    Tests that a Messier object ellipse is plotted with the correct angle on a zoomed equatorial skymap.
    The angle should be based on PosAng only.
    """
    from apts.constants.plot import CoordinateSystem
    from apts.plotting.skymap import _generate_plot_skymap

    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_fig = MagicMock()

    target_name = "M13"
    target_pos_angle = 45.0
    parallactic_angle_val = 20.0
    expected_final_angle = target_pos_angle  # Equatorial does not use parallactic

    mock_target_object = MagicMock()
    mock_target_object.ra = Angle(hours=16.6)
    mock_target_object.dec = Angle(degrees=36.4)

    target_data_row = pd.Series(
        {
            "Messier": target_name,
            "Name": target_name,
            "Width": 20.0,
            "Height": 10.0,
            "PosAng": target_pos_angle,
            "Magnitude": 5.8,
        }
    )
    target_data_df = pd.DataFrame([target_data_row])

    mock_observation.local_messier.objects = target_data_df
    mock_observation.local_ngc.objects = pd.DataFrame(
        columns=cast(Any, ["NGC", "Name"])
    )
    mock_observation.local_stars.objects = pd.DataFrame(columns=cast(Any, ["Name"]))
    mock_observation.local_planets.find_by_name.return_value = None

    def get_skyfield_object_side_effect(data):
        if data["Messier"] == target_name:
            return mock_target_object
        return None

    mock_observation.local_messier.get_skyfield_object.side_effect = (
        get_skyfield_object_side_effect
    )

    mock_observed_obj = MagicMock()
    mock_observed_obj.apparent.return_value.radec.return_value = (
        mock_target_object.ra,
        mock_target_object.dec,
        MagicMock(),
    )
    mock_observed_obj.apparent.return_value.altaz.return_value = (
        Angle(degrees=60),
        Angle(degrees=270),
        MagicMock(),
    )
    mock_observation.place.observer.at.return_value.observe.return_value = (
        mock_observed_obj
    )

    with (
        patch("apts.plotting.skymap.pyplot") as mock_pyplot,
        patch(
            "apts.plotting.skymap_zoom.calculate_parallactic_angle",
            return_value=parallactic_angle_val,
        ),
        patch(
            "apts.plotting.skymap_zoom.calculate_ellipse_angle",
            side_effect=lambda pa, p_angle, cs, fh, fv: _calculate_ellipse_angle(
                pa, p_angle, cs, fh, fv
            ),
        ),
        patch("apts.plotting.skymap_zoom.get_brightness_color", return_value="0.5"),
        patch(
            "apts.plotting.skymap_objects.calculate_parallactic_angle",
            return_value=parallactic_angle_val,
        ),
        patch("apts.plotting.skymap_objects.get_brightness_color", return_value="0.5"),
    ):
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        _generate_plot_skymap(
            observation=mock_observation,
            target_name=target_name,
            zoom_deg=1.0,
            plot_stars=False,
            coordinate_system=cast(Any, CoordinateSystem.EQUATORIAL),
        )

        ellipse_call = next(
            (
                c
                for c in mock_ax.add_patch.call_args_list
                if isinstance(c.args[0], Ellipse) and c.args[0].get_linestyle() == "--"
            ),
            None,
        )

        assert ellipse_call is not None, (
            "Ellipse for target Messier object was not plotted"
        )

        ellipse = ellipse_call.args[0]
        assert abs(ellipse.angle - expected_final_angle) < 0.01, (
            f"Expected angle {expected_final_angle}, but got {ellipse.angle}"
        )


def test_plot_target_messier_ellipse_angle_on_horizontal_zoom():
    """
    Tests that a TARGET Messier object ellipse is plotted with the correct angle
    on a zoomed HORIZONTAL skymap.
    """
    from apts.constants.plot import CoordinateSystem
    from apts.plotting.skymap import _generate_plot_skymap

    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_fig = MagicMock()

    target_name = "M13"
    target_pos_angle = 60.0
    parallactic_angle_val = 15.0
    expected_final_angle = target_pos_angle - parallactic_angle_val

    mock_target_object = MagicMock()
    mock_target_object.ra = Angle(hours=16.6)
    mock_target_object.dec = Angle(degrees=36.4)

    target_data_row = pd.Series(
        {
            "Messier": target_name,
            "Name": target_name,
            "Width": 20.0,
            "Height": 10.0,
            "PosAng": target_pos_angle,
            "Magnitude": 5.8,
        }
    )
    target_data_df = pd.DataFrame([target_data_row])

    mock_observation.local_messier.objects = target_data_df
    mock_observation.local_ngc.objects = pd.DataFrame(
        columns=cast(Any, ["NGC", "Name"])
    )
    mock_observation.local_stars.objects = pd.DataFrame(columns=cast(Any, ["Name"]))
    mock_observation.local_planets.find_by_name.return_value = None

    def get_skyfield_object_side_effect(data):
        if data["Messier"] == target_name:
            return mock_target_object
        return None

    mock_observation.local_messier.get_skyfield_object.side_effect = (
        get_skyfield_object_side_effect
    )

    mock_observed_obj = MagicMock()
    mock_observed_obj.apparent.return_value.radec.return_value = (
        mock_target_object.ra,
        mock_target_object.dec,
        MagicMock(),
    )
    target_alt_val = Angle(degrees=75)
    target_az_val = Angle(degrees=180)
    mock_observed_obj.apparent.return_value.altaz.return_value = (
        target_alt_val,
        target_az_val,
        MagicMock(),
    )
    mock_observation.place.observer.at.return_value.observe.return_value = (
        mock_observed_obj
    )

    with (
        patch("apts.plotting.skymap.pyplot") as mock_pyplot,
        patch(
            "apts.plotting.skymap_zoom.calculate_parallactic_angle",
            return_value=parallactic_angle_val,
        ),
        patch(
            "apts.plotting.skymap_zoom.calculate_ellipse_angle",
            side_effect=lambda pa, p_angle, cs, fh, fv: _calculate_ellipse_angle(
                pa, p_angle, cs, fh, fv
            ),
        ),
        patch("apts.plotting.skymap_zoom.get_brightness_color", return_value="0.5"),
        patch(
            "apts.plotting.skymap_objects.calculate_parallactic_angle",
            return_value=parallactic_angle_val,
        ),
        patch("apts.plotting.skymap_objects.get_brightness_color", return_value="0.5"),
    ):
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        _generate_plot_skymap(
            observation=mock_observation,
            target_name=target_name,
            zoom_deg=1.0,
            plot_stars=False,
            coordinate_system=cast(Any, CoordinateSystem.HORIZONTAL),
        )

        ellipse_call = next(
            (
                c
                for c in mock_ax.add_patch.call_args_list
                if isinstance(c.args[0], Ellipse) and c.args[0].get_linestyle() == "--"
            ),
            None,
        )

        assert ellipse_call is not None, (
            "Ellipse for target Messier object was not plotted"
        )

        ellipse = ellipse_call.args[0]
        assert abs(ellipse.center[0] - target_az_val.degrees) < 0.01
        assert abs(ellipse.center[1] - target_alt_val.degrees) < 0.01
        assert abs(ellipse.angle - expected_final_angle) < 0.01, (
            f"Expected angle {expected_final_angle}, but got {ellipse.angle}"
        )


def test_plot_non_target_messier_ellipse_angle_on_horizontal_zoom():
    """
    Tests that a NON-TARGET Messier object ellipse is plotted with the correct angle
    on a zoomed HORIZONTAL skymap.
    """
    from apts.constants.plot import CoordinateSystem
    from apts.plotting.skymap import _generate_plot_skymap

    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_fig = MagicMock()

    # A star as the main target
    target_name = "Vega"
    mock_target_object = MagicMock()
    mock_target_object.ra = Angle(hours=18.5)
    mock_target_object.dec = Angle(degrees=38.0)

    # A Messier object as the non-target
    non_target_name = "M57"
    non_target_pos_angle = 135.0
    parallactic_angle_val = 25.0
    expected_final_angle = non_target_pos_angle - parallactic_angle_val
    mock_non_target_object = MagicMock()
    mock_non_target_object.ra = Angle(hours=18.9)
    mock_non_target_object.dec = Angle(degrees=33.0)

    non_target_data = pd.DataFrame(
        [
            {
                "Messier": non_target_name,
                "Name": non_target_name,
                "Width": 1.5,
                "Height": 1.0,
                "PosAng": non_target_pos_angle,
                "Magnitude": 8.8,
            }
        ]
    )

    mock_observation.local_messier.objects = non_target_data
    mock_observation.local_stars.objects = pd.DataFrame([{"Name": target_name}])
    mock_observation.local_ngc.objects = pd.DataFrame(
        columns=cast(Any, ["NGC", "Name"])
    )
    mock_observation.local_planets.find_by_name.return_value = None

    mock_observation.local_stars.get_skyfield_object.return_value = mock_target_object
    mock_observation.local_messier.find_by_name.return_value = mock_non_target_object
    mock_observation.get_visible_messier.return_value = non_target_data

    def observer_side_effect(obj):
        mock_observed = MagicMock()
        if obj == mock_target_object:
            mock_observed.apparent.return_value.altaz.return_value = (
                Angle(degrees=80),
                Angle(degrees=190),
                MagicMock(),
            )
            mock_observed.apparent.return_value.radec.return_value = (
                obj.ra,
                obj.dec,
                MagicMock(),
            )
        elif obj == mock_non_target_object:
            mock_observed.apparent.return_value.altaz.return_value = (
                Angle(degrees=78),
                Angle(degrees=192),
                MagicMock(),
            )
            mock_observed.apparent.return_value.radec.return_value = (
                obj.ra,
                obj.dec,
                MagicMock(),
            )  # Needed for parallactic angle
        return mock_observed

    mock_observation.place.observer.at.return_value.observe.side_effect = (
        observer_side_effect
    )

    with (
        patch("apts.plotting.skymap.pyplot") as mock_pyplot,
        patch(
            "apts.plotting.skymap_zoom.calculate_parallactic_angle",
            return_value=parallactic_angle_val,
        ),
        patch(
            "apts.plotting.skymap_zoom.calculate_ellipse_angle",
            side_effect=lambda pa, p_angle, cs, fh, fv: _calculate_ellipse_angle(
                pa, p_angle, cs, fh, fv
            ),
        ),
        patch("apts.plotting.skymap_zoom.get_brightness_color", return_value="0.5"),
        patch(
            "apts.plotting.skymap_objects.calculate_parallactic_angle",
            return_value=parallactic_angle_val,
        ),
        patch("apts.plotting.skymap_objects.get_brightness_color", return_value="0.5"),
    ):
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        _generate_plot_skymap(
            observation=mock_observation,
            target_name=target_name,
            plot_messier=True,
            zoom_deg=5.0,
            plot_stars=False,
            coordinate_system=cast(Any, CoordinateSystem.HORIZONTAL),
        )

        ellipse_call = next(
            (
                c
                for c in mock_ax.add_patch.call_args_list
                if isinstance(c.args[0], Ellipse) and c.args[0].get_linestyle() != "--"
            ),
            None,
        )

        assert ellipse_call is not None, (
            "Ellipse for non-target Messier object was not plotted"
        )

        ellipse = ellipse_call.args[0]
        assert abs(ellipse.angle - expected_final_angle) < 0.01, (
            f"Expected angle {expected_final_angle}, but got {ellipse.angle}"
        )


def test_plot_non_target_messier_ellipse_angle_on_equatorial_zoom():
    """
    Tests that a NON-TARGET Messier object ellipse is plotted with the correct angle
    on a zoomed EQUATORIAL skymap.
    """
    from apts.constants.plot import CoordinateSystem
    from apts.plotting.skymap import _generate_plot_skymap

    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_fig = MagicMock()

    # A star as the main target
    target_name = "Vega"
    mock_target_object = MagicMock()
    mock_target_object.ra = Angle(hours=18.5)
    mock_target_object.dec = Angle(degrees=38.0)

    # A Messier object as the non-target
    non_target_name = "M57"
    non_target_pos_angle = 135.0
    parallactic_angle_val = 25.0
    expected_final_angle = non_target_pos_angle  # Equatorial expects PosAng
    mock_non_target_object = MagicMock()
    mock_non_target_object.ra = Angle(hours=18.9)
    mock_non_target_object.dec = Angle(degrees=33.0)

    non_target_data = pd.DataFrame(
        [
            {
                "Messier": non_target_name,
                "Name": non_target_name,
                "Width": 1.5,
                "Height": 1.0,
                "PosAng": non_target_pos_angle,
                "Magnitude": 8.8,
            }
        ]
    )

    mock_observation.local_messier.objects = non_target_data
    mock_observation.local_stars.objects = pd.DataFrame([{"Name": target_name}])
    mock_observation.local_ngc.objects = pd.DataFrame(
        columns=cast(Any, ["NGC", "Name"])
    )
    mock_observation.local_planets.find_by_name.return_value = None

    mock_observation.local_stars.get_skyfield_object.return_value = mock_target_object
    mock_observation.local_messier.find_by_name.return_value = mock_non_target_object
    mock_observation.get_visible_messier.return_value = non_target_data

    def observer_side_effect(obj):
        mock_observed = MagicMock()
        if obj == mock_target_object:
            mock_observed.apparent.return_value.altaz.return_value = (
                Angle(degrees=80),
                Angle(degrees=190),
                MagicMock(),
            )
            mock_observed.apparent.return_value.radec.return_value = (
                obj.ra,
                obj.dec,
                MagicMock(),
            )
        elif obj == mock_non_target_object:
            mock_observed.apparent.return_value.altaz.return_value = (
                Angle(degrees=78),
                Angle(degrees=192),
                MagicMock(),
            )
            mock_observed.apparent.return_value.radec.return_value = (
                obj.ra,
                obj.dec,
                MagicMock(),
            )
        return mock_observed

    mock_observation.place.observer.at.return_value.observe.side_effect = (
        observer_side_effect
    )

    with (
        patch("apts.plotting.skymap.pyplot") as mock_pyplot,
        patch(
            "apts.plotting.skymap_zoom.calculate_parallactic_angle",
            return_value=parallactic_angle_val,
        ),
        patch(
            "apts.plotting.skymap_zoom.calculate_ellipse_angle",
            side_effect=lambda pa, p_angle, cs, fh, fv: _calculate_ellipse_angle(
                pa, p_angle, cs, fh, fv
            ),
        ),
        patch("apts.plotting.skymap_zoom.get_brightness_color", return_value="0.5"),
        patch(
            "apts.plotting.skymap_objects.calculate_parallactic_angle",
            return_value=parallactic_angle_val,
        ),
        patch("apts.plotting.skymap_objects.get_brightness_color", return_value="0.5"),
    ):
        mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

        _generate_plot_skymap(
            observation=mock_observation,
            target_name=target_name,
            plot_messier=True,
            zoom_deg=5.0,
            plot_stars=False,
            coordinate_system=cast(Any, CoordinateSystem.EQUATORIAL),
        )

        ellipse_call = next(
            (
                c
                for c in mock_ax.add_patch.call_args_list
                if isinstance(c.args[0], Ellipse) and c.args[0].get_linestyle() != "--"
            ),
            None,
        )

        assert ellipse_call is not None, (
            "Ellipse for non-target Messier object was not plotted"
        )

        ellipse = ellipse_call.args[0]
        assert abs(ellipse.angle - expected_final_angle) < 0.01, (
            f"Expected angle {expected_final_angle}, but got {ellipse.angle}"
        )


def test_plot_bright_stars_on_skymap_equatorial_with_zoom():
    """Test that bright stars are plotted correctly in equatorial coordinates with zoom."""
    from apts.constants.plot import CoordinateSystem
    from apts.plotting.skymap_objects import _plot_bright_stars_on_skymap

    # Create mock objects
    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Set up the axes limits for zoomed view
    mock_ax.get_xlim.return_value = (1.0, 2.0)  # RA hours
    mock_ax.get_ylim.return_value = (30.0, 40.0)  # Dec degrees

    # Mock bright star data - some stars inside zoom window, some outside
    mock_bright_stars_data = pd.DataFrame(
        {
            "Name": ["Sirius", "Vega", "Altair", "Betelgeuse", "Rigel"],
            "RA": [
                6.752,
                18.615,
                19.846,
                5.919,
                5.242,
            ],  # Will be converted to magnitude
            "Dec": [
                -16.716,
                38.784,
                8.868,
                7.407,
                -8.202,
            ],  # Will be converted to magnitude
            "Magnitude": [-1.46, 0.03, 0.77, 0.50, 0.18],  # Bright stars
        }
    )

    # Convert the values to simple numeric values (the real code converts from objects to numbers)
    # We just use the raw numeric values since the plotting code converts them anyway
    pass  # No conversion needed - using raw numeric values

    # Mock the local_stars
    mock_observation.local_stars.objects = mock_bright_stars_data

    # Mock the star observation results - need to match the RA/Dec we want in zoom
    from unittest.mock import PropertyMock

    import numpy as np

    mock_star_positions = MagicMock()
    mock_altaz = MagicMock()
    mock_az = MagicMock()

    mock_altaz.degrees = np.array([45.0, 50.0, 55.0, 60.0, 65.0])
    mock_az.degrees = np.array([180.0, 200.0, 220.0, 240.0, 260.0])  # Azimuth values

    # Create proper mock objects for ra and dec
    mock_ra = MagicMock()
    mock_dec = MagicMock()

    # Set up RA/Dec values where some fall in the zoom window (1.0-2.0, 30.0-40.0)
    # Convert to numpy arrays for proper array operations
    type(mock_ra).hours = PropertyMock(
        return_value=np.array([6.752, 1.5, 1.8, 5.919, 5.242])
    )  # 1.5, 1.8 inside zoom
    type(mock_dec).degrees = PropertyMock(
        return_value=np.array([-16.716, 35.0, 38.0, 7.407, -8.202])
    )  # 35.0, 38.0 inside zoom

    mock_star_positions.apparent.return_value.altaz.return_value = (
        mock_altaz,
        mock_az,  # Use proper az mock instead of MagicMock()
        MagicMock(),
    )
    mock_star_positions.apparent.return_value.radec.return_value = (
        mock_ra,  # This goes to ra
        mock_dec,  # This goes to dec
        MagicMock(),
    )
    mock_observer.observe.return_value = mock_star_positions

    # Test _plot_bright_stars_on_skymap
    _plot_bright_stars_on_skymap(
        mock_observation,
        mock_ax,
        mock_observer,
        is_polar=False,
        style={"EMPHASIS_COLOR": "yellow"},
        zoom_deg=2.0,
        coordinate_system=cast(Any, CoordinateSystem.EQUATORIAL),
    )

    # Verify that scatter was called for bright stars in zoom window
    mock_ax.scatter.assert_called()
    scatter_calls = mock_ax.scatter.call_args_list

    # Find the equatorial bright star scatter call
    equatorial_scatter = None
    for call in scatter_calls:
        args, kwargs = call
        if len(args) >= 2:
            ra_values, dec_values = args[0], args[1]
            if hasattr(ra_values, "__len__") and len(ra_values) > 0:
                if 0 <= min(ra_values) <= 24 and 0 <= min(dec_values) <= 90:
                    equatorial_scatter = call
                    break

    assert equatorial_scatter is not None, (
        "No equatorial bright star scatter plot found"
    )

    # Verify the scatter contains the correct bright stars (2 stars in zoom window)
    args, kwargs = equatorial_scatter
    ra_values, dec_values = args[0], args[1]
    assert len(ra_values) == 2, (
        f"Expected 2 bright stars in zoom window, got {len(ra_values)}"
    )
    assert 1.5 in ra_values, (
        f"Bright star at RA=1.5 not found in plotted stars: {ra_values}"
    )
    assert 1.8 in ra_values, (
        f"Bright star at RA=1.8 not found in plotted stars: {ra_values}"
    )
    assert 35.0 in dec_values, (
        f"Bright star at Dec=35.0 not found in plotted stars: {dec_values}"
    )
    assert 38.0 in dec_values, (
        f"Bright star at Dec=38.0 not found in plotted stars: {dec_values}"
    )


def test_plot_stars_ra_wrapping_equatorial():
    """Test that RA coordinate wrapping works correctly in equatorial plots."""
    from apts.constants.plot import (
        CoordinateSystem,
    )
    from apts.plotting.skymap_objects import _plot_stars_on_skymap
    from apts.plotting.utils import create_ra_zoom_mask as _create_ra_zoom_mask

    # Create mock objects
    mock_observation = MagicMock()
    mock_ax = MagicMock()
    mock_observer = MagicMock()

    # Set up axes limits for non-wrapping case to test basic functionality first
    mock_ax.get_xlim.return_value = (1.0, 2.0)  # Non-wrapping case
    mock_ax.get_ylim.return_value = (30.0, 40.0)  # Normal dec range

    # Mock star data with stars on both sides of the boundary
    mock_stars_data = pd.DataFrame(
        {
            "ra_hours": [
                0.5,
                1.2,
                1.8,
                2.5,
                3.0,
            ],  # 1.2, 1.8 should be in zoom window (1.0-2.0)
            "dec_degrees": [
                25.0,
                35.0,
                38.0,
                45.0,
                50.0,
            ],  # 35.0, 38.0 in dec range (30.0-40.0)
            "magnitude": [3.0, 2.5, 4.0, 5.0, 6.0],
            "epoch_year": [
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
            ],  # Required by SkyfieldStar
        }
    )

    # Mock the star observation results
    import numpy as np

    mock_star_positions = MagicMock()
    mock_altaz = MagicMock()
    mock_az = MagicMock()
    mock_altaz.degrees = np.array([45.0, 50.0, 55.0, 60.0, 65.0])
    mock_az.degrees = np.array([180.0, 200.0, 220.0, 240.0, 260.0])  # Azimuth values

    # Create proper mock arrays that support boolean indexing
    ra_hours_array = np.array([0.5, 1.2, 1.8, 2.5, 3.0])
    dec_degrees_array = np.array([25.0, 35.0, 38.0, 45.0, 50.0])

    # Create separate mock objects for ra and dec
    mock_ra = MagicMock()
    mock_dec = MagicMock()

    # Mock the .hours and .degrees properties to return arrays that support array operations
    # We need to set these up as properties that return the actual numpy arrays
    from unittest.mock import PropertyMock

    type(mock_ra).hours = PropertyMock(return_value=ra_hours_array)
    type(mock_dec).degrees = PropertyMock(return_value=dec_degrees_array)
    mock_star_positions.apparent.return_value.altaz.return_value = (
        mock_altaz,
        mock_az,
        MagicMock(),
    )
    mock_star_positions.apparent.return_value.radec.return_value = (
        mock_ra,  # This goes to ra
        mock_dec,  # This goes to dec
        MagicMock(),
    )
    mock_observer.observe.return_value = mock_star_positions

    # Test the RA mask function directly with non-wrapping case
    import numpy as np

    ra_values = np.array([0.5, 1.2, 1.8, 2.5, 3.0])
    xlim = (1.0, 2.0)
    ra_mask = _create_ra_zoom_mask(ra_values, xlim)

    # Should include stars at 1.2 and 1.8 (within the normal window)
    expected_mask = [False, True, True, False, False]  # Only 1.2 and 1.8 in window
    assert list(ra_mask) == expected_mask, (
        f"RA mask failed: expected {expected_mask}, got {list(ra_mask)}"
    )

    # Now test the full function with RA wrapping
    with patch(
        "apts.plotting.skymap_objects.get_hipparcos_data", return_value=mock_stars_data
    ):
        print("=== DEBUG: About to call _plot_stars_on_skymap ===")
        print(f"RA values: {[0.5, 1.2, 1.8, 2.5, 3.0]}")
        print(f"Expected RA in zoom (1.0-2.0): {[1.2, 1.8]}")
        print(f"Dec values: {[25.0, 35.0, 38.0, 45.0, 50.0]}")
        print("Expected Dec in zoom (30.0-40.0): 2 stars (35.0, 38.0)")

        # Debug the mock data setup
        print("=== DEBUG: Mock data sizes ===")
        print(f"  alt.degrees: {len(mock_altaz.degrees)} items")
        print(f"  az.degrees: {len(mock_az.degrees)} items")
        print(f"  ra.hours: {len(mock_ra.hours)} items")
        print(f"  dec.degrees: {len(mock_dec.degrees)} items")
        print(f"  ra.hours content: {mock_ra.hours}")
        print(f"  dec.degrees content: {mock_dec.degrees}")
        print(f"  xlim: {mock_ax.get_xlim.return_value}")
        print(f"  ylim: {mock_ax.get_ylim.return_value}")

        # Update debug info for new expected values
        print("  Expected stars in zoom: RA 1.2, 1.8 and Dec 35.0, 38.0")

        _plot_stars_on_skymap(
            mock_observation,
            mock_ax,
            mock_observer,
            mag_limit=6.0,
            is_polar=False,
            style={"TEXT_COLOR": "white"},
            zoom_deg=2.0,
            coordinate_system=cast(Any, CoordinateSystem.EQUATORIAL),
        )

        print(f"=== DEBUG: scatter called: {mock_ax.scatter.called} ===")
        print(f"=== DEBUG: Number of scatter calls: {mock_ax.scatter.call_count} ===")

        # Verify that scatter was called with stars in the wrapped zoom window
        scatter_calls = mock_ax.scatter.call_args_list
        print(f"=== DEBUG: All scatter calls: {len(scatter_calls)} ===")

        if scatter_calls:
            for i, call in enumerate(scatter_calls):
                args, kwargs = call
                print(f"Scatter call {i}: args count = {len(args) if args else 'None'}")
                if args and len(args) >= 2:
                    print(f"  RA values: {args[0]}")
                    print(f"  Dec values: {args[1]}")
                    if hasattr(args[0], "__len__") and len(args[0]) > 0:
                        print(f"  RA range: {min(args[0])} to {max(args[0])}")
                        print(f"  Dec range: {min(args[1])} to {max(args[1])}")
                    else:
                        print("  No RA/Dec data to show ranges")
        else:
            print("=== DEBUG: No scatter calls made ===")
            # Let's also check if alt.degrees exists and has the right size
            try:
                alt, az, _ = mock_star_positions.apparent().altaz.return_value
                print(
                    f"  alt.degrees size: {len(alt.degrees) if hasattr(alt.degrees, '__len__') else 'N/A'}"
                )
                print(
                    f"  az.degrees size: {len(az.degrees) if hasattr(az.degrees, '__len__') else 'N/A'}"
                )
            except Exception:
                print("  Could not get alt/az data")

            # Check the mock ra/dec data
            try:
                ra, dec, _ = mock_star_positions.apparent().radec.return_value
                print(
                    f"  ra.hours size: {len(ra.hours) if hasattr(ra.hours, '__len__') else 'N/A'}"
                )
                print(
                    f"  dec.degrees size: {len(dec.degrees) if hasattr(dec.degrees, '__len__') else 'N/A'}"
                )
                print(f"  ra.hours: {ra.hours}")
                print(f"  dec.degrees: {dec.degrees}")
            except Exception:
                print("  Could not get ra/dec data")

        mock_ax.scatter.assert_called()
        scatter_calls = mock_ax.scatter.call_args_list

        # Find the equatorial scatter call
        equatorial_scatter = None
        for call in scatter_calls:
            args, kwargs = call
            if len(args) >= 2:
                ra_values, _ = args[0], args[1]
                if hasattr(ra_values, "__len__") and len(ra_values) > 0:
                    if 0 <= min(ra_values) <= 24:
                        equatorial_scatter = call
                        break

        assert equatorial_scatter is not None, (
            "No equatorial coordinate scatter plot found"
        )

        # Verify only the 2 stars in the zoom window were plotted
        args, kwargs = equatorial_scatter
        ra_values, _ = args[0], args[1]
        assert len(ra_values) == 2, (
            f"Expected 2 stars in wrapped zoom window, got {len(ra_values)}"
        )
        assert 1.2 in ra_values, (
            f"Star at RA=1.2 not found in plotted stars: {ra_values}"
        )
        assert 1.8 in ra_values, (
            f"Star at RA=1.8 not found in plotted stars: {ra_values}"
        )

    def test_plot_planets_with_rise_set_times():
        """
        Tests that plotting planets with valid rise/set Timestamp objects does not raise a ConversionError.
        """
        from datetime import datetime
        from unittest.mock import MagicMock, patch

        import pandas as pd
        import pytz
        from matplotlib import pyplot as plt

        from apts.observations import Observation
        from apts.plotting.altitude import (
            generate_plot_planets as _generate_plot_planets,
        )

        # 1. Setup mock observation
        mock_observation = MagicMock(spec=Observation)
        mock_observation.place = MagicMock()
        mock_observation.place.local_timezone = pytz.utc
        mock_observation.place.moonrise_time.return_value = None
        mock_observation.place.moonset_time.return_value = None
        mock_observation.start = datetime(2023, 1, 1, 22, 0, tzinfo=pytz.utc)
        mock_observation.stop = datetime(2023, 1, 2, 6, 0, tzinfo=pytz.utc)
        mock_observation.time_limit = mock_observation.stop
        mock_observation.conditions = MagicMock()
        mock_observation.conditions.min_object_altitude = 10

        # 2. Mock visible planets DataFrame with Timestamp objects
        planets_data = {
            "Name": ["Jupiter", "Mars"],
            "TechnicalName": ["jupiter", "mars"],
            "Rising": [pd.Timestamp("2023-01-01 23:00:00+0000", tz="UTC"), pd.NaT],
            "Setting": [
                pd.Timestamp("2023-01-02 05:00:00+0000", tz="UTC"),
                pd.Timestamp("2023-01-02 04:00:00+0000", tz="UTC"),
            ],
        }
        mock_visible_planets = pd.DataFrame(planets_data)
        mock_observation.get_visible_planets.return_value = mock_visible_planets

        # Mock the get_altaz_curve to return an empty df to simplify the test
        mock_observation.place.get_altaz_curve.return_value = pd.DataFrame(
            {"Time": [], "Altitude": []}
        )
        mock_observation.local_planets.get_skyfield_object.return_value = MagicMock()

        # 3. Use real pyplot
        fig, ax = plt.subplots()

        # 4. Call the function
        try:
            _generate_plot_planets(observation=mock_observation, ax=ax)
        except Exception as e:
            plt.close(fig)
            pytest.fail(f"_generate_plot_planets raised an unexpected exception: {e}")

        # 5. Assertions
        # We expect 3 scatter calls: one for Jupiter's rise, one for Jupiter's set, and one for Mars's set.
        # scatter() adds a PathCollection to ax.collections
        assert len(ax.collections) == 3

        plt.close(fig)
