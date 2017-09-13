import igraph
from . import utils
from .models.optical import *
from enum import Enum


class Type(Enum):
  OPTICAL = 1
  INPUT = 2
  OUTPUT = 3
  IMAGE = 4
  

class Equipment(object):
  """This class represents all possesed astronomical equpiment. Allows to computer
  all possiable hardware configuration. It uses directed graph for internal processing. 
  """
  
  SPACE_ID = "space"
  IMAGE_ID = "image"
  
  OUT = "_out"
  IN = "_in"
  
  COLORS = {
      Type.OPTICAL : "blue",
      Type.INPUT : "red",
      Type.OUTPUT : "green",
      Type.IMAGE : "yellow"
  } 
  
  TYPE = "node_type"
  LABEL = "label"
  COLOR = "color"
  EQUIPMENT = "equipment" 
  
  def __init__(self):
    self.connection_garph = igraph.Graph(directed=True) 
    self.add_vertex(Equipment.SPACE_ID, Equipment.SPACE_ID, Type.IMAGE)
    self.add_vertex(Equipment.IMAGE_ID, Equipment.IMAGE_ID, Type.IMAGE)
  
  def get_possiable_views(self):
    # connect all outputs with inputs
    self.connect()
    space_node = self.connection_garph.vs.find(name=Equipment.SPACE_ID)
    image_node = self.connection_garph.vs.find(name=Equipment.IMAGE_ID)
    for optical_path in utils.find_all_paths(self.connection_garph, space_node.index, image_node.index):
      result = [self.connection_garph.vs.find(name=id)[Equipment.EQUIPMENT] for id in optical_path]
      print([str(item) for item in result if item is not None])
      
  def plot_connection_garph(self):
    return igraph.plot(self.connection_garph)
  
  def get_all(self):
    return self.optical_items
     
  def connect(self):
    for out_node in self.connection_garph.vs.select(node_type = Type.OUTPUT):
      for in_node in self.connection_garph.vs.select(node_type = Type.INPUT):
        #connect all outputs with all inputs
        self.add_edge(out_node, in_node)

     
  def add_vertex(self, node_name, node_label, node_type, equipment = None):
    """ 
    Add single node to graph. Return vertex
    """
    self.connection_garph.add_vertex(node_name) 
    node = self.connection_garph.vs.find(name = node_name)
    node[Equipment.LABEL] = node_label
    node[Equipment.TYPE] = node_type
    node[Equipment.COLOR] = Equipment.COLORS[node_type]
    node[Equipment.EQUIPMENT] = equipment
    return node  
  
  def add_edge(self, node_from, node_to):
    self.connection_garph.add_edge(node_from, node_to)

  def register_telescope(self, new_telescope):
    """ 
    Telescope node is build out of multipe verteces - telescope and its outputs.  
    """    
    #add telescope vertex
    self.add_vertex(new_telescope.id, new_telescope.label(), Type.OPTICAL, new_telescope) 
    #add telescope output vertex
    self.add_vertex(new_telescope.id + Equipment.OUT, new_telescope.label() + Equipment.OUT, Type.OUTPUT) 
    #connect telescope vertex to space
    self.add_edge(Equipment.SPACE_ID, new_telescope.id)
    #connect telescope vertex to its outpus
    self.add_edge(new_telescope.id, new_telescope.id + Equipment.OUT)
    
  def register_ocular(self, new_okular):    
    #add ocular vertex
    self.add_vertex(new_okular.id, new_okular.label(), Type.OPTICAL, new_okular)
    #add ocular input vertex
    self.add_vertex(new_okular.id + Equipment.IN, new_okular.label() + Equipment.IN, Type.INPUT) 
    #connect ocular with output image vertex 
    self.add_edge(new_okular.id, Equipment.IMAGE_ID)
    #connect input to ocular vertex 
    self.add_edge(new_okular.id + Equipment.IN, new_okular.id)
  
  def register_barlow(self, new_barlow):   
    #add barlow vertex
    self.add_vertex(new_barlow.id, new_barlow.label(), Type.OPTICAL, new_barlow)
    #add barlow input vertex
    self.add_vertex(new_barlow.id + Equipment.IN, new_barlow.label() + Equipment.IN, Type.INPUT) 
    #add barlow output vertex
    self.add_vertex(new_barlow.id + Equipment.OUT, new_barlow.label() + Equipment.OUT, Type.OUTPUT) 
    #connect barlow with output vertex 
    self.add_edge(new_barlow.id, new_barlow.id + Equipment.OUT)
    #connect input with barlow vertex
    self.add_edge(new_barlow.id + Equipment.IN, new_barlow.id)
    
