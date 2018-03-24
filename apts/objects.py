import ephem
import numpy
import pytz
import datetime

from datetime import timedelta
from apts import utils


class Objects:
  def __init__(self, place):
    self.place = place

  def get_visible(self, conditions, start, stop, hours_margin=0, sort_by=[utils.Labels.TRANSIT]):
    visible = self.objects
    visible = visible[
      # Filter objects by they transit
      (visible.Transit > start - timedelta(hours=hours_margin)) &
      (visible.Transit < stop + timedelta(hours=hours_margin)) &
      # Filter objects by they min altitude at transit
      (visible.Altitude > conditions.min_object_altitude) &
      # Filter object by they magnitude
      (visible.Magnitude < conditions.max_object_magnitude)]
    # Sort objects by given order    
    visible = visible.sort_values(sort_by, ascending=[1])
    return visible

  def fixed_body(RA, Dec):
    # Create body at given coordinates
    body = ephem.FixedBody()
    body._ra = str(RA)
    body._dec = str(Dec)
    return body

  def compute_tranzit(self, body):
    # Return transit time in local time
    self.place.date = datetime.datetime.now()
    return self.place.next_transit(body).datetime().replace(tzinfo=pytz.UTC).astimezone(self.place.local_timezone)

  def altitude_at_transit(self, body, transit):
    # Calculate objects altitude at transit time
    self.place.date = transit.astimezone(pytz.UTC)
    body.compute(self.place)
    return numpy.degrees(body.alt)
