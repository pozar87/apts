import pandas as pd
from importlib import resources
import pint

class Catalogs:
    @staticmethod
    def _load_messier_with_units():
        # Load Messier catalogue data
        messier_df = pd.read_csv(str(resources.files('apts').joinpath('data/messier.csv')))

        # Create unit registry
        ureg = pint.UnitRegistry()

        # Define astronomical units that might not be in Pint by default
        ureg.define('mag = [magnitude] = mag')  # Astronomical magnitude
        ureg.define('hour = 60 * minute = h = hr')  # Hour for Right Ascension

        # Convert columns to quantities with units
        messier_df['Distance'] = messier_df['Distance'].apply(lambda x: x * ureg.light_year)
        messier_df['RA'] = messier_df['RA'].apply(lambda x: x * ureg.hour)
        messier_df['Dec'] = messier_df['Dec'].apply(lambda x: x * ureg.degree)
        messier_df['Width'] = messier_df['Width'].apply(lambda x: x * ureg.arcminute)
        messier_df['Height'] = messier_df['Height'].apply(lambda x: x * ureg.arcminute)
        messier_df['Magnitude'] = messier_df['Magnitude'].apply(lambda x: x * ureg.mag)

        return messier_df

    # Initialize the catalog with pint unit objects
    MESSIER = _load_messier_with_units()

    # Load NGC catalogue data
    #NGC = pandas.read_csv(pkg_resources.resource_filename('apts', 'data/ngc.csv'))
