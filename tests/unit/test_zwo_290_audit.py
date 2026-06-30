import pytest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def test_zwo_asi290mm_audit():
    """
    Audit test for ZWO ASI290MM based on official ZWO manual.
    Source: https://www.atc-astro.eu/eshop/ZWO_ASI290_Manual_EN.pdf
    """
    camera = ZwoCamera.ZWO_ASI_290MM()

    assert camera.vendor == "ZWO ASI290MM"
    assert camera.width == 1936
    assert camera.height == 1096
    assert camera.pixel_size().magnitude == 2.9
    assert camera.sensor_width.magnitude == 5.6
    assert camera.sensor_height.magnitude == 3.2
    assert camera.quantum_efficiency == 80
    assert camera.full_well == 14600
    assert camera.read_noise == 1.0
    assert camera.mass.magnitude == 120

def test_zwo_asi290mc_audit():
    """
    Audit test for ZWO ASI290MC based on official ZWO manual.
    Source: https://www.atc-astro.eu/eshop/ZWO_ASI290_Manual_EN.pdf
    """
    camera = ZwoCamera.ZWO_ASI_290MC()

    assert camera.vendor == "ZWO ASI290MC"
    assert camera.width == 1936
    assert camera.height == 1096
    assert camera.pixel_size().magnitude == 2.9
    assert camera.sensor_width.magnitude == 5.6
    assert camera.sensor_height.magnitude == 3.2
    assert camera.quantum_efficiency == 80
    assert camera.full_well == 14600
    assert camera.read_noise == 1.0
    assert camera.mass.magnitude == 120

def test_zwo_asi290mm_mini_audit():
    """
    Audit test for ZWO ASI290MM Mini based on official ZWO manual.
    Source: https://www.atc-astro.eu/eshop/ZWO_ASI290_Manual_EN.pdf
    """
    camera = ZwoCamera.ZWO_ASI_290MM_Mini()

    assert camera.vendor == "ZWO ASI290MM Mini"
    assert camera.width == 1936
    assert camera.height == 1096
    assert camera.pixel_size().magnitude == 2.9
    assert camera.sensor_width.magnitude == 5.6
    assert camera.sensor_height.magnitude == 3.2
    assert camera.quantum_efficiency == 80
    assert camera.full_well == 14600
    assert camera.read_noise == 1.0
    assert camera.mass.magnitude == 60

def test_zwo_asi290mc_mini_audit():
    """
    Audit test for ZWO ASI290MC Mini based on official ZWO manual (IMX291 sensor).
    Source: https://www.atc-astro.eu/eshop/ZWO_ASI290_Manual_EN.pdf
    """
    camera = ZwoCamera.ZWO_ASI_290MC_Mini()

    assert camera.vendor == "ZWO ASI290MC Mini"
    assert camera.width == 1936
    assert camera.height == 1096
    assert camera.pixel_size().magnitude == 2.9
    assert camera.sensor_width.magnitude == 5.6
    assert camera.sensor_height.magnitude == 3.2
    assert camera.quantum_efficiency == 80
    assert camera.full_well == 14600
    assert camera.read_noise == 1.0
    assert camera.mass.magnitude == 60
