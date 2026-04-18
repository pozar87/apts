from typing import Optional, cast
import pandas as pd
from apts.i18n import gettext_
from .utils import generic_line_plot, generic_pie_plot, get_plot_setup

def plot_clouds(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["cloudCover"])
    return generic_line_plot(
        data,
        gettext_("Clouds"),
        gettext_("Cloud cover [%]"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        ylim=(0, 105),
        **args
    )

def plot_precipitation(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["precipIntensity", "precipProbability"])
    return generic_line_plot(
        data,
        gettext_("Precipitation intensity and probability"),
        gettext_("Probability"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        **args
    )

def plot_precipitation_type_summary(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["precipType"])
    return generic_pie_plot(
        data,
        "precipType",
        gettext_("Precipitation type summary"),
        dark_mode_override=dark_mode_override,
        **args
    )

def plot_clouds_summary(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["summary"])
    return generic_pie_plot(
        data,
        "summary",
        gettext_("Cloud summary"),
        dark_mode_override=dark_mode_override,
        **args
    )

def plot_temperature(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["temperature", "apparentTemperature", "dewPoint"])
    return generic_line_plot(
        data,
        gettext_("Temperatures"),
        gettext_("Temperature [°C]"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        **args
    )

def plot_wind(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["windSpeed"])
    # Ensure windSpeed is numeric for max calculation
    data["windSpeed"] = pd.to_numeric(data["windSpeed"], errors="coerce")
    max_wind_speed = data[["windSpeed"]].max().max()

    ylim = (0, max_wind_speed + 1) if not pd.isna(max_wind_speed) else None

    return generic_line_plot(
        data,
        gettext_("Wind speed"),
        gettext_("Wind speed [km/h]"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        y="windSpeed",
        ylim=ylim,
        **args
    )

def plot_pressure_and_ozone(weather, dark_mode_override: Optional[bool] = None, **args):
    available_columns = [
        col
        for col in ["pressure", "ozone"]
        if col in cast(pd.DataFrame, weather.data).columns
        and bool(
            cast(pd.DataFrame, weather.data)[col].astype(str).str.lower().nunique() > 1
        )
        and bool(cast(pd.DataFrame, weather.data)[col].notna().any())
    ]
    if not available_columns:
        data = pd.DataFrame()
    else:
        data = weather._filter_data(available_columns)

    plot_title = gettext_("Pressure")
    secondary_y_plot = []
    if "ozone" in available_columns and "pressure" in available_columns:
        plot_title = gettext_("Pressure and Ozone")
        secondary_y_plot = ["ozone"]
    elif "ozone" in available_columns:
        plot_title = gettext_("Ozone")

    effective_dark_mode, style = get_plot_setup(dark_mode_override)

    primary_y_label = ""
    if "pressure" in available_columns:
        primary_y_label = gettext_("Pressure [hPa]")
    elif "ozone" in available_columns:
        primary_y_label = gettext_("Ozone [DU]")

    ax = generic_line_plot(
        data,
        plot_title,
        primary_y_label,
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        secondary_y=secondary_y_plot,
        **args
    )

    if not data.empty and secondary_y_plot and hasattr(ax, "right_ax"):
        ax_secondary = ax.right_ax
        ax_secondary.set_ylabel(
            gettext_("Ozone [DU]"),
            color=style["TEXT_COLOR"],
        )
        ax_secondary.tick_params(axis="y", colors=style["TICK_COLOR"])
        ax_secondary.spines["right"].set_color(style["AXIS_COLOR"])

    return ax

def plot_visibility(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["visibility"])
    data = data[data["visibility"].notna()]
    return generic_line_plot(
        data,
        gettext_("Visibility"),
        gettext_("Visibility [km]"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        **args
    )

def plot_fog(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["fog"])
    return generic_line_plot(
        data,
        gettext_("Fog"),
        gettext_("Fog [%]"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        ylim=(0, 105),
        **args
    )

def plot_moon_illumination(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["moonIllumination", "moonWaxing"])
    if data.empty:
        is_waxing = True
    else:
        is_waxing = data["moonWaxing"].iloc[0]

    title = (
        f"{gettext_('Moon Illumination')} "
        f"({gettext_('Waxing') if is_waxing else gettext_('Waning')})"
    )

    return generic_line_plot(
        data,
        title,
        gettext_("Illumination [%]"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        y="moonIllumination",
        ylim=(0, 105),
        **args
    )

def plot_aurora(weather, dark_mode_override: Optional[bool] = None, **args):
    if "aurora" not in weather.data.columns:
        data = pd.DataFrame()
    else:
        data = weather._filter_data(["aurora"])

    return generic_line_plot(
        data,
        gettext_("Aurora"),
        gettext_("Aurora"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        y="aurora",
        ylim=(0, 105),
        **args
    )

def plot_seeing(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["seeing"])
    return generic_line_plot(
        data,
        gettext_("Seeing"),
        gettext_("Seeing [arcsec]"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        y="seeing",
        ylim=(0, 5.5),
        **args
    )

def plot_sqm(weather, dark_mode_override: Optional[bool] = None, **args):
    data = weather._filter_data(["sqm"])
    return generic_line_plot(
        data,
        gettext_("Sky brightness"),
        gettext_("SQM [mag/arcsec²]"),
        weather.local_timezone,
        dark_mode_override=dark_mode_override,
        y="sqm",
        ylim=(10, 22.5),
        **args
    )
