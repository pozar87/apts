import numpy as np
import pandas as pd
from skyfield.api import Star
from apts.cache import get_ephemeris, get_timescale
from apts.utils.astronomy import calculate_ecliptic_latitude_mask


def test_ecliptic_latitude_mask_accuracy():
    # Test array of coordinates across equatorial sky
    ra_hours = np.array([0.0, 6.0, 12.0, 18.0, 0.0, 6.0, 12.0, 18.0])
    dec_degrees = np.array([0.0, 23.439, 0.0, -23.439, 90.0, -90.0, 45.0, -45.0])

    ts = get_timescale()
    eph = get_ephemeris()
    earth = eph["earth"]
    t_ref = ts.utc(2024, 6, 1)

    # Reference calculation with Skyfield
    stars_vector = Star(ra_hours=ra_hours, dec_degrees=dec_degrees)
    spos = earth.at(t_ref).observe(stars_vector)
    lats_skyfield, _, _ = spos.ecliptic_latlon()

    # Fast geometric calculation
    mask_fast_10 = calculate_ecliptic_latitude_mask(
        ra_hours, dec_degrees, threshold_degrees=10.0
    )
    mask_skyfield_10 = np.abs(lats_skyfield.degrees) < 10.0

    # Masks must be identical
    np.testing.assert_array_equal(mask_fast_10, mask_skyfield_10)

    # Test with custom threshold (e.g., 7.0 degrees)
    mask_fast_7 = calculate_ecliptic_latitude_mask(
        ra_hours, dec_degrees, threshold_degrees=7.0
    )
    mask_skyfield_7 = np.abs(lats_skyfield.degrees) < 7.0
    np.testing.assert_array_equal(mask_fast_7, mask_skyfield_7)


def test_ecliptic_latitude_mask_with_dataframe_columns():
    ra_hours = np.array([0.0, 6.0, 12.0, 18.0])
    dec_degrees = np.array([0.0, 23.439, 0.0, -23.439])

    ra_rad = np.deg2rad(ra_hours * 15.0)
    dec_rad = np.deg2rad(dec_degrees)
    sin_dec = np.sin(dec_rad)
    cos_dec = np.cos(dec_rad)

    df = pd.DataFrame({
        "ra_hours": ra_hours,
        "dec_degrees": dec_degrees,
        "sin_dec": sin_dec,
        "cos_dec_sin_ra": cos_dec * np.sin(ra_rad),
    })

    mask_raw = calculate_ecliptic_latitude_mask(ra_hours, dec_degrees, threshold_degrees=10.0)
    mask_df = calculate_ecliptic_latitude_mask(ra_hours, dec_degrees, threshold_degrees=10.0, df=df)

    np.testing.assert_array_equal(mask_raw, mask_df)


def test_ecliptic_latitude_mask_boundary_cases():
    # Ecliptic equator object (RA=0, Dec=0 -> Ecliptic Lat = 0)
    ra = np.array([0.0])
    dec = np.array([0.0])
    mask = calculate_ecliptic_latitude_mask(ra, dec, threshold_degrees=1.0)
    assert mask[0]

    # Celestial pole (Dec = 90 -> Ecliptic Lat ~ 66.56 deg)
    ra_pole = np.array([0.0])
    dec_pole = np.array([90.0])
    mask_pole = calculate_ecliptic_latitude_mask(ra_pole, dec_pole, threshold_degrees=10.0)
    assert not mask_pole[0]
