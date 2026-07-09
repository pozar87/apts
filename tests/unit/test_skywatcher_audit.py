from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def test_skywatcher_esprit_specs():
    # Esprit 80ED
    esprit80 = Sky_watcherTelescope.Sky_Watcher_Esprit_80ED()
    assert esprit80.aperture.magnitude == 80
    assert esprit80.focal_length.magnitude == 400
    assert esprit80.mass.to('g').magnitude == 3970

    # Esprit 100ED
    esprit100 = Sky_watcherTelescope.Sky_Watcher_Esprit_100ED()
    assert esprit100.aperture.magnitude == 100
    assert esprit100.focal_length.magnitude == 550
    assert esprit100.mass.to('g').magnitude == 6300

    # Esprit 120ED
    esprit120 = Sky_watcherTelescope.Sky_Watcher_Esprit_120ED()
    assert esprit120.aperture.magnitude == 120
    assert esprit120.focal_length.magnitude == 840
    assert esprit120.mass.to('g').magnitude == 10300

    # Esprit 150ED
    esprit150 = Sky_watcherTelescope.Sky_Watcher_Esprit_150ED()
    assert esprit150.aperture.magnitude == 150
    assert esprit150.focal_length.magnitude == 1050
    assert esprit150.mass.to('g').magnitude == 14520

def test_skywatcher_quattro_specs():
    # Quattro 150P
    q150 = Sky_watcherTelescope.Sky_Watcher_Quattro_150P()
    assert q150.aperture.magnitude == 150
    assert q150.focal_length.magnitude == 600
    assert q150.mass.to('g').magnitude == 5700
    assert q150.central_obstruction.magnitude == 64

    # Quattro 200P
    q200 = Sky_watcherTelescope.Sky_Watcher_Quattro_200P()
    assert q200.aperture.magnitude == 205
    assert q200.focal_length.magnitude == 800
    assert q200.mass.to('g').magnitude == 9500
    assert q200.central_obstruction.magnitude == 70

    # Quattro 250P
    q250 = Sky_watcherTelescope.Sky_Watcher_Quattro_250P()
    assert q250.aperture.magnitude == 254
    assert q250.focal_length.magnitude == 1000
    assert q250.mass.to('g').magnitude == 15100
    assert q250.central_obstruction.magnitude == 89

    # Quattro 300P
    q300 = Sky_watcherTelescope.Sky_Watcher_Quattro_300P()
    assert q300.aperture.magnitude == 305
    assert q300.focal_length.magnitude == 1200
    assert q300.mass.to('g').magnitude == 21800
    assert q300.central_obstruction.magnitude == 102
