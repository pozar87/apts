from datetime import timedelta

import ephem
import numpy
import pandas
import pint

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
    # Set proper dtype for string columns
    self.objects[ObjectTableLabels.NAME] = self.objects[ObjectTableLabels.NAME].astype('string')
    # Compute positions
    self.compute()

  def compute(self):
    # Create unit registry
    ureg = pint.UnitRegistry()
    
    # Define astronomical units that might not be in Pint by default
    ureg.define('mag = [magnitude] = mag')  # Astronomical magnitude
    ureg.define('hour = 60 * minute = h = hr')  # Hour for Right Ascension
    ureg.define('AU = 149597870700 * meter = au')  # Astronomical Unit
    ureg.define('arcsecond = degree / 3600 = arcsec')  # Arc second
    
    # Compute transit of planets at given place
    self.objects[ObjectTableLabels.TRANSIT] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: self._compute_tranzit(body.Ephem), axis=1)
    # Compute rising of planets at given place
    self.objects[ObjectTableLabels.RISING] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: self._compute_rising(body.Ephem), axis=1)
    # Compute transit of planets at given place
    self.objects[ObjectTableLabels.SETTING] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: self._compute_setting(body.Ephem), axis=1)
    # Compute altitude of planets at transit (at given place)
    self.objects[ObjectTableLabels.ALTITUDE] = self.objects[[ObjectTableLabels.EPHEM, ObjectTableLabels.TRANSIT]].apply(
      lambda body: self._altitude_at_transit(body.Ephem, body.Transit), axis=1)
    # Calculate planets magnitude
    self.objects[ObjectTableLabels.MAGNITUDE] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: body.Ephem.mag * ureg.mag, axis=1)
    # Calculate planets RA
    self.objects[ObjectTableLabels.RA] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: numpy.degrees(body.Ephem.ra) * 24 / 360 * ureg.hour, axis=1)
    # Calculate planets Dec
    self.objects[ObjectTableLabels.DEC] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: numpy.degrees(body.Ephem.dec) * ureg.degree, axis=1)
    # Calculate planets distance from Earth
    self.objects[ObjectTableLabels.DISTANCE] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: body.Ephem.earth_distance * ureg.AU, axis=1)
    # Calculate planets size
    self.objects[ObjectTableLabels.SIZE] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: body.Ephem.size * ureg.arcsecond, axis=1)
    # Calculate planets elongation
    self.objects[ObjectTableLabels.ELONGATION] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: numpy.degrees(body.Ephem.elong) * ureg.degree, axis=1)
    # Calculate planets phase
    self.objects[ObjectTableLabels.PHASE] = self.objects[[ObjectTableLabels.EPHEM]].apply(
      lambda body: body.Ephem.phase * ureg.dimensionless, axis=1)

  def get_visible(self, conditions, start, stop, hours_margin=0, sort_by=ObjectTableLabels.TRANSIT):
    visible = self.objects
    # Add ID collumn
    visible['ID'] = visible.index
    visible = visible[
      # Filter objects by they rising and setting or transit
      ((visible.Setting < stop + timedelta(hours=hours_margin)) |
       (visible.Rising < stop + timedelta(hours=hours_margin)) |
       (
           (visible.Transit > start - timedelta(hours=hours_margin)) &
           (visible.Transit < stop + timedelta(hours=hours_margin)))
       ) &
      # Filter object by they magnitude
      # Handle pint.Quantity objects for magnitude
      (visible.Magnitude.apply(lambda x: x.magnitude if hasattr(x, 'magnitude') else x) < conditions.max_object_magnitude)]
    # Sort objects by given order
    visible = visible.sort_values(by = sort_by, ascending=True)
    return visible
