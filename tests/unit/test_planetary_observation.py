from apts.utils import planetary
from apts.cache import get_timescale
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def test_planetary_calculations():
    ts = get_timescale()
    # Reference date: 2024-05-23 12:00 UTC
    t = ts.utc(2024, 5, 23, 12, 0)

    # Phase Angle
    moon_phase_angle = planetary.get_planet_phase_angle("moon", t)
    assert isinstance(moon_phase_angle, float)
    # Near Full Moon (May 23, 2024)
    assert 0 <= moon_phase_angle < 10.0

    # Moon Libration
    lib_lon, lib_lat = planetary.get_moon_libration(t)
    assert isinstance(lib_lon, float)
    assert isinstance(lib_lat, float)
    assert -10 <= lib_lon <= 10
    assert -10 <= lib_lat <= 10

    # Moon Position Angle
    moon_pa = planetary.get_moon_position_angle_bright_limb(t)
    assert isinstance(moon_pa, float)
    assert 0 <= moon_pa <= 360.0

def test_optical_path_exposure():
    # Setup a simple optical path
    telescope = Sky_watcherTelescope.Sky_Watcher_Evostar_80ED()
    camera = ZwoCamera.ZWO_ASI294MC_PRO()
    path = OpticalPath.from_path([telescope, camera])

    ts = get_timescale()
    t = ts.utc(2024, 5, 23, 12, 0)

    # Test exposed methods
    assert isinstance(path.planetary_phase_angle("moon", t), float)

    lib = path.moon_libration(t)
    assert len(lib) == 2
    assert all(isinstance(v, float) for v in lib)

    assert isinstance(path.moon_position_angle_bright_limb(t), float)
