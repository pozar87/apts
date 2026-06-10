"""Tests for skymap object filtering operations.

These tests guard against broadcasting errors when comparing target_name
(string from URL) against pandas/numpy arrays. The target_name can be
misinterpreted as a list-like sequence (e.g., "IC 434" has len=6) by
certain pandas/numpy comparison paths, causing:
  ValueError: Lengths of operands do not match
  ValueError: operands could not be broadcast together
"""

import unittest
from unittest.mock import MagicMock

import numpy
import pandas as pd

from apts.constants import ObjectTableLabels
from apts.plotting.skymap_objects.messier import _prepare_messier_data
from apts.plotting.skymap_objects.ngc import _get_ngc_plot_mask


class TestGetNgcPlotMask(unittest.TestCase):
    """Direct unit tests for _get_ngc_plot_mask.

    This function is self-contained: takes a DataFrame, a target_name
    string, a numpy array, and a bool. No mocking needed.
    """

    def setUp(self):
        # Build a minimal NGC-like DataFrame with names that mirror real data
        self.df = pd.DataFrame(
            {
                ObjectTableLabels.NGC: ["NGC 224", numpy.nan, "NGC 598", numpy.nan],
                ObjectTableLabels.NAME: ["M31", "IC 434", "M33", "NGC 7000"],
            }
        )
        self.altitudes = numpy.array([30.0, 15.0, -5.0, 45.0])

    def test_broadcast_safe_with_short_target_name(self):
        """Target name shorter than 6 chars should not cause broadcast errors.

        The NGC column takes priority via fillna(). Row 0 has NGC="NGC 224"
        (not NaN), so it is used instead of NAME="M31". Therefore no row
        matches "M31", and only the altitude filter applies.
        """
        mask, names = _get_ngc_plot_mask(
            self.df, "M31", self.altitudes, ignore_horizon=False
        )
        # No row matches "M31" (NGC column takes priority); alt <= 0 removes row 2
        expected = numpy.array([True, True, False, True])
        numpy.testing.assert_array_equal(mask, expected)

    def test_broadcast_safe_with_6char_ic_target_name(self):
        """Target name like 'IC 434' (6 chars) must not trigger broadcast errors."""
        mask, names = _get_ngc_plot_mask(
            self.df, "IC 434", self.altitudes, ignore_horizon=False
        )
        # IC 434 excluded; others above horizon remain
        expected = numpy.array([True, False, False, True])
        numpy.testing.assert_array_equal(mask, expected)

    def test_broadcast_safe_with_long_target_name(self):
        """Target name longer than 6 chars should work too."""
        mask, names = _get_ngc_plot_mask(
            self.df, "NGC 7000", self.altitudes, ignore_horizon=False
        )
        expected = numpy.array([True, True, False, False])
        numpy.testing.assert_array_equal(mask, expected)

    def test_ignore_horizon_keeps_all_above_zero(self):
        """When ignore_horizon is True, horizon check is skipped.

        No row matches "M31" since the NGC column takes priority, so all
        4 rows pass the name filter.
        """
        mask, names = _get_ngc_plot_mask(
            self.df, "M31", self.altitudes, ignore_horizon=True
        )
        expected = numpy.array([True, True, True, True])
        numpy.testing.assert_array_equal(mask, expected)

    def test_target_not_in_dataframe(self):
        """Target name not present in the DataFrame should not affect results."""
        mask, names = _get_ngc_plot_mask(
            self.df, "DoesNotExist", self.altitudes, ignore_horizon=False
        )
        expected = numpy.array([True, True, False, True])
        numpy.testing.assert_array_equal(mask, expected)

    def test_empty_dataframe(self):
        """Empty DataFrame should produce empty outputs."""
        empty_df = pd.DataFrame(columns=[ObjectTableLabels.NGC, ObjectTableLabels.NAME])
        mask, names = _get_ngc_plot_mask(
            empty_df, "IC 434", numpy.array([]), ignore_horizon=False
        )
        self.assertEqual(len(mask), 0)
        self.assertEqual(len(names), 0)

    def test_none_target_name_not_passed(self):
        """target_name=None is not passed in practice (the guard at line 212 checks 'if target_name:'), but
        the function annotation says 'str' so we only test with valid strings."""
        mask, names = _get_ngc_plot_mask(
            self.df, "IC 434", self.altitudes, ignore_horizon=True
        )
        self.assertEqual(len(mask), len(self.df))
        self.assertEqual(len(names), len(self.df))

    def test_various_name_patterns(self):
        """Test with various name patterns including IC numbers with different lengths."""
        df = pd.DataFrame(
            {
                ObjectTableLabels.NGC: [numpy.nan, numpy.nan, numpy.nan, numpy.nan],
                ObjectTableLabels.NAME: ["IC0001", "IC00434", "NGC1234", "M99"],
            }
        )
        alts = numpy.array([10.0, 20.0, 30.0, 40.0])

        mask, names = _get_ngc_plot_mask(df, "IC0001", alts, ignore_horizon=False)
        expected = numpy.array([False, True, True, True])
        numpy.testing.assert_array_equal(mask, expected)


