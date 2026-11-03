from apts.opticalequipment.flip_mirror import (
    FlipMirror,
    normalize_flip_mirror_database_entry,
)
from apts.utils import ConnectionType, Gender


def test_normalize_flip_mirror_database_entry():
    raw_entry = {
        "brand": "Baader",
        "name": "FlipMirror II",
        "optical_length": 59,
        "mass": 290,
        "tside_thread": "M48",
        "tside_gender": "F",
        "cside_thread": "T2",
        "cside_gender": "M",
    }

    normalized = normalize_flip_mirror_database_entry(raw_entry)

    assert normalized["vendor"] == "Baader FlipMirror II"
    assert normalized["optical_length"] == 59
    assert normalized["mass"] == 290
    assert normalized["inputs"] == [(ConnectionType.M48, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.T2, Gender.MALE)]


def test_flip_mirror_from_database():
    raw_entry = {
        "brand": "Baader",
        "name": "FlipMirror II",
        "optical_length": 59,
        "mass": 290,
        "tside_thread": "M48",
        "tside_gender": "F",
        "cside_thread": "T2",
        "cside_gender": "M",
    }

    fm = FlipMirror.from_database(raw_entry)
    assert fm.get_vendor() == "Baader FlipMirror II"
    assert fm.optical_length.magnitude == 59
    assert fm.mass.magnitude == 290


def test_flip_mirror_normalize_database_entry_and_get_database_entries():
    raw_entry = {
        "brand": "Baader",
        "name": "FlipMirror II",
        "optical_length": 59.124,
        "mass": 290,
        "tside_thread": "M48",
        "tside_gender": "F",
        "cside_thread": "T2",
        "cside_gender": "M",
    }

    normalized = FlipMirror.normalize_database_entry(raw_entry)
    assert normalized["vendor"] == "Baader FlipMirror II"
    assert normalized["optical_length"] == 59.12
    assert normalized["inputs"] == [(ConnectionType.M48, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.T2, Gender.MALE)]

    entries = FlipMirror.get_database_entries()
    assert len(entries) > 0
    for entry in entries:
        assert "vendor" in entry
        assert "optical_length" in entry
        assert "inputs" in entry
        assert "outputs" in entry
