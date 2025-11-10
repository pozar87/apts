
from matplotlib import pyplot
import matplotlib.dates as mdates

from apts.i18n import gettext_
from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style

def set_time_axis_label(ax: pyplot.Axes, local_timezone):
    """
    Sets the label for the time axis and formats the ticks.
    """
    style = get_plot_style(get_dark_mode())
    ax.set_xlabel(gettext_("Time"), color=style["TEXT_COLOR"])
    date_format = mdates.DateFormatter("%H:%M", tz=local_timezone)
    ax.xaxis.set_major_formatter(date_format)
