import pickle
import unittest
from unittest.mock import MagicMock, patch

import pint
import pytest

from apts import catalogs
from apts.cache import download_all_data, get_hipparcos_data, get_mpcorb_data
from apts.equipment import Equipment
from apts.objects.messier import Messier
from apts.objects import SolarObjects
from apts.observations import Observation
from apts.opticalequipment import Eyepiece, Telescope
from apts.place import Place
from apts.units import ureg


class CacheTest(unittest.TestCase):
    def setUp(self):
        pint.set_application_registry(ureg)

    def test_place_pickle(self):
        p = Place(lat=52.2, lon=21.0, name="Warsaw")
        pickled_place = pickle.dumps(p)
        unpickled_place = pickle.loads(pickled_place)
        self.assertIsNotNone(unpickled_place)
        self.assertEqual(p.name, unpickled_place.name)
        self.assertIsNotNone(unpickled_place.sun)

    def test_equipment_pickle(self):
        e = Equipment()
        t = Telescope(
            aperture=150,
            focal_length=750,
            vendor="SW 150/750",
        )
        e.register(t)
        ep = Eyepiece(
            focal_length=24,
            vendor="ES 24",
            field_of_view=68,
        )
        e.register(ep)
        pickled_equipment = pickle.dumps(e)
        unpickled_equipment = pickle.loads(pickled_equipment)
        self.assertIsNotNone(unpickled_equipment)
        self.assertEqual(len(e.data()), len(unpickled_equipment.data()))

    @pytest.mark.clear_mpcorb
    def test_solar_objects_pickle(self):
        p = Place(lat=52.2, lon=21.0, name="Warsaw")
        so = SolarObjects(p)
        pickled_so = pickle.dumps(so)
        unpickled_so = pickle.loads(pickled_so)
        self.assertIsNotNone(unpickled_so)
        self.assertEqual(len(so.objects), len(unpickled_so.objects))

    def test_messier_pickle(self):
        p = Place(lat=52.2, lon=21.0, name="Warsaw")
        m = Messier(p, catalogs)
        pickled_m = pickle.dumps(m)
        unpickled_m = pickle.loads(pickled_m)
        self.assertIsNotNone(unpickled_m)
        self.assertEqual(len(m.objects), len(unpickled_m.objects))

    @pytest.mark.clear_mpcorb
    def test_observation_pickle(self):
        p = Place(lat=52.2, lon=21.0, name="Warsaw")
        e = Equipment()
        o = Observation(p, e)
        pickled_o = pickle.dumps(o)
        unpickled_o = pickle.loads(pickled_o)
        self.assertIsNotNone(unpickled_o)
        self.assertEqual(o.place.name, unpickled_o.place.name)
        self.assertIsNotNone(unpickled_o.local_planets)

    @pytest.mark.clear_mpcorb
    @patch("apts.cache.catalogs.get_minor_planet_settings")
    def test_get_mpcorb_data_filtered(self, mock_get_settings):
        # Mock the settings to return a specific list of planets
        mock_get_settings.return_value = ["00001", "00002"]  # Ceres and Pallas

        # Call the function
        df = get_mpcorb_data()

        # Assert that the dataframe contains only Ceres and Pallas
        self.assertEqual(len(df), 2)
        self.assertIn("(1) Ceres", df.index)
        self.assertIn("(2) Pallas", df.index)

    @patch("apts.cache.base.get_ephemeris")
    @patch("apts.cache.base.get_hipparcos_data")
    @patch("apts.cache.base.get_mpcorb_data")
    @patch("apts.cache.base.get_jovian_ephemeris")
    def test_download_all_data(
        self,
        mock_get_jovian_ephemeris,
        mock_get_mpcorb_data,
        mock_get_hipparcos_data,
        mock_get_ephemeris,
    ):
        download_all_data()
        mock_get_ephemeris.assert_called_once()
        mock_get_hipparcos_data.assert_called_once()
        mock_get_mpcorb_data.assert_called_once()
        mock_get_jovian_ephemeris.assert_called_once()

    @patch("apts.cache.catalogs.Loader")
    def test_get_hipparcos_data_failure(self, mock_loader_class):
        # Mock loader.open to raise an exception
        mock_loader_instance = mock_loader_class.return_value
        mock_loader_instance.open.side_effect = Exception("Network error")

        # Clear cache before test
        get_hipparcos_data.cache_clear()

        # Call the function
        df = get_hipparcos_data()

        # Assertions
        self.assertTrue(df.empty)
        expected_columns = [
            "magnitude",
            "ra_degrees",
            "dec_degrees",
            "parallax_mas",
            "ra_hours",
            "epoch_year",
        ]
        self.assertListEqual(list(df.columns), expected_columns)

        # Clear cache after test to avoid leaking mocks
        get_hipparcos_data.cache_clear()

    @patch("apts.cache.skyfield.load")
    @patch("apts.cache.skyfield.get_ephemeris")
    def test_get_jovian_ephemeris(self, mock_get_ephemeris, mock_load):
        from apts.cache import get_jovian_ephemeris

        # Mock base ephemeris
        mock_eph = MagicMock()
        mock_eph.segments = ["segment1"]
        mock_get_ephemeris.return_value = mock_eph

        # Mock Jovian ephemeris
        mock_jovian = MagicMock()
        mock_jovian.segments = ["segment2"]
        mock_load.return_value = mock_jovian

        # Clear cache before test
        get_jovian_ephemeris.cache_clear()

        # Call the function
        merged_eph = get_jovian_ephemeris()

        # Assertions
        segments = getattr(merged_eph, "segments")
        self.assertIn("segment1", segments)
        self.assertIn("segment2", segments)
        self.assertEqual(len(segments), 2)
        mock_load.assert_called_once()

        # Clear cache after test to avoid leaking mocks
        get_jovian_ephemeris.cache_clear()

    @pytest.mark.clear_mpcorb
    @patch("apts.cache.catalogs.get_minor_planet_settings")
    def test_get_mpcorb_data_empty(self, mock_get_settings):
        # Mock settings to return a planet that doesn't exist in our small test data
        mock_get_settings.return_value = ["NONEXISTENT"]

        # Call the function
        # We need to clear the cache first because get_mpcorb_data is cached
        get_mpcorb_data.cache_clear()
        df = get_mpcorb_data()

        # Assertions
        self.assertTrue(df.empty)
        self.assertEqual(df.index.name, "designation")
        # Check some of the expected columns
        self.assertIn("semimajor_axis_au", df.columns)
        self.assertIn("eccentricity", df.columns)

        # Clear cache after test
        get_mpcorb_data.cache_clear()
