import pytest
from datetime import datetime, timezone
from typing import Any, cast

from apts.cache import get_timescale
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.base import Telescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils import planetary

def test_jupiter_angular_diameter():
    ts = get_timescale()
    # Jupiter opposition was around 2023-11-03
    t = ts.utc(2023, 11, 3, 12, 0)

    # Expected angular diameter for Jupiter at opposition is ~49 arcseconds
    diam = planetary.get_planet_angular_diameter("Jupiter", t)
    assert diam == pytest.approx(49.5, abs=1.0)

def test_planetary_projection_size():
    ts = get_timescale()
    t = ts.utc(2023, 11, 3, 12, 0)

    # Setup: C8 (2032mm focal length) with ASI224MC (3.75um pixels)
    # Using a 2x Barlow (effective FL = 4064mm)
    scope = Telescope(203, 2032, vendor="C8")
    camera = cast(Any, ZwoCamera).ZWO_ASI_224MC()

    from apts.opticalequipment.barlow import Barlow
    barlow = Barlow(2.0, "2x Barlow")

    path = OpticalPath(scope, [barlow], [], [], [], camera)

    # Pixel scale: (3.75 / 4064) * 206265 = 0.19 arcsec/pixel
    scale = path.pixel_scale()
    assert scale.magnitude == pytest.approx(0.19, abs=0.01)

    # Jupiter size in pixels: 49.5 / 0.19 = ~260 pixels
    size_px = path.planetary_size_in_pixels("Jupiter", t)
    assert size_px == pytest.approx(260, abs=10)

def test_planet_radius_lookup():
    assert planetary.get_planet_radius_km("Mars") == pytest.approx(3396.2)
    assert planetary.get_planet_radius_km("Jupiter") == pytest.approx(71492.0)
    with pytest.raises(ValueError):
        planetary.get_planet_radius_km("UnknownBody")

def test_planet_distance():
    ts = get_timescale()
    t = ts.utc(2023, 11, 3, 12, 0)
    # Geocentric distance to Jupiter at opposition is roughly 4 AU
    dist = planetary.get_planet_distance_km("Jupiter", t)
    assert dist / 149597870.7 == pytest.approx(3.98, abs=0.1)
