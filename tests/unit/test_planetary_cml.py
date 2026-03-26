import pytest
import numpy as np
from apts.cache import get_timescale
from apts.utils import planetary

def test_shared_iau_cml_model():
    ts = get_timescale()
    t = ts.utc(2025, 1, 1)

    # Verify Mars CML (refactored)
    # Target value from previous implementation or JPL Horizons
    cml_mars = planetary.get_mars_cml(t)
    assert 0 <= cml_mars < 360

def test_saturn_cml_systems():
    ts = get_timescale()
    t = ts.utc(2025, 1, 1)

    cml1 = planetary.get_saturn_cml(t, system=1)
    cml2 = planetary.get_saturn_cml(t, system=2)
    cml3 = planetary.get_saturn_cml(t, system=3)

    # Systems have different rotation rates, so values should differ
    assert cml1 != cml2
    assert cml2 != cml3
    assert 0 <= cml1 < 360
    assert 0 <= cml2 < 360
    assert 0 <= cml3 < 360

def test_jupiter_system_iii():
    ts = get_timescale()
    t = ts.utc(2025, 1, 1)

    cml3 = planetary.get_jupiter_cml(t, system=3)
    cml2 = planetary.get_jupiter_cml(t, system=2)

    assert cml3 != cml2
    assert 0 <= cml3 < 360

def test_neptune_pole_precision():
    ts = get_timescale()
    # Test at J2000.0 (T=0)
    t0 = ts.utc(2000, 1, 1, 12, 0, 0)
    alpha, delta = planetary.get_planet_pole_coords("neptune", t0)

    # N = 357.85
    # alpha = 299.36 + 0.70 * sin(357.85) approx 299.36 - 0.026 = 299.33
    # delta = 43.46 - 0.51 * cos(357.85) approx 43.46 - 0.51 = 42.95
    assert pytest.approx(alpha, abs=0.1) == 299.33
    assert pytest.approx(delta, abs=0.1) == 42.95

def test_invalid_systems():
    ts = get_timescale()
    t = ts.utc(2025, 1, 1)

    with pytest.raises(ValueError, match="Only System I"):
        planetary.get_saturn_cml(t, system=4)

    with pytest.raises(ValueError, match="Only System I"):
        planetary.get_jupiter_cml(t, system=4)

def test_vectorized_iau_cml():
    ts = get_timescale()
    t = ts.utc(2025, 1, [1, 2])

    cml_mars = planetary.get_mars_cml(t)
    assert isinstance(cml_mars, np.ndarray)
    assert len(cml_mars) == 2

    cml_saturn = planetary.get_saturn_cml(t, system=3)
    assert isinstance(cml_saturn, np.ndarray)
    assert len(cml_saturn) == 2
