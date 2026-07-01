from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

from apts.utils import ConnectionType

def test_skymax_127_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_SkyMax_127()
    # Audited value: 1540mm focal length, 127mm aperture, 2" thread
    assert telescope.focal_length.magnitude == 1540
    assert telescope.aperture.magnitude == 127
    assert telescope.connection_type == ConnectionType.F_2

def test_mak_127_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_Mak_127()
    # Audited value: 1540mm focal length
    assert telescope.focal_length.magnitude == 1540
    assert telescope.aperture.magnitude == 127
    assert telescope.connection_type == ConnectionType.F_2

def test_skymax_127_az_gti_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_SkyMax_127_AZ_GTi()
    # Audited value: 1540mm focal length
    assert telescope.focal_length.magnitude == 1540
    assert telescope.aperture.magnitude == 127
    assert telescope.connection_type == ConnectionType.F_2
