import unittest
from typing import cast

import numpy as np
import pandas as pd
import pytz

from apts.cache import get_timescale
from apts.utils.astronomy import (
    calculate_refraction,
    vectorized_angular_separation,
    vectorized_geometric_altaz,
    vectorized_geometric_compute,
    vectorized_geometric_imaging_duration,
)


class TestAstronomyPackage(unittest.TestCase):
    def test_calculate_refraction(self):
        # Above -1 deg, it should return positive refraction
        ref_45 = calculate_refraction(45.0)
        self.assertGreater(ref_45, 0.0)
        self.assertLess(ref_45, 1.0)

        # Below -1 deg, refraction should be 0.0 to prevent instability
        ref_minus_2 = calculate_refraction(-2.0)
        self.assertEqual(ref_minus_2, 0.0)

        # Vectorized input
        alts = np.array([45.0, -2.0])
        refs = np.atleast_1d(calculate_refraction(alts))
        self.assertGreater(refs[0], 0.0)
        self.assertEqual(refs[1], 0.0)

    def test_vectorized_geometric_altaz(self):
        lat_deg = 52.2297  # Warsaw
        lon_decimal = 21.0122
        ras = np.array([12.0])  # RA in hours
        decs = np.array([45.0])  # Dec in degrees
        check_times_gmst = 12.0  # GMST in hours

        alt, az = vectorized_geometric_altaz(
            lat_deg, lon_decimal, ras, decs, check_times_gmst
        )
        self.assertIsInstance(alt, np.ndarray)
        self.assertIsInstance(az, np.ndarray)
        self.assertEqual(alt.shape, (1,))
        self.assertEqual(cast(np.ndarray, az).shape, (1,))

    def test_vectorized_geometric_altaz_partial_precomputed(self):
        """A partial precomputed set (e.g. only sin_dec) must fall back to recomputation."""
        lat_deg = 52.2297  # Warsaw
        lon_decimal = 21.0122
        ras = np.array([10.0, 12.0])  # RA in hours
        decs = np.array([40.0, 45.0])  # Dec in degrees

        dec_rad = np.deg2rad(decs)
        sin_dec_only = np.sin(dec_rad)

        # Scalar time: partial input must fall back to recomputation
        alt_ref, az_ref = vectorized_geometric_altaz(
            lat_deg, lon_decimal, ras, decs, 12.0
        )
        alt_partial, az_partial = vectorized_geometric_altaz(
            lat_deg, lon_decimal, ras, decs, 12.0, sin_dec=sin_dec_only
        )
        np.testing.assert_allclose(alt_partial, alt_ref)
        np.testing.assert_allclose(
            cast(np.ndarray, az_partial), cast(np.ndarray, az_ref)
        )

        # Multi-time: partial input must fall back to recomputation
        alt_ref, az_ref = vectorized_geometric_altaz(
            lat_deg, lon_decimal, ras, decs, np.array([12.0, 13.0])
        )
        alt_partial, az_partial = vectorized_geometric_altaz(
            lat_deg,
            lon_decimal,
            ras,
            decs,
            np.array([12.0, 13.0]),
            sin_dec=sin_dec_only,
        )
        np.testing.assert_allclose(alt_partial, alt_ref)
        np.testing.assert_allclose(
            cast(np.ndarray, az_partial), cast(np.ndarray, az_ref)
        )

    def test_vectorized_angular_separation(self):
        # Same coordinates should have 0 separation
        sep = vectorized_angular_separation(12.0, 45.0, 12.0, 45.0)
        self.assertAlmostEqual(cast(float, sep), 0.0, places=4)

        # Different coordinates
        sep_diff = vectorized_angular_separation(12.0, 45.0, 13.0, 45.0)
        self.assertGreater(sep_diff, 0.0)

    def test_vectorized_geometric_compute(self):
        ts = get_timescale()
        lat_deg = 52.2297
        lon_decimal = 21.0122
        local_timezone = pytz.timezone("Europe/Warsaw")

        # Set up a specific date
        observer_date = ts.utc(2023, 11, 28, 12, 0, 0)

        ras = np.array([12.0])
        decs = np.array([45.0])
        valid_mask = np.array([True])

        transits, alts, rises, sets = vectorized_geometric_compute(
            ts,
            lat_deg,
            lon_decimal,
            local_timezone,
            observer_date,
            ras,
            decs,
            valid_mask,
            df_len=1,
        )

        self.assertEqual(len(transits), 1)
        self.assertEqual(len(alts), 1)
        self.assertEqual(len(rises), 1)
        self.assertEqual(len(sets), 1)
        self.assertIsNotNone(transits[0])
        self.assertGreater(alts[0], 0.0)

    def test_vectorized_geometric_imaging_duration(self):
        lat_deg = 52.2297
        ras = np.array([12.0])
        decs = np.array([45.0])
        valid_mask = np.array([True])

        # Setting transit, dark start, dark end
        local_timezone = pytz.timezone("Europe/Warsaw")
        transit_time = pd.Timestamp("2023-11-28 20:00:00", tz=local_timezone)
        transits = pd.Series([transit_time])

        dark_start = pd.Timestamp("2023-11-28 18:00:00", tz=local_timezone)
        dark_end = pd.Timestamp("2023-11-29 06:00:00", tz=local_timezone)

        durations = vectorized_geometric_imaging_duration(
            lat_deg,
            ras,
            decs,
            valid_mask,
            transits,
            dark_start,
            dark_end,
            min_altitude=30.0,
        )

        self.assertEqual(len(durations), 1)
        self.assertGreater(durations[0], 0.0)


if __name__ == "__main__":
    unittest.main()
