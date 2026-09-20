from apts.opticalequipment.barlow import Barlow, normalize_barlow_database_entry
from apts.utils import ConnectionType, Gender


def test_normalize_barlow_database_entry_basic():
    entry = {
        "brand": "TeleVue",
        "name": "2x Barlow (1.25\")",
        "mass": 150,
        "optical_length": 45,
        "tside_thread": "1.25\"",
        "tside_gender": "Female",
        "cside_thread": "1.25\"",
        "cside_gender": "Male",
    }
    normalized = normalize_barlow_database_entry(entry)

    assert normalized["vendor"] == "TeleVue 2x Barlow (1.25\")"
    assert normalized["magnification"] == 2.0
    assert normalized["mass"] == 150
    assert normalized["optical_length"] == 45
    assert normalized["inputs"] == [(ConnectionType.F_1_25, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.F_1_25, Gender.MALE)]


def test_normalize_barlow_database_entry_t2_output():
    entry = {
        "brand": "Celestron",
        "name": "Omni 2x Barlow",
        "tside_thread": "1.25\"",
        "tside_gender": "Female",
        "cside_thread": "1.25\"",
        "cside_gender": "Male",
        "t2_output": True,
    }
    normalized = normalize_barlow_database_entry(entry)

    assert normalized["vendor"] == "Celestron Omni 2x Barlow"
    assert normalized["magnification"] == 2.0
    assert normalized["outputs"] == [
        (ConnectionType.F_1_25, Gender.MALE),
        (ConnectionType.T2, Gender.MALE),
    ]


def test_barlow_from_database():
    entry = {
        "brand": "GSO",
        "name": "2.5x Barlow",
        "mass": 120,
        "optical_length": 30,
        "tside_thread": "1.25\"",
        "tside_gender": "Female",
        "cside_thread": "1.25\"",
        "cside_gender": "Male",
    }
    barlow = Barlow.from_database(entry)

    assert barlow.magnification == 2.5
    assert barlow.get_vendor() == "GSO 2.5x Barlow"
    assert barlow.optical_length.magnitude == 30
    assert barlow.mass.magnitude == 120
