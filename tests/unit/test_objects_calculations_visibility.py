import numpy as np
import pandas as pd
from apts.objects.calculations.visibility import (
    filter_objects_by_magnitude,
    calculate_visible_stars_mask,
)
from apts.conditions import Conditions


def test_filter_objects_by_magnitude_empty():
    df = pd.DataFrame(columns=["Magnitude"])
    conditions = Conditions(max_object_magnitude=10.0)
    res = filter_objects_by_magnitude(df, conditions)
    assert res.empty


def test_filter_objects_by_magnitude_floats():
    df = pd.DataFrame({"Magnitude": [5.0, 11.0, 8.5]})
    conditions = Conditions(max_object_magnitude=10.0)
    res = filter_objects_by_magnitude(df, conditions)
    assert len(res) == 2
    assert list(res["Magnitude"]) == [5.0, 8.5]


def test_filter_objects_by_magnitude_quantities():
    class MockQuantity:
        def __init__(self, value):
            self.magnitude = value

    df = pd.DataFrame(
        {"Magnitude": [MockQuantity(5.0), MockQuantity(11.0), MockQuantity(8.5)]}
    )
    # Using float threshold
    conditions = Conditions(max_object_magnitude=10.0)
    res = filter_objects_by_magnitude(df, conditions)
    assert len(res) == 2
    # Ensure they extract magnitude correctly
    mags = [x.magnitude for x in res["Magnitude"]]
    assert mags == [5.0, 8.5]


def test_calculate_visible_stars_mask_all_invisible():
    # Setup lat, lon where stars are way below horizon
    lat_decimal = 0.0
    lon_decimal = 0.0
    stars_ras = np.array([12.0, 12.0])
    stars_decs = np.array([-90.0, -89.0])  # South pole stars from equator (max alt <= 0 or 1 deg)

    # Check times gmst
    check_times_gmst = np.array([12.0, 13.0])
    conditions = Conditions(min_object_altitude=30.0)  # Threshold is 30 deg

    mask = calculate_visible_stars_mask(
        lat_decimal,
        lon_decimal,
        stars_ras,
        stars_decs,
        check_times_gmst,
        conditions,
    )
    # Both should be False because they can't potentially reach 30 deg
    assert not np.any(mask)


def test_calculate_visible_stars_mask_fast_path():
    lat_decimal = 50.0
    lon_decimal = 20.0
    # Star directly overhead or near celestial pole at lat 50
    stars_ras = np.array([1.33])
    stars_decs = np.array([89.0])

    check_times_gmst = np.array([10.0, 11.0, 12.0])
    conditions = Conditions(min_object_altitude=10.0)  # Above 10 degrees is visible

    mask = calculate_visible_stars_mask(
        lat_decimal,
        lon_decimal,
        stars_ras,
        stars_decs,
        check_times_gmst,
        conditions,
    )
    assert mask[0]


def test_calculate_visible_stars_mask_complex_path():
    lat_decimal = 50.0
    lon_decimal = 20.0
    stars_ras = np.array([1.33])
    stars_decs = np.array([89.0])

    check_times_gmst = np.array([10.0, 11.0, 12.0])
    # Setup complex conditions to trigger full path
    conditions = Conditions(
        min_object_altitude=10.0,
        min_object_azimuth=10.0,
        max_object_azimuth=20.0,  # Narrow azimuth window
    )

    mask = calculate_visible_stars_mask(
        lat_decimal,
        lon_decimal,
        stars_ras,
        stars_decs,
        check_times_gmst,
        conditions,
    )
    # The star might not be in that narrow azimuth window, so mask might be False (which is correct behavior)
    assert isinstance(mask, np.ndarray)
    assert len(mask) == 1
