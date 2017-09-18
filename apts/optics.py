import operator
import functools
import math

from .utils import Utils

class OpticsUtils:
  def _expand(path):
    # First item in the path should be the telescope
    telescop = path[0]
    # Last item in the path is output
    output = path[-1]
    # Barlow lenses are in the middle
    barlows = [item.magnification for item in path[1:-1]]
    return (telescop, barlows, output)

  def compute_zoom(path):
    # First item in the path should be the telescopem second barows lenses and finally eyepiece
    telescop, barlows, output = OpticsUtils._expand(path)
    # Multiply all barlows
    magnification = functools.reduce(operator.mul, barlows, 1)
    zoom = telescop.focal_length * magnification / output.zoom_divider()
    return zoom

  def compute_field_of_view(path):
    telescop, barlows, output = OpticsUtils._expand(path)
    magnification = functools.reduce(operator.mul, barlows, 1)
    zoom = OpticsUtils.compute_zoom(path)
    return output.field_of_view(telescop, zoom, magnification) #TODO: this is not best way to do it
    
class OpticalPath(list):
  def __init__(self, *args):
    list.__init__(self, *args)
    self._zoom = OpticsUtils.compute_zoom(self)
    self._field_of_view = OpticsUtils.compute_field_of_view(self)

  def zoom(self):
    return self.zoom
    
  def print(self):
    items = "\n * ".join([str(item) for item in self]) 
    print("""Setup:\n * {}\nZoom: {:.2f}\nField of view: {}""".format(items, self._zoom, Utils.decdeg2dms(self._field_of_view, True))) 
