from apts.opticalequipment.anti_tilt import normalize_anti_tilt_database_entry, AntiTilt
from apts.utils import ConnectionType, Gender


def test_normalize_anti_tilt_database_entry():
    raw_entry = {
        "brand": "ZWO",
        "name": "M54 Tilter",
        "optical_length": 5,
        "mass": 100,
        "tside_thread": "M54",
        "tside_gender": "F",
        "cside_thread": "M54",
        "cside_gender": "M",
    }

    normalized = normalize_anti_tilt_database_entry(raw_entry)

    assert normalized["vendor"] == "ZWO M54 Tilter"
    assert normalized["optical_length"] == 5
    assert normalized["mass"] == 100
    assert normalized["inputs"] == [(ConnectionType.M54, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.M54, Gender.MALE)]


def test_anti_tilt_from_database():
    raw_entry = {
        "brand": "ZWO",
        "name": "M54 Tilter",
        "optical_length": 5,
        "mass": 100,
        "tside_thread": "M54",
        "tside_gender": "F",
        "cside_thread": "M54",
        "cside_gender": "M",
    }

    at = AntiTilt.from_database(raw_entry)
    assert at.get_vendor() == "ZWO M54 Tilter"
    assert at.optical_length.magnitude == 5
    assert at.mass.magnitude == 100
