import pytest
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.base import Telescope
from apts.opticalequipment.camera.base import Camera
from apts.opticalequipment.barlow.base import Barlow

def test_airy_disk_diameter():
    # Test setup: f/10 telescope (e.g., 100mm aperture, 1000mm focal length)
    t = Telescope(100, 1000, vendor="Test Scope")
    c = Camera(36, 24, 6000, 4000, vendor="Test Camera")
    path = OpticalPath.from_path([t, c])

    # Airy disk at 550nm (green) for f/10
    # D = 2.44 * 0.55 * 10 = 13.42 um
    diameter = path.airy_disk_diameter(wavelength_nm=550)
    assert diameter.magnitude == pytest.approx(13.42, abs=0.01)
    assert str(diameter.units) == "micrometer"

    # Test with Barlow: f/10 scope + 2x Barlow = f/20
    b = Barlow(2.0, vendor="Test Barlow")
    path_barlow = OpticalPath.from_path([t, b, c])

    # Airy disk at 550nm for f/20
    # D = 2.44 * 0.55 * 20 = 26.84 um
    diameter_barlow = path_barlow.airy_disk_diameter(wavelength_nm=550)
    assert diameter_barlow.magnitude == pytest.approx(26.84, abs=0.01)

def test_airy_disk_different_wavelengths():
    t = Telescope(100, 800, vendor="Test Scope") # f/8
    c = Camera(36, 24, 6000, 4000, vendor="Test Camera")
    path = OpticalPath.from_path([t, c])

    # Airy disk at 400nm (violet) for f/8
    # D = 2.44 * 0.4 * 8 = 7.808 um
    diameter_violet = path.airy_disk_diameter(wavelength_nm=400)
    assert diameter_violet.magnitude == pytest.approx(7.808, abs=0.01)

    # Airy disk at 700nm (red) for f/8
    # D = 2.44 * 0.7 * 8 = 13.664 um
    diameter_red = path.airy_disk_diameter(wavelength_nm=700)
    assert diameter_red.magnitude == pytest.approx(13.664, abs=0.01)
