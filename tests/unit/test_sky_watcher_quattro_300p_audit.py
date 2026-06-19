import pytest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.units import get_unit_registry

def test_sky_watcher_quattro_300p_audit():
    # Instantiate the audited telescope
    scope = Sky_watcherTelescope.Sky_Watcher_Quattro_300P()
    ureg = get_unit_registry()

    # Verify physical specs
    assert scope.get_vendor() == "Sky-Watcher Quattro 300P"
    assert scope.mass.to(ureg.g).magnitude == 21800
    assert scope.aperture.to(ureg.mm).magnitude == 305
    assert scope.focal_length.to(ureg.mm).magnitude == 1200
    assert scope.central_obstruction.to(ureg.mm).magnitude == 102

    # Verify focal ratio (stated f/4)
    assert scope.focal_ratio() == 1200 / 305
