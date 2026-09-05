from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType, Gender

def test_esprit_120ed_audit():
    telescope = Sky_watcherTelescope.Sky_Watcher_Esprit_120ED()
    assert telescope.get_vendor() == "Sky-Watcher Esprit 120ED"
    assert telescope.aperture.to('mm').magnitude == 120
    assert telescope.focal_length.to('mm').magnitude == 840
    assert abs(telescope.focal_ratio() - 7.0) < 0.01
    assert telescope.central_obstruction.to('mm').magnitude == 0
    assert telescope.mass.to('g').magnitude == 10300
    assert telescope.connection_type == ConnectionType.M74
    assert telescope.connection_gender == Gender.FEMALE
