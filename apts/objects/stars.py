import pandas as pd
import pytz
from datetime import timedelta
from types import SimpleNamespace

from skyfield.api import Star

from .base import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels
from .utils import calculate_refraction


class Stars(Objects):
    def __init__(self, place, catalogs: Catalogs, calculation_date=None):
        super(Stars, self).__init__(place, calculation_date=calculation_date)
        self.objects = catalogs.BRIGHT_STARS.copy()  # type: ignore
        self.objects[ObjectTableLabels.TRANSIT] = None
        self.objects[ObjectTableLabels.ALTITUDE] = None
        self.calculation_date = (
            calculation_date  # Store calculation_date for lazy computation
        )

    def compute(self, calculation_date=None, df_to_compute=None):
        if calculation_date is not None:
            # It's a Skyfield Time object. If it's an array, use the first element.
            if hasattr(calculation_date, "shape") and calculation_date.shape:
                t = calculation_date[0]
            elif isinstance(calculation_date, type(self.ts.now())):
                t = calculation_date
            else:
                t = self.ts.utc(calculation_date)

            # Avoid creating a whole new Place object, which is slow.
            observer_to_use = SimpleNamespace(
                date=t,
                local_timezone=self.place.local_timezone,
                lat_decimal=self.place.lat_decimal,
                lon_decimal=self.place.lon_decimal,
                elevation=self.place.elevation,
                observer=self.place.observer,
            )
        else:
            observer_to_use = self.place

        # If no specific DataFrame is provided, use the class's default.
        if df_to_compute is None:
            df_to_compute = self.objects

        # Work on a copy to avoid modifying the original DataFrame slice
        computed_df = df_to_compute.copy()

        # Fast transit and altitude calculation for stars
        transits, alts, rises, sets = self._vectorized_geometric_compute(
            computed_df, observer_to_use
        )
        computed_df[ObjectTableLabels.TRANSIT] = transits
        computed_df[ObjectTableLabels.ALTITUDE] = alts
        computed_df[ObjectTableLabels.RISING] = rises
        computed_df[ObjectTableLabels.SETTING] = sets
        self.objects.update(computed_df)
        return computed_df

    def get_skyfield_object(self, obj):
        if "skyfield_object" in obj:
            return obj["skyfield_object"]

        # Reconstruct if possible
        if "ra_hours" in obj and "dec_degrees" in obj:
            return self.fixed_body(obj["ra_hours"], obj["dec_degrees"])

        return None

    def find_by_name(self, name):
        """
        Finds a star by its name (e.g., "Sirius").
        """
        result = self.objects[self.objects["Name"] == name]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None

    def _compute_tranzit(self, skyfield_object, observer):
        """
        Calculates the upper meridian transit of a celestial object.
        For stars, a fast sidereal time approximation is used.
        """
        if skyfield_object is None:
            return None

        # Optimization for stars: use sidereal time formula
        if isinstance(skyfield_object, Star):
            current_dt = observer.date.utc_datetime()
            # Start search from the beginning of the UTC day
            t0_dt = current_dt.replace(
                hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC
            )
            t0 = self.ts.utc(t0_dt)

            # RA of the star
            ra_hours = skyfield_object.ra.hours
            lon_hours = self.place.lon_decimal / 15.0

            # LST = GMST + lon
            # We want LST == RA => GMST + lon == RA => GMST == RA - lon
            target_gmst = (ra_hours - lon_hours) % 24

            current_gmst = t0.gmst

            # Sidereal day is shorter than solar day
            # 1 solar hour = 1.0027379 sidereal hours
            # 1 sidereal hour = 0.99726957 solar hours
            sidereal_to_solar = 0.99726957

            dt_sidereal = (target_gmst - current_gmst) % 24
            dt_solar = dt_sidereal * sidereal_to_solar

            transit_dt = t0_dt + timedelta(hours=dt_solar)

            # Ensure we catch the transit relevant to the observation window
            # If it already happened more than 12 hours before observation start,
            # we might want the next one (stars transit once per sidereal day)
            if transit_dt < current_dt - timedelta(hours=12):
                transit_dt += timedelta(hours=24 * sidereal_to_solar)

            return transit_dt.astimezone(observer.local_timezone)

        return super()._compute_tranzit(skyfield_object, observer)

    def _altitude_at_transit(self, skyfield_object, transit, observer):
        # Calculate objects altitude at transit time
        if transit is None or pd.isna(transit):
            return 0

        # Optimization for stars: geometric formula
        if isinstance(skyfield_object, Star):
            lat = self.place.lat_decimal
            dec = skyfield_object.dec.degrees
            # Max altitude = 90 - abs(lat - dec)
            # Add refraction for better accuracy
            true_alt = 90.0 - abs(lat - dec)
            return true_alt + calculate_refraction(true_alt)

        return super()._altitude_at_transit(skyfield_object, transit, observer)

