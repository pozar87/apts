import pytest
import numpy as np
from apts.utils import planetary
from apts.cache import get_timescale

def test_mars_cml_accuracy():
    ts = get_timescale()
    # Reference: 2023-10-27 00:00:00 UTC
    # Verified via JPL HORIZONS: ObsSub-LON = 315.6192
    t = ts.utc(2023, 10, 27, 0, 0, 0)
    cml = planetary.get_mars_cml(t)

    assert pytest.approx(cml, abs=0.05) == 315.62

    # Reference: 2020-10-06 00:00:00 UTC (Opposition)
    # Verified via JPL HORIZONS: ObsSub-LON = 242.1466
    t2 = ts.utc(2020, 10, 6, 0, 0, 0)
    cml2 = planetary.get_mars_cml(t2)
    assert pytest.approx(cml2, abs=0.05) == 242.15

def test_mars_cml_vectorized():
    ts = get_timescale()
    t = ts.utc(2023, 10, 27, [0, 1, 2])
    cmls = planetary.get_mars_cml(t)

    assert isinstance(cmls, np.ndarray)
    assert len(cmls) == 3
    # Mars rotates ~14.6 degrees per hour (sidereal)
    # Sidereal day is 24.62h, so ~360/24.62 = 14.62 deg/h
    # Longitude increases westward
    assert cmls[1] > cmls[0]
    assert pytest.approx(cmls[1] - cmls[0], abs=0.1) == 14.62

def test_sub_observer_latitude_light_time():
    ts = get_timescale()
    t = ts.utc(2023, 10, 27, 0, 0, 0)
    # The sub-observer latitude (tilt)
    # For Oct 27, 2023, JPL HORIZONS: ObsSub-LAT = 17.98
    de = planetary.get_sub_observer_latitude("mars", t)
    assert pytest.approx(de, abs=0.3) == 17.98

    # For Oct 06, 2020, JPL HORIZONS: ObsSub-LAT = -19.66
    t2 = ts.utc(2020, 10, 6, 0, 0, 0)
    de2 = planetary.get_sub_observer_latitude("mars", t2)
    assert pytest.approx(de2, abs=0.3) == -19.66
