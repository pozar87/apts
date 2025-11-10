import matplotlib.dates as mdates
from matplotlib import pyplot

from apts.constants.graphconstants import get_plot_style
from apts.i18n import gettext_


class Utils:
    @staticmethod
    def annotate_plot(
        ax: pyplot.Axes,
        y_label: str,
        dark_mode: bool,
        local_timezone: object,
        x_label: str = "Time",
    ):
        style = get_plot_style(dark_mode)
        ax.set_ylabel(gettext_(y_label), color=style["TEXT_COLOR"])
        ax.set_xlabel(gettext_(x_label), color=style["TEXT_COLOR"])
        ax.tick_params(axis="x", colors=style["TICK_COLOR"])
        ax.tick_params(axis="y", colors=style["TICK_COLOR"])
        ax.spines["bottom"].set_color(style["AXIS_COLOR"])
        ax.spines["top"].set_color(style["AXIS_COLOR"])
        ax.spines["right"].set_color(style["AXIS_COLOR"])
        ax.spines["left"].set_color(style["AXIS_COLOR"])
        ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)
        if x_label == "Time":
            date_format = mdates.DateFormatter("%H:%M", tz=local_timezone)
            ax.xaxis.set_major_formatter(date_format)
