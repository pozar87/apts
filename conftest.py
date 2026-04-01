import pytest
from skyfield.api import load
import apts.cache
import copy
import os

@pytest.fixture(autouse=True)
def use_jup310(monkeypatch):
    if os.path.exists('jup310.bsp'):
        print("\n[DEBUG] conftest: loading jup310.bsp")
        eph_jovian = load('jup310.bsp')
        # Load de421 for planetary data
        eph_planetary = load('de421.bsp')
        merged_eph = copy.copy(eph_jovian)
        merged_eph.segments = list(eph_jovian.segments) + list(eph_planetary.segments)

        # Test if it actually merged
        print(f"[DEBUG] conftest: Merged segments: {len(merged_eph.segments)}")

        monkeypatch.setattr(apts.cache, "get_jovian_ephemeris", lambda: merged_eph)
        monkeypatch.setattr(apts.cache, "get_ephemeris", lambda: merged_eph)
    else:
        print("\n[DEBUG] conftest: jup310.bsp NOT FOUND")
