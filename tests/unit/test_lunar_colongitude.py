import pytest
import numpy as np
from apts.cache import get_timescale
from apts.utils import planetary

def test_moon_colongitude_scalar():
    ts = get_timescale()
    # 2026-01-25 05:37 UTC
    t = ts.utc(2026, 1, 25, 5, 37)

    # Expected approx 352.19 (calculated manually with IAU 2015 model)
    colong = planetary.get_moon_colongitude(t)

    assert isinstance(colong, float)
    assert 0 <= colong < 360
    assert pytest.approx(colong, abs=0.01) == 352.19

def test_moon_colongitude_vectorized():
    ts = get_timescale()
    t = ts.utc(2026, 1, 25, [5, 17], 37)

    colongs = planetary.get_moon_colongitude(t)

    assert isinstance(colongs, np.ndarray)
    assert len(colongs) == 2
    assert pytest.approx(colongs[0], abs=0.01) == 352.19
    assert pytest.approx(colongs[1], abs=0.01) == 358.27

def test_moon_colongitude_first_quarter():
    ts = get_timescale()
    # First Quarter is approx colongitude 270 (Sunrise at PM) or 358 (Standard definition for X/V)
    # Let's check a known First Quarter date: 2026-01-25 approx 20:00 UTC
    t = ts.utc(2026, 1, 25, 17, 53)
    colong = planetary.get_moon_colongitude(t)

    # Lunar X/V occur near colongitude 358
    assert pytest.approx(colong, abs=0.5) == 358.4
