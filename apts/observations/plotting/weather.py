from typing import Optional, TYPE_CHECKING
from ...conditions import Conditions
from ...i18n import language_context

if TYPE_CHECKING:
    from ...plotting import NullPlotter, Plotter


class WeatherPlottingMixIn:
    if TYPE_CHECKING:
        @property
        def plot(self) -> "Plotter | NullPlotter": ...

    def plot_weather(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.weather(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_clouds(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.clouds(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_clouds_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.clouds_summary(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_precipitation(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.precipitation(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_precipitation_type_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.precipitation_type_summary(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_temperature(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.temperature(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_wind(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.wind(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_pressure_and_ozone(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.pressure_and_ozone(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_visibility(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.visibility(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_moon_illumination(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.moon_illumination(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_fog(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.fog(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_aurora(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.aurora(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_seeing(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.seeing(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_sqm(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.sqm(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_weather_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.weather_summary(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )
