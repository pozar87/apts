from apts.opticalequipment.smart_telescope import (
    SmartTelescope,
    normalize_smart_telescope_database_entry,
)


def test_normalize_smart_telescope_database_entry():
    raw_entry = {
        "aperture": 50,
        "focal_length": 250,
        "sensor_width": 6.4,
        "sensor_height": 4.5,
        "width": 1920,
        "height": 1080,
    }
    normalized = normalize_smart_telescope_database_entry(raw_entry)
    assert normalized["brand"] == "Unknown"
    assert normalized["name"] == "Unknown"
    assert normalized["mass"] == 0
    assert normalized["aperture"] == 50
    assert normalized["focal_length"] == 250


def test_smart_telescope_from_database_normalization():
    raw_entry = {
        "brand": "DWARFLAB",
        "name": "DWARF 3",
        "aperture": 35,
        "focal_length": 150,
        "sensor_width": 5.6,
        "sensor_height": 3.1,
        "width": 3840,
        "height": 2160,
        "pixel_size_um": 1.4,
        "mass": 1350,
    }
    scope = SmartTelescope.from_database(raw_entry)
    assert scope.vendor == "DWARFLAB DWARF 3"
    assert scope.aperture.to("mm").magnitude == 35
    assert scope.focal_length.to("mm").magnitude == 150
    assert scope.sensor_width.to("mm").magnitude == 5.6
    assert scope.sensor_height.to("mm").magnitude == 3.1
    assert scope.width == 3840
    assert scope.height == 2160
