import pytest
from apts.opticalequipment.telescope.vendors.svbony import SvbonyTelescope
from apts.units import get_unit_registry

def test_svbony_sv550_122ed_specs():
    telescope = SvbonyTelescope.SVBony_SV550_122ED()
    assert "SVBony" in telescope.get_vendor()
    assert "SV550 122ED" in telescope.get_vendor()
    assert telescope.aperture.to(get_unit_registry().mm).magnitude == 122
    assert telescope.focal_length.to(get_unit_registry().mm).magnitude == 854
    assert telescope.mass.to(get_unit_registry().gram).magnitude == 6440

def test_svbony_sv550_60_specs():
    telescope = SvbonyTelescope.SVBony_SV550_60()
    assert "SVBony" in telescope.get_vendor()
    assert "SV550 60" in telescope.get_vendor()
    assert telescope.aperture.to(get_unit_registry().mm).magnitude == 60
    assert telescope.focal_length.to(get_unit_registry().mm).magnitude == 300
    assert telescope.mass.to(get_unit_registry().gram).magnitude == 2030
