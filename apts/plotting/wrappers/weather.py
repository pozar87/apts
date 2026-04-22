from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ...observations import Observation
    from ...conditions import Conditions

def _ensure_weather(
    observation: "Observation", conditions: Optional["Conditions"] = None
):
    if observation.place.weather is None:
        obs_window = (
            (observation.start, observation.stop)
            if observation.start is not None and observation.stop is not None
            else None
        )
        observation.place.get_weather(
            conditions=conditions or observation.conditions,
            observation_window=obs_window,
        )


def plot_weather(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_weather(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_clouds(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_clouds(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_clouds_summary(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .. import weather

    _ensure_weather(observation)
    return weather.generate_plot_clouds_summary(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_precipitation(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_precipitation(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_precipitation_type_summary(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .. import weather

    _ensure_weather(observation)
    return weather.generate_plot_precipitation_type_summary(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_temperature(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_temperature(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_wind(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_wind(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_pressure_and_ozone(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .. import weather

    _ensure_weather(observation)
    return weather.generate_plot_pressure_and_ozone(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_visibility(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_visibility(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_moon_illumination(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_moon_illumination(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_fog(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_fog(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_aurora(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_aurora(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_seeing(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_seeing(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_sqm(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_sqm(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_weather_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .. import weather

    _ensure_weather(observation, conditions)
    return weather.generate_plot_weather_summary(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )
