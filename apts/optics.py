import operator
import functools
import math

from .utils import Utils

class OpticsUtils:
  def expand(path):
    # First item in the path should be the telescope
    telescope = path[0]
    # Last item in the path is output
    output = path[-1]
    # Barlow lenses are in the middle
    barlows = path[1:-1]
    return (telescope, barlows, output)

  def barlows_multiplications(barlows):
    return [barlow.magnification for barlow in barlows]

  def compute_zoom(telescope, barlows, output):
    # Multiply all barlows
    magnification = functools.reduce(operator.mul, OpticsUtils.barlows_multiplications(barlows), 1)
    zoom = telescope.focal_length * magnification / output.zoom_divider()
    return zoom

  def compute_field_of_view(telescop, barlows, output):
    magnification = functools.reduce(operator.mul, OpticsUtils.barlows_multiplications(barlows), 1)
    zoom = OpticsUtils.compute_zoom(telescop, barlows, output)
    return output.field_of_view(telescop, zoom, magnification) #TODO: this is not best way to do it
    
class OpticalPath:
  def __init__(self, telescope, barlows, output):
    self.telescope = telescope
    self.barlows = barlows
    self.output = output
    self._zoom = OpticsUtils.compute_zoom(telescope, barlows, output)
    self._field_of_view = OpticsUtils.compute_field_of_view(telescope, barlows, output)

  def zoom(self):
    return self._zoom
  
  def label(self):
    return ", ".join([str(self.telescope)]+[str(item) for item in self.barlows]+[str(self.output)])
  
  def length(self):
    return 2 + len(self.barlows)
  
  def fov(self):
    return self._field_of_view  
 
  def elements(self):
    """Return immutable set of elements - used for removing redundant optical paths"""
    elements = set((self.telescope,self.output))
    elements |= set(self.barlows)
    return frozenset(elements)
    
  #def print(self):
  #  items = "\n * ".join([str(item) for item in self]) 
  #  print("""Setup:\n * {}\nZoom: {:.2f}\nField of view: {}""".format(items, self._zoom, Utils.decdeg2dms(self._field_of_view, True))) 
