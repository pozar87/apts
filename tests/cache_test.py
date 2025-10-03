import pickle
from apts.place import Place
from apts.equipment import Equipment
from apts.objects.solar_objects import SolarObjects
from apts.objects.messier import Messier
from apts.observations import Observation
from apts.opticalequipment import Telescope, Eyepiece
import unittest
import pint
from apts.units import ureg
from apts import catalogs
from unittest.mock import patch
from apts.cache import get_mpcorb_data


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

    def test_observation_pickle(self):
        p = Place(lat=52.2, lon=21.0, name="Warsaw")
        e = Equipment()
        o = Observation(p, e)
        pickled_o = pickle.dumps(o)
        unpickled_o = pickle.loads(pickled_o)
        self.assertIsNotNone(unpickled_o)
        self.assertEqual(o.place.name, unpickled_o.place.name)
        self.assertIsNotNone(unpickled_o.local_planets)

    @patch("apts.cache.get_minor_planet_settings")
    def test_get_mpcorb_data_filtered(self, mock_get_settings):
        # Mock the settings to return a specific list of planets
        mock_get_settings.return_value = ["00001", "00002"]  # Ceres and Pallas

        # Call the function
        df = get_mpcorb_data()

        # Assert that the dataframe contains only Ceres and Pallas
        self.assertEqual(len(df), 2)
        self.assertIn("(1) Ceres", df.index)
        self.assertIn("(2) Pallas", df.index)
