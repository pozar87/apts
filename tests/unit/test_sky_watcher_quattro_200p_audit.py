from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType

def test_sky_watcher_quattro_200p_audit():
    """
    Audit for Sky-Watcher Quattro 200P Imaging Newtonian.
    Source: https://www.skywatcherusa.com/products/sky-watcher-quattro-200p-imaging-newtonian-8-205-mm
    """
    telescope = Sky_watcherTelescope.Sky_Watcher_Quattro_200P()

    # Official name and brand
    assert telescope.get_vendor() == "Sky-Watcher Quattro 200P"

    # Physical specs
    assert telescope.aperture.magnitude == 205
    assert telescope.focal_length.magnitude == 800
    assert telescope.mass.magnitude == 9500
    assert telescope.central_obstruction.magnitude == 70

    # Connection type (2" Female visual back/focuser)
    assert telescope.connection_type == ConnectionType.F_2

    # Calculated specs
    assert telescope.focal_ratio().magnitude == 800 / 205
