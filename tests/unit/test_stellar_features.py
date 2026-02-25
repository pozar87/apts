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


def test_zwo_asi2600mm_pro_specs():
    camera = Camera.ZWO_ASI2600MM_PRO()
    assert camera.vendor == "ZWO ASI2600MM Pro"
    assert camera.sensor_width.magnitude == 23.5
    assert camera.sensor_height.magnitude == 15.7
    assert camera.width == 6248
    assert camera.height == 4176
    assert camera.pixel_size().to("micrometer").magnitude == pytest.approx(3.76)
    assert camera.quantum_efficiency == 91
    assert camera.full_well == 50000
    assert camera.read_noise == 1.0


def test_moon_phase_names():
    # We'll use a Place to test moon_phase_name
    # Coordinates for Greenwich
    place = Place(51.4778, 0.0015, "Greenwich")

    # New Moon: 2024-02-09 23:00 UTC
    place.date = place.ts.utc(2024, 2, 9, 23, 0)
    assert place.moon_phase_name() == "New Moon"

    # First Quarter: 2024-02-16 15:00 UTC
    place.date = place.ts.utc(2024, 2, 16, 15, 0)
    assert place.moon_phase_name() == "First Quarter"

    # Full Moon: 2024-02-24 12:30 UTC
    place.date = place.ts.utc(2024, 2, 24, 12, 30)
    assert place.moon_phase_name() == "Full Moon"

    # Last Quarter: 2024-03-03 15:23 UTC
    place.date = place.ts.utc(2024, 3, 3, 15, 23)
    assert place.moon_phase_name() == "Last Quarter"


def test_npf_rule_with_k():
    from apts.opticalequipment.telescope.base import Telescope
    from apts.optics import OpticalPath

    telescope = Telescope(80, 480, vendor="RedCat 51 Equivalent")  # f/6
    camera = Camera.ZWO_ASI2600MM_PRO()  # 3.76um
    path = OpticalPath(telescope, [], [], [], [], camera)

    # Declination 0
    t1 = path.npf_rule(declination=0, k=1.0)
    # n=6, p=3.76, f=480
    # t = (35*6 + 30*3.76) / 480 = (210 + 112.8) / 480 = 322.8 / 480 = 0.6725
    assert t1.magnitude == pytest.approx(0.6725)

    # With k=2.0
    t2 = path.npf_rule(declination=0, k=2.0)
    assert t2.magnitude == pytest.approx(1.345)

    # At the pole
    t_pole = path.npf_rule(declination=90)
    assert t_pole.magnitude == 3600
