import logging

import cairo as ca
import igraph as ig
import matplotlib.pyplot as plt
import pandas as pd

from .constants import NodeLabels
from .opticalequipment import *
from .optics import *

logger = logging.getLogger(__name__)


class Equipment:
  """
  This class represents all possessed astronomical equipment. Allows to compute all possible 
  hardware configuration. It uses directed graph for internal processing.
  """

  def __init__(self):
    self.connection_garph = ig.Graph(directed=True)
    # Register standard input and outputs
    self.add_vertex(Constants.SPACE_ID)
    self.add_vertex(Constants.EYE_ID)
    self.add_vertex(Constants.IMAGE_ID)

  def _get_paths(self, output_id):
    # Connect all outputs with inputs
    self._connect()
    # Find input and output nodes
    space_node = self.connection_garph.vs.find(name=Constants.SPACE_ID)
    output_node = self.connection_garph.vs.find(name=output_id)
    results = []
    results_set = set()
    for optical_path in Utils.find_all_paths(self.connection_garph, space_node.index, output_node.index):
      result = [self.connection_garph.vs.find(
        name=id)[NodeLabels.EQUIPMENT] for id in optical_path]
      op = OpticalPath.from_path(
        [item for item in result if item is not None])
      if op.elements() not in results_set:
        results_set.add(op.elements())
        results.append(op)
    return results

  def get_zooms(self, node_id):
    """
    Compute all possible zooms
    :param node_id:
    :return: sorted list of zooms
    """
    result = [OpticsUtils.compute_zoom(path)
              for path in self._get_paths(node_id)]
    result.sort()
    return result

  def data(self):
    columns = [Labels.LABEL, Labels.TYPE, Labels.ZOOM, Labels.USEFUL_ZOOM,
               Labels.FOV, Labels.EXIT_PUPIL, Labels.DAWES_LIMIT, Labels.RANGE, Labels.BRIGHTNESS, Labels.ELEMENTS]

    def append(result_data, paths):
      for path in paths:
        data = [[path.label(),
                 path.output.output_type(),
                 path.zoom().magnitude,
                 path.zoom() < path.telescope.max_useful_zoom(),
                 path.fov().magnitude,
                 path.output.focal_length / (path.telescope.focal_ratio() * path.effective_barlow()),
                 path.telescope.dawes_limit(),
                 path.telescope.limiting_magnitude(),
                 path.brightness().magnitude,
                 path.length()]]
        result_data = result_data.append(pd.DataFrame(
          data, columns=columns), ignore_index=True)
      return result_data

    result = pd.DataFrame(columns=columns)
    result = append(result, self._get_paths(Constants.EYE_ID))
    result = append(result, self._get_paths(Constants.IMAGE_ID))
    # Add ID column as first
    result['ID'] = result.index
    return result[['ID'] + columns]

  def plot_zoom(self, **args):
    """
    Plot available magnification
    """
    plot = self._plot(Labels.ZOOM, 'Available zoom', 'Used equipment', 'Magnification', **args)
    # Add marker for maximal useful zoom
    max_zoom = self.max_zoom()
    plot.axhline(max_zoom, color='orange', linestyle='--', alpha=0.7)
    plot.annotate("Max useful zoom due to atmosphere", (-0.4, max_zoom + 2), alpha=0.7)

  def max_zoom(self):
    """
    Max useful zoom due to atmosphere
    """
    return 350

  def plot_fov(self, **args):
    """
    Plot available fields of view
    """

    def formatter(tick, pos):
      return Utils.decdeg2dms(tick, pretty=True)

    def add_line(description, position):
      position = Utils.dms2decdeg(position)
      plot.axhline(position, color='orange', linestyle='--', alpha=0.7)
      plot.annotate(description, (-0.4, position + 0.03), alpha=0.7)

    plot = self._plot(Labels.FOV, 'Available fields of view', 'Used equipment', 'Field if view [°]', **args)
    plot.yaxis.set_major_formatter(plt.FuncFormatter(formatter))
    # Pleiades width is 1°50'
    add_line("Pleiades size", (1, 50, 0))
    # Average moon size is 0°31'42"
    add_line("Moon size", (0, 31, 42))
    # M51 width is 0°11'
    add_line("M51 size", (0, 11, 0))

  def _plot(self, to_plot, title, x_label, y_label, autolayout=False, multiline_labels=True, **args):
    data = self._filter_and_merge(to_plot, multiline_labels)
    if autolayout:
      plt.rcParams.update({'figure.autolayout': True})
    ax = data.plot(kind='bar', title=title, stacked=True, **args)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend(loc='upper right')
    return ax

  def _filter_and_merge(self, to_plot, multiline_labels):
    """
    This methods filter data to plot and merge Eye and Image series together
    """
    # Filter only relevant data - by to_plot key
    data = self.data()[[to_plot, Labels.TYPE, Labels.LABEL]].sort_values(by=to_plot)
    if (len(data) <= 8):
      # Split label by ',' if multiline_labels is set to true
      labels = [label.replace(',', '\n') if multiline_labels else label for label in data[Labels.LABEL].values]
    else:
      # For more than 8 option display only ids
      labels = data.index
    # Merge Image and Eye series together
    return pd.DataFrame([{row[1]: row[0]} for row in data.values], index=labels)

  def plot_connection_graph(self, **args):
    # Connect all outputs with inputs
    self._connect()
    return ig.plot(self.connection_garph, margin=80, **args)

  def plot_connection_graph_svg(self, **args):
    surface = ca.ImageSurface(ca.FORMAT_ARGB32, 800, 600)
    plot = self.plot_connection_graph(target=surface, **args)
    return plot._repr_svg_()

  def _connect(self):
    logger.debug("Connecting nodes")
    for out_node in self.connection_garph.vs.select(node_type=OpticalType.OUTPUT):
      # Get output type
      connection_type = out_node[NodeLabels.CONNECTION_TYPE]
      for in_node in self.connection_garph.vs.select(node_type=OpticalType.INPUT, connection_type=connection_type):
        # Connect all outputs with all inputs, excluding connecting part to itself
        out_id = OpticalEqipment.get_parent_id(
          out_node[NodeLabels.NAME])
        in_id = OpticalEqipment.get_parent_id(in_node[NodeLabels.NAME])
        if out_id != in_id:
          self.add_edge(out_node, in_node)

  def add_vertex(self, node_name, equipment=None, node_type=OpticalType.GENERIC, connection_type=None):
    """ 
    Add single node to graph. Return new vertex.
    """
    self.connection_garph.add_vertex(node_name, label_dist=1.5)
    node = self.connection_garph.vs.find(name=node_name)

    if equipment is not None:
      node_type = equipment.type()
      node_label = "\n".join([equipment.get_name(), equipment.label()])
    elif node_type == OpticalType.GENERIC:
      node_label = node_name
    elif node_type == OpticalType.INPUT:
      node_label = str(connection_type) + " " + OpticalEqipment.IN
    elif node_type == OpticalType.OUTPUT:
      node_label = str(connection_type) + " " + OpticalEqipment.OUT
    else:
      node_label = ""

    node[NodeLabels.TYPE] = node_type
    node[NodeLabels.LABEL] = node_label
    node[NodeLabels.COLOR] = Constants.COLORS[node_type]
    node[NodeLabels.EQUIPMENT] = equipment
    node[NodeLabels.CONNECTION_TYPE] = connection_type

    return node

  def add_edge(self, node_from, node_to):
    # Add edge if only it doesn't exist
    if not self.connection_garph.are_connected(node_from, node_to):
      self.connection_garph.add_edge(node_from, node_to)

  def register(self, optical_eqipment):
    """ 
    Register any optical equipment in a optical graph.
    """
    optical_eqipment.register(self)
