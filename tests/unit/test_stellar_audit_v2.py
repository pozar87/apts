import pytest
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.opticalequipment.telescope.vendors.dwarflab import DwarfLabTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def test_seestar_s30_full_well():
    # S30 is a SmartTelescope, it returns an instance of SmartTelescope via ZwoTelescope factory
    s30 = ZwoTelescope.ZWO_Seestar_S30()
    assert s30.full_well == 38200

def test_dwarf_3_full_well():
    d3 = DwarfLabTelescope.DwarfLab_Dwarf_3()
    assert d3.full_well == 11270

def test_asi2600_air_specs():
    mc_air = ZwoCamera.ZWO_ASI_2600MC_Air()
    assert mc_air.full_well == 73000
    assert mc_air.mass.magnitude == 760
    assert mc_air.quantum_efficiency == 80
    assert mc_air.read_noise == 1.0

    mm_air = ZwoCamera.ZWO_ASI_2600MM_Air()
    assert mm_air.full_well == 73000
    assert mm_air.mass.magnitude == 760
    assert mm_air.quantum_efficiency == 91
    assert mm_air.read_noise == 1.0
