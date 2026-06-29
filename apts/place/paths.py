import datetime
from typing import TYPE_CHECKING, Any, Iterable, Optional, cast

import numpy as np
import pandas as pd
from skyfield import almanac
from skyfield.api import Time

from .conditions.base import PlaceConditionsMixIn

class PlacePathsMixIn(PlaceConditionsMixIn):
    def get_altaz_curve(
        self,
        skyfield_object,
        start_time,
        end_time,
        num_points=100,
        observer_at_times=None,
        fast=False,
    ):
        if observer_at_times is not None:
            times = observer_at_times.t
        else:
            t0 = start_time if isinstance(start_time, Time) else self.ts.utc(start_time)
            t1 = end_time if isinstance(end_time, Time) else self.ts.utc(end_time)
            times = self.ts.linspace(t0, t1, num_points)
            observer_at_times = self.observer.at(times)

        if fast:
            # Fast AltAz calculation that bypasses expensive nutation, aberration,
            # and light deflection calculations (Standard Apparent) by manually
            # wrapping an Astrometric position in an Apparent object.
            from skyfield.positionlib import Apparent

            pos = observer_at_times.observe(skyfield_object)
            app = Apparent(pos.position.au, pos.velocity.au_per_d, pos.t)
            app.center = pos.center
            alt, az, _ = app.altaz()
        else:
            alt, az, _ = observer_at_times.observe(skyfield_object).apparent().altaz()

        # Vectorized conversion to datetime
        utcs = times.utc_datetime()

        df = pd.DataFrame(
            {
                "Time": list(cast(Iterable[Any], times)),
                "UTC_datetime": utcs,
                "Altitude": alt.degrees,
                "Azimuth": az.degrees,
            }
        )

        # For Southern Hemisphere, the transit is North (0/360 degrees).
        # If the path crosses this point, matplotlib will draw a line across the plot.
        # To prevent this, we find the wrap-around point and insert a NaN row.
        if self.lat_decimal < 0:
            diffs = cast(pd.Series, df["Azimuth"].diff())
            wrap_around_indices = cast(pd.Series, diffs[diffs.abs() > 180]).index
            if len(wrap_around_indices) > 0:
                idx = cast(Any, wrap_around_indices[0])
                new_index = idx - 0.5
                nan_row = pd.DataFrame(
                    {
                        "Time": [pd.NaT],
                        "UTC_datetime": [pd.NaT],
                        "Altitude": [np.nan],
                        "Azimuth": [np.nan],
                    },
                    index=[new_index],  # type: ignore
                )
                df = pd.concat([df, nan_row]).sort_index().reset_index(drop=True)  # type: ignore

        # Ensure UTC_datetime is recognized as a datetime series
        df["UTC_datetime"] = pd.to_datetime(df["UTC_datetime"])
        local_datetimes = df["UTC_datetime"]
        if local_datetimes.dt.tz is None:
            local_datetimes = local_datetimes.dt.tz_localize("UTC")

        df["Local_time"] = local_datetimes.dt.tz_convert(
            self.local_timezone
        ).dt.strftime("%H:%M")
        return df

    def moon_path(self) -> pd.DataFrame:
        start_time = self.date.utc_datetime().replace(  # type: ignore
            hour=0, minute=0, second=0, microsecond=0
        )
        end_time = start_time + datetime.timedelta(days=1)
        df = self.get_altaz_curve(self.moon, start_time, end_time, num_points=26 * 8)
        df = df.rename(columns={"Altitude": "Moon altitude"})

        # Vectorized moon phase calculation
        if "UTC_datetime" in df.columns:
            valid_mask = df["UTC_datetime"].notna()
        else:
            # Fallback for mocks
            # Optimization: list comprehension over .values is faster than .apply() for fallback path.
            df["UTC_datetime"] = [
                t.utc_datetime() if hasattr(t, "utc_datetime") else pd.NaT
                for t in df["Time"].values
            ]
            df["UTC_datetime"] = pd.to_datetime(df["UTC_datetime"])
            valid_mask = df["UTC_datetime"].notna()

        if bool(valid_mask.any()):
            # Reconstruct valid Skyfield Time vector from existing list in DataFrame.
            # This is significantly faster than self.ts.from_datetimes().
            valid_times_list = df.loc[valid_mask, "Time"].tolist()
            # Re-wrap list of Time objects into a single vectorized Time object
            tt = np.array([t.tt for t in valid_times_list])
            delta_t = np.array([t.delta_t for t in valid_times_list])
            times_vec = Time(self.ts, tt, delta_t)

            moon_phase_angles = almanac.moon_phase(self.eph, times_vec).degrees
            df.loc[valid_mask, "Phase"] = (
                cast(np.ndarray[Any, Any], moon_phase_angles) / 360.0
            ) * 100
            df.loc[valid_mask, "Lunation"] = (
                cast(np.ndarray[Any, Any], moon_phase_angles) / 360.0
            )
        else:
            df["Phase"] = pd.NA
            df["Lunation"] = pd.NA

        df["Time"] = df["UTC_datetime"].dt.time
        return df

    def sun_path(self) -> pd.DataFrame:
        start_time = self.date.utc_datetime().replace(  # type: ignore
            hour=0, minute=0, second=0, microsecond=0
        )
        end_time = start_time + datetime.timedelta(days=1)
        df = self.get_altaz_curve(self.sun, start_time, end_time, num_points=26 * 4)
        df = df.rename(columns={"Altitude": "Sun altitude"})

        if "UTC_datetime" not in df.columns:
            # Fallback for mocks
            # Optimization: list comprehension over .values is faster than .apply() for fallback path.
            df["UTC_datetime"] = [
                t.utc_datetime() if hasattr(t, "utc_datetime") else pd.NaT
                for t in df["Time"].values
            ]
            df["UTC_datetime"] = pd.to_datetime(df["UTC_datetime"])

        df["Time"] = df["UTC_datetime"].dt.time
        return df

    def plot_sun_path(self, dark_mode_override: Optional[bool] = None, **args):
        from ..plotting.path import generate_plot_sun_path

        if TYPE_CHECKING:
            from .base import Place
        return generate_plot_sun_path(cast("Place", self), dark_mode_override, **args)

    def plot_moon_path(self, dark_mode_override: Optional[bool] = None, **args):
        from ..plotting.path import generate_plot_moon_path

        if TYPE_CHECKING:
            from .base import Place
        return generate_plot_moon_path(cast("Place", self), dark_mode_override, **args)
