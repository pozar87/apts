from apts import equipment, observations, place
import ephem

def setup_equipment():
  # Setup basic equipment
  e = equipment.Equipment()
  e.register(equipment.Telescope(150, 750, t2_output=True))
  e.register(equipment.Eyepiece(25))
  return e


def setup_place():
  p = place.Place(
      lat=50.1637973,
      lon=19.7855169,
      date = ephem.Date('2025/02/18 20:00:00'))
  return p


def setup_observation():
  # Setup basic observations
  p = setup_place()
  e = setup_equipment()
  o = observations.Observation(p, e)
  return o
