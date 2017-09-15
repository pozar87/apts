import uuid
from enum import Enum

class Type(Enum):
  OPTICAL = 1
  INPUT = 2
  OUTPUT = 3
  GENERIC = 4  

class OpticalEqipment:
  """
  Basic class for optical equipment
  """
  
  OUT = "_out"
  IN = "_in"
  
  def __init__(self, focal_length, vendor):
    self._id = str(uuid.uuid4())
    self._type = Type.OPTICAL 
    
    self.focal_length = focal_length
    self.vendor = vendor 

  def register(self, equipment):
    #register equipment vertex
    equipment.add_vertex(self.id(), self) 
    
  def __str__(self):
    return "{}, f={}".format(self.vendor,self.focal_length)

  def type(self):
    return self._type

  def label(self):
    return str(self)
    
  def id(self):
    return self._id  
    
  def in_id(self):
    return self._id + self.IN
    
  def out_id(self):
    return self._id + self.OUT
  

class Telescope(OpticalEqipment):
  """
  Class representing telescope
  """

  def __init__(self, focal_length, vendor = "unknown telescope", output_size = "1.25"):
    self.output_size = output_size
    super(Telescope, self).__init__(focal_length, vendor)

  def register(self, equipment):
    """ 
    Register itself in optical equipment graph. Telescope node is build out of two vertices - telescope node and its outputs.  
    """ 
    #add telescope vertex   
    super(Telescope, self).register(equipment)
    #add telescope output vertex
    equipment.add_vertex(self.out_id(), node_type = Type.OUTPUT) 
    #connect telescope vertex to space
    equipment.add_edge(equipment.SPACE_ID, self.id())
    #connect telescope vertex to its outpus
    equipment.add_edge(self.id(), self.out_id())
       
class Ocular(OpticalEqipment):   
  """
  Class representing ocular
  """
  
  def __init__(self, focal_length,vendor = "unknown ocular", input_size = "1.25"):
    self.input_size = input_size
    super(Ocular, self).__init__(focal_length, vendor)
    
  def register(self, equipment):
    #add ocular vertex
    super(Ocular, self).register(equipment)
    #add ocular input vertex
    equipment.add_vertex(self.in_id(), node_type = Type.INPUT) 
    #connect ocular with output image vertex 
    equipment.add_edge(self.id(), equipment.IMAGE_ID)
    #connect input to ocular vertex 
    equipment.add_edge(self.in_id(), self.id())
    
class Barlow(OpticalEqipment):   
  """
  Class representing barlow lense
  """
  
  def __init__(self, magnification, vendor = "unknown barlow", input_size = "1.25", output_size = "1.25"):
    self.input_size = input_size
    self.output_size = output_size
    self.magnification = magnification
    super(Barlow, self).__init__(0, vendor)
    
  def register(self, equipment):
    #add barlow vertex
    super(Barlow, self).register(equipment)
    #add barlow input vertex
    equipment.add_vertex(self.in_id(), node_type = Type.INPUT) 
    #add barlow output vertex
    equipment.add_vertex(self.out_id(), node_type = Type.OUTPUT) 
    #connect barlow with output vertex 
    equipment.add_edge(self.id(), self.out_id())
    #connect input with barlow vertex
    equipment.add_edge(self.in_id(), self.id())
    
  def __str__(self):
    return "{}, x{}".format(self.vendor,self.magnification)

