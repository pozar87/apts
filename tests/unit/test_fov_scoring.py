import pytest
import numpy as np
import pandas as pd
from apts.optics.utils import OpticsUtils
from apts.units import get_unit_registry

ureg = get_unit_registry()

def test_calculate_fov_ratio_scalar_float():
    ratio = OpticsUtils.calculate_fov_ratio((60, 30), (22.2, 14.8), 750)
    assert isinstance(ratio, (float, np.float64))
    # 60 arcmin = 1 deg.
    # FOV width = 2 * arctan(22.2 / 1500) = 1.6958 deg
    # Ratio = 1 / 1.6958 * 100 = 58.96
    assert ratio == pytest.approx(58.96, rel=1e-3)

def test_calculate_fov_ratio_scalar_quantity():
    ratio = OpticsUtils.calculate_fov_ratio(
        (1 * ureg.degree, 30 * ureg.arcminute),
        (22.2, 14.8),
        750
    )
    assert ratio == pytest.approx(58.96, rel=1e-3)

def test_calculate_fov_ratio_array_float():
    ratios = OpticsUtils.calculate_fov_ratio(
        (np.array([60, 120]), np.array([30, 60])),
        (22.2, 14.8),
        750
    )
    assert len(ratios) == 2
    assert ratios[0] == pytest.approx(58.96, rel=1e-3)
    assert ratios[1] == pytest.approx(117.93, rel=1e-3)

def test_calculate_fov_ratio_array_quantities():
    # This is the case that was failing
    major = np.array([60 * ureg.arcminute, 120 * ureg.arcminute], dtype=object)
    minor = np.array([30 * ureg.arcminute, 60 * ureg.arcminute], dtype=object)
    ratios = OpticsUtils.calculate_fov_ratio(
        (major, minor),
        (22.2, 14.8),
        750
    )
    assert len(ratios) == 2
    assert ratios[0] == pytest.approx(58.96, rel=1e-3)
    assert ratios[1] == pytest.approx(117.93, rel=1e-3)

def test_calculate_fov_ratio_quantity_wrapping_array():
    major = np.array([60, 120]) * ureg.arcminute
    minor = np.array([30, 60]) * ureg.arcminute
    ratios = OpticsUtils.calculate_fov_ratio(
        (major, minor),
        (22.2, 14.8),
        750
    )
    assert len(ratios) == 2
    assert ratios[0] == pytest.approx(58.96, rel=1e-3)
    assert ratios[1] == pytest.approx(117.93, rel=1e-3)

def test_calculate_fov_ratio_mixed_list():
    major = [60 * ureg.arcminute, 120] # 120 assumed arcmin if raw float
    minor = [30, 60 * ureg.arcminute]
    ratios = OpticsUtils.calculate_fov_ratio(
        (major, minor),
        (22.2, 14.8),
        750
    )
    assert len(ratios) == 2
    assert ratios[0] == pytest.approx(58.96, rel=1e-3)
    assert ratios[1] == pytest.approx(117.93, rel=1e-3)
