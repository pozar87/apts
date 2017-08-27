class OpticalEqipment(object):
  """Basic class for optical equipment"""
  
  def __init__(self, focal_length, vendor):
    self.focal_length = focal_length
    self.vendor = vendor 

  def __str__(self):
    return "{}, f={}".format(self.vendor,self.focal_length)


class Telescope(OpticalEqipment):
  """Class representing telescope"""

  def __init__(self, focal_length, vendor = "unknown telescope", output_size = "1.25"):
    self.output_size = output_size
    super(Telescope, self).__init__(focal_length, vendor)

       
class Ocular(OpticalEqipment):   
  """Class representing ocular"""
  
  def __init__(self, focal_length,vendor = "unknown ocular", size = "1.25"):
    self.size = size
    super(Ocular, self).__init__(focal_length, vendor)
    
class Barlow(OpticalEqipment):   
  """Class representing barlow lense"""
  
  def __init__(self, focal_length,vendor = "unknown barlow", size = "1.25"):
    self.size = size
    super(Barlow, self).__init__(focal_length, vendor)
    
  def __str__(self):
    return "{}, x{}".format(self.vendor,self.focal_length)

