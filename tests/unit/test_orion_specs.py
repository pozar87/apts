import pytest
from apts.opticalequipment.telescope.vendors.orion import OrionTelescope

def test_orion_eon_130mm_ed_specs():
    telescope = OrionTelescope.Orion_EON_130mm_ED()
    assert telescope.get_vendor() == 'Orion EON 130mm ED'
    assert telescope.aperture.magnitude == 130
    assert telescope.focal_length.magnitude == 910
    assert telescope.mass.magnitude == 10210
    assert telescope.central_obstruction.magnitude == 0

def test_orion_8_astrograph_specs():
    telescope = OrionTelescope.Orion_8_f_3_9_Astrograph()
    assert telescope.get_vendor() == 'Orion 8" f/3.9 Astrograph'
    assert telescope.aperture.magnitude == 203
    assert telescope.focal_length.magnitude == 800
    assert telescope.central_obstruction.magnitude == 70
    assert telescope.mass.magnitude == 7940

def test_orion_eon_110mm_ed_specs():
    telescope = OrionTelescope.Orion_EON_110mm_ED()
    assert telescope.get_vendor() == 'Orion EON 110mm ED'
    assert telescope.aperture.magnitude == 110
    assert telescope.focal_length.magnitude == 660
    assert telescope.mass.magnitude == 5220
    assert telescope.central_obstruction.magnitude == 0

def test_orion_eon_80mm_ed_specs():
    telescope = OrionTelescope.Orion_EON_80mm_ED()
    assert telescope.get_vendor() == 'Orion EON 80mm ED'
    assert telescope.aperture.magnitude == 80
    assert telescope.focal_length.magnitude == 500
    assert telescope.mass.magnitude == 2950
    assert telescope.central_obstruction.magnitude == 0

def test_orion_xt8_specs():
    telescope = OrionTelescope.Orion_XT8_Classic_Dob()
    assert telescope.get_vendor() == 'Orion XT8 Classic Dob'
    assert telescope.aperture.magnitude == 203
    assert telescope.focal_length.magnitude == 1200
    assert telescope.mass.magnitude == 9210
    assert telescope.central_obstruction.magnitude == 47

def test_orion_xt10_specs():
    telescope = OrionTelescope.Orion_XT10_Classic_Dob()
    assert telescope.get_vendor() == 'Orion XT10 Classic Dob'
    assert telescope.aperture.magnitude == 254
    assert telescope.focal_length.magnitude == 1200
    assert telescope.mass.magnitude == 13110
    assert telescope.central_obstruction.magnitude == 63

def test_orion_xt12_specs():
    telescope = OrionTelescope.Orion_XT12_Classic_Dob()
    assert telescope.get_vendor() == 'Orion XT12 Classic Dob'
    assert telescope.aperture.magnitude == 305
    assert telescope.focal_length.magnitude == 1500
    assert telescope.mass.magnitude == 22680
    assert telescope.central_obstruction.magnitude == 70

def test_orion_spaceprobe_130st_specs():
    telescope = OrionTelescope.Orion_SpaceProbe_130ST()
    assert telescope.get_vendor() == 'Orion SpaceProbe 130ST'
    assert telescope.aperture.magnitude == 130
    assert telescope.focal_length.magnitude == 650
    assert telescope.mass.magnitude == 2810
    assert telescope.central_obstruction.magnitude == 36.4
