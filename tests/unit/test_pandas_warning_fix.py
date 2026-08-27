import datetime
import warnings

import pytest

from apts.catalogs import Catalogs
from apts.conditions import Conditions
from apts.objects import Messier, NGC, SolarObjects
from apts.place import Place


@pytest.fixture
def place_and_catalogs():
    place = Place(50.0, 20.0, 100)
    catalogs = Catalogs()
    return place, catalogs


def test_messier_compute_no_future_warning(place_and_catalogs):
    place, catalogs = place_and_catalogs
    messier = Messier(place, catalogs)

    # Work on a subset copy where Constellation is a string column
    subset = messier.objects.iloc[:10].copy()

    with warnings.catch_warnings(record=True) as captured_warnings:
        warnings.simplefilter("always", FutureWarning)
        messier.compute(df_to_compute=subset)

    future_warnings = [
        w for w in captured_warnings if issubclass(w.category, FutureWarning)
    ]
    assert len(future_warnings) == 0, f"Unexpected FutureWarnings: {future_warnings}"


def test_solar_objects_compute_no_future_warning(place_and_catalogs):
    place, _ = place_and_catalogs
    solar = SolarObjects(place)

    subset = solar.objects.iloc[:2].copy()

    with warnings.catch_warnings(record=True) as captured_warnings:
        warnings.simplefilter("always", FutureWarning)
        solar.compute(df_to_compute=subset)

    future_warnings = [
        w for w in captured_warnings if issubclass(w.category, FutureWarning)
    ]
    assert len(future_warnings) == 0, f"Unexpected FutureWarnings: {future_warnings}"


def test_messier_get_visible_no_future_warning(place_and_catalogs):
    place, catalogs = place_and_catalogs
    messier = Messier(place, catalogs)
    cond = Conditions()
    start = datetime.datetime(2025, 5, 1, 20, 0, tzinfo=datetime.timezone.utc)
    stop = datetime.datetime(2025, 5, 2, 4, 0, tzinfo=datetime.timezone.utc)

    with warnings.catch_warnings(record=True) as captured_warnings:
        warnings.simplefilter("always", FutureWarning)
        visible = messier.get_visible(cond, start, stop)

    future_warnings = [
        w for w in captured_warnings if issubclass(w.category, FutureWarning)
    ]
    assert len(future_warnings) == 0, f"Unexpected FutureWarnings: {future_warnings}"
    assert not visible.empty


def test_ngc_get_visible_no_future_warning(place_and_catalogs):
    place, catalogs = place_and_catalogs
    ngc = NGC(place, catalogs)
    cond = Conditions()
    start = datetime.datetime(2025, 5, 1, 20, 0, tzinfo=datetime.timezone.utc)
    stop = datetime.datetime(2025, 5, 2, 4, 0, tzinfo=datetime.timezone.utc)

    with warnings.catch_warnings(record=True) as captured_warnings:
        warnings.simplefilter("always", FutureWarning)
        visible = ngc.get_visible(cond, start, stop)

    future_warnings = [
        w for w in captured_warnings if issubclass(w.category, FutureWarning)
    ]
    assert len(future_warnings) == 0, f"Unexpected FutureWarnings: {future_warnings}"
