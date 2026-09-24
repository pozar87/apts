from apts.opticalequipment.filter import Filter, normalize_filter_database_entry
from apts.utils import ConnectionType, Gender


def test_normalize_filter_database_entry_basic():
    entry = {
        "brand": "Optolong",
        "name": "L-Pro 2\"",
        "transmission": 0.95,
        "optical_length": 5,
        "mass": 40,
        "tside_thread": "2\"",
    }
    normalized = normalize_filter_database_entry(entry)

    assert normalized["name"] == "L-Pro 2\""
    assert normalized["vendor"] == "Optolong L-Pro 2\""
    assert normalized["connection_type"] == ConnectionType.F_2
    assert normalized["transmission"] == 0.95
    assert normalized["optical_length"] == 5
    assert normalized["mass"] == 40
    assert normalized["inputs"] is None
    assert normalized["outputs"] is None


def test_normalize_filter_database_entry_with_inputs_and_outputs():
    entry = {
        "brand": "Astronomik",
        "name": "OIII 1.25\"",
        "inputs": [("1.25\"", "Female")],
        "outputs": [("1.25\"", "Male")],
    }
    normalized = normalize_filter_database_entry(entry)

    assert normalized["inputs"] == [(ConnectionType.F_1_25, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.F_1_25, Gender.MALE)]


def test_filter_from_database():
    entry = {
        "brand": "Baader",
        "name": "UHC-S 1.25\"",
        "transmission": 0.92,
        "optical_length": 6,
        "mass": 35,
        "tside_thread": "1.25\"",
    }
    filter_obj = Filter.from_database(entry)

    assert filter_obj.name == "UHC-S 1.25\""
    assert filter_obj.get_vendor() == "Baader UHC-S 1.25\""
    assert filter_obj.transmission == 0.92
    assert filter_obj.optical_length.magnitude == 6
    assert filter_obj.mass.magnitude == 35
