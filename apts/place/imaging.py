import datetime
from typing import cast

from apts.constants.twilight import Twilight

from .conditions import PlaceConditionsMixIn

class PlaceImagingMixIn(PlaceConditionsMixIn):
    def get_imaging_window(
        self,
        skyfield_object,
        min_altitude=30,
        target_date=None,
        astro_twilight_start=None,
        astro_twilight_end=None,
    ) -> dict:
        """
        Calculate total continuous minutes an object remains above the threshold during "darkness"
        (Astronomical Twilight to Astronomical Twilight).
        Provides start_time and end_time for this window.
        """
        # 1. Determine the night window (astronomical twilight)
        if astro_twilight_start is None or astro_twilight_end is None:
            # We look for the night following the given target_date or self.date
            t_start = (
                target_date
                if target_date is not None
                else cast(datetime.datetime, self.date.utc_datetime()).replace(
                    tzinfo=datetime.timezone.utc
                )
            )
            # Ensure it's a datetime
            if isinstance(t_start, datetime.date) and not isinstance(
                t_start, datetime.datetime
            ):
                t_start = datetime.datetime.combine(t_start, datetime.time.min).replace(
                    tzinfo=self.local_timezone
                )

            # Get sunset and sunrise (astronomical twilight)
            astro_twilight_start = self.sunset_time(
                start_search_from=t_start, twilight=Twilight.ASTRONOMICAL
            )

        # Re-check in case sunset_time returned None
        if astro_twilight_start is None:
            return {
                "total_minutes": 0,
                "start_time": None,
                "end_time": None,
            }

        if astro_twilight_end is None:
            astro_twilight_end = self.sunrise_time(
                start_search_from=astro_twilight_start, twilight=Twilight.ASTRONOMICAL
            )
        if astro_twilight_end is None:
            return {
                "total_minutes": 0,
                "start_time": None,
                "end_time": None,
            }

        # 2. Check object altitude during this window
        num_points = 60 * 12  # Every 2 minutes for 24h
        df = self.get_altaz_curve(
            skyfield_object, astro_twilight_start, astro_twilight_end, num_points
        )

        above_threshold = df[df["Altitude"] >= min_altitude]
        if above_threshold.empty:
            return {
                "total_minutes": 0,
                "start_time": None,
                "end_time": None,
            }

        # Find the longest continuous block
        above_threshold = above_threshold.copy()
        above_threshold["group"] = (
            above_threshold.index.to_series().diff() > 1
        ).cumsum()
        longest_group = above_threshold.groupby("group").size().idxmax()
        window_df = above_threshold[above_threshold["group"] == longest_group]

        start_time = window_df["UTC_datetime"].iloc[0].to_pydatetime()
        end_time = window_df["UTC_datetime"].iloc[-1].to_pydatetime()
        total_minutes = (end_time - start_time).total_seconds() / 60.0

        return {
            "total_minutes": total_minutes,
            "start_time": start_time,
            "end_time": end_time,
        }
