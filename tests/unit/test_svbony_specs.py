from apts.opticalequipment.telescope.vendors.svbony import SvbonyTelescope
from apts.opticalequipment.telescope.base import TelescopeType

def test_svbony_sv503_specs() -> None:
    # SV503 70ED
    scope = SvbonyTelescope.SVBony_SV503_70ED()
    assert scope.aperture.magnitude == 70
    assert scope.focal_length.magnitude == 420
    assert scope.central_obstruction.magnitude == 0
    assert scope.mass.magnitude == 2220
    assert scope.telescope_type == TelescopeType.REFRACTOR

    # SV503 80ED
    scope = SvbonyTelescope.SVBony_SV503_80ED()
    assert scope.aperture.magnitude == 80
    assert scope.focal_length.magnitude == 560
    assert scope.central_obstruction.magnitude == 0
    assert scope.mass.magnitude == 2900

    # SV503 102ED
    scope = SvbonyTelescope.SVBony_SV503_102ED()
    assert scope.aperture.magnitude == 102
    assert scope.focal_length.magnitude == 714
    assert scope.central_obstruction.magnitude == 0
    assert scope.mass.magnitude == 4000

    # SV503 80
    scope = SvbonyTelescope.SVBony_SV503_80()
    assert scope.aperture.magnitude == 80
    assert scope.focal_length.magnitude == 560
    assert scope.central_obstruction.magnitude == 0
    assert scope.mass.magnitude == 2900

def test_svbony_sv550_specs() -> None:
    # SV550 80ED
    scope = SvbonyTelescope.SVBony_SV550_80ED()
    assert scope.aperture.magnitude == 80
    assert scope.focal_length.magnitude == 480
    assert scope.central_obstruction.magnitude == 0
    assert scope.mass.magnitude == 2450
    assert scope.telescope_type == TelescopeType.REFRACTOR

    # SV550 122ED
    scope = SvbonyTelescope.SVBony_SV550_122ED()
    assert scope.aperture.magnitude == 122
    assert scope.focal_length.magnitude == 854
    assert scope.central_obstruction.magnitude == 0
    assert scope.mass.magnitude == 6440

def test_svbony_sv48_specs() -> None:
    # SV48
    scope = SvbonyTelescope.SVBony_SV48()
    assert scope.aperture.magnitude == 90
    assert scope.focal_length.magnitude == 500
    assert scope.central_obstruction.magnitude == 0
    assert scope.mass.magnitude == 2410
    assert scope.telescope_type == TelescopeType.REFRACTOR
