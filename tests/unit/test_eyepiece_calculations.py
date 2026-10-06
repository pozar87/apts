from apts.opticalequipment.eyepiece import Eyepiece, normalize_eyepiece_database_entry
from apts.utils import ConnectionType, Gender


def test_normalize_eyepiece_database_entry_defaults():
    raw_entry = {
        "brand": "Tele Vue",
        "name": "Nagler 31mm 82°",
        "tside_thread": '1.25"',
        "tside_gender": "Female",
    }
    normalized = normalize_eyepiece_database_entry(raw_entry)

    assert normalized["focal_length_mm"] == 31.0
    assert normalized["field_of_view_deg"] == 82.0
    assert normalized["inputs"] == [(ConnectionType.F_1_25, Gender.FEMALE)]


def test_normalize_eyepiece_database_entry_explicit():
    raw_entry = {
        "brand": "Custom",
        "name": "Custom Ocular",
        "focal_length_mm": 25,
        "field_of_view_deg": 60,
        "inputs": [('2"', "Male")],
    }
    normalized = normalize_eyepiece_database_entry(raw_entry)

    assert normalized["focal_length_mm"] == 25
    assert normalized["field_of_view_deg"] == 60
    assert normalized["inputs"] == [(ConnectionType.F_2, Gender.MALE)]


def test_eyepiece_class_normalize_and_from_database():
    raw_entry = {
        "brand": "Tele Vue",
        "name": "Ethos 21mm 100°",
        "tside_thread": '2"',
        "tside_gender": "Female",
    }
    normalized = Eyepiece.normalize_database_entry(raw_entry)
    assert normalized["focal_length_mm"] == 21.0
    assert normalized["field_of_view_deg"] == 100.0
    assert normalized["inputs"] == [(ConnectionType.F_2, Gender.FEMALE)]

    eyepiece = Eyepiece.from_database(raw_entry)
    assert eyepiece.focal_length.magnitude == 21.0
    assert eyepiece._field_of_view.magnitude == 100.0
    assert eyepiece.vendor == "Tele Vue Ethos 21mm 100°"
