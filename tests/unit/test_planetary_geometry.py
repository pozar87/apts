from skyfield.api import load
from apts.utils import planetary
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def test_planetary_geometry_oblateness():
    ts = load.timescale()
    t = ts.utc(2024, 5, 22)

    # Jupiter is highly oblate
    d_eq = planetary.get_planet_angular_diameter("Jupiter", t, which="equatorial")
    d_pol = planetary.get_planet_angular_diameter("Jupiter", t, which="polar")
    d_app = planetary.get_planet_angular_diameter("Jupiter", t, which="apparent_polar")

    # Equatorial diameter should be greater than polar
    assert d_eq > d_pol
    # Apparent polar diameter should be between polar and equatorial (or equal to one of them)
    assert d_pol <= d_app <= d_eq

    # Check specific values (approximate)
    # Jupiter eq radius ~71492, pol ~66854 -> ratio ~0.935
    assert 0.93 <= (d_pol / d_eq) <= 0.94

def test_planetary_phase_percentage():
    ts = load.timescale()
    t = ts.utc(2024, 5, 22)

    # Venus phase in May 2024 should be high
    phase = planetary.get_planet_phase("Venus", t)
    assert 0 <= phase <= 100
    assert phase > 90 # Venus is near superior conjunction

def test_optical_path_planetary_size():
    ts = load.timescale()
    t = ts.utc(2024, 5, 22)

    # Setup: 8" Newtonian (1000mm) + ASI585MC (2.9um)
    telescope = Sky_watcherTelescope.Sky_Watcher_200PDS_Newtonian()
    camera = ZwoCamera.ZWO_ASI585MC()
    path = OpticalPath.from_path([telescope, camera])

    # Get Jupiter size in pixels
    size_eq = path.planetary_size_in_pixels("Jupiter", t, which="equatorial")
    size_pol = path.planetary_size_in_pixels("Jupiter", t, which="polar")

    assert size_eq > 0
    assert size_pol > 0
    assert size_eq > size_pol

def test_sub_observer_latitude_range():
    ts = load.timescale()
    t = ts.utc(2024, 5, 22)

    # Saturn tilt should be significant
    lat = planetary.get_sub_observer_latitude("Saturn", t)
    # Saturn's rings are currently closing but tilt is still non-zero
    assert -30 <= lat <= 30

def test_planetary_geometry_apparent_polar_coverage():
    ts = load.timescale()
    # Test Saturn when tilt is significant (e.g., 2017)
    t = ts.utc(2017, 6, 15)

    d_eq = planetary.get_planet_angular_diameter("Saturn", t, which="equatorial")
    d_pol = planetary.get_planet_angular_diameter("Saturn", t, which="polar")
    d_app = planetary.get_planet_angular_diameter("Saturn", t, which="apparent_polar")

    # In 2017, Saturn's tilt was near maximum (~27°).
    # d_app = d_eq * sqrt(1 - (2f - f^2) * cos^2(tilt))
    # As tilt increases (away from 0), d_app should increase from d_pol towards d_eq.
    assert d_pol < d_app < d_eq

    # Test Mars (oblate)
    d_eq_m = planetary.get_planet_angular_diameter("Mars", t, which="equatorial")
    d_pol_m = planetary.get_planet_angular_diameter("Mars", t, which="polar")
    d_app_m = planetary.get_planet_angular_diameter("Mars", t, which="apparent_polar")

    assert d_eq_m > d_pol_m
    assert d_pol_m <= d_app_m <= d_eq_m
