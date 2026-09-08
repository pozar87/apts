import math

import pytest

from apts import Catalogs, Place
from apts.discovery import DiscoveryService
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.william_optics import (
    William_opticsTelescope,
)
from apts.optics import OpticalPath


@pytest.fixture
def test_setup():
    place = Place(52.2297, 21.0122)  # Warsaw
    telescope = William_opticsTelescope.William_Optics_RedCat_61()
    camera = ZwoCamera.ZWO_ASI_2600MC_Pro()
    path = OpticalPath(telescope, [], [], [], [], camera)
    catalogs = Catalogs()
    return place, path, catalogs


def test_discovery_default_include_ngc_false(test_setup):
    place, path, catalogs = test_setup
    picks = DiscoveryService.get_top_picks(
        place, path, catalogs, limit=20, include_ngc=False
    )

    assert len(picks) > 0
    for item in picks:
        assert "Name" in item
        assert "Type" in item
        assert "Score" in item
        assert "Details" in item
        assert "fov_ratio" in item
        assert "size_major_arcmin" in item
        assert "size_minor_arcmin" in item
        assert isinstance(item["fov_ratio"], float)


def test_discovery_include_ngc_true(test_setup):
    place, path, catalogs = test_setup
    picks_messier_only = DiscoveryService.get_top_picks(
        place, path, catalogs, limit=100, include_ngc=False
    )
    messier_names = {p["Name"] for p in picks_messier_only}

    picks_with_ngc = DiscoveryService.get_top_picks(
        place, path, catalogs, limit=100, include_ngc=True, ngc_magnitude_limit=12.0
    )

    assert len(picks_with_ngc) > 0

    # Should contain NGC objects that were not in Messier-only list
    new_ngc_objects = [p for p in picks_with_ngc if p["Name"] not in messier_names]
    assert len(new_ngc_objects) > 0, "Expected NGC objects to be recommended"

    # Confirm formatting
    for p in picks_with_ngc:
        assert "fov_ratio" in p
        assert "size_major_arcmin" in p
        assert "size_minor_arcmin" in p


def test_discovery_ngc_magnitude_limit(test_setup):
    place, path, catalogs = test_setup
    # Strict magnitude limit (only bright objects <= 7.0 mag)
    picks_strict = DiscoveryService.get_top_picks(
        place, path, catalogs, limit=100, include_ngc=True, ngc_magnitude_limit=7.0
    )
    # Lenient magnitude limit (up to 13.0 mag)
    picks_lenient = DiscoveryService.get_top_picks(
        place, path, catalogs, limit=100, include_ngc=True, ngc_magnitude_limit=13.0
    )

    assert len(picks_lenient) >= len(picks_strict)


def test_discovery_min_fov_ratio_hard_filter(test_setup):
    place, path, catalogs = test_setup
    min_ratio = 30.0

    picks_filtered = DiscoveryService.get_top_picks(
        place,
        path,
        catalogs,
        limit=50,
        include_ngc=True,
        ngc_magnitude_limit=13.0,
        min_fov_ratio=min_ratio,
    )

    assert len(picks_filtered) > 0
    for p in picks_filtered:
        assert p["fov_ratio"] >= min_ratio
        assert not math.isnan(p["fov_ratio"])
