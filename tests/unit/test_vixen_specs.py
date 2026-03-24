import pytest
from apts.opticalequipment.telescope.vendors.vixen import VixenTelescope

def test_vixen_vc200l_specs():
    telescope = VixenTelescope.Vixen_VC200L()
    assert telescope.aperture.magnitude == 200
    assert telescope.focal_length.magnitude == 1800
    assert telescope.central_obstruction.magnitude == 77
    assert telescope.mass.magnitude == 6000

def test_vixen_vmc200l_specs():
    telescope = VixenTelescope.Vixen_VMC200L()
    assert telescope.aperture.magnitude == 200
    assert telescope.focal_length.magnitude == 1950
    assert telescope.central_obstruction.magnitude == 80
    assert telescope.mass.magnitude == 5900

def test_vixen_r200ss_specs():
    telescope = VixenTelescope.Vixen_R200SS()
    assert telescope.aperture.magnitude == 200
    assert telescope.focal_length.magnitude == 800
    assert telescope.central_obstruction.magnitude == 65
    assert telescope.mass.magnitude == 5300

def test_vixen_sd81s_specs():
    telescope = VixenTelescope.Vixen_SD81S()
    assert telescope.aperture.magnitude == 81
    assert telescope.focal_length.magnitude == 625
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.mass.magnitude == 2300

def test_vixen_sd103s_specs():
    telescope = VixenTelescope.Vixen_SD103S()
    assert telescope.aperture.magnitude == 103
    assert telescope.focal_length.magnitude == 795
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.mass.magnitude == 3600

def test_vixen_sd115s_specs():
    telescope = VixenTelescope.Vixen_SD115S()
    assert telescope.aperture.magnitude == 115
    assert telescope.focal_length.magnitude == 890
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.mass.magnitude == 4400

def test_vixen_ax103s_specs():
    telescope = VixenTelescope.Vixen_AX103S()
    assert telescope.aperture.magnitude == 103
    assert telescope.focal_length.magnitude == 825
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.mass.magnitude == 4600

def test_vixen_fl55ss_specs():
    telescope = VixenTelescope.Vixen_FL55SS()
    assert telescope.aperture.magnitude == 55
    assert telescope.focal_length.magnitude == 303
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.mass.magnitude == 1500

def test_vixen_vsd100_specs():
    telescope = VixenTelescope.Vixen_VSD100_F3_8()
    assert telescope.aperture.magnitude == 100
    assert telescope.focal_length.magnitude == 380
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.mass.magnitude == 4500
