from apts.opticalequipment.diagonal import Diagonal, normalize_diagonal_database_entry
from apts.utils import ConnectionType, Gender


def test_normalize_diagonal_database_entry_basic():
    entry = {
        "brand": "TeleVue",
        "name": "2\" Dielectric Diagonal",
        "mass": 450,
        "optical_length": 100,
        "tside_thread": "2\"",
        "tside_gender": "Female",
        "cside_thread": "2\"",
        "cside_gender": "Male",
    }
    normalized = normalize_diagonal_database_entry(entry)

    assert normalized["vendor"] == "TeleVue 2\" Dielectric Diagonal"
    assert normalized["mass"] == 450
    assert normalized["optical_length"] == 100
    assert normalized["inputs"] == [(ConnectionType.F_2, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.F_2, Gender.MALE)]


def test_normalize_diagonal_database_entry_t2_output():
    entry = {
        "brand": "Baader",
        "name": "T2 Maxbright Diagonal",
        "tside_thread": "1.25\"",
        "tside_gender": "Female",
        "cside_thread": "1.25\"",
        "cside_gender": "Male",
        "t2_output": True,
    }
    normalized = normalize_diagonal_database_entry(entry)

    assert normalized["vendor"] == "Baader T2 Maxbright Diagonal"
    assert normalized["outputs"] == [
        (ConnectionType.F_1_25, Gender.MALE),
        (ConnectionType.T2, Gender.MALE),
    ]


def test_diagonal_from_database():
    entry = {
        "brand": "Celestron",
        "name": "1.25\" Star Diagonal",
        "mass": 200,
        "optical_length": 75,
        "tside_thread": "1.25\"",
        "tside_gender": "Female",
        "cside_thread": "1.25\"",
        "cside_gender": "Male",
    }
    diagonal = Diagonal.from_database(entry)

    assert diagonal.vendor == "Celestron 1.25\" Star Diagonal"
    assert diagonal.optical_length.magnitude == 75
    assert diagonal.mass.magnitude == 200
