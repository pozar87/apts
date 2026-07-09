from apts.opticalequipment.telescope.vendors.svbony import SvbonyTelescope

def test_sv503_70ed_specs():
    telescope = SvbonyTelescope.SVBony_SV503_70ED()
    assert telescope.aperture.magnitude == 70
    assert telescope.focal_length.magnitude == 420
    assert telescope.mass.magnitude == 2220
    assert telescope.central_obstruction.magnitude == 0

def test_sv503_70ed_quad_specs():
    telescope = SvbonyTelescope.SVBony_SV503_70ED_Quad()
    assert telescope.aperture.magnitude == 70
    assert telescope.focal_length.magnitude == 474
    assert telescope.mass.magnitude == 2685
    assert telescope.central_obstruction.magnitude == 0

def test_sv503_80ed_specs():
    telescope = SvbonyTelescope.SVBony_SV503_80ED()
    assert telescope.aperture.magnitude == 80
    assert telescope.focal_length.magnitude == 560
    assert telescope.mass.magnitude == 3500
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.optical_length.magnitude == 90
    assert telescope.backfocus.magnitude == 90
    assert telescope.connection_type.value == "2"
    assert telescope.connection_gender.value == "F"

def test_sv503_102ed_specs():
    telescope = SvbonyTelescope.SVBony_SV503_102ED()
    assert telescope.aperture.magnitude == 102
    assert telescope.focal_length.magnitude == 714
    assert telescope.mass.magnitude == 5700
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.optical_length.magnitude == 101.9
    assert telescope.backfocus.magnitude == 101.9
    assert telescope.connection_type.value == "2"
    assert telescope.connection_gender.value == "F"

def test_sv550_60_specs():
    telescope = SvbonyTelescope.SVBony_SV550_60()
    assert telescope.aperture.magnitude == 60
    assert telescope.focal_length.magnitude == 300
    assert telescope.mass.magnitude == 2030
    assert telescope.central_obstruction.magnitude == 0

def test_sv550_80ed_specs():
    telescope = SvbonyTelescope.SVBony_SV550_80ED()
    assert telescope.aperture.magnitude == 80
    assert telescope.focal_length.magnitude == 480
    assert telescope.mass.magnitude == 2450
    assert telescope.central_obstruction.magnitude == 0

def test_sv550_122ed_specs():
    telescope = SvbonyTelescope.SVBony_SV550_122ED()
    assert telescope.aperture.magnitude == 122
    assert telescope.focal_length.magnitude == 854
    assert telescope.mass.magnitude == 6440
    assert telescope.central_obstruction.magnitude == 0

def test_sv48_specs():
    telescope = SvbonyTelescope.SVBony_SV48()
    assert telescope.aperture.magnitude == 90
    assert telescope.focal_length.magnitude == 500
    assert telescope.mass.magnitude == 2730
    assert telescope.central_obstruction.magnitude == 0

def test_sv48p_102_specs():
    telescope = SvbonyTelescope.SVBony_SV48P_102()
    assert telescope.aperture.magnitude == 102
    assert telescope.focal_length.magnitude == 663
    assert telescope.mass.magnitude == 3400
    assert telescope.central_obstruction.magnitude == 0

