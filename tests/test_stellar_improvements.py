from typing import Any, cast

import numpy
import pytest

from apts.opticalequipment.camera import Camera
from apts.opticalequipment.filter import Filter
from apts.opticalequipment.telescope import Telescope
from apts.optics import OpticalPath
from apts.units import get_unit_registry


def test_new_cameras():
    mc = cast(Any, Camera).ZWO_ASI294MC_PRO()
    assert mc.vendor == "ZWO ASI294MC Pro"
    assert mc.sensor_width.magnitude == 19.1
    assert mc.sensor_height.magnitude == 13.0
    assert mc.width == 4144
    assert mc.height == 2822
    assert mc.read_noise == 1.2
    assert mc.full_well == 63700
    assert mc.quantum_efficiency == 75
    assert cast(Any, mc._pixel_size).to("micrometer").magnitude == 4.63

    mm = cast(Any, Camera).ZWO_ASI294MM_PRO()
    assert mm.vendor == "ZWO ASI294MM Pro"
    assert mm.quantum_efficiency == 90
    assert mm.full_well == 66000


def test_sky_flux_with_filters():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(
        sensor_width=36,
        sensor_height=24,
        width=6000,
        height=4000,
        pixel_size=3.76,
        read_noise=1.2,
        quantum_efficiency=80,
    )
    f1 = Filter(name="L-Pro", transmission=0.9)
    f2 = Filter(name="Some Filter", transmission=0.8)

    path_no_filter = OpticalPath(t, [], [], [], [], c)
    path_with_filters = OpticalPath(t, [], [], [f1, f2], [], c)

    flux_no_filter = path_no_filter.sky_flux(sqm=21)
    flux_with_filters = path_with_filters.sky_flux(sqm=21)

    # Ensure fluxes are not None before calculation
    assert flux_no_filter is not None
    assert flux_with_filters is not None

    # Flux with filters should be 0.9 * 0.8 = 0.72 of flux without filters
    assert numpy.isclose(flux_with_filters, flux_no_filter * 0.72)


def test_object_flux():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(
        sensor_width=36,
        sensor_height=24,
        width=6000,
        height=4000,
        pixel_size=3.76,
        read_noise=1.2,
        quantum_efficiency=80,
    )
    path = OpticalPath(t, [], [], [], [], c)

    # If sqm == magnitude, object_flux should be sky_flux / pixel_area_arcsec2
    sqm = 21
    mag = 21
    s_flux = path.sky_flux(sqm=sqm)
    o_flux = path.object_flux(magnitude=mag)
    p_scale = path.pixel_scale()

    assert s_flux is not None
    assert o_flux is not None
    assert p_scale is not None

    scale = cast(Any, path.pixel_scale()).magnitude

    assert numpy.isclose(o_flux, s_flux / (scale**2))


def test_snr():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(
        sensor_width=36,
        sensor_height=24,
        width=6000,
        height=4000,
        pixel_size=3.76,
        read_noise=1.2,
        quantum_efficiency=80,
    )
    path = OpticalPath(t, [], [], [], [], c)

    # High SNR case: bright star, dark sky, long exposure
    snr_high = path.snr(magnitude=10, sqm=21, exposure_time=60)
    # Low SNR case: faint star, bright sky, short exposure
    snr_low = path.snr(magnitude=18, sqm=18, exposure_time=1)

    assert snr_high is not None
    assert snr_low is not None

    assert snr_high > snr_low
    assert snr_high > 0
    assert snr_low > 0

    # Stacking subs should increase SNR by sqrt(N) approximately (if not dominated by shot noise)
    snr_1 = path.snr(magnitude=15, sqm=21, exposure_time=30, n_subs=1)
    snr_4 = path.snr(magnitude=15, sqm=21, exposure_time=30, n_subs=4)

    assert snr_1 is not None
    assert snr_4 is not None

    assert numpy.isclose(snr_4, snr_1 * 2, rtol=0.1)


def test_stellar_limits_and_helpers():
    # 8-inch SCT (203.2 mm aperture, 2032 mm focal length)
    telescope = Telescope(203.2, 2032, vendor="Celestron C8")
    # ZWO ASI2600MM Pro (3.76 micron pixels)
    camera = Camera(23.5, 15.7, 6248, 4176, vendor="ZWO ASI2600MM Pro", pixel_size=3.76)

    path = OpticalPath(telescope, [], [], [], [], camera)

    # Dawes' Limit: 11.6 / 20.32 cm = 0.57086...
    assert cast(Any, path.dawes_limit()).magnitude == pytest.approx(0.571, abs=1e-3)

    # Rayleigh Limit: 1.22 * 550e-9 / 0.2032 * 206265 = 0.6808...
    assert cast(Any, path.rayleigh_limit()).magnitude == pytest.approx(0.681, abs=1e-3)

    # Ideal Planetary Focal Ratio: 5 * 3.76 = 18.8
    assert path.ideal_planetary_focal_ratio(k=5.0) == pytest.approx(18.8)
    # With k=3.0: 3 * 3.76 = 11.28
    assert path.ideal_planetary_focal_ratio(k=3.0) == pytest.approx(11.28)


def test_limits_without_telescope_support():
    # Create a mock-like object that doesn't have the methods
    class FakeOptic:
        def __init__(self):
            self.focal_length = 500 * get_unit_registry().mm

    path = OpticalPath(FakeOptic(), [], [], [], [], None)
    assert path.dawes_limit() is None
    assert path.rayleigh_limit() is None
    assert path.ideal_planetary_focal_ratio() is None


