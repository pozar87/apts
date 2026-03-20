import pytest
from apts.opticalequipment.telescope.vendors.william_optics import William_opticsTelescope

def test_william_optics_gt153_specs():
    telescope = William_opticsTelescope.William_Optics_GT153()
    assert telescope.aperture.magnitude == 153
    assert telescope.focal_length.magnitude == 1188
    assert telescope.mass.magnitude == 13500
    assert telescope.central_obstruction.magnitude == 0

def test_william_optics_redcat51_specs():
    telescope = William_opticsTelescope.William_Optics_RedCat_51()
    assert telescope.aperture.magnitude == 51
    assert telescope.focal_length.magnitude == 250
    assert telescope.mass.magnitude == 1450
    assert telescope.central_obstruction.magnitude == 0

def test_william_optics_pleiades68_specs():
    telescope = William_opticsTelescope.William_Optics_Pleiades_68()
    assert telescope.aperture.magnitude == 68
    assert telescope.focal_length.magnitude == 258.4
    assert telescope.mass.magnitude == 2980
    assert telescope.central_obstruction.magnitude == 0

def test_william_optics_pleiades111_specs():
    telescope = William_opticsTelescope.William_Optics_Pleiades_111()
    assert telescope.aperture.magnitude == 111
    assert telescope.focal_length.magnitude == 528
    assert telescope.mass.magnitude == 7950
    assert telescope.central_obstruction.magnitude == 0
