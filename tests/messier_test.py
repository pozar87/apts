from . import setup_observation

def test_visiable_messier():
  o = setup_observation()
  m = o.get_visible_messier()
  assert len(m) == 11
  
  # Check that string columns have string dtype
  assert m["Messier"].dtype == "string"
  assert m["NGC"].dtype == "string"
  assert m["Name"].dtype == "string"
  assert m["Type"].dtype == "string"
  assert m["Constellation"].dtype == "string"
  
  # Check that unit fields have proper units
  assert hasattr(m["RA"].iloc[0], 'magnitude')
  assert hasattr(m["RA"].iloc[0], 'units')
  assert m["RA"].iloc[0].units == 'hour'
  
  assert hasattr(m["Dec"].iloc[0], 'magnitude')
  assert hasattr(m["Dec"].iloc[0], 'units')
  assert m["Dec"].iloc[0].units == 'degree'
  
  assert hasattr(m["Distance"].iloc[0], 'magnitude')
  assert hasattr(m["Distance"].iloc[0], 'units')
  assert str(m["Distance"].iloc[0].units) == 'light_year'
  
  assert hasattr(m["Width"].iloc[0], 'magnitude')
  assert hasattr(m["Width"].iloc[0], 'units')
  assert m["Width"].iloc[0].units == 'arcminute'
  
  assert hasattr(m["Magnitude"].iloc[0], 'magnitude')
  assert hasattr(m["Magnitude"].iloc[0], 'units')
  assert m["Magnitude"].iloc[0].units == 'mag'

def test_visible_planets():
  o = setup_observation()
  p = o.get_visible_planets()
  assert len(p) == 7
  
  # Check that Name is string type
  assert p["Name"].dtype == "string"
  
  # Check that unit fields have proper units
  assert hasattr(p["RA"].iloc[0], 'magnitude')
  assert hasattr(p["RA"].iloc[0], 'units')
  assert p["RA"].iloc[0].units == 'hour'
  
  assert hasattr(p["Dec"].iloc[0], 'magnitude')
  assert hasattr(p["Dec"].iloc[0], 'units')
  assert p["Dec"].iloc[0].units == 'degree'
  
  assert hasattr(p["Distance"].iloc[0], 'magnitude')
  assert hasattr(p["Distance"].iloc[0], 'units')
  assert p["Distance"].iloc[0].units == 'AU'
  
  assert hasattr(p["Size"].iloc[0], 'magnitude')
  assert hasattr(p["Size"].iloc[0], 'units')
  assert p["Size"].iloc[0].units == 'arcsecond'
  
  assert hasattr(p["Magnitude"].iloc[0], 'magnitude')
  assert hasattr(p["Magnitude"].iloc[0], 'units')
  assert p["Magnitude"].iloc[0].units == 'mag'
  
  assert hasattr(p["Elongation"].iloc[0], 'magnitude')
  assert hasattr(p["Elongation"].iloc[0], 'units')
  assert p["Elongation"].iloc[0].units == 'degree'
  
  assert hasattr(p["Phase"].iloc[0], 'magnitude')
  assert hasattr(p["Phase"].iloc[0], 'units')
  assert str(p["Phase"].iloc[0].units) == 'dimensionless'

def test_plot_messier():
  o = setup_observation()
  result = o.plot_messier()
  assert result is not None
