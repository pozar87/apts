import pytest

from apts import equipment
from apts.constants import EquipmentTableLabels
from apts.opticalequipment import Barlow
from . import setup_equipment


def test_zoom():
  e = setup_equipment()
  row = e.data().iloc[0]
  # Only possiable zoom should be 750/25 = 30
  assert row[EquipmentTableLabels.ZOOM] == 30
  # Only possiable fov should be 2.333 ± 0.001
  assert row[EquipmentTableLabels.FOV] == pytest.approx(2.333, 0.001)
  # Range 12.880 ± 0.001
  assert row[EquipmentTableLabels.RANGE] == pytest.approx(13.580, 0.001)


def test_barlow():
  e = setup_equipment()
  e.register(Barlow(2))
  row = e.data().iloc[0]
  # Only possiable zoom should be 750/25 * 2 = 60
  assert row[EquipmentTableLabels.ZOOM] == 60
  # Using 3 elements
  assert row[EquipmentTableLabels.ELEMENTS] == 3


def test_barlow_stacking():
  e = setup_equipment()
  e.register(equipment.Barlow(2))
  e.register(equipment.Barlow(3))
  # Get row with biggest zoom
  row = e.data().sort_values([EquipmentTableLabels.ZOOM], ascending=[0]).iloc[0]
  # With two stacked barlows max zoom should be 180 (30 * 3 * 2)
  assert row[EquipmentTableLabels.ZOOM] == 180
  # Using 4 elements
  assert row[EquipmentTableLabels.ELEMENTS] == 4


def test_multi_barlow():
  e = setup_equipment()
  e.register(equipment.Barlow(2))
  e.register(equipment.Barlow(3))
  # With two barlows and single eyepiece number of possiable connection is 4 (with barlow stacking)
  assert len(e.data()[EquipmentTableLabels.ZOOM]) == 4


def test_camera():
  e = setup_equipment()
  e.register(equipment.Camera(30, 40, 100, 200))
  # Zoom of camera (sqrt(30^2 + 40^2) = 50)
  data = e.data()
  assert data[data.Type == "Image"].iloc[0][EquipmentTableLabels.ZOOM] == 15

def test_telecsope():
  t = equipment.Telescope(150, 750)
  assert t.dawes_limit().magnitude == pytest.approx(0.773, 0.001)
