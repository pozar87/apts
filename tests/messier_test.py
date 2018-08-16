from . import setup_observation

def test_visiable_messier():
  o = setup_observation()
  m = o.get_visible_messier()
  p = o.get_visible_planets()
  #assert len(m) == 27
  #assert len(p) == 0


def test_plot_messier():
  o = setup_observation()
  #o.plot_messier()