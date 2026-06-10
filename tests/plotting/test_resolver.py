import unittest
from types import SimpleNamespace

import pandas as pd

from apts.plotting.skymaps.resolver import resolve_target


def _make_catalog_df(column_name, entries, extra_names=None):
    """Create a DataFrame with a StringDtype column mimicking catalog objects.

    Parameters
    ----------
    column_name : str
        The primary designation column (e.g. "Messier", "NGC").
    entries : list of str
        Values for the primary column.
    extra_names : list of str, optional
        Values for the "Name" column. Defaults to f"Name_{entry}".
        When column_name is "Name", pass this as None to avoid dict key collision.
    """
    data = {column_name: list(entries)}
    if column_name != "Name":
        data["Name"] = extra_names or [f"Name_{e}" for e in entries]
    df = pd.DataFrame(data, dtype="string")
    df["RA"] = "00:00:00"
    df["Dec"] = "+00:00:00"
    df = df.astype("string")
    return df


class MockCatalog:
    """Mock catalog object that mimics local_messier / local_ngc / local_stars."""

    def __init__(self, df, column_name, skyfield_return=None):
        self.objects = df
        self._column_name = column_name
        self._skyfield_return = skyfield_return

    def get_skyfield_object(self, obj_row):
        return self._skyfield_return

    def find_by_name(self, name):
        from apts.objects.ngc import NGC

        norm_name = NGC.normalize_name(name)
        mask = (self.objects[self._column_name].apply(NGC.normalize_name) == norm_name) | (
            self.objects["Name"].apply(NGC.normalize_name) == norm_name
        )
        if "IC" in self.objects.columns:
            mask |= self.objects["IC"].apply(NGC.normalize_name) == norm_name
        res = self.objects[mask]
        if not res.empty:
            return self.get_skyfield_object(res.iloc[0])
        return None


class MockPlanets:
    def find_by_name(self, name):
        return None


