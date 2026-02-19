import io
from typing import overload, Literal, Tuple, Union, Any
from enum import Enum

from matplotlib import pyplot

from apts.config import get_plot_format
from apts.constants.graphconstants import get_plot_style
from apts.units import ureg as ureg
from .planetary import MINOR_PLANET_NAMES

__all__ = ["ureg", "MINOR_PLANET_NAMES"]


class ConnectionType(Enum):
    F_1_25 = "1.25"
    F_2 = "2"
    T2 = "T2"

    def __str__(self) -> str:
        return str(self.value)


class Utils:
    @staticmethod
    def find_all_paths(graph, start, end, mode="OUT", maxlen=None):
        import networkx as nx

        start_nodes = start if isinstance(start, list) else [start]
        end_nodes = end if isinstance(end, list) else [end]

        all_paths = []
        for s in start_nodes:
            for e in end_nodes:
                # networkx.all_simple_paths cutoff is in edges,
                # so maxlen-1 if maxlen is the number of nodes.
                cutoff = maxlen - 1 if maxlen is not None else None
                try:
                    paths = list(nx.all_simple_paths(graph, s, e, cutoff=cutoff))
                    all_paths.extend(paths)
                except nx.NodeNotFound:
                    continue
        return all_paths

    @staticmethod
    @overload
    def decdeg2dms(dd: Any, pretty: Literal[True]) -> str: ...
    @staticmethod
    @overload
    def decdeg2dms(dd: Any, pretty: Literal[False] = False) -> Tuple[float, float, float]: ...
    @staticmethod
    def decdeg2dms(dd: Any, pretty: bool = False) -> Union[str, Tuple[float, float, float]]:
        is_pandas_series = hasattr(dd, "iloc")
        dd_val = dd.iloc[0] if is_pandas_series else dd
        mnt, sec = divmod(dd_val * 3600, 60)
        deg, mnt = divmod(mnt, 60)

        if pretty:
            return f"{int(deg)}°{int(mnt)}'{int(sec)}\""
        else:
            return deg, mnt, sec

    @staticmethod
    def dms2decdeg(dms):
        deg, mnt, sec = dms
        return deg + mnt / 60 + sec / 3600

    @staticmethod
    def format_date(date):
        return date.strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def plot_to_bytes(plot):
        plot_bytes = io.BytesIO()
        plot.savefig(plot_bytes, format=get_plot_format())
        # Prevent showing plot in ipython
        pyplot.close(plot)
        plot_bytes.seek(0)
        return plot_bytes

    @staticmethod
    def date_format(date_time):
        return date_time.isoformat(timespec="seconds")

    @staticmethod
    def mask_secret(secret: Any) -> str:
        from ..secrets import mask_secret

        return mask_secret(secret)

    @staticmethod
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
