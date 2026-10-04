from apts.opticalequipment.binoculars.calculations import normalize_binoculars_database_entry
from apts.utils import ConnectionType, Gender


def test_normalize_binoculars_database_entry_basic():
    entry = {
        "brand": "Orion",
        "name": "GiantView 25x100 Binocular",
        "mass": 2500,
        "cside_thread": '2"',
        "cside_gender": "Male",
    }
    normalized = normalize_binoculars_database_entry(entry)
    assert normalized["vendor"] == "Orion GiantView 25x100 Binocular"
    assert normalized["mass"] == 2500
    assert normalized["magnification"] == 25
    assert normalized["objective_diameter"] == 100
    assert len(normalized["outputs"]) == 1


def test_normalize_binoculars_database_entry_explicit_outputs():
    entry = {
        "brand": "Nikon",
        "name": "Action EX 10x50",
        "outputs": [('2"', "Male")],
    }
    normalized = normalize_binoculars_database_entry(entry)
    assert normalized["vendor"] == "Nikon Action EX 10x50"
    assert normalized["magnification"] == 10
    assert normalized["objective_diameter"] == 50
    assert normalized["outputs"] == [(ConnectionType.F_2, Gender.MALE)]
