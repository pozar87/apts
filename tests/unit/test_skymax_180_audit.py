from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def test_skymax_180_pro_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_SkyMax_180_Pro()
    # Audited value: 41mm (approx 23% of 180mm aperture)
    assert telescope.central_obstruction.magnitude == 41
    assert telescope.mass.magnitude == 7800
    assert telescope.aperture.magnitude == 180
    assert telescope.focal_length.magnitude == 2700

def test_mak_180_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_Mak_180()
    # Audited value: 41mm
    assert telescope.central_obstruction.magnitude == 41
    assert telescope.mass.magnitude == 7800
    assert telescope.aperture.magnitude == 180
    assert telescope.focal_length.magnitude == 2700
