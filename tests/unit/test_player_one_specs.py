import pytest
from apts.opticalequipment.camera.vendors.player_one import Player_oneCamera
from apts.units import get_unit_registry

def test_poseidon_c_pro_specs():
    camera = Player_oneCamera.Player_One_Poseidon_C_Pro()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Poseidon-C Pro"
    assert camera.width == 6252
    assert camera.height == 4176
    assert camera.sensor_width.to(ureg.mm).magnitude == pytest.approx(23.5)
    assert camera.sensor_height.to(ureg.mm).magnitude == pytest.approx(15.7)
    assert camera.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(3.76)
    assert camera.full_well == 71700
    assert camera.read_noise == 1.0
    assert camera.quantum_efficiency == 81
    assert camera.mass.to(ureg.gram).magnitude == pytest.approx(650)
    assert camera.backfocus is not None
    assert camera.backfocus.to(ureg.mm).magnitude == pytest.approx(17.5)

def test_poseidon_m_pro_specs():
    camera = Player_oneCamera.Player_One_Poseidon_M_Pro()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Poseidon-M Pro"
    assert camera.quantum_efficiency == 91
    assert camera.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(3.76)
    assert camera.mass.to(ureg.gram).magnitude == pytest.approx(650)

def test_artemis_c_pro_specs():
    camera = Player_oneCamera.Player_One_Artemis_C_Pro()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Artemis-C Pro"
    assert camera.width == 4144
    assert camera.height == 2822
    assert camera.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(4.63)
    assert camera.quantum_efficiency == 75

def test_ares_m_pro_specs():
    camera = Player_oneCamera.Player_One_Ares_M_Pro()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Ares-M Pro"
    assert camera.width == 3008
    assert camera.height == 3008
    assert camera.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(3.76)
    assert camera.quantum_efficiency == 91

def test_apollo_max_c_pro_specs():
    camera = Player_oneCamera.Player_One_Apollo_MAX_C_Pro()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Apollo-MAX-C Pro"
    assert camera.width == 1608
    assert camera.height == 1104
    assert camera.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(9.0)
    assert camera.quantum_efficiency == 79

def test_xena_585m_specs():
    camera = Player_oneCamera.Player_One_Xena_585M()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Xena 585M"
    assert camera.width == 3856
    assert camera.height == 2180
    assert camera.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(2.9)
    assert camera.sensor_width.to(ureg.mm).magnitude == pytest.approx(11.2)
    assert camera.sensor_height.to(ureg.mm).magnitude == pytest.approx(6.3)
    assert camera.full_well == 47000
    assert camera.read_noise == 0.7
    assert camera.quantum_efficiency == 91
    assert camera.backfocus.to(ureg.mm).magnitude == pytest.approx(7.5)
    assert camera.mass.to(ureg.gram).magnitude == pytest.approx(65)

def test_ceres_462m_specs():
    camera = Player_oneCamera.Player_One_Ceres_462M()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Ceres 462M"
    assert camera.width == 1944
    assert camera.height == 1096
    assert camera.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(2.9)
    assert camera.sensor_width.to(ureg.mm).magnitude == pytest.approx(5.6)
    assert camera.sensor_height.to(ureg.mm).magnitude == pytest.approx(3.2)
    assert camera.full_well == 12000
    assert camera.read_noise == 0.7
    assert camera.quantum_efficiency == 91
    assert camera.backfocus.to(ureg.mm).magnitude == pytest.approx(7.5)

def test_ceres_c_updated_specs():
    camera = Player_oneCamera.Player_One_Ceres_C()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Ceres-C"
    assert camera.width == 1304
    assert camera.height == 976
    assert camera.sensor_width.to(ureg.mm).magnitude == pytest.approx(4.9)
    assert camera.sensor_height.to(ureg.mm).magnitude == pytest.approx(3.7)
    assert camera.full_well == 19400
    assert camera.read_noise == 0.74
    assert camera.backfocus.to(ureg.mm).magnitude == pytest.approx(7.5)
    assert camera.mass.to(ureg.gram).magnitude == pytest.approx(65)

def test_ceres_m_updated_specs():
    camera = Player_oneCamera.Player_One_Ceres_M()
    ureg = get_unit_registry()

    assert camera.vendor == "Player One Ceres-M"
    assert camera.width == 1284
    assert camera.height == 964
    assert camera.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(3.75)
    assert camera.full_well == 18000
    assert camera.read_noise == 3.6
