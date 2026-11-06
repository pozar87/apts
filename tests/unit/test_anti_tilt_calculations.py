from apts.opticalequipment.anti_tilt import AntiTilt, normalize_anti_tilt_database_entry
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


def test_anti_tilt_normalize_database_entry_and_get_database_entries():
    raw_entry = {
        "brand": "ZWO",
        "name": "M54 Tilter",
        "optical_length": 5.126,
        "mass": 100,
        "tside_thread": "M54",
        "tside_gender": "F",
        "cside_thread": "M54",
        "cside_gender": "M",
    }

    normalized = AntiTilt.normalize_database_entry(raw_entry)
    assert normalized["vendor"] == "ZWO M54 Tilter"
    assert normalized["optical_length"] == 5.13
    assert normalized["inputs"] == [(ConnectionType.M54, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.M54, Gender.MALE)]

    entries = AntiTilt.get_database_entries()
    assert len(entries) > 0
    for entry in entries:
        assert "vendor" in entry
        assert "optical_length" in entry
        assert "inputs" in entry
        assert "outputs" in entry
