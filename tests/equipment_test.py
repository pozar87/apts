import pytest
from default import *

def test_zoom():
  e = setup_equipment()
  row = e.data().iloc[0]
  # Only possiable zoom should be 750/25 = 30
  assert row["zoom"] == 30
  # Only possiable fov should be 1.733 ± 0.001
  assert row["fov"] == pytest.approx(1.733, 0.001)
  # Range 12.880 ± 0.001
  assert row["range"] == pytest.approx(12.880, 0.001)
 
def test_barlow():
  e = setup_equipment()
  e.register(equipment.Barlow(2))
  row = e.data().iloc[0]
  # Only possiable zoom should be 750/25 * 2 = 60
  assert row["zoom"] == 60
  # Using 3 elements
  assert row["elements"] == 3 

def test_barlow_stacking():
  e = setup_equipment()
  e.register(equipment.Barlow(2))
  e.register(equipment.Barlow(3))
  # Get row with biggest zoom 
  row = e.data().sort_values(['zoom'], ascending=[0]).iloc[0]
  # With two stacked barlows max zoom should be 180 (30 * 3 * 2) 
  assert row["zoom"] == 180 
  # Using 4 elements
  assert row["elements"] == 4 
  
def test_multi_barlow():
  e = setup_equipment()
  e.register(equipment.Barlow(2))
  e.register(equipment.Barlow(3))
  # With two barlows and single eyepiece number of possiable connection is 4 (with barlow stacking)
  assert len(e.data()["zoom"]) == 4  

def test_camera():
  e = setup_equipment()
  e.register(equipment.Camera(30, 40, 100, 200))
  # Zoom of camera (sqrt(30^2 + 40^2) = 50)
  data = e.data()
  assert data[data.type == "Image"].iloc[0]["zoom"] == 15
  
  
   
