from typing import Any, Optional, TYPE_CHECKING
import pandas as pd

if TYPE_CHECKING:
    pass

class WeatherPlottingMixIn:
    if TYPE_CHECKING:
        local_timezone: Any
        data: pd.DataFrame
        def _filter_data(self, rows: list[str]) -> pd.DataFrame: ...

    def plot_clouds(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        from apts.plotting.weather import core
        return core.plot_clouds(self, dark_mode_override=dark_mode_override, **args)

    def plot_precipitation(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        from apts.plotting.weather import core
        return core.plot_precipitation(self, dark_mode_override=dark_mode_override, **args)

    def plot_precipitation_type_summary(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        from apts.plotting.weather import core
        return core.plot_precipitation_type_summary(self, dark_mode_override=dark_mode_override, **args)

    def plot_clouds_summary(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        from apts.plotting.weather import core
        return core.plot_clouds_summary(self, dark_mode_override=dark_mode_override, **args)

    def plot_temperature(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        from apts.plotting.weather import core
        return core.plot_temperature(self, dark_mode_override=dark_mode_override, **args)

    def plot_wind(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        from apts.plotting.weather import core
        return core.plot_wind(self, dark_mode_override=dark_mode_override, **args)

    def plot_pressure_and_ozone(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        from apts.plotting.weather import core
        return core.plot_pressure_and_ozone(self, dark_mode_override=dark_mode_override, **args)

    def plot_visibility(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        from apts.plotting.weather import core
        return core.plot_visibility(self, dark_mode_override=dark_mode_override, **args)

    def plot_fog(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        from apts.plotting.weather import core
        return core.plot_fog(self, dark_mode_override=dark_mode_override, **args)

    def plot_moon_illumination(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        from apts.plotting.weather import core
        return core.plot_moon_illumination(self, dark_mode_override=dark_mode_override, **args)

    def plot_aurora(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        from apts.plotting.weather import core
        return core.plot_aurora(self, dark_mode_override=dark_mode_override, **args)

    def plot_seeing(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        from apts.plotting.weather import core
        return core.plot_seeing(self, dark_mode_override=dark_mode_override, **args)

    def plot_sqm(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        from apts.plotting.weather import core
        return core.plot_sqm(self, dark_mode_override=dark_mode_override, **args)
