from apts.opticalequipment.rotator import normalize_rotator_database_entry, Rotator
from apts.utils import ConnectionType, Gender


def test_normalize_rotator_database_entry():
    raw_entry = {
        "brand": "Pegasus Astro",
        "name": "Falcon Rotator",
        "optical_length": 18,
        "mass": 280,
        "tside_thread": "M54",
        "tside_gender": "F",
        "cside_thread": "M54",
        "cside_gender": "M",
    }

    normalized = normalize_rotator_database_entry(raw_entry)

    assert normalized["vendor"] == "Pegasus Astro Falcon Rotator"
    assert normalized["optical_length"] == 18
    assert normalized["mass"] == 280
    assert normalized["inputs"] == [(ConnectionType.M54, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.M54, Gender.MALE)]


def test_rotator_from_database():
    raw_entry = {
        "brand": "Pegasus Astro",
        "name": "Falcon Rotator",
        "optical_length": 18,
        "mass": 280,
        "tside_thread": "M54",
        "tside_gender": "F",
        "cside_thread": "M54",
        "cside_gender": "M",
    }

    rotator = Rotator.from_database(raw_entry)
    assert rotator.get_vendor() == "Pegasus Astro Falcon Rotator"
    assert rotator.optical_length.magnitude == 18
    assert rotator.mass.magnitude == 280
