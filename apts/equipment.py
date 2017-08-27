import igraph
from . import utils
from .models.optical import *


class Equipment(object):
  """This class represents all possesed astronomical equpiment. Allows to computer
  all possiable hardware configuration. It uses directed graph for internal processing. 
  """
  
  SPACE_ID = "space"
  IMAGE_ID = "image"
  
  def __init__(self):
    self.optical_items = {}
    self.connection_garph = igraph.Graph(directed=True) 
    self.connection_garph.add_vertex(Equipment.SPACE_ID)
    self.connection_garph.add_vertex(Equipment.IMAGE_ID)  
  
  def get_possiable_views(self):
    for optical_path in utils.find_all_paths(self.connection_garph,
        self.connection_garph.vs.find(name=Equipment.SPACE_ID).index,
        self.connection_garph.vs.find(name=Equipment.IMAGE_ID).index):
  
      print([str(self.optical_items[id]) for id in optical_path if id in self.optical_items.keys()])
  def plot_connection_garph(self):
    return igraph.plot(self.connection_garph)
  
  def get_all(self):
    return self.optical_items
     
  def register(self, item, optical):
    try: #TODO: this is realy ugly ... :(
      self.connection_garph.vs.find(name=str(item))
    except ValueError:  
      self.connection_garph.add_vertex(str(item)) 
      id = self.connection_garph.vs.find(name=str(item)).index #TODO: fix unique names
    if optical:
      self.optical_items[id] = item   

  def register_telescope(self, new_telescope):    
    self.register(new_telescope, True) 
    self.register(new_telescope.output_size, False)  
        
    self.connection_garph.add_edge(Equipment.SPACE_ID,str(new_telescope))
    self.connection_garph.add_edge(str(new_telescope),new_telescope.output_size)
    
  def register_ocular(self, new_okular):    
    self.register(new_okular, True)
    self.register(new_okular.size, False)  
 
    self.connection_garph.add_edge(str(new_okular),Equipment.IMAGE_ID)
    self.connection_garph.add_edge(new_okular.size,str(new_okular))
    
  def register_barlow(self, new_barlow, for_telescope):    
    self.register(new_barlow, True)
    self.register(new_barlow.size, False)  
 
    self.connection_garph.add_edge(str(for_telescope), str(new_barlow))  
    self.connection_garph.add_edge(str(new_barlow), new_barlow.size)  
    
