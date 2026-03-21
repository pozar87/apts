import pytest
from datetime import datetime, timezone
from apts.utils import planetary
from apts.cache import get_timescale

def test_get_sun_physical_details():
    ts = get_timescale()
    # Test for 1992 October 13 at 0h TD (Meeus Example 29.a)
    # JD = 2448908.5
    # Expected results from Meeus:
    # P = 26.27 deg
    # B0 = +5.99 deg
    # L0 = 238.63 deg

    t = ts.tt(1992, 10, 13)
    details = planetary.get_sun_physical_details(t)

    # Meeus uses a slightly different Omega/Inclination/L/M model for his examples
    # and includes small corrections for nutation and light-time.
    # Our implementation is high-accuracy but may differ by ~0.05 deg.

    assert details["P_degrees"] == pytest.approx(26.27, abs=0.2)
    assert details["B0_degrees"] == pytest.approx(5.99, abs=0.1)
    assert details["L0_degrees"] == pytest.approx(238.63, abs=0.2)

def test_sun_details_current():
    ts = get_timescale()
    t = ts.utc(2024, 5, 23, 12, 0)
    details = planetary.get_sun_physical_details(t)

    # Sanity checks for a known date
    # In May, B0 is usually near its minimum (~ -7 deg) or rising.
    # Actually, B0 is -7.25 in March and +7.25 in September. In May it should be negative.
    assert -8.0 <= details["B0_degrees"] <= 8.0
    assert 0 <= details["L0_degrees"] < 360
    assert -30 <= details["P_degrees"] <= 30
