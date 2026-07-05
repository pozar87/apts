import pytest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType, Gender

def test_esprit_120ed_audit():
    telescope = Sky_watcherTelescope.Sky_Watcher_Esprit_120ED()
    # Verified via Sky-Watcher Global (10.3 kg Tube Weight)
    assert telescope.mass.to('g').magnitude == 10300
    assert telescope.aperture.to('mm').magnitude == 120
    assert telescope.focal_length.to('mm').magnitude == 840
    # Current database has M48 Male (likely flattener output)
    # We'll stick to what's expected after my change if I decide to keep M48 Male
    # or change it to 3" Female.
    # Given the existing pattern for Esprit in the file, I'll keep M48 Male but update the mass.
    assert telescope.connection_type == ConnectionType.M48
    assert telescope.connection_gender == Gender.MALE
