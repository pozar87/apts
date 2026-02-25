import pytest
from apts.place import Place
from apts.opticalequipment.camera import Camera


def test_moon_metrics():
    # New Moon was on 2024-02-09 around 22:59 UTC
    # Let's test on 2024-02-10 22:59 UTC - should be exactly 1.0 day

    place = Place(52.2297, 21.0122, name="Warsaw")
    place.date = place.ts.utc(2024, 2, 10, 22, 59)

    age = place.moon_age()
    # Skyfield returns days as float
    assert age >= 0.9 and age <= 1.1

    distance = place.moon_distance()
    # Typical moon distance 356k to 406k km
    assert distance > 350000 and distance < 410000


def test_asi585mc_specs():
    camera = Camera.ZWO_ASI585MC()
    assert camera.vendor == "ZWO ASI585MC"
    assert camera.sensor_width.magnitude == 11.13
    assert camera.sensor_height.magnitude == 6.26
    assert camera.width == 3840
    assert camera.height == 2160
    assert camera.pixel_size().to("micrometer").magnitude == pytest.approx(2.9)
    assert camera.quantum_efficiency == 91
    assert camera.full_well == 40000
    assert camera.read_noise == 0.8
