import pytest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def test_sky_watcher_quattro_300p_specs():
    telescope = Sky_watcherTelescope.Sky_Watcher_Quattro_300P()
    assert telescope.get_vendor() == "Sky-Watcher Quattro 300P"
    assert telescope.aperture.magnitude == 305
    assert telescope.focal_length.magnitude == 1200
    assert telescope.mass.magnitude == 21800 # Corrected to 21.8 kg per Altair Astro technical specs
    assert telescope.central_obstruction.magnitude == 102
    assert telescope.focal_ratio().magnitude == 1200 / 305
