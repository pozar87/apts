import uuid
from enum import Enum

class Type(Enum):
  OPTICAL = 1
  INPUT = 2
  OUTPUT = 3
  GENERIC = 4  

class OpticalEqipment(object):
  """Basic class for optical equipment"""
  
  OUT = "_out"
  IN = "_in"
  
  def __init__(self, focal_length, vendor):
    self._id = str(uuid.uuid4())
    self._type = Type.OPTICAL 
    
    self.focal_length = focal_length
    self.vendor = vendor 


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
  """Class representing telescope"""

  def __init__(self, focal_length, vendor = "unknown telescope", output_size = "1.25"):
    self.output_size = output_size
    super(Telescope, self).__init__(focal_length, vendor)

       
class Ocular(OpticalEqipment):   
  """Class representing ocular"""
  
  def __init__(self, focal_length,vendor = "unknown ocular", input_size = "1.25"):
    self.input_size = input_size
    super(Ocular, self).__init__(focal_length, vendor)
    
class Barlow(OpticalEqipment):   
  """Class representing barlow lense"""
  
  def __init__(self, magnification, vendor = "unknown barlow", input_size = "1.25", output_size = "1.25"):
    self.input_size = input_size
    self.output_size = output_size
    self.magnification = magnification
    super(Barlow, self).__init__(0, vendor)
    
  def __str__(self):
    return "{}, x{}".format(self.vendor,self.magnification)

