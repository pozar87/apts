import pytest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.askar import AskarTelescope

def test_seestar_sensor_specs():
    """Verify Seestar sensor entries in ZwoCamera database."""
    # S50 Sensor (IMX462)
    s50 = ZwoCamera.ZWO_Seestar_S50_Sensor()
    assert s50.sensor_width.magnitude == 5.6
    assert s50.sensor_height.magnitude == 3.2
    assert s50.width == 1920
    assert s50.height == 1080
    assert s50.pixel_size().to("micrometer").magnitude == pytest.approx(2.9)
    assert s50.full_well == 12000

    # S30 Sensor (IMX662)
    s30 = ZwoCamera.ZWO_Seestar_S30_Sensor()
    assert s30.sensor_width.magnitude == 5.57
    assert s30.sensor_height.magnitude == 3.13
    assert s30.pixel_size().to("micrometer").magnitude == pytest.approx(2.9)
    assert s30.full_well == 38200

    # S30 Pro Sensor (IMX678)
    s30p = ZwoCamera.ZWO_Seestar_S30_Pro_Sensor()
    assert s30p.sensor_width.magnitude == 7.68
    assert s30p.sensor_height.magnitude == 4.32
    assert s30p.width == 3840
    assert s30p.height == 2160
    assert s30p.pixel_size().to("micrometer").magnitude == pytest.approx(2.0)
    assert s30p.full_well == 11270

def test_askar_apo_specs():
    """Verify Askar APO refractor entries including reduced variants."""
    # 103APO
    a103 = AskarTelescope.Askar_103APO()
    assert a103.aperture.magnitude == 103
    assert a103.focal_length.magnitude == pytest.approx(700.4)

    # 103APO Reduced (0.8x)
    a103r = AskarTelescope.Askar_103APO_Reduced()
    assert a103r.focal_length.magnitude == 560

    # 120APO
    a120 = AskarTelescope.Askar_120APO()
    assert a120.aperture.magnitude == 120
    assert a120.focal_length.magnitude == 840

    # 120APO Reduced (0.8x)
    a120r = AskarTelescope.Askar_120APO_Reduced()
    assert a120r.focal_length.magnitude == 672

    # 140APO
    a140 = AskarTelescope.Askar_140APO()
    assert a140.aperture.magnitude == 140
    assert a140.focal_length.magnitude == 980

    # 140APO Reduced (0.8x)
    a140r = AskarTelescope.Askar_140APO_Reduced()
    assert a140r.focal_length.magnitude == 784

    # 185APO
    a185 = AskarTelescope.Askar_185APO()
    assert a185.aperture.magnitude == 185
    assert a185.focal_length.magnitude == 1295
