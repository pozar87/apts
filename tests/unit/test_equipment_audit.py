import pytest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.telescope.vendors.bresser import BresserTelescope
from apts.opticalequipment.telescope.vendors.gso import GsoTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.eyepiece.base import Eyepiece
from apts.utils.equipment import ConnectionType, Gender, get_default_gender

def test_pushfit_defaults():
    # Standard: Telescope push-fit output should be Female
    assert get_default_gender(ConnectionType.F_1_25, is_input=False) == Gender.FEMALE
    assert get_default_gender(ConnectionType.F_2, is_input=False) == Gender.FEMALE

    # Standard: Eyepiece push-fit input should be Male
    assert get_default_gender(ConnectionType.F_1_25, is_input=True) == Gender.MALE
    assert get_default_gender(ConnectionType.F_2, is_input=True) == Gender.MALE

def test_celestron_pushfit_genders():
    # AstroFi 130 has 2" output
    scope = CelestronTelescope.Celestron_AstroFi_130()
    assert (ConnectionType.F_2, Gender.FEMALE) in scope._outputs

    # AstroMaster 70AZ has 1.25" output
    scope = CelestronTelescope.Celestron_AstroMaster_70AZ()
    assert (ConnectionType.F_1_25, Gender.FEMALE) in scope._outputs

def test_bresser_pushfit_genders():
    # Messier MC-127 has 1.25" output
    scope = BresserTelescope.Bresser_Messier_MC_127()
    assert (ConnectionType.F_1_25, Gender.FEMALE) in scope._outputs

    # Messier NT-150L has 2" output
    scope = BresserTelescope.Bresser_Messier_NT_150L_6()
    assert (ConnectionType.F_2, Gender.FEMALE) in scope._outputs

def test_gso_pushfit_genders():
    # GSO Dobson 8" has 2" output
    scope = GsoTelescope.GSO_Dobson_8()
    assert (ConnectionType.F_2, Gender.FEMALE) in scope._outputs

def test_zwo_mini_camera_inputs():
    # ASI120MM Mini should have 1.25" Male input
    camera = ZwoCamera.ZWO_ASI_120MM_Mini()
    assert (ConnectionType.F_1_25, Gender.MALE) in camera._inputs

    # ASI290MM Mini should have 1.25" Male input
    camera = ZwoCamera.ZWO_ASI_290MM_Mini()
    assert (ConnectionType.F_1_25, Gender.MALE) in camera._inputs

def test_connection_compatibility():
    # Test if a Female scope output can connect to a Male eyepiece/camera input
    scope = CelestronTelescope.Celestron_AstroMaster_70AZ() # 1.25" Female
    eyepiece = Eyepiece(20, vendor="Generic") # 1.25" Male by default
    camera = ZwoCamera.ZWO_ASI_120MM_Mini() # 1.25" Male

    scope_output = scope._outputs[0]
    eyepiece_input = eyepiece._inputs[0]
    camera_pushfit_input = next(inp for inp in camera._inputs if inp[0] == ConnectionType.F_1_25)

    # Check 1.25" Female vs 1.25" Male
    assert scope_output[0] == eyepiece_input[0]
    assert scope_output[1] != eyepiece_input[1]

    assert scope_output[0] == camera_pushfit_input[0]
    assert scope_output[1] != camera_pushfit_input[1]
