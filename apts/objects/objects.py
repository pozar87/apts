import logging
import ephem
import numpy
import pytz
import pandas

from datetime import timedelta
from ..constants import ObjectTableLabels

logger = logging.getLogger(__name__)


class Objects:
  def __init__(self, place):
    self.place = place
    self.objects : pandas.DataFrame = pandas.DataFrame()

  def get_visible(self, conditions, start, stop, hours_margin=0, sort_by=ObjectTableLabels.TRANSIT):
    visible = self.objects
    # Add ID collumn
    visible['ID'] = visible.index
    visible = visible[
      # Filter objects by they transit
      (visible.Transit > start - timedelta(hours=hours_margin)) &
      (visible.Transit < stop + timedelta(hours=hours_margin)) &
      # Filter objects by they min altitude at transit
      (visible.Altitude > conditions.min_object_altitude) &
      # Filter object by they magnitude
      # Handle pint.Quantity objects for magnitude
      (visible.Magnitude.apply(lambda x: x.magnitude if hasattr(x, 'magnitude') else x) < conditions.max_object_magnitude)]
    # Sort objects by given order
    visible = visible.sort_values(by=sort_by, ascending=True)
    return visible

  @staticmethod
  def fixed_body(RA, Dec):
    # Create body at given coordinates
    body = ephem.FixedBody()
    # Handle pint.Quantity objects
    if hasattr(RA, 'magnitude'):
      body._ra = str(RA.magnitude)
    else:
      body._ra = str(RA)
    
    if hasattr(Dec, 'magnitude'):
      body._dec = str(Dec.magnitude)
    else:
      body._dec = str(Dec)
    return body

  def _compute_tranzit(self, body):
    # Return transit time in local time
    logger.debug(f"Computing transit time for body {body.name} at {self.place.date}")
    return self.place.next_transit(body).datetime().replace(tzinfo=pytz.UTC).astimezone(self.place.local_timezone)

  def _compute_setting(self, body):
    # Return setting time in local time
    logger.debug(f"Computing setting time for body {body.name} at {self.place.date}")
    return self.place.next_setting(body).datetime().replace(tzinfo=pytz.UTC).astimezone(self.place.local_timezone)

  def _compute_rising(self, body):
    # Return rising time in local time
    logger.debug(f"Computing rising time for body {body.name} at {self.place.date}")
    return self.place.next_rising(body).datetime().replace(tzinfo=pytz.UTC).astimezone(self.place.local_timezone)

  def _altitude_at_transit(self, body, transit):
    # Calculate objects altitude at transit time
    body.compute(self.place)
    return numpy.degrees(body.alt)
