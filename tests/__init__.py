from apts import equipment, observations, place

def setup_equipment():
  # Setup basic equipment
  e = equipment.Equipment()
  e.register(equipment.Telescope(150, 750, t2_output=True))
  e.register(equipment.Eyepiece(25))
  return e


def setup_place():
  p = place.Place(lat=50.1637973, lon=19.7855169)
  return p


def setup_observation():
  # Setup basic observations
  p = setup_place()
  p.date = '2000/01/01 01:00:00'
  e = setup_equipment()
  o = observations.Observation(p, e)
  return o
