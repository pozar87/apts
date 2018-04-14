import ephem
import pandas
import numpy

from .objects import Objects
from ..constants import ObjectTableLabels


class Planets(Objects):
  def __init__(self, place):
    super(Planets, self).__init__(place)
    # Init object list with all planets
    self.objects = pandas.DataFrame([
      ephem.Mercury(),
      ephem.Venus(),
      ephem.Mars(),
      ephem.Jupiter(),
      ephem.Saturn(),
      ephem.Uranus(),
      ephem.Neptune()],
      columns=[ObjectTableLabels.EPHEM])
    # Add name
    self.objects[ObjectTableLabels.NAME] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: body.Ephem.name, axis=1)
    # Compute transit of planets at given place
    self.objects[ObjectTableLabels.TRANSIT] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: self._compute_tranzit(body.Ephem), axis=1)
    # Compute altitude of planets at transit (at given place)
    self.objects[ObjectTableLabels.ALTITUDE] = self.objects[[ObjectTableLabels.EPHEM, ObjectTableLabels.TRANSIT]].apply(
      lambda body: self._altitude_at_transit(body.Ephem, body.Transit), axis=1)
    # Calculate planets magnitude
    self.objects[ObjectTableLabels.MAGNITUDE] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: body.Ephem.mag, axis=1)
    # Calculate planets RA
    self.objects[ObjectTableLabels.RA] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: numpy.degrees(body.Ephem.ra) * 24 / 360, axis=1)
    # Calculate planets Dec
    self.objects[ObjectTableLabels.DEC] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: numpy.degrees(body.Ephem.dec), axis=1)
    # Calculate planets distance from Earth
    self.objects[ObjectTableLabels.DISTANCE] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: body.Ephem.earth_distance, axis=1)
    # Calculate planets phase
    self.objects[ObjectTableLabels.PHASE] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: body.Ephem.phase, axis=1)
