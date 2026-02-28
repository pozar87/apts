import numpy
from typing import Any, cast
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.barlow import Barlow
from apts.optics import OpticalPath


def test_sampling():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(36, 24, 6000, 4000, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)

    # Pixel scale = (3.76 / 750) * 206265 = 1.034 arcsec/pixel
    # Seeing 2.0 / 1.034 = 1.93 -> Well-sampled (1.0 <= ratio <= 2.0)
    assert path.sampling(2.0) == "Well-sampled"
    assert path.sampling_status(2.0) == "Well-sampled"

    # Seeing 0.5 / 1.034 = 0.48 -> Under-sampled (ratio < 1.0)
    assert path.sampling(0.5) == "Under-sampled"

    # Seeing 3.0 / 1.034 = 2.9 -> Over-sampled (ratio > 2.0)
    assert path.sampling(3.0) == "Over-sampled"


def test_sampling_none():
    t = Telescope(aperture=150, focal_length=750)
    # Output is not a camera
    path = OpticalPath(t, [], [], [], [], t)
    assert path.sampling(2.0) is None


def test_critical_focus_zone():
    t = Telescope(aperture=150, focal_length=750)  # f/5
    path = OpticalPath(t, [], [], [], [], t)

    # CFZ = 2.44 * (550/1000) * 5^2 = 2.44 * 0.55 * 25 = 33.55 micrometer
    cfz = path.critical_focus_zone(wavelength=550)
    assert cfz is not None
    # Cast to Any to handle Pint Quantity type ambiguity in static analysis
    assert numpy.isclose(cast(Any, cfz).to("micrometer").magnitude, 33.55)


def test_npf_rule():
    t = Telescope(aperture=150, focal_length=750)  # f/5
    c = Camera(36, 24, 6000, 4000, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)

    # N = 5, P = 3.76, F = 750, dec = 0
    # t = (35 * 5 + 30 * 3.76) / (750 * cos(0))
    # t = (175 + 112.8) / 750 = 287.8 / 750 = 0.3837 seconds
    npf = path.npf_rule(declination=0)
    assert npf is not None
    assert numpy.isclose(cast(Any, npf).to("second").magnitude, 0.3837, atol=0.001)


def test_npf_rule_zero_focal_length():
    t = Telescope(aperture=150, focal_length=0)
    c = Camera(36, 24, 6000, 4000, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)
    npf = path.npf_rule(declination=0)
    assert npf is not None
    assert cast(Any, npf).to("second").magnitude == 0


def test_rule_of_500():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(36, 24, 6000, 4000, pixel_size=3.76)  # Full frame-ish sensor
    path = OpticalPath(t, [], [], [], [], c)

    # diagonal = sqrt(36^2 + 24^2) = 43.266
    # crop_factor = 43.27 / 43.266 = 1.00008
    # t = 500 / (750 * 1.00008) = 500 / 750.06 = 0.6666 seconds
    r500 = path.rule_of_500()
    assert r500 is not None
    assert numpy.isclose(cast(Any, r500).to("second").magnitude, 0.6666, atol=0.001)


def test_rule_of_500_with_barlow():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(36, 24, 6000, 4000, pixel_size=3.76)
    b = Barlow(magnification=2.0)
    path = OpticalPath(t, [b], [], [], [], c)

    # effective F = 1500
    # t = 500 / (1500 * 1.00008) = 0.3333 seconds
    r500 = path.rule_of_500()
    assert r500 is not None
    assert numpy.isclose(cast(Any, r500).to("second").magnitude, 0.3333, atol=0.001)
