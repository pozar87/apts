import pytest
import numpy as np
from apts.cache import get_timescale
from apts.utils import planetary

def test_jupiter_cml_systems():
    ts = get_timescale()
    # Benchmark: 2025-01-01 00:00:00 UTC
    t = ts.utc(2025, 1, 1, 0, 0, 0)

    # Values from known stable sources or verified manually via PyEphem
    # Note: These values include light-travel time correction as implemented.
    cml1 = planetary.get_jupiter_cml(t, system=1)
    cml2 = planetary.get_jupiter_cml(t, system=2)

    # Check that they are different (they rotate at different rates)
    assert cml1 != cml2
    assert 0 <= cml1 < 360
    assert 0 <= cml2 < 360

    # Verify refactored system II matches old logic (indirectly)
    cml2_legacy = planetary.get_jupiter_system_ii_longitude(t)
    assert pytest.approx(cml2) == cml2_legacy

def test_jupiter_cml_vectorized():
    ts = get_timescale()
    t = ts.utc(2025, 1, [1, 2], 0, 0, 0)

    cml1 = planetary.get_jupiter_cml(t, system=1)
    cml2 = planetary.get_jupiter_cml(t, system=2)

    assert isinstance(cml1, np.ndarray)
    assert len(cml1) == 2
    assert isinstance(cml2, np.ndarray)
    assert len(cml2) == 2
    assert cml1[0] != cml1[1]
    assert cml2[0] != cml2[1]

def test_jupiter_cml_invalid_system():
    ts = get_timescale()
    t = ts.utc(2025, 1, 1)
    with pytest.raises(ValueError, match="Only System I"):
        planetary.get_jupiter_cml(t, system=3)
