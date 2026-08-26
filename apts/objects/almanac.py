from typing import TYPE_CHECKING, Any

from .calculations import (
    calculate_altitude_at_transit,
    calculate_rising_and_setting,
    calculate_transit,
)

if TYPE_CHECKING:
    from skyfield.api import Timescale


class AlmanacMixIn:
    if TYPE_CHECKING:
        ts: Timescale
        place: Any

    def _compute_tranzit(self, skyfield_object, observer):
        """
        Calculates the upper meridian transit of a celestial object.
        For stars, a fast sidereal time approximation is used.
        """
        return calculate_transit(
            skyfield_object,
            self.place.eph,
            self.place.location,
            self.place.lat_decimal,
            self.place.lon_decimal,
            observer.date.utc_datetime(),
            observer.local_timezone,
            self.ts,
        )

    def _compute_rising_and_setting(self, skyfield_object, observer, transit_time):
        """
        Calculates rising and setting times for a celestial object.
        """
        return calculate_rising_and_setting(
            skyfield_object,
            self.place.eph,
            self.place.location,
            transit_time,
            observer.local_timezone,
            self.ts,
        )

    def _altitude_at_transit(self, skyfield_object, transit, observer):
        """
        Calculates object's altitude at transit time.
        """
        return calculate_altitude_at_transit(
            skyfield_object,
            transit,
            self.place.lat_decimal,
            self.place.observer,
            self.ts,
        )
