from apts.opticalequipment.focuser import Focuser, normalize_focuser_database_entry
from apts.utils import ConnectionType, Gender


def test_normalize_focuser_database_entry_basic():
    entry = {
        "brand": "ZWO",
        "name": "EAF",
        "mass": 200,
        "optical_length": 0,
        "tside_thread": "M42",
        "tside_gender": "Female",
        "cside_thread": "M42",
        "cside_gender": "Male",
    }
    normalized = normalize_focuser_database_entry(entry)

    assert normalized["vendor"] == "ZWO EAF"
    assert normalized["mass"] == 200
    assert normalized["optical_length"] == 0
    assert normalized["inputs"] == [(ConnectionType.M42, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.M42, Gender.MALE)]


def test_focuser_from_database():
    entry = {
        "brand": "MoonLite",
        "name": "CR2 Focuser",
        "mass": 600,
        "optical_length": 50,
        "tside_thread": "2\"",
        "tside_gender": "Female",
        "cside_thread": "2\"",
        "cside_gender": "Male",
    }
    focuser = Focuser.from_database(entry)

    assert focuser.get_vendor() == "MoonLite CR2 Focuser"
    assert focuser.optical_length.magnitude == 50
    assert focuser.mass.magnitude == 600
