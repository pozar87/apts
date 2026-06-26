from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def test_esprit_150ed_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_Esprit_150ED()
    assert telescope.get_vendor() == "Sky-Watcher Esprit 150ED"
    assert telescope.mass.magnitude == 14520

def test_evostar_72ed_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_Evostar_72ED()
    assert telescope.get_vendor() == "Sky-Watcher Evostar 72ED"
    assert telescope.mass.magnitude == 2000

def test_evolux_82ed_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_Evolux_82ED()
    assert telescope.get_vendor() == "Sky-Watcher Evolux 82ED"
    assert telescope.mass.magnitude == 2920
