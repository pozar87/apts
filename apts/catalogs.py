import pandas
from importlib import resources

class Catalogs:
  # Load Messier catalogue data
  MESSIER = pandas.read_csv(str(resources.files('apts').joinpath('data/messier.csv')))
  # Load NGC catalogue data
  #NGC = pandas.read_csv(pkg_resources.resource_filename('apts', 'data/ngc.csv'))
