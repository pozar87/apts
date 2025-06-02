import logging

import cairo as ca
import igraph as ig
import matplotlib.pyplot as plt
import pandas as pd

from .constants import EquipmentTableLabels, OpticalType, GraphConstants, NodeLabels
from .opticalequipment import OpticalEquipment, Telescope, Camera, Eyepiece, Barlow
from .optics import OpticalPath, OpticsUtils
from .utils import Utils

logger = logging.getLogger(__name__)


class Equipment:
  """
  This class represents all possessed astronomical equipment. Allows to compute all possible
  hardware configuration. It uses directed graph for internal processing.
  """

  def __init__(self):
    self.connection_garph = ig.Graph(directed=True)
    # Register standard input and outputs
    self.add_vertex(GraphConstants.SPACE_ID)
    self.add_vertex(GraphConstants.EYE_ID)
    self.add_vertex(GraphConstants.IMAGE_ID)

  def _get_paths(self, output_id):
    # Connect all outputs with inputs
    self._connect()
    # Find input and output nodes
    space_node = self.connection_garph.vs.find(name=GraphConstants.SPACE_ID)
    output_node = self.connection_garph.vs.find(name=output_id)
    results = []
    results_set = set()
    logger.debug(f"Space {space_node}, Output {output_node}")
    for optical_path in Utils.find_all_paths(self.connection_garph, space_node.index, output_node.index):
      logger.debug(f"Optical Path: {optical_path}")
      result = [self.connection_garph.vs[id][NodeLabels.EQUIPMENT] for id in optical_path]
      op = OpticalPath.from_path(
        [item for item in result if item is not None])
      if op.elements() not in results_set:
        results_set.add(op.elements())
        results.append(op)
    return results

  def get_zooms(self, node_id) -> list[float]:
    """
    Compute all possible zooms
    :param node_id:
    :return: sorted list of zooms
    """
    result = [OpticsUtils.compute_zoom(path)
              for path in self._get_paths(node_id)]
    result.sort()
    return result

  def data(self) -> pd.DataFrame:
    columns = [
        EquipmentTableLabels.LABEL,
        EquipmentTableLabels.TYPE,
        EquipmentTableLabels.ZOOM,
        EquipmentTableLabels.USEFUL_ZOOM,
        EquipmentTableLabels.FOV,
        EquipmentTableLabels.EXIT_PUPIL,
        EquipmentTableLabels.DAWES_LIMIT,
        EquipmentTableLabels.RANGE,
        EquipmentTableLabels.BRIGHTNESS,
        EquipmentTableLabels.ELEMENTS
    ]

    # Import Binoculars here to keep it local to where it's used for isinstance
    # and avoid potential circular imports if Binoculars ever needed Equipment.
    from .opticalequipment.binoculars import Binoculars

    def append(result_data, paths):
        rows = []
        logging.debug(f"Appending paths {paths}")
        for path in paths:
            # path.telescope is the main optic (telescope or binoculars)
            # path.output is the final element (eyepiece, camera, or binoculars itself)

            # Determine if the main optic is Binoculars
            is_binoculars = isinstance(path.telescope, Binoculars)

            # Calculate useful_zoom
            useful_zoom_value = True # Default for binoculars
            if not is_binoculars:
                if hasattr(path.telescope, 'max_useful_zoom'):
                    # max_useful_zoom() on Telescope returns a float, zoom() is a Quantity
                    useful_zoom_value = path.zoom().magnitude < path.telescope.max_useful_zoom()
                else:
                    useful_zoom_value = False # Should not happen for Telescope objects

            # Get output type. For Binoculars, path.output is the Binocular instance.
            output_type_value = path.output.output_type()

            # Calculate Exit Pupil
            # path.exit_pupil() now returns a Quantity (e.g., mm)
            exit_pupil_value = path.exit_pupil().to('mm').magnitude
            if exit_pupil_value < 0: # Guard against potential negative values
                exit_pupil_value = 0

            rows.append([
                path.label(),
                output_type_value,
                path.zoom().magnitude,
                useful_zoom_value,
                path.fov().magnitude,
                exit_pupil_value,
                path.telescope.dawes_limit().magnitude, # dawes_limit() in Binoculars/Telescope returns Quantity
                path.telescope.limiting_magnitude(),    # limiting_magnitude() in Binoculars/Telescope returns float/int
                path.brightness().magnitude, # brightness() in OpticalPath returns Quantity
                path.length() # length() in OpticalPath returns int
            ])

        if rows:
            new_data = pd.DataFrame(rows, columns=columns)
            if result_data.empty:
                result_data = new_data
            else:
                for col in result_data.columns:
                    if result_data[col].dtype != new_data[col].dtype:
                        # Try to convert new_data's column to result_data's dtype if they are compatible
                        try:
                            new_data[col] = new_data[col].astype(result_data[col].dtype)
                        except Exception as e:
                            logging.warning(f"Could not align dtype for column {col}: {e}. This might lead to concat issues.")
                result_data = pd.concat([result_data, new_data], ignore_index=True)
        return result_data

    result = pd.DataFrame(columns=columns)
    result = append(result, self._get_paths(GraphConstants.EYE_ID))
    result = append(result, self._get_paths(GraphConstants.IMAGE_ID))

    # Add ID column as first
    if not result.empty: # Only add ID if DataFrame is not empty
        result['ID'] = result.index
        result = result[['ID'] + columns]
    else: # If empty, ensure ID column exists for consistency if expected by other code
        result['ID'] = [] # Initialize with empty list or appropriate empty type for ID
        result = result[['ID'] + columns]

    return result

  def plot_zoom(self, **args):
    """
    Plot available magnification
    """
    plot = self._plot(EquipmentTableLabels.ZOOM, 'Available zoom', 'Used equipment', 'Magnification', **args)
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

    plot = self._plot(EquipmentTableLabels.FOV, 'Available fields of view', 'Used equipment', 'Field if view [°]',
                      **args)
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
    data = self.data()[[to_plot, EquipmentTableLabels.TYPE, EquipmentTableLabels.LABEL]].sort_values(by=to_plot)
    if (len(data) <= 8):
      # Split label by ',' if multiline_labels is set to true
      labels = [label.replace(',', '\n') if multiline_labels else label for label in
                data[EquipmentTableLabels.LABEL].values]
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
    return plot._repr_svg_()[0] # SVG string is first in tuple

  def _connect(self):
    logger.debug("Connecting nodes")
    for out_node in self.connection_garph.vs.select(node_type=OpticalType.OUTPUT):
      # Get output type
      connection_type = out_node[NodeLabels.CONNECTION_TYPE]
      for in_node in self.connection_garph.vs.select(node_type=OpticalType.INPUT, connection_type=connection_type):
        # Connect all outputs with all inputs, excluding connecting part to itself
        out_id = OpticalEquipment.get_parent_id(
          out_node[NodeLabels.NAME])
        in_id = OpticalEquipment.get_parent_id(in_node[NodeLabels.NAME])
        if out_id != in_id:
          self.add_edge(out_node, in_node)
    logger.debug(self.connection_garph)

  def add_vertex(self, node_name, equipment=None, node_type=OpticalType.GENERIC, connection_type=None):
    """
    Add single node to graph. Return new vertex.
    """
    logger.debug(f"Adding vertex {node_name}")
    self.connection_garph.add_vertex(node_name, label_dist=1.5)
    node = self.connection_garph.vs.find(name=node_name)

    if equipment is not None:
      node_type = equipment.type()
      node_label = "\n".join([equipment.get_name(), equipment.label()])
    elif node_type == OpticalType.GENERIC:
      node_label = node_name
    elif node_type == OpticalType.INPUT:
      node_label = str(connection_type) + " " + OpticalEquipment.IN
    elif node_type == OpticalType.OUTPUT:
      node_label = str(connection_type) + " " + OpticalEquipment.OUT
    else:
      node_label = ""

    node[NodeLabels.TYPE] = node_type
    node[NodeLabels.LABEL] = node_label
    node[NodeLabels.COLOR] = GraphConstants.COLORS[node_type]
    node[NodeLabels.EQUIPMENT] = equipment
    node[NodeLabels.CONNECTION_TYPE] = connection_type

    return node

  def add_edge(self, node_from, node_to):
    logger.debug(f"Adding edge {node_from} -> {node_to}")
    # Add edge if only it doesn't exist
    if not self.connection_garph.are_adjacent(node_from, node_to):
      self.connection_garph.add_edge(node_from, node_to)

  def register(self, optical_eqipment):
    """
    Register any optical equipment in a optical graph.
    """
    optical_eqipment.register(self)
