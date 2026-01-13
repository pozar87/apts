from apts import equipment, observations, place, opticalequipment
import datetime

def setup_equipment():
  # Setup basic equipment
  e = equipment.Equipment()
  e.register(opticalequipment.Telescope(150, 750, t2_output=True))
  e.register(opticalequipment.Eyepiece(25))
  return e


def setup_place():
  p = place.Place(
      name='Zelków',
      lat=50.1637973,
      lon=19.7855169,
      date = datetime.datetime(2025, 2, 18, 12, 0, 0, tzinfo=datetime.timezone.utc))
  return p


def setup_observation():
  # Setup basic observations
  p = setup_place()
  e = setup_equipment()
  o = observations.Observation(p, e)
  return o


def setup_southern_place():
  p = place.Place(
      name='Sydney',
      lat=-33.8688,
      lon=151.2093,
      date = datetime.datetime(2025, 2, 18, 22, 0, 0, tzinfo=datetime.timezone.utc))
  return p


def setup_southern_observation():
  # Setup basic observations
  p = setup_southern_place()
  e = setup_equipment()
  o = observations.Observation(p, e)
  return o
