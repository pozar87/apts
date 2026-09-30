from apts.opticalequipment.camera import Camera, normalize_camera_database_entry
from apts.utils import ConnectionType, Gender


def test_normalize_camera_database_entry_complete():
    entry = {
        "brand": "ZWO",
        "name": "ASI533MC Pro",
        "sensor_width_mm": 11.31,
        "sensor_height_mm": 11.31,
        "width": 3008,
        "height": 3008,
        "inputs": [(ConnectionType.M42, Gender.FEMALE)],
    }
    normalized = normalize_camera_database_entry(entry)
    assert normalized["sensor_width_mm"] == 11.31
    assert normalized["sensor_height_mm"] == 11.31
    assert normalized["width"] == 3008
    assert normalized["height"] == 3008
    assert normalized["inputs"] == [(ConnectionType.M42, Gender.FEMALE)]


def test_normalize_camera_database_entry_default_heuristics():
    entry = {
        "brand": "Generic",
        "name": "ApsC Camera",
        "tside_thread": "T2",
        "tside_gender": "Female",
    }
    normalized = normalize_camera_database_entry(entry)
    assert normalized["sensor_width_mm"] == 23.5
    assert normalized["sensor_height_mm"] == 15.7
    assert normalized["width"] == 6000
    assert normalized["height"] == 4000
    assert normalized["inputs"] == [(ConnectionType.T2, Gender.FEMALE)]


def test_normalize_camera_database_entry_full_frame_heuristics():
    entry = {
        "brand": "Canon",
        "name": "EOS Full Frame 36x24",
    }
    normalized = normalize_camera_database_entry(entry)
    assert normalized["sensor_width_mm"] == 35.9
    assert normalized["sensor_height_mm"] == 23.9
    assert normalized["width"] == 8256
    assert normalized["height"] == 5504


def test_normalize_camera_database_entry_mft_heuristics():
    entry = {
        "brand": "ZWO",
        "name": "ASI Micro Four Thirds",
    }
    normalized = normalize_camera_database_entry(entry)
    assert normalized["sensor_width_mm"] == 17.3
    assert normalized["sensor_height_mm"] == 13.0
    assert normalized["width"] == 4656
    assert normalized["height"] == 3520


def test_camera_class_normalize_and_from_database():
    raw_entry = {
        "brand": "ZWO",
        "name": "ASI533MC Pro",
        "sensor_width_mm": 11.31,
        "sensor_height_mm": 11.31,
        "width": 3008,
        "height": 3008,
        "tside_thread": "M42",
        "tside_gender": "Female",
    }
    normalized = Camera.normalize_database_entry(raw_entry)
    assert normalized["inputs"] == [(ConnectionType.M42, Gender.FEMALE)]

    cam = Camera.from_database(raw_entry)
    assert cam.sensor_width.magnitude == 11.31
    assert cam.sensor_height.magnitude == 11.31
    assert cam.width == 3008
    assert cam.height == 3008
    assert cam.vendor == "ZWO ASI533MC Pro"
