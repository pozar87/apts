import igraph
import operator
import functools

from . import utils
from . import constants

from .models.optical import *

class Equipment(object):
  """This class represents all possesed astronomical equpiment. Allows to computer
  all possiable hardware configuration. It uses directed graph for internal processing. 
  """
  
  SPACE_ID = "space"
  IMAGE_ID = "image"
 
  COLORS = {
      Type.OPTICAL : "blue",
      Type.INPUT : "red",
      Type.OUTPUT : "green",
      Type.GENERIC : "yellow"
  } 
  
  def __init__(self):
    self.connection_garph = igraph.Graph(directed=True) 
    self.add_vertex(Equipment.SPACE_ID)
    self.add_vertex(Equipment.IMAGE_ID)
  
  def get_possiable_paths(self):
    # connect all outputs with inputs
    self.connect()
    space_node = self.connection_garph.vs.find(name=Equipment.SPACE_ID)
    image_node = self.connection_garph.vs.find(name=Equipment.IMAGE_ID)
    results = []
    for optical_path in utils.find_all_paths(self.connection_garph, space_node.index, image_node.index):
      result = [self.connection_garph.vs.find(name=id)[constants.NodeLabels.EQUIPMENT] for id in optical_path]
      results.append([item for item in result if item is not None])
    return results 
  
  def get_possiable_zooms(self):
    result = [self.compute_zoom(path) for path in self.get_possiable_paths()]
    result.sort()
    return result
  
  def compute_zoom(self, path):
    telescop = path[0]
    okular = path[-1]
    barlow = [item.magnification for item in path[1:-1]]
    magnification = functools.reduce(operator.mul, barlow, 1)
    zoom = telescop.focal_length * magnification / okular.focal_length
    return zoom
      
  def plot_connection_garph(self):
    return igraph.plot(self.connection_garph)
     
  def connect(self):
    for out_node in self.connection_garph.vs.select(node_type = Type.OUTPUT):
      for in_node in self.connection_garph.vs.select(node_type = Type.INPUT):
        #connect all outputs with all inputs, excluding connecting part to itself
        out_id = out_node["name"].split("_")[0]
        in_id = in_node["name"].split("_")[0]
        if out_id != in_id:
          self.add_edge(out_node, in_node)
     
  def add_vertex(self, node_name, equipment = None, node_type = Type.GENERIC):
    """ 
    Add single node to graph. Return new vertex
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
    
    node[constants.NodeLabels.TYPE] = node_type  
    node[constants.NodeLabels.LABEL] = node_label  
    node[constants.NodeLabels.COLOR] = Equipment.COLORS[node_type]
    node[constants.NodeLabels.EQUIPMENT] = equipment
    return node  
  
  def add_edge(self, node_from, node_to):
    self.connection_garph.add_edge(node_from, node_to)

  def register(self, optical_eqipment): 
    optical_eqipment.register(self)
 
