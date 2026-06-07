import logging
from typing import TYPE_CHECKING, Optional

import pandas as pd

from apts.i18n import gettext_
from .utils import (
    get_plot_setup,
    handle_no_weather,
    apply_colors,
)

if TYPE_CHECKING:
    from apts.observations import Observation
    from apts.conditions import Conditions

logger = logging.getLogger(__name__)


def generate_plot_clouds_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    if observation.place.weather is None:
        return handle_no_weather(gettext_("Cloud summary"), effective_dark_mode, style)

    return observation.place.weather.plot_clouds_summary(
        dark_mode_override=effective_dark_mode, **args
    )


def generate_plot_precipitation_type_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    if observation.place.weather is None:
        return handle_no_weather(
            gettext_("Precipitation type summary"), effective_dark_mode, style
        )

    return observation.place.weather.plot_precipitation_type_summary(
        dark_mode_override=effective_dark_mode, **args
    )


def generate_plot_weather_summary(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    effective_dark_mode, style = get_plot_setup(dark_mode_override)
    eff_conditions = conditions or observation.conditions

    if observation.place.weather is None:
        return handle_no_weather(
            gettext_("Weather summary"), effective_dark_mode, style
        )

    analysis = observation.get_weather_analysis(conditions=eff_conditions)
    if not analysis:
        return handle_no_weather(
            gettext_("Weather summary"), effective_dark_mode, style
        )

    df = pd.DataFrame(analysis)
    ax = args.pop("ax", None)

    # Pie chart of good vs bad hours
    good_count = df[df.is_good_hour].shape[0]
    bad_count = df.shape[0] - good_count

    if good_count == 0 and bad_count == 0:
        return handle_no_weather(
            gettext_("Weather summary"), effective_dark_mode, style
        )

    summary_data = pd.Series(
        [good_count, bad_count],
        index=[gettext_("Good hours"), gettext_("Bad hours")],
    )

    # Use the same style as other summary plots
    plot_ax = summary_data.plot(
        kind="pie",
        ax=ax,
        autopct="%1.1f%%",
        colors=["#90EE90", "#FF6B6B"]
        if not effective_dark_mode
        else ["#00FF7F", "#FF5252"],
        **args,
    )

    if not ax:
        ax = plot_ax
        fig = ax.figure
    else:
        fig = ax.figure

    apply_colors(ax, fig, style)

    ax.set_title(gettext_("Weather goodness summary"), color=style["TEXT_COLOR"])
    ax.set_ylabel("")  # Remove default ylabel

    for text_obj in ax.texts:
        text_obj.set_color(style["TEXT_COLOR"])

    return ax
