from math import radians as rad

from . import setup_place


def test_place_should_have_correct_coordinates():
  p = setup_place()
  lat = 50.1637973
  lon = 19.7855169

  assert p.lat_decimal == lat
  assert p.lat == rad(lat)
  assert p.lon_decimal == lon
  assert p.lon == rad(lon)
