from apts.i18n import gettext_
from matplotlib import pyplot


def set_time_axis_label(ax: pyplot.Axes):
    """Sets the x-axis label to the translated 'Time' string."""
    ax.set_xlabel(gettext_("Time"))
