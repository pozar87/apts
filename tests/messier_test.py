import pytest
from default import *


def test_visiable_messier():
  o = setup_observations()
  m = o.get_visible_messier()
  p = o.get_visible_planets()
  #assert len(m) == 27
  #assert len(p) == 0
