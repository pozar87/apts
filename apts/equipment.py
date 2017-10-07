import igraph as ig
import pandas as pd
import seaborn as sns
sns.set_style('whitegrid') #TODO: make this global and configurable in all apts



from .constants import NodeLabels
from .utils import Utils
from .models.optical import *
from .optics import *

class Equipment(object):
  """
  This class represents all possessed astronomical equipment. Allows to compute all possible 
  hardware configuration. It uses directed graph for internal processing.
  """
  
  SPACE_ID = "Space"
  EYE_ID   = "Eye"
  IMAGE_ID = "Image"
 
  COLORS = {
      Type.OPTICAL : "blue",
      Type.INPUT : "red",
      Type.OUTPUT : "green",
      Type.GENERIC : "yellow"
  } 
  
  def __init__(self):
    self.connection_garph = ig.Graph(directed=True)
    # Register standard input and outputs
    self.add_vertex(Equipment.SPACE_ID)
    self.add_vertex(Equipment.EYE_ID)
    self.add_vertex(Equipment.IMAGE_ID)
  
  def _get_paths(self, output_id):
    # Connect all outputs with inputs
    self._connect()
    # Find input and output nodes 
    space_node = self.connection_garph.vs.find(name=Equipment.SPACE_ID)
    output_node = self.connection_garph.vs.find(name=output_id)
    results = []
    results_set = set()
    for optical_path in Utils.find_all_paths(self.connection_garph, space_node.index, output_node.index):
      result = [self.connection_garph.vs.find(name=id)[NodeLabels.EQUIPMENT] for id in optical_path]
      telescope, barlows, output = OpticsUtils.expand([item for item in result if item is not None])
      op = OpticalPath(telescope, barlows, output)
      if op.elements() not in results_set:
        results_set.add(op.elements())
        results.append(op)
    return results
  
  def get_zooms(self, node_id):
    result = [OpticsUtils.compute_zoom(path) for path in self._get_paths(node_id)]
    result.sort()
    return result
    
  def data(self): #TODO: Refactor needed
    columns=['label','type','zoom','useful_zoom','fov','elements']
    def append(result_data, columns, type_name, paths):
      for path in paths:
        data = [[path.label(), type_name, path.zoom().magnitude, path.zoom() < path.telescope.max_useful_zoom(), path.fov().magnitude, path.length()]]
        result_data = result_data.append(pd.DataFrame(data, columns=columns), ignore_index=True)
      return result_data 
    result_data = pd.DataFrame(columns=columns)
    result_data = append(result_data, columns, 'eye', self._get_paths(Equipment.EYE_ID))
    result_data = append(result_data, columns, 'image', self._get_paths(Equipment.IMAGE_ID))
    return result_data    
  
  def plot(self, to_plot):
    x = self.data()[[to_plot,'type','label']].sort_values(by=to_plot)
    df = pd.DataFrame([{row[1]:row[0]} for row in x.values], index=x['label'].values)
    df.plot(kind="bar", stacked = True) 
    
  def plot_connection_garph(self):
    return ig.plot(self.connection_garph)
     
  def _connect(self):
    for out_node in self.connection_garph.vs.select(node_type = Type.OUTPUT):
      # Get output type
      connection_type = out_node[NodeLabels.CONNECTION_TYPE]
      for in_node in self.connection_garph.vs.select(node_type = Type.INPUT, connection_type=connection_type):
        # Connect all outputs with all inputs, excluding connecting part to itself
        out_id = OpticalEqipment.get_parent_id(out_node[NodeLabels.NAME])
        in_id = OpticalEqipment.get_parent_id(in_node[NodeLabels.NAME])
        if out_id != in_id:
          self.add_edge(out_node, in_node)
     
  def add_vertex(self, node_name, equipment = None, node_type = Type.GENERIC, connection_type = None):
    """ 
    Add single node to graph. Return new vertex.
    """
    self.connection_garph.add_vertex(node_name) 
    node = self.connection_garph.vs.find(name = node_name)

    if equipment is not None:
      node_type = equipment.type()
      node_label = "\n".join([equipment.get_name(),equipment.label()])
    elif node_type == Type.GENERIC:
      node_label = node_name 
    else:
      node_label = ""  
    
    node[NodeLabels.TYPE] = node_type
    node[NodeLabels.LABEL] = node_label
    node[NodeLabels.COLOR] = Equipment.COLORS[node_type]
    node[NodeLabels.EQUIPMENT] = equipment
    node[NodeLabels.CONNECTION_TYPE] = connection_type

    return node  
  
  def add_edge(self, node_from, node_to):
    # Add edge if only it doesn't exist
    if not self.connection_garph.are_connected(node_from, node_to): #TODO: are_connected is the right method?
      self.connection_garph.add_edge(node_from, node_to)

  def register(self, optical_eqipment): 
    """ 
    Register any optical equipment in a optical graph.
    """
    optical_eqipment.register(self)
 
