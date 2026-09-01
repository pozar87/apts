import numpy as np
import pytest

from apts.optics.calculations.telescope import (
    calculate_focal_ratio,
    calculate_aperture_area,
    calculate_effective_aperture,
    calculate_light_grasp_ratio,
    calculate_dawes_limit,
    calculate_rayleigh_limit,
    calculate_limiting_magnitude,
    calculate_highest_useful_magnification,
    calculate_lowest_useful_magnification,
)
from apts.opticalequipment.telescope import Telescope


def test_calculate_focal_ratio():
    assert calculate_focal_ratio(1000.0, 200.0) == pytest.approx(5.0)
    assert calculate_focal_ratio(500.0, 80.0) == pytest.approx(6.25)
    assert calculate_focal_ratio(1000.0, 0.0) == 0.0


def test_calculate_aperture_area():
    # 200mm aperture without obstruction: pi * 100^2 = 31415.9265
    area_clear = calculate_aperture_area(200.0, 0.0)
    assert area_clear == pytest.approx(np.pi * 10000.0)

    # 200mm aperture with 50mm obstruction
    area_obs = calculate_aperture_area(200.0, 50.0)
    assert area_obs == pytest.approx(np.pi * (40000.0 - 2500.0) / 4.0)


def test_calculate_effective_aperture():
    eff_clear = calculate_effective_aperture(200.0, 0.0)
    assert eff_clear == pytest.approx(200.0)

    eff_obs = calculate_effective_aperture(200.0, 50.0)
    assert eff_obs == pytest.approx(np.sqrt(40000.0 - 2500.0))


def test_calculate_light_grasp_ratio():
    # Comparing 200mm to 100mm -> ratio = (200/100)^2 = 4.0
    ratio = calculate_light_grasp_ratio(200.0, 100.0)
    assert ratio == pytest.approx(4.0)

    assert calculate_light_grasp_ratio(200.0, 0.0) == 0.0


def test_telescope_class_delegations():
    scope = Telescope(200.0, 1000.0, central_obstruction=50.0)

    # Test focal_ratio
    assert float(scope.focal_ratio().magnitude) == pytest.approx(5.0)

    # Test aperture_area
    expected_area = np.pi * (200.0**2 - 50.0**2) / 4.0
    assert float(scope.aperture_area().magnitude) == pytest.approx(expected_area)

    # Test effective_aperture
    expected_eff = np.sqrt(200.0**2 - 50.0**2)
    assert float(scope.effective_aperture().magnitude) == pytest.approx(expected_eff)

    # Test light_grasp_ratio
    assert float(scope.light_grasp_ratio(100.0)) == pytest.approx((expected_eff / 100.0) ** 2)
