import pytest
from apts.opticalequipment.telescope.vendors.vaonis import VaonisTelescope
from apts.opticalequipment.smart_telescope import SmartTelescope

def test_vaonis_stellina_specs():
    stellina = VaonisTelescope.Vaonis_Stellina()
    assert isinstance(stellina, SmartTelescope)
    assert stellina.aperture.magnitude == 80
    assert stellina.focal_length.magnitude == 400
    assert stellina.mass.to("kg").magnitude == pytest.approx(11.2)
    assert stellina.width == 3096
    assert stellina.height == 2080

    # Check FOV (1.0 x 0.7 degrees approx)
    fov_h = stellina.field_of_view_height(stellina, 1.0, 1.0).to("deg").magnitude
    fov_w = stellina.field_of_view_width(stellina, 1.0, 1.0).to("deg").magnitude
    assert fov_h == pytest.approx(0.71, abs=0.01)
    assert fov_w == pytest.approx(1.06, abs=0.01)
    assert stellina.fov().to("deg").magnitude == fov_h

def test_vaonis_vespera_ii_specs():
    vespera_ii = VaonisTelescope.Vaonis_Vespera_II()
    assert isinstance(vespera_ii, SmartTelescope)
    assert vespera_ii.aperture.magnitude == 50
    assert vespera_ii.focal_length.magnitude == 250
    assert vespera_ii.pixel_size().magnitude == 2.9

    # Check FOV (2.5 x 1.4 degrees approx)
    fov_w = vespera_ii.field_of_view_width(vespera_ii, 1.0, 1.0).to("deg").magnitude
    fov_h = vespera_ii.field_of_view_height(vespera_ii, 1.0, 1.0).to("deg").magnitude
    assert fov_w == pytest.approx(2.55, abs=0.01)
    assert fov_h == pytest.approx(1.43, abs=0.01)

def test_vaonis_vespera_pro_specs():
    vespera_pro = VaonisTelescope.Vaonis_Vespera_Pro()
    assert vespera_pro.width == 3536
    assert vespera_pro.height == 3536

    # Square sensor, FOV should be equal
    fov_w = vespera_pro.field_of_view_width(vespera_pro, 1.0, 1.0).to("deg").magnitude
    fov_h = vespera_pro.field_of_view_height(vespera_pro, 1.0, 1.0).to("deg").magnitude
    assert fov_w == fov_h
    assert fov_w == pytest.approx(1.62, abs=0.01)

def test_vaonis_hyperia_specs():
    hyperia = VaonisTelescope.Vaonis_Hyperia()
    assert hyperia.aperture.magnitude == 150
    assert hyperia.focal_length.magnitude == 1050
    assert hyperia.mass.to("kg").magnitude == pytest.approx(75.0)
    assert hyperia.pixel_size().magnitude == 3.76

    # Full frame sensor on 1050mm
    fov_w = hyperia.field_of_view_width(hyperia, 1.0, 1.0).to("deg").magnitude
    fov_h = hyperia.field_of_view_height(hyperia, 1.0, 1.0).to("deg").magnitude
    assert fov_w == pytest.approx(1.96, abs=0.01)
    assert fov_h == pytest.approx(1.31, abs=0.01)