class TestPrepareMessierData(unittest.TestCase):
    """Tests for _prepare_messier_data with mocked observation."""

    def setUp(self):
        self.base_messier_df = pd.DataFrame(
            {
                ObjectTableLabels.MESSIER: ["M31", "M42", "M45", "M57", "M81", "M101"],
                ObjectTableLabels.NAME: [
                    "Andromeda",
                    "Orion",
                    "Pleiades",
                    "Ring",
                    "Bode's",
                    "Pinwheel",
                ],
            }
        )
        self.empty_messier_df = pd.DataFrame(
            columns=[ObjectTableLabels.MESSIER, ObjectTableLabels.NAME]
        )

    def _make_mock_obs(self, visible_df):
        """Helper: create a mock observation that returns the given visible_messier."""
        obs = MagicMock()
        # Configure local_messier as a nested mock so obs.local_messier.objects works
        local_messier_mock = MagicMock()
        local_messier_mock.objects = visible_df
        obs.local_messier = local_messier_mock
        obs.get_visible_messier.return_value = visible_df
        return obs

    def test_filter_output_with_short_target(self):
        """Short target name 'M31' should be filtered out without error."""
        obs = self._make_mock_obs(self.base_messier_df)
        result = _prepare_messier_data(obs, "M31", ignore_horizon=False)
        self.assertNotIn("M31", result[ObjectTableLabels.MESSIER].values)
        self.assertEqual(len(result), 5)

    def test_filter_output_with_6char_ic_target(self):
        """A 6-character target name like 'IC 434' must not cause broadcast errors.
        Since 'IC 434' is not in the Messier catalog, all rows remain."""
        obs = self._make_mock_obs(self.base_messier_df)
        result = _prepare_messier_data(obs, "IC 434", ignore_horizon=False)
        self.assertEqual(len(result), 6)

    def test_filter_output_with_long_target(self):
        """Longer target name should not cause errors."""
        obs = self._make_mock_obs(self.base_messier_df)
        result = _prepare_messier_data(obs, "NGC 7000", ignore_horizon=False)
        self.assertEqual(len(result), 6)

    def test_empty_visible_messier(self):
        """Empty messier data should return empty DataFrame."""
        obs = self._make_mock_obs(self.empty_messier_df)
        result = _prepare_messier_data(obs, "IC 434", ignore_horizon=False)
        self.assertTrue(result.empty)

    def test_ignore_horizon_uses_local_messier(self):
        """When ignore_horizon is True, local_messier.objects is used."""
        obs = self._make_mock_obs(self.base_messier_df)

        result = _prepare_messier_data(obs, "M42", ignore_horizon=True)
        self.assertNotIn("M42", result[ObjectTableLabels.MESSIER].values)
        self.assertEqual(len(result), 5)


class TestBrightStarsFiltering(unittest.TestCase):
    """Tests for the bright stars filtering logic used in _plot_bright_stars_on_skymap."""

    def setUp(self):
        # Simulate the bright stars catalog Name column (StringDtype)
        self.star_df = pd.DataFrame(
            {
                "Name": pd.array(
                    [
                        "Sirius",
                        "Canopus",
                        "Rigil Kentaurus & Toliman",
                        "Arcturus",
                        "Vega",
                    ],
                    dtype="string",
                ),
            }
        )

    def test_filter_out_existing_star(self):
        """Filtering out a star that exists in the DataFrame should reduce its length."""
        filtered = self.star_df[~self.star_df["Name"].isin(["Sirius"])]
        self.assertEqual(len(filtered), 4)
        self.assertNotIn("Sirius", filtered["Name"].values)

    def test_filter_out_6char_name(self):
        """Filtering with a 6-character name that doesn't exist should keep all rows."""
        filtered = self.star_df[~self.star_df["Name"].isin(["IC 434"])]
        self.assertEqual(len(filtered), 5)

    def test_filter_out_ic_pattern(self):
        """Filtering with IC-prefixed names of varying lengths."""
        filtered = self.star_df[~self.star_df["Name"].isin(["IC0001"])]
        self.assertEqual(len(filtered), 5)

    def test_filter_out_long_name(self):
        """Filtering with long strings should not cause broadcast errors."""
        filtered = self.star_df[~self.star_df["Name"].isin(["NGC 7000"])]
        self.assertEqual(len(filtered), 5)

    def test_filter_out_multiple_no_match(self):
        """All stars remain when filtering for a non-existent name."""
        filtered = self.star_df[~self.star_df["Name"].isin(["NotAStar"])]
        self.assertEqual(len(filtered), 5)


class TestIsinBroadcastingSafety(unittest.TestCase):
    """Low-level tests to verify .isin() is immune to the broadcast errors
    that .__ne__() can trigger with certain pandas/numpy version interactions."""

    def test_stringarray_ne_with_6char_string_fails_on_some_configs(self):
        """Demonstrate that .__ne__() CAN fail with certain combinations:
        numpy array of strings != a 6-char list raises broadcast error.
        This is the pattern that .isin() avoids."""
        names = numpy.array(["NGC 224", "IC 434", "M31", "M42"], dtype=object)
        # Triggering the exact error: comparing array with a list of 6 elements
        six_element_list = ["IC", "NGC", "M", "M31", "Sirius", "Vega"]
        with self.assertRaises(ValueError):
            _ = names != six_element_list

    def test_isin_is_safe_with_6char_target(self):
        """Verify .isin() approach is safe regardless of input length or type."""
        names = numpy.array(["NGC 224", "IC 434", "M31", "M42"], dtype=object)
        # This is the pattern we use in the fix - wrapping target in a list
        result = ~numpy.isin(names, ["IC 434"])
        expected = numpy.array([True, False, True, True])
        numpy.testing.assert_array_equal(result, expected)

    def test_isin_safe_with_any_string(self):
        """.isin() handles any string length safely."""
        names = numpy.array(["A", "B", "C", "D"], dtype=object)
        for target in ["A", "AB", "ABC", "ABCD", "ABCDE", "ABCDEF"]:
            result = ~numpy.isin(names, [target])
            self.assertEqual(len(result), 4)
            self.assertEqual(result[0], (target != "A"))


if __name__ == "__main__":
    unittest.main()
