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
    Add single node to graph. Return vertex
    """
    self.connection_garph.add_vertex(node_name) 
    node = self.connection_garph.vs.find(name = node_name)

    if equipment is not None:
      node_type = equipment.type()
      node_label = equipment.label()
    else:
      node_label = "" 
    
    node[constants.NodeLabels.TYPE] = node_type  
    node[constants.NodeLabels.LABEL] = node_label  
    node[constants.NodeLabels.COLOR] = Equipment.COLORS[node_type]
    node[constants.NodeLabels.EQUIPMENT] = equipment
    return node  
  
  def add_edge(self, node_from, node_to):
    self.connection_garph.add_edge(node_from, node_to)

  def register_telescope(self, new_telescope):
    """ 
    Telescope node is build out of multipe vertices - telescope and its outputs.  
    """    
    #add telescope vertex
    self.add_vertex(new_telescope.id(), new_telescope) 
    #add telescope output vertex
    self.add_vertex(new_telescope.out_id(), node_type = Type.OUTPUT) 
    #connect telescope vertex to space
    self.add_edge(Equipment.SPACE_ID, new_telescope.id())
    #connect telescope vertex to its outpus
    self.add_edge(new_telescope.id(), new_telescope.out_id())
    
  def register_ocular(self, new_okular):    
    #add ocular vertex
    self.add_vertex(new_okular.id(), new_okular)
    #add ocular input vertex
    self.add_vertex(new_okular.in_id(), node_type = Type.INPUT) 
    #connect ocular with output image vertex 
    self.add_edge(new_okular.id(), Equipment.IMAGE_ID)
    #connect input to ocular vertex 
    self.add_edge(new_okular.in_id(), new_okular.id())
  
  def register_barlow(self, new_barlow):   
    #add barlow vertex
    self.add_vertex(new_barlow.id(), new_barlow)
    #add barlow input vertex
    self.add_vertex(new_barlow.in_id(), node_type = Type.INPUT) 
    #add barlow output vertex
    self.add_vertex(new_barlow.out_id(), node_type = Type.OUTPUT) 
    #connect barlow with output vertex 
    self.add_edge(new_barlow.id(), new_barlow.out_id())
    #connect input with barlow vertex
    self.add_edge(new_barlow.in_id(), new_barlow.id())
    
