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
    magnification = functools.reduce(
        operator.mul, OpticsUtils.barlows_multiplications(barlows), 1)
    return telescope.focal_length * magnification / output.zoom_divider()

  def compute_field_of_view(telescop, barlows, output):
    barlow_magnification = functools.reduce(
        operator.mul, OpticsUtils.barlows_multiplications(barlows), 1)
    zoom = OpticsUtils.compute_zoom(telescop, barlows, output)
    # TODO: this is not best way to do it
    return output.field_of_view(telescop, zoom, barlow_magnification)


class OpticalPath:
  """
  Class for optical path
  """

  def __init__(self, telescope, barlows, output):
    self.telescope = telescope
    self.barlows = barlows
    self.output = output

  @classmethod
  def from_path(cls, path):
    telescope, barlows, output = OpticsUtils.expand(path)
    return cls(telescope, barlows, output)

  def zoom(self):
    return OpticsUtils.compute_zoom(self.telescope, self.barlows, self.output)

  def label(self):
    return ", ".join([str(self.telescope)] + [str(item) for item in self.barlows] + [str(self.output)])

  def length(self):
    return 2 + len(self.barlows)

  def fov(self):
    return OpticsUtils.compute_field_of_view(self.telescope, self.barlows, self.output)

  def brightness(self):
    return self.output.brightness(self.telescope, self.zoom())

  def elements(self):
    """
    Return immutable set of elements - used for removing redundant optical paths
    """
    elements = set((self.telescope, self.output))
    elements |= set(self.barlows)
    return frozenset(elements)

  # def print(self):
  #  items = "\n * ".join([str(item) for item in self])
  #  print("""Setup:\n * {}\nZoom: {:.2f}\nField of view: {}""".format(items, self._zoom, Utils.decdeg2dms(self._field_of_view, True)))
