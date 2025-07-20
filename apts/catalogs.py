import pandas as pd
from importlib import resources
from .utils import ureg


class Catalogs:
    @staticmethod
    def _load_messier_with_units():
        # Load Messier catalogue data
        messier_df = pd.read_csv(
            str(resources.files("apts").joinpath("data/messier.csv"))
        )

        # Set proper dtypes for string columns
        string_columns = ["Messier", "NGC", "Name", "Type", "Constellation"]
        for column in string_columns:
            messier_df[column] = messier_df[column].astype("string")

        # Convert columns to quantities with units
        messier_df["Distance"] = messier_df["Distance"].apply(
            lambda x: x * ureg.light_year
        )
        messier_df["RA"] = messier_df["RA"].apply(lambda x: x * ureg.hour)
        messier_df["Dec"] = messier_df["Dec"].apply(lambda x: x * ureg.degree)
        messier_df["Width"] = messier_df["Width"].apply(lambda x: x * ureg.arcminute)
        messier_df["Height"] = messier_df["Height"].apply(lambda x: x * ureg.arcminute)
        messier_df["Magnitude"] = messier_df["Magnitude"].apply(lambda x: x * ureg.mag)

        return messier_df

    @staticmethod
    def _load_bright_stars_with_units():
        # Load bright stars catalogue data
        bright_stars_df = pd.read_csv(
            str(resources.files("apts").joinpath("data/bright_stars.csv"))
        )

        # Set proper dtypes for string columns
        string_columns = ["Name"]
        for column in string_columns:
            bright_stars_df[column] = bright_stars_df[column].astype("string")

        # Convert columns to quantities with units
        bright_stars_df["RA"] = bright_stars_df["RA"].apply(lambda x: x * ureg.hour)
        bright_stars_df["Dec"] = bright_stars_df["Dec"].apply(lambda x: x * ureg.degree)
        bright_stars_df["Magnitude"] = bright_stars_df["Magnitude"].apply(
            lambda x: x * ureg.mag
        )

        return bright_stars_df

    # Initialize the catalog with pint unit objects
    MESSIER = _load_messier_with_units()
    BRIGHT_STARS = _load_bright_stars_with_units()

    # Load NGC catalogue data
    # NGC = pandas.read_csv(pkg_resources.resource_filename('apts', 'data/ngc.csv'))
