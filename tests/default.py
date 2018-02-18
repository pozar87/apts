from apts import *

def setup_equipment():
  # Setup basic equipment
  e = Equipment()
  e.register(equipment.Telescope(150, 750, t2_output = True))
  e.register(equipment.Eyepiece(25))
  return e

def setup_observations():
  # Setup basic observations
  p = Place(lat=50.1637973, lon=19.7855169)
  p.date = '1987/7/7 22:00:00' 
  e = setup_equipment()
  o = Observation(p, e)
  return o  
