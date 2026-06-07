import logging
from typing import TYPE_CHECKING, Optional

from apts.i18n import gettext_
from .utils import (
    get_plot_setup,
    handle_no_weather,
    generate_observation_weather_plot,
    mark_observation,
)

if TYPE_CHECKING:
    from apts.observations import Observation
    from apts.conditions import Conditions

logger = logging.getLogger(__name__)


def _generate_param_plot(
    observation: "Observation",
    plot_func_name: str,
    translated_title: str,
    min_val_attr: Optional[str],
    max_val_attr: Optional[str],
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    default_min: float = 0.0,
    default_max: float = 100.0,
    **args,
):
    eff_conditions = conditions or observation.conditions

    min_val = default_min
    if min_val_attr:
        min_val = getattr(eff_conditions, min_val_attr, default_min)

    max_val = default_max
    if max_val_attr:
        max_val = getattr(eff_conditions, max_val_attr, default_max)

    return generate_observation_weather_plot(
        observation,
        plot_func_name,
        translated_title,
        min_val,
        max_val,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_clouds(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    return _generate_param_plot(
        observation,
        "plot_clouds",
        gettext_("Clouds"),
        None,
        "max_clouds",
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_precipitation(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions
    max_val = min(
        eff_conditions.max_precipitation_probability,
        eff_conditions.max_precipitation_intensity,
    )
    return generate_observation_weather_plot(
        observation,
        "plot_precipitation",
        gettext_("Precipitation intensity and probability"),
        0,
        max_val,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_temperature(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    return _generate_param_plot(
        observation,
        "plot_temperature",
        gettext_("Temperatures"),
        "min_temperature",
        "max_temperature",
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_wind(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    return _generate_param_plot(
        observation,
        "plot_wind",
        gettext_("Wind speed"),
        None,
        "max_wind",
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_pressure_and_ozone(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    if observation.place.weather is None:
        return handle_no_weather(
            gettext_("Pressure and Ozone"), effective_dark_mode, style
        )

    ax = observation.place.weather.plot_pressure_and_ozone(
        dark_mode_override=effective_dark_mode, **args
    )
    if ax:
        mark_observation(observation, ax, effective_dark_mode, style)
    return ax


def generate_plot_visibility(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    return _generate_param_plot(
        observation,
        "plot_visibility",
        gettext_("Visibility"),
        "min_visibility",
        None,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        default_max=100.0,
        **args,
    )


def generate_plot_moon_illumination(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    return _generate_param_plot(
        observation,
        "plot_moon_illumination",
        gettext_("Moon Illumination"),
        None,
        "max_moon_illumination",
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_fog(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    return _generate_param_plot(
        observation,
        "plot_fog",
        gettext_("Fog"),
        None,
        "max_fog",
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_aurora(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    eff_conditions = conditions or observation.conditions

    if (
        observation.place.weather is not None
        and "aurora" in observation.place.weather.data.columns
    ):
        return generate_observation_weather_plot(
            observation,
            "plot_aurora",
            gettext_("Aurora"),
            eff_conditions.min_aurora,
            100,
            dark_mode_override=dark_mode_override,
            conditions=conditions,
            **args,
        )
    elif observation.place.weather is None:
        effective_dark_mode, style = get_plot_setup(dark_mode_override)
        return handle_no_weather(gettext_("Aurora"), effective_dark_mode, style)

    return None


def generate_plot_seeing(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    return _generate_param_plot(
        observation,
        "plot_seeing",
        gettext_("Seeing"),
        None,
        "max_seeing",
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def generate_plot_sqm(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    return _generate_param_plot(
        observation,
        "plot_sqm",
        gettext_("Sky brightness"),
        "min_sqm",
        None,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        default_max=22.0,
        **args,
    )
