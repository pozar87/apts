from apts.opticalequipment.telescope import (
    Telescope,
    TelescopeType,
    normalize_telescope_database_entry,
)
from apts.utils import ConnectionType, Gender


def test_normalize_telescope_database_entry_complete():
    entry = {
        "brand": "Celestron",
        "name": "NexStar 8SE",
        "aperture_mm": 203.2,
        "focal_length_mm": 2032,
        "type": "schmidt_cassegrain",
        "cside_thread": "SC (Schmidt-Cassegrain)",
        "cside_gender": "Male",
    }
    normalized = normalize_telescope_database_entry(entry)
    assert normalized["aperture_mm"] == 203.2
    assert normalized["focal_length_mm"] == 2032
    assert normalized["telescope_type"] == TelescopeType.SCHMIDT_CASSEGRAIN
    assert normalized["outputs"] == [(ConnectionType.SC, Gender.MALE)]


def test_normalize_telescope_database_entry_defaults_and_guessing():
    entry = {
        "brand": "Sky-Watcher",
        "name": "Evostar 80ED Refractor",
        "focal_length_mm": 600,
        "cside_thread": '2"',
        "cside_gender": "Female",
    }
    normalized = normalize_telescope_database_entry(entry)
    assert normalized["aperture_mm"] == 80.0
    assert normalized["focal_length_mm"] == 600
    assert normalized["telescope_type"] == TelescopeType.REFRACTOR
    assert normalized["outputs"] == [(ConnectionType.F_2, Gender.FEMALE)]


def test_normalize_telescope_database_entry_t2_output_and_types():
    entry = {
        "brand": "Generic",
        "name": "Newtonian 150/750",
        "type": "newtonian",
        "cside_thread": '1.25"',
        "cside_gender": "Female",
        "t2_output": True,
    }
    normalized = normalize_telescope_database_entry(entry)
    assert normalized["telescope_type"] == TelescopeType.NEWTONIAN_REFLECTOR
    assert normalized["outputs"] == [
        (ConnectionType.F_1_25, Gender.FEMALE),
        (ConnectionType.T2, Gender.MALE),
    ]


def test_telescope_from_database_integration():
    entry = {
        "brand": "Sky-Watcher",
        "name": "Evostar 72ED",
        "aperture_mm": 72,
        "focal_length_mm": 420,
        "type": "refractor",
        "cside_thread": '2"',
        "cside_gender": "Female",
        "mass": 1950,
        "optical_length": 420,
    }
    scope = Telescope.from_database(entry)
    assert scope.vendor == "Sky-Watcher Evostar 72ED"
    assert scope.aperture.to("mm").magnitude == 72
    assert scope.focal_length.to("mm").magnitude == 420
    assert scope.telescope_type == TelescopeType.REFRACTOR
    assert scope.connection_type == ConnectionType.F_2
    assert scope.connection_gender == Gender.FEMALE
