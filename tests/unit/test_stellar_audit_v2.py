import pytest
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.opticalequipment.telescope.vendors.dwarflab import DwarfLabTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.opticalequipment.telescope.vendors.dwarflab import DwarfLabTelescope

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

def test_zwo_pro_v2_specs():
    # Test a few representative models from the update
    cam_2600mc_v2 = ZwoCamera.ZWO_ASI_2600MC_Pro_v2()
    assert cam_2600mc_v2.full_well == 73000
    assert cam_2600mc_v2.pixel_size().magnitude == 3.76
    assert cam_2600mc_v2.width == 6248
    assert cam_2600mc_v2.sensor_width.magnitude == 23.5

    cam_533mm_v2 = ZwoCamera.ZWO_ASI_533MM_Pro_v2()
    assert cam_533mm_v2.full_well == 50000
    assert cam_533mm_v2.quantum_efficiency == 91
    assert cam_533mm_v2.height == 3008

    cam_183mc_v2 = ZwoCamera.ZWO_ASI_183MC_Pro_v2()
    assert cam_183mc_v2.full_well == 15000
    assert cam_183mc_v2.pixel_size().magnitude == 2.4

def test_zwo_air_specs():
    cam_air = ZwoCamera.ZWO_ASI_2600MC_Air()
    assert cam_air.full_well == 73000
    assert cam_air.mass.magnitude == 1050
    assert "Air" in cam_air.vendor

def test_smart_telescope_audit():
    s30 = ZwoTelescope.ZWO_Seestar_S30()
    assert s30.full_well == 38200

    d3 = DwarfLabTelescope.DwarfLab_Dwarf_3()
    assert d3.full_well == 11270
    assert d3.aperture.magnitude == 35
