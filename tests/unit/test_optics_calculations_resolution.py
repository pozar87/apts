import pytest
import math
from apts.optics.calculations.resolution import (
    calculate_critical_focus_zone,
    calculate_nyquist_focal_ratio,
    calculate_psf_peak_fraction,
)


def test_calculate_critical_focus_zone():
    # CFZ = 2.44 * (wavelength_nm / 1000) * focal_ratio^2
    # At focal_ratio = 5.0 and wavelength = 550nm:
    # CFZ = 2.44 * 0.55 * 25.0 = 33.55
    cfz = calculate_critical_focus_zone(focal_ratio=5.0, wavelength_nm=550)
    assert pytest.approx(cfz, abs=1e-5) == 33.55

    # At focal_ratio = 10.0 and wavelength = 400nm:
    # CFZ = 2.44 * 0.40 * 100.0 = 97.6
    cfz_2 = calculate_critical_focus_zone(focal_ratio=10.0, wavelength_nm=400)
    assert pytest.approx(cfz_2, abs=1e-5) == 97.6


def test_calculate_nyquist_focal_ratio():
    # f/D = (pixel_pitch_um * sampling_factor) / (1.22 * (wavelength_nm / 1000))
    # At pixel_pitch = 3.76, sampling_factor = 3.0, wavelength = 550nm:
    # (3.76 * 3.0) / (1.22 * 0.55) = 11.28 / 0.671 = 16.81073
    nfr = calculate_nyquist_focal_ratio(
        pixel_pitch_um=3.76, wavelength_nm=550, sampling_factor=3.0
    )
    expected = (3.76 * 3.0) / (1.22 * 0.55)
    assert pytest.approx(nfr, abs=1e-5) == expected


def test_calculate_psf_peak_fraction():
    # fraction = erf((pixel_scale_arcsec * sqrt(ln(2))) / seeing_arcsec)^2
    # If seeing_arcsec <= 0, returns 0.0
    assert calculate_psf_peak_fraction(pixel_scale_arcsec=1.0, seeing_arcsec=-0.5) == 0.0
    assert calculate_psf_peak_fraction(pixel_scale_arcsec=1.0, seeing_arcsec=0.0) == 0.0

    # At pixel_scale = 2.392674 and seeing = 1.0:
    # arg = 2.392674 * sqrt(ln(2)) / 1.0 = 1.992
    # expected = erf(1.992)^2
    pixel_scale = 2.392674
    seeing = 1.0
    arg = (pixel_scale * math.sqrt(math.log(2))) / seeing
    expected = math.erf(arg) ** 2
    fraction = calculate_psf_peak_fraction(pixel_scale_arcsec=pixel_scale, seeing_arcsec=seeing)
    assert pytest.approx(fraction, abs=1e-5) == expected
