import pandas
import pkg_resources

class Catalogs:
  # Load Messier catalogue data
  MESSIER = pandas.read_csv(pkg_resources.resource_filename('apts', 'data/messier.csv'))
  # Load NGC catalogue data
  #NGC = pandas.read_csv(pkg_resources.resource_filename('apts', 'data/ngc.csv'))

