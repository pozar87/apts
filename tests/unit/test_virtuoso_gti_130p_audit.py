import pytest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def test_virtuoso_gti_130p_audit():
    """
    Verify the audited specifications for Sky-Watcher Virtuoso GTi 130P.
    Reference: https://www.skywatcherusa.com/products/virtuoso-gti-130p
    """
    telescope = Sky_watcherTelescope.Sky_Watcher_Virtuoso_GTi_130P()

    # In Telescope.from_database, vendor is constructed as f"{brand} {name}"
    assert telescope.get_vendor() == "Sky-Watcher Virtuoso GTi 130P"
    assert telescope.aperture.to('mm').magnitude == 130
    assert telescope.focal_length.to('mm').magnitude == 650
    # Central obstruction: 40mm
    assert telescope.central_obstruction.to('mm').magnitude == 40
    # Mass: 2948g (6.5 lbs)
    assert telescope.mass.to('gram').magnitude == 2948
    # Focal ratio: f/5
    assert telescope.focal_ratio().magnitude == 5.0
