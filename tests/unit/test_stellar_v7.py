from apts.opticalequipment.telescope.vendors.askar import AskarTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def test_askar_sqa55_specs():
    scope = AskarTelescope.Askar_SQA55()
    assert scope.get_vendor() == "Askar SQA55"
    assert scope.aperture.to("mm").magnitude == 55
    assert scope.focal_length.to("mm").magnitude == 264
    assert scope.mass.to("g").magnitude == 1840

def test_zwo_asi664_full_well_correction():
    camera_mc = ZwoCamera.ZWO_ASI_664MC()
    camera_mm = ZwoCamera.ZWO_ASI_664MM()

    assert camera_mc.full_well == 38500
    assert camera_mm.full_well == 38500