def test_camera_pixel_size_units():
    ureg = get_unit_registry()
    # Case 1: Explicit pixel size
    cam1 = Camera(
        sensor_width=23.5, sensor_height=15.7, width=6000, height=4000, pixel_size=3.76
    )
    ps1 = cam1.pixel_size()
    assert ps1.units == ureg.micrometer
    assert ps1.magnitude == pytest.approx(3.76)

    # Case 2: Calculated pixel size from mm dimensions
    cam2 = Camera(sensor_width=23.5, sensor_height=15.7, width=6000, height=4000)
    ps2 = cam2.pixel_size()
    assert ps2.units == ureg.micrometer
    assert ps2.magnitude == pytest.approx(3.919, abs=1e-3)


def test_seestar_s30_instantiation():
    ureg = get_unit_registry()
    from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope

    s30 = ZwoTelescope.ZWO_Seestar_S30()
    assert s30.get_vendor() == "ZWO Seestar S30"
    assert s30.aperture.to(ureg.mm).magnitude == 30
    assert s30.focal_length.to(ureg.mm).magnitude == 150
    assert s30.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(2.9)
    assert s30.mass.to(ureg.gram).magnitude == 1650


def test_seestar_s30_pro_instantiation():
    ureg = get_unit_registry()
    from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope

    s30p = ZwoTelescope.ZWO_Seestar_S30_Pro()
    assert s30p.get_vendor() == "ZWO Seestar S30 Pro"
    assert s30p.aperture.to(ureg.mm).magnitude == 30
    assert s30p.focal_length.to(ureg.mm).magnitude == 160
    assert s30p.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(2.9)
    assert s30p.mass.to(ureg.gram).magnitude == 1650


def test_planetary_radii():
    from apts.constants import astronomy

    assert astronomy.JUPITER_RADIUS_KM == 71492.0
    assert astronomy.SATURN_RADIUS_KM == 60268.0
    assert astronomy.EARTH_RADIUS_KM == 6378.1
    assert astronomy.VENUS_RADIUS_KM == 6051.8
    assert astronomy.MARS_RADIUS_KM == 3396.2
    assert astronomy.URANUS_RADIUS_KM == 25559.0
    assert astronomy.NEPTUNE_RADIUS_KM == 24764.0
    assert astronomy.PLUTO_RADIUS_KM == 1188.3


def test_total_solar_eclipse_classification():
    # April 8, 2024 Total Solar Eclipse
    # Dallas, TX (in path of totality)
    from datetime import datetime, timezone

    from apts.place import Place
    from apts.skyfield_searches import find_solar_eclipses

    dallas = Place(32.7767, -96.7970, "Dallas", 131)
    start = datetime(2024, 4, 8, 17, 0, tzinfo=timezone.utc)
    end = datetime(2024, 4, 8, 20, 0, tzinfo=timezone.utc)

    eclipses = find_solar_eclipses(dallas.observer, start, end)

    assert len(eclipses) > 0
    best_eclipse = max(eclipses, key=lambda x: x["obscuration"])

    assert best_eclipse["eclipse_type"] == "Total"
    assert (
        best_eclipse["obscuration"] >= 0.99
    )  # Numerical precision with topocentric radii
    assert best_eclipse["magnitude"] >= 1.0


def test_partial_solar_eclipse_classification():
    # April 8, 2024 Total Solar Eclipse
    # New York, NY (Partial from here)
    from datetime import datetime, timezone

    from apts.place import Place
    from apts.skyfield_searches import find_solar_eclipses

    nyc = Place(40.7128, -74.0060, "NYC", 10)
    start = datetime(2024, 4, 8, 17, 0, tzinfo=timezone.utc)
    end = datetime(2024, 4, 8, 20, 0, tzinfo=timezone.utc)

    eclipses = find_solar_eclipses(nyc.observer, start, end)

    assert len(eclipses) > 0
    best_eclipse = max(eclipses, key=lambda x: x["obscuration"])

    assert best_eclipse["eclipse_type"] == "Partial"
    assert 0.8 < best_eclipse["obscuration"] < 1.0
    assert 0.8 < best_eclipse["magnitude"] < 1.0


def test_conjunction_step_logic():
    # Check that Moon conjunctions use fine step
    # and results are accurate.
    # Moon-Jupiter on Jan 18, 2024
    from datetime import datetime, timezone

    from apts.place import Place
    from apts.skyfield_searches import find_conjunctions

    place = Place(51.4779, 0.0, "Greenwich", 46)
    start = datetime(2024, 1, 18, 0, 0, tzinfo=timezone.utc)
    end = datetime(2024, 1, 19, 0, 0, tzinfo=timezone.utc)

    conjs = find_conjunctions(place.observer, "moon", "jupiter barycenter", start, end)

    assert len(conjs) > 0
    peak = conjs[0]
    # Expected peak is around 18:41 UTC
    assert peak["date"].hour == 18
    assert 35 <= peak["date"].minute <= 45


def test_eclipse_rarity_and_naming():
    # April 8, 2024 Dallas
    from datetime import datetime, timezone

    from apts.constants.event_types import EventType
    from apts.events import AstronomicalEvents
    from apts.place import Place

    dallas = Place(32.7767, -96.7970, "Dallas", 131)
    start = datetime(2024, 4, 8, 0, 0, tzinfo=timezone.utc)
    end = datetime(2024, 4, 9, 0, 0, tzinfo=timezone.utc)

    events_obj = AstronomicalEvents(
        dallas, start, end, events_to_calculate=[EventType.SOLAR_ECLIPSES]
    )
    events = events_obj.get_events()

    assert not events.empty
    eclipse_event = events[events["type"] == "Solar Eclipse"].iloc[0]

    assert "Total Solar Eclipse" in eclipse_event["event"]
    assert eclipse_event["rarity"] == 5
