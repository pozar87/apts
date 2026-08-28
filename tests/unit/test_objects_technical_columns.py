from datetime import datetime, timezone

import pandas as pd

from apts.catalogs import Catalogs
from apts.conditions import Conditions
from apts.constants.objecttablelabels import TECHNICAL_COLUMNS
from apts.equipment.base import Equipment
from apts.objects import Messier, SolarObjects
from apts.objects.utils import filter_technical_columns
from apts.observations import Observation
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.place import Place


def test_filter_technical_columns_helper():
    dummy_df = pd.DataFrame(
        {
            "Name": ["M31", "Jupiter"],
            "skyfield_object": [None, None],
            "ra_hours": [0.7, 12.5],
            "dec_degrees": [41.2, -2.5],
            "Magnitude_float": [3.4, -2.1],
            "sin_dec": [0.65, -0.04],
            "cos_dec_cos_ra": [0.5, 0.8],
            "cos_dec_sin_ra": [0.4, 0.1],
            "NGC_norm": ["NGC0224", None],
            "IC_norm": [None, None],
            "Name_norm": ["M31", "JUPITER"],
            "TechnicalName": [None, "jupiter barycenter"],
            "current_alt": [45.0, 30.0],
            "current_az": [180.0, 90.0],
            "Magnitude": [3.4, -2.1],
        }
    )

    expected_technical_columns = [
        "NGC_norm",
        "IC_norm",
        "Name_norm",
        "sin_dec",
        "cos_dec_cos_ra",
        "cos_dec_sin_ra",
    ]
    for col in expected_technical_columns:
        assert col in TECHNICAL_COLUMNS

    cleaned = filter_technical_columns(dummy_df)
    assert "Name" in cleaned.columns
    assert "Magnitude" in cleaned.columns
    for col in TECHNICAL_COLUMNS:
        assert col not in cleaned.columns


def test_objects_data_and_drop_technical():
    place = Place(50.0647, 19.9450, "Krakow", 200)
    catalogs = Catalogs()
    messier = Messier(place, catalogs)

    # Master catalog should retain technical columns
    assert "ra_hours" in messier.objects.columns
    assert "Magnitude_float" in messier.objects.columns

    # Clean data view
    clean_df = messier.data(clean=True)
    for col in TECHNICAL_COLUMNS:
        assert col not in clean_df.columns

    # Unclean data view
    unclean_df = messier.data(clean=False)
    assert "ra_hours" in unclean_df.columns
    assert "Magnitude_float" in unclean_df.columns


def test_get_visible_filters_technical_columns():
    place = Place(50.0647, 19.9450, "Krakow", 200)
    catalogs = Catalogs()
    conditions = Conditions()
    start = datetime(2025, 5, 20, 22, 0, 0, tzinfo=timezone.utc)
    stop = datetime(2025, 5, 20, 23, 0, 0, tzinfo=timezone.utc)

    messier = Messier(place, catalogs)
    visible_m = messier.get_visible(conditions, start, stop, clean=True)
    if not visible_m.empty:
        for col in TECHNICAL_COLUMNS:
            assert col not in visible_m.columns

    unclean_m = messier.get_visible(conditions, start, stop, clean=False)
    if not unclean_m.empty:
        assert "ra_hours" in unclean_m.columns

    solar = SolarObjects(place)
    visible_s = solar.get_visible(conditions, start, stop, clean=True)
    if not visible_s.empty:
        for col in TECHNICAL_COLUMNS:
            assert col not in visible_s.columns


def test_observation_catalog_mixins_cleaned():
    place = Place(50.0647, 19.9450, "Krakow", 200)
    telescope = Sky_watcherTelescope.Sky_Watcher_Explorer_150P()
    camera = ZwoCamera.ZWO_ASI_178MM()
    equipment = Equipment()
    equipment.add_vertex("Telescope", telescope)
    equipment.add_vertex("Camera", camera)
    equipment.add_edge("Space", "Telescope")
    equipment.add_edge("Telescope", "Camera")
    conditions = Conditions()
    target_date = datetime(2025, 5, 20, 22, 0, 0, tzinfo=timezone.utc)
    obs = Observation(place, equipment, conditions, target_date=target_date)

    messier_df = obs.get_visible_messier()
    for col in TECHNICAL_COLUMNS:
        assert col not in messier_df.columns

    ngc_df = obs.get_visible_ngc()
    for col in TECHNICAL_COLUMNS:
        assert col not in ngc_df.columns

    planets_df = obs.get_visible_planets()
    for col in TECHNICAL_COLUMNS:
        assert col not in planets_df.columns
