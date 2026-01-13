import matplotlib.axes
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from apts.constants.graphconstants import get_plot_style
from apts.i18n import gettext_

__all__ = ["Utils"]


class Utils:
    @staticmethod
    def plot_no_data(ax, title, dark_mode_enabled):
        style = get_plot_style(dark_mode_enabled)
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])
        ax.text(
            0.5,
            0.5,
            gettext_("No data to plot"),
            horizontalalignment="center",
            verticalalignment="center",
            transform=ax.transAxes,
            color=style["TEXT_COLOR"],
            fontsize=16,
        )
        ax.set_xticks([])
        ax.set_yticks([])

        # Apply styling to be consistent with other plots
        ax.set_title(title, color=style["TEXT_COLOR"])
        ax.spines["bottom"].set_color(style["AXIS_COLOR"])
        ax.spines["top"].set_color(style["AXIS_COLOR"])
        ax.spines["left"].set_color(style["AXIS_COLOR"])
        ax.spines["right"].set_color(style["AXIS_COLOR"])
        return ax

    @staticmethod
    def annotate_plot(
        ax: matplotlib.axes.Axes,
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
