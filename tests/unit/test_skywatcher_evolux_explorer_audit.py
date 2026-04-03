from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def test_evolux_62ed_specs():
    model = Sky_watcherTelescope.Sky_Watcher_Evolux_62ED()
    assert model.aperture.magnitude == 62
    assert model.focal_length.magnitude == 400
    assert model.mass.to('g').magnitude == 2500
    assert model.central_obstruction.magnitude == 0

def test_evolux_82ed_specs():
    model = Sky_watcherTelescope.Sky_Watcher_Evolux_82ED()
    assert model.aperture.magnitude == 82
    assert model.focal_length.magnitude == 530
    assert model.mass.to('g').magnitude == 2920
    assert model.central_obstruction.magnitude == 0

def test_explorer_200p_specs():
    model = Sky_watcherTelescope.Sky_Watcher_Explorer_200P()
    assert model.aperture.magnitude == 200
    assert model.focal_length.magnitude == 1000
    assert model.mass.to('g').magnitude == 8800
    assert model.central_obstruction.magnitude == 52

def test_quattro_200p_specs():
    model = Sky_watcherTelescope.Sky_Watcher_Quattro_200P()
    assert model.aperture.magnitude == 205
    assert model.focal_length.magnitude == 800
    assert model.mass.to('g').magnitude == 9500
    assert model.central_obstruction.magnitude == 70
