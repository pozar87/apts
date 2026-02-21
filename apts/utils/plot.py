from datetime import timedelta

import matplotlib.axes
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker
from babel.dates import format_datetime

from apts.constants.graphconstants import get_plot_style
from apts.i18n import get_language, gettext_

__all__ = ["Utils"]


class Utils:
    @staticmethod
    def plot_no_data(ax, title, dark_mode_enabled):
        style = get_plot_style(dark_mode_enabled)
        if ax is None:
            fig, ax = plt.subplots(
                facecolor=style["FIGURE_FACE_COLOR"], edgecolor="none"
            )
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
        ax.tick_params(axis="x", colors=style["TICK_COLOR"], labelrotation=30)
        ax.tick_params(axis="y", colors=style["TICK_COLOR"])
        ax.spines["bottom"].set_color(style["AXIS_COLOR"])
        ax.spines["top"].set_color(style["AXIS_COLOR"])
        ax.spines["right"].set_color(style["AXIS_COLOR"])
        ax.spines["left"].set_color(style["AXIS_COLOR"])
        ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)
        if x_label == "Time":
            # Use AutoDateLocator with hints for tick density.
            # Relaxed tick count requirements (from 8-12 to 5-15) to avoid UserWarning
            # from matplotlib when no nice interval can be found in a narrow range.
            locator = mdates.AutoDateLocator(
                tz=local_timezone, minticks=5, maxticks=15
            )
            ax.xaxis.set_major_locator(locator)
            # Only set formatter if one hasn't been set by the caller
            # (i.e., it's still the default AutoDateFormatter or ScalarFormatter)
            if isinstance(
                ax.xaxis.get_major_formatter(),
                (mdates.AutoDateFormatter, matplotlib.ticker.ScalarFormatter),
            ):
                # Capture the current language to ensure it's used when the plot is rendered,
                # even if the language context has changed or ended.
                current_lang = get_language()

                def babel_formatter(x, pos):
                    dt = mdates.num2date(x, tz=local_timezone)
                    return format_datetime(dt, "d MMM HH:mm", locale=current_lang)

                ax.xaxis.set_major_formatter(
                    matplotlib.ticker.FuncFormatter(babel_formatter)
                )

            # Mark midnights for clearer "next day" visualization
            try:
                limits = ax.get_xlim()
                xmin, xmax = limits
                dmin = mdates.num2date(xmin, tz=local_timezone)
                dmax = mdates.num2date(xmax, tz=local_timezone)

                # Start from the first midnight after dmin
                current_midnight = dmin.replace(hour=0, minute=0, second=0, microsecond=0)
                if current_midnight < dmin:
                    current_midnight += timedelta(days=1)

                while current_midnight <= dmax:
                    ax.axvline(
                        current_midnight,
                        color=style["AXIS_COLOR"],
                        linestyle="-",
                        alpha=0.5,
                        linewidth=1.5,
                        label="_nolegend_",
                    )
                    current_midnight += timedelta(days=1)
            except Exception:
                # Fallback if limits are not set or not unpackable (e.g. in unit tests)
                pass

    @staticmethod
    def style_legend(ax, style):
        """
        Applies a unified style to the legend of the provided axes.
        """
        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text in legend.get_texts():
                text.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])
