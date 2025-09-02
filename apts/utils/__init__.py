import io
from aenum import Enum, auto

from matplotlib import pyplot

from apts.constants.graphconstants import get_plot_style
from apts.units import ureg as ureg

__all__ = ["ureg"]


class ConnectionType(Enum):
    F_1_25 = auto()
    F_2 = auto()
    T2 = auto()

    def __str__(self):
        return self.name.replace("F_", "").replace("_", ".")


class Utils:
    def find_all_paths(graph, start, end, mode="OUT", maxlen=None):
        def find_all_paths_aux(adjlist, start, end, path, maxlen=None):
            path = path + [start]
            if start == end:
                return [path]
            paths = []
            if maxlen is None or len(path) <= maxlen:
                for node in adjlist[start] - set(path):
                    paths.extend(find_all_paths_aux(adjlist, node, end, path, maxlen))
            return paths

        adjlist = [
            set(graph.neighbors(node, mode=mode)) for node in range(graph.vcount())
        ]
        all_paths = []
        start = start if type(start) is list else [start]
        end = end if type(end) is list else [end]
        for s in start:
            for e in end:
                all_paths.extend(find_all_paths_aux(adjlist, s, e, [], maxlen))
        return all_paths

    def decdeg2dms(dd, pretty=False):
        mnt, sec = divmod(dd * 3600, 60)
        deg, mnt = divmod(mnt, 60)
        if pretty:
            return "{}°{}'{}\"".format(int(deg), int(mnt), int(sec))
        else:
            return deg, mnt, sec

    def dms2decdeg(dms):
        deg, mnt, sec = dms
        return deg + mnt / 60 + sec / 3600

    def format_date(date):
        return date.strftime("%Y-%m-%d %H:%M")

    def plot_to_bytes(plot):
        plot_bytes = io.BytesIO()
        plot.savefig(plot_bytes, format="png")
        # Prevent showing plot in ipython
        pyplot.close(plot)
        plot_bytes.seek(0)
        return plot_bytes

    def date_format(date_time):
        return date_time.isoformat(timespec="seconds")

    def annotate_plot(plot, y_label, dark_mode_enabled: bool): # Removed local_tz
        style = get_plot_style(dark_mode_enabled)

        plot.set_xlabel("Time", color=style['TEXT_COLOR'])
        plot.set_ylabel(y_label, color=style['TEXT_COLOR'])
        # The following line was found to cause incorrect date range scaling on the x-axis.
        # Pandas/Matplotlib's default formatter handles timezone-aware dates correctly.
        # plot.xaxis.set_major_formatter(mdates.DateFormatter("%d %b %H:%M", tz=local_tz))
        plot.tick_params(axis='x', which='both', colors=style['TICK_COLOR'], labelcolor=style['TEXT_COLOR'], bottom=True, top=False, labelbottom=True)
        plot.tick_params(axis='y', colors=style['TICK_COLOR'], labelcolor=style['TEXT_COLOR']) # Also making y-axis labelcolor explicit

        plot.spines['bottom'].set_color(style['AXIS_COLOR'])
        plot.spines['top'].set_color(style['AXIS_COLOR'])
        plot.spines['left'].set_color(style['AXIS_COLOR'])
        plot.spines['right'].set_color(style['AXIS_COLOR'])
