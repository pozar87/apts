from typing import TYPE_CHECKING, Optional

from ...i18n import language_context

if TYPE_CHECKING:
    from ...conditions import Conditions


class WeatherPlottingMixIn:
    def plot_weather(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.weather(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_clouds(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.clouds(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_clouds_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.clouds_summary(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, **args
            )

    def plot_precipitation(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.precipitation(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_precipitation_type_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.precipitation_type_summary(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, **args
            )

    def plot_temperature(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.temperature(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_wind(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.wind(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_pressure_and_ozone(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.pressure_and_ozone(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, **args
            )

    def plot_visibility(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.visibility(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_moon_illumination(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.moon_illumination(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_fog(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.fog(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_aurora(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.aurora(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_seeing(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.seeing(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_sqm(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.sqm(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_weather_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional["Conditions"] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.weather_summary(  # type: ignore[attr-defined]
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )
