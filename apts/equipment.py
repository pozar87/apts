import igraph

from .constants import NodeLabels
from .utils import Utils
from .models.optical import *
from .optics import Optics

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
    self.connection_garph = igraph.Graph(directed=True)
    # Register standard input and outputs
    self.add_vertex(Equipment.SPACE_ID)
    self.add_vertex(Equipment.EYE_ID)
    self.add_vertex(Equipment.IMAGE_ID)
  
  def _get_possiable_paths(self, output_id):
    # Connect all outputs with inputs
    self.connect()
    space_node = self.connection_garph.vs.find(name=Equipment.SPACE_ID)
    image_node = self.connection_garph.vs.find(name=output_id)
    results = []
    for optical_path in Utils.find_all_paths(self.connection_garph, space_node.index, image_node.index):
      result = [self.connection_garph.vs.find(name=id)[NodeLabels.EQUIPMENT] for id in optical_path]
      results.append([item for item in result if item is not None])
    return results 
  
  def get_possiable_paths_for_eye(self):
    return self._get_possiable_paths(Equipment.EYE_ID)

  def get_possiable_paths_for_image(self):
    return self._get_possiable_paths(Equipment.IMAGE_ID)

  def get_possiable_zooms(self):
    result = [Optics.compute_zoom(path) for path in self.get_possiable_paths_for_eye()]
    result.sort()
    return result

  def get_possiable_camera_zooms(self):
    result = [Optics.compute_camera_zoom(path) for path in self.get_possiable_paths_for_image()]
    result.sort()
    return result
      
  def plot_connection_garph(self):
    return igraph.plot(self.connection_garph)
     
  def connect(self):
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
      node_label = equipment.label()
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
    # Add edge if ony it doesn't exist
    if not self.connection_garph.are_connected(node_from, node_to): #TODO: are_connected is the right method?
      self.connection_garph.add_edge(node_from, node_to)

  def register(self, optical_eqipment): 
    """ 
    Register any optical equipment in a optical graph.
    """
    optical_eqipment.register(self)
 
