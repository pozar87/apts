import io
from aenum import Enum, auto

import matplotlib.dates as mdates
import pint
from matplotlib import pyplot

# Unit registry
ureg = pint.UnitRegistry()


class ConnectionType(Enum):
  F_1_25 = auto()
  F_2 = auto()
  T2 = auto()

  def __str__(self):
    return self.name.replace('F_', '').replace('_', '.')


class Utils:

  def find_all_paths(graph, start, end, mode='OUT', maxlen=None):
    def find_all_paths_aux(adjlist, start, end, path, maxlen=None):
      path = path + [start]
      if start == end:
        return [path]
      paths = []
      if maxlen is None or len(path) <= maxlen:
        for node in adjlist[start] - set(path):
          paths.extend(find_all_paths_aux(
            adjlist, node, end, path, maxlen))
      return paths

    adjlist = [set(graph.neighbors(node, mode=mode))
               for node in range(graph.vcount())]
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
    plot.savefig(plot_bytes, format='png')
    # Prevent showing plot in ipython
    pyplot.close(plot)
    plot_bytes.seek(0)
    return plot_bytes

  def date_format(date_time):
    return date_time.isoformat(timespec='seconds')

  def annotate_plot(plot, y_label):
    plot.set_xlabel('Time')
    plot.set_ylabel(y_label)
    plot.xaxis.set_major_formatter(mdates.DateFormatter('%d %b %H:%M'))
