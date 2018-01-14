import pandas
import ephem
import pytz
import numpy
import pkg_resources

class Catalogs:

  # Load Messier catalogue data
  MESSIER = pandas.read_csv(pkg_resources.resource_filename('apts', 'data/messier.csv'))

  def fixed_body(RA, Dec):
    # Create body at given coordinates
    body = ephem.FixedBody()
    body._ra = str(RA)
    body._dec = str(Dec)
    return body

  def compute_tranzit(body, place):
    # Return transit time in local time
    return place.next_transit(body).datetime().replace(tzinfo=pytz.UTC).astimezone(place.local_timezone)

  def altitude_at_transit(body, place, transit):
    place.date = transit.astimezone(pytz.UTC)
    body.compute(place)
    return numpy.degrees(body.alt)
