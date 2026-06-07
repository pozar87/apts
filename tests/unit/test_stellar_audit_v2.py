from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.opticalequipment.telescope.vendors.dwarflab import DwarfLabTelescope

def test_zwo_pro_specs():
    # Test a few representative models from the update
    cam_2600mc = ZwoCamera.ZWO_ASI_2600MC_Pro()
    assert cam_2600mc.full_well == 50000
    assert cam_2600mc.pixel_size().magnitude == 3.76
    assert cam_2600mc.width == 6248
    assert cam_2600mc.sensor_width.magnitude == 23.5

    cam_533mm = ZwoCamera.ZWO_ASI_533MM_Pro()
    assert cam_533mm.full_well == 50000
    assert cam_533mm.quantum_efficiency == 91
    assert cam_533mm.height == 3008

    cam_183mc = ZwoCamera.ZWO_ASI_183MC_Pro()
    assert cam_183mc.full_well == 15000
    assert cam_183mc.pixel_size().magnitude == 2.4

def test_zwo_air_specs():
    cam_air = ZwoCamera.ZWO_ASI_2600MC_Air()
    assert cam_air.full_well == 73000
    assert cam_air.mass.magnitude == 760 # Verified for Air model
    assert "Air" in cam_air.vendor

def test_smart_telescope_audit():
    s30 = ZwoTelescope.ZWO_Seestar_S30()
    assert s30.full_well == 38200

    d3 = DwarfLabTelescope.DwarfLab_Dwarf_3()
    assert d3.full_well == 11270
    assert d3.aperture.magnitude == 35
