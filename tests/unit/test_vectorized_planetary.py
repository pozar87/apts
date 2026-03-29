import pytest
import numpy as np
from apts.utils import planetary
from apts.cache import get_timescale
from apts.equipment import OpticalEquipment
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def test_vectorized_planetary_utilities():
    ts = get_timescale()
    # Vector of 3 times
    times = ts.utc(2024, 1, [1, 2, 3])

    # Test distance
    dist = planetary.get_planet_distance_km("Jupiter", times)
    assert isinstance(dist, np.ndarray)
    assert len(dist) == 3

    # Test angular diameter (equatorial)
    diam_eq = planetary.get_planet_angular_diameter("Jupiter", times, which="equatorial")
    assert isinstance(diam_eq, np.ndarray)
    assert len(diam_eq) == 3

    # Test angular diameter (apparent polar - involves sub-observer latitude and pole coords)
    diam_pol = planetary.get_planet_angular_diameter("Jupiter", times, which="apparent_polar")
    assert isinstance(diam_pol, np.ndarray)
    assert len(diam_pol) == 3

    # Test Saturn ring details
    rings = planetary.get_saturn_ring_details(times)
    assert isinstance(rings["tilt_degrees"], np.ndarray)
    assert isinstance(rings["major_axis_arcsec"], np.ndarray)
    assert isinstance(rings["minor_axis_arcsec"], np.ndarray)
    assert len(rings["tilt_degrees"]) == 3

def test_vectorized_optical_path_methods():
    ts = get_timescale()
    times = ts.utc(2024, 1, [1, 2])

    telescope = Sky_watcherTelescope.Sky_Watcher_Evostar_80ED_DS_Pro()
    camera = ZwoCamera.ZWO_ASI_2600MC_Pro()
    path = OpticalPath.from_path([telescope, camera])

    # Test planetary size in pixels
    px_size = path.planetary_size_in_pixels("Jupiter", times)
    assert isinstance(px_size, np.ndarray)
    assert len(px_size) == 2

    # Test Saturn ring size in pixels
    major, minor = path.saturn_ring_size_in_pixels(times)
    assert isinstance(major, np.ndarray)
    assert isinstance(minor, np.ndarray)
    assert len(major) == 2

def test_scalar_consistency():
    ts = get_timescale()
    t_scalar = ts.utc(2024, 6, 15)
    t_vector = ts.utc(2024, 6, [15])

    # Distance
    dist_s = planetary.get_planet_distance_km("Mars", t_scalar)
    dist_v = planetary.get_planet_distance_km("Mars", t_vector)
    assert np.isscalar(dist_s)
    assert isinstance(dist_v, np.ndarray)
    assert float(dist_s) == pytest.approx(float(dist_v[0]))

    # Ring details
    rings_s = planetary.get_saturn_ring_details(t_scalar)
    rings_v = planetary.get_saturn_ring_details(t_vector)
    assert np.isscalar(rings_s["tilt_degrees"])
    assert isinstance(rings_v["tilt_degrees"], np.ndarray)
    assert float(rings_s["tilt_degrees"]) == pytest.approx(float(rings_v["tilt_degrees"][0]))