class TestResolveTargetPandasCompatibility(unittest.TestCase):
    """Tests that resolve_target works correctly with pandas StringDtype columns,
    guarding against the regression seen in pandas 2.3.3 where
    StringArray._cmp_method fails with 'Lengths of operands do not match'
    when comparing with a scalar string."""

    def setUp(self):
        self.planets = MockPlanets()

    def _make_observation(self, messier_df=None, ngc_df=None, stars_df=None):
        """Build a mock Observation object with the given catalog DataFrames.

        Ensures every catalog DataFrame has the required columns, even when
        the caller only provides one catalog - this prevents KeyError when
        resolve_target probes the next catalog after a miss.
        """
        if messier_df is None:
            messier_df = pd.DataFrame({"Messier": pd.array([], dtype="string")})
        if ngc_df is None:
            ngc_df = pd.DataFrame(
                {
                    "NGC": pd.array([], dtype="string"),
                    "Name": pd.array([], dtype="string"),
                }
            )
        if stars_df is None:
            stars_df = pd.DataFrame({"Name": pd.array([], dtype="string")})
        return SimpleNamespace(
            local_messier=MockCatalog(
                messier_df, "Messier", skyfield_return="mock_skyfield_obj"
            ),
            local_ngc=MockCatalog(ngc_df, "NGC", skyfield_return="mock_skyfield_obj"),
            local_stars=MockCatalog(
                stars_df, "Name", skyfield_return="mock_skyfield_obj"
            ),
            local_planets=self.planets,
        )

    # ── Messier lookups ──────────────────────────────────────────────

    def test_messier_found_by_designation(self):
        """resolve_target finds a Messier object by its 'Messier' column."""
        df = _make_catalog_df("Messier", ["M1", "M31", "M42", "M101", "M104"])
        obs = self._make_observation(messier_df=df)
        obj, data = resolve_target(obs, "M42")
        self.assertIsNotNone(obj)
        self.assertIsNotNone(data)
        self.assertEqual(data["Messier"], "M42")

    def test_messier_not_found_falls_through(self):
        """resolve_target returns (None, None) when no catalog matches."""
        df = _make_catalog_df("Messier", ["M1", "M31"])
        obs = self._make_observation(messier_df=df)
        obj, data = resolve_target(obs, "M999")
        self.assertIsNone(obj)
        self.assertIsNone(data)

    def test_messier_with_exact_name_match(self):
        """resolve_target handles Messier names that look like other catalog IDs."""
        df = _make_catalog_df("Messier", ["M1", "NGC 1", "M42"])
        obs = self._make_observation(messier_df=df)
        obj, data = resolve_target(obs, "M1")
        self.assertIsNotNone(data)
        self.assertEqual(data["Messier"], "M1")

    # ── NGC lookups ─────────────────────────────────────────────────

    def test_ngc_found_by_number(self):
        """resolve_target finds an NGC object by its 'NGC' column."""
        df = _make_catalog_df("NGC", ["NGC 1", "NGC 7000", "NGC 891"])
        obs = self._make_observation(ngc_df=df)
        obj, data = resolve_target(obs, "NGC 7000")
        self.assertIsNotNone(obj)
        self.assertIsNotNone(data)
        self.assertEqual(data["NGC"], "NGC 7000")

    def test_ngc_found_by_name(self):
        """resolve_target finds an NGC object by its 'Name' column."""
        df = _make_catalog_df("NGC", ["NGC 1", "NGC 7000"])
        df["Name"] = pd.array(["NGC 1", "North America Nebula"], dtype="string")
        obs = self._make_observation(ngc_df=df)
        obj, data = resolve_target(obs, "North America Nebula")
        self.assertIsNotNone(obj)
        self.assertIsNotNone(data)
        self.assertEqual(data["Name"], "North America Nebula")

    # ── Stars lookups ───────────────────────────────────────────────

    def test_star_found_by_name(self):
        """resolve_target finds a star by its 'Name' column."""
        df = _make_catalog_df("Name", ["Sirius", "Vega", "Polaris"])
        obs = self._make_observation(stars_df=df)
        obj, data = resolve_target(obs, "Vega")
        self.assertIsNotNone(obj)
        self.assertIsNotNone(data)
        self.assertEqual(data["Name"], "Vega")

    # ── Priority order (Messier > NGC > Stars > Planets) ────────────

    def test_messier_takes_priority_over_ngc(self):
        """resolve_target checks Messier before NGC."""
        messier = _make_catalog_df("Messier", ["M1", "NGC 1"])
        ngc = _make_catalog_df("NGC", ["NGC 1"])
        obs = self._make_observation(messier_df=messier, ngc_df=ngc)
        obj, data = resolve_target(obs, "NGC 1")
        # Should find in Messier first
        self.assertIsNotNone(data)
        self.assertIn("Messier", data)

    # ── Stress test: many rows (replicates the real-world 110-row case) ──

    def test_large_catalog_lookup(self):
        """resolve_target handles a ~110-row Messier catalog without length-mismatch errors."""
        designations = [f"M{i}" for i in range(1, 111)]
        df = _make_catalog_df("Messier", designations)
        obs = self._make_observation(messier_df=df)
        obj, data = resolve_target(obs, "M42")
        self.assertIsNotNone(data)
        self.assertEqual(data["Messier"], "M42")

    def test_large_catalog_not_found(self):
        """resolve_target returns (None, None) for missing entry in a large catalog."""
        designations = [f"M{i}" for i in range(1, 111)]
        df = _make_catalog_df("Messier", designations)
        obs = self._make_observation(messier_df=df)
        obj, data = resolve_target(obs, "M999")
        self.assertIsNone(obj)
        self.assertIsNone(data)

    # ── Edge cases ──────────────────────────────────────────────────

    def test_empty_dataframe(self):
        """resolve_target handles an empty catalog DataFrame."""
        df = pd.DataFrame({"Messier": pd.array([], dtype="string")})
        obs = self._make_observation(messier_df=df)
        obj, data = resolve_target(obs, "M1")
        self.assertIsNone(obj)
        self.assertIsNone(data)

    def test_target_name_with_spaces(self):
        """resolve_target handles target names containing spaces."""
        df = _make_catalog_df("NGC", ["NGC 7000"])
        df["Name"] = pd.array(["North America Nebula"], dtype="string")
        obs = self._make_observation(ngc_df=df)
        obj, data = resolve_target(obs, "North America Nebula")
        self.assertIsNotNone(data)
        self.assertEqual(data["Name"], "North America Nebula")

    def test_partial_match_does_not_false_positive(self):
        """resolve_target does not match partial substrings."""
        df = _make_catalog_df("Messier", ["M1", "M10", "M101"])
        obs = self._make_observation(messier_df=df)
        # "M1" should NOT match "M10" or "M101"
        obj, data = resolve_target(obs, "M1")
        self.assertIsNotNone(data)
        self.assertEqual(data["Messier"], "M1")


if __name__ == "__main__":
    unittest.main()
