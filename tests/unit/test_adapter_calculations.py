from apts.opticalequipment.adapter import Adapter, Spacer, normalize_adapter_database_entry
from apts.utils import ConnectionType, Gender


def test_normalize_adapter_database_entry_basic():
    entry = {
        "brand": "ZWO",
        "name": "M42-M48 Adapter",
        "mass": 30,
        "optical_length": 16.5,
        "tside_thread": "M42",
        "tside_gender": "Female",
        "cside_thread": "M48",
        "cside_gender": "Male",
    }
    normalized = normalize_adapter_database_entry(entry)

    assert normalized["vendor"] == "ZWO M42-M48 Adapter"
    assert normalized["mass"] == 30
    assert normalized["optical_length"] == 16.5
    assert normalized["inputs"] == [(ConnectionType.M42, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.M48, Gender.MALE)]


def test_normalize_adapter_database_entry_custom_inputs_outputs():
    entry = {
        "brand": "Baader",
        "name": "VariLock 29",
        "optical_length": 29,
        "mass": 80,
        "inputs": [(ConnectionType.M48, Gender.FEMALE)],
        "outputs": [(ConnectionType.T2, Gender.MALE)],
    }
    normalized = normalize_adapter_database_entry(entry)

    assert normalized["vendor"] == "Baader VariLock 29"
    assert normalized["inputs"] == [(ConnectionType.M48, Gender.FEMALE)]
    assert normalized["outputs"] == [(ConnectionType.T2, Gender.MALE)]


def test_adapter_from_database():
    entry = {
        "brand": "TS-Optics",
        "name": "M48 Spacer 10mm",
        "mass": 25,
        "optical_length": 10,
        "tside_thread": "M48",
        "tside_gender": "Female",
        "cside_thread": "M48",
        "cside_gender": "Male",
    }
    adapter = Adapter.from_database(entry)

    assert adapter.get_vendor() == "TS-Optics M48 Spacer 10mm"
    assert adapter.optical_length.magnitude == 10
    assert adapter.mass.magnitude == 25


def test_spacer_from_database():
    entry = {
        "brand": "ZWO",
        "name": "21mm M42 Extension",
        "mass": 40,
        "optical_length": 21,
        "tside_thread": "M42",
        "tside_gender": "Female",
        "cside_thread": "M42",
        "cside_gender": "Male",
    }
    spacer = Spacer.from_database(entry)

    assert spacer.get_vendor() == "ZWO 21mm M42 Extension"
    assert spacer.optical_length.magnitude == 21
    assert spacer.mass.magnitude == 40
