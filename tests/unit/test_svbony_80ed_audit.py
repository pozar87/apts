from apts.opticalequipment.telescope.vendors.svbony import SvbonyTelescope
from apts.utils import ConnectionType, Gender

def test_svbony_503_80ed_audit():
    telescope = SvbonyTelescope.SVBony_SV503_80ED()
    # Verified specs via Svbony documentation
    assert telescope.get_vendor() == "SVBony SV503 80ED"
    assert telescope.aperture.magnitude == 80
    assert telescope.focal_length.magnitude == 560
    assert telescope.mass.magnitude == 3500 # 3.5 kg verified
    assert telescope.optical_length.magnitude == 90 # 90mm back focus verified
    assert telescope.backfocus.magnitude == 90
    assert telescope.connection_type == ConnectionType.F_2
    assert telescope.connection_gender == Gender.FEMALE
    assert telescope.central_obstruction.magnitude == 0
