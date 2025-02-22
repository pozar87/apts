from . import setup_observation

def test_visiable_messier():
  o = setup_observation()
  print(o)
  m = o.get_visible_messier()
  assert len(m) == 11

def test_visible_planets():
  o = setup_observation()
  p = o.get_visible_planets()
  assert len(p) == 7

def test_plot_messier():
  o = setup_observation()
  result = o.plot_messier()
  assert result is not None
