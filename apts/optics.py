import functools
import operator


class OpticsUtils:

  @staticmethod
  def expand(path):
    # First item in the path should be the telescope
    telescope = path[0]
    # Last item in the path is output
    output = path[-1]
    # Barlow lenses are in the middle
    barlows = path[1:-1]
    return (telescope, barlows, output)

  @staticmethod
  def barlows_multiplications(barlows_list):
    barlows = [barlow.magnification for barlow in barlows_list]
    # Multiply all barlows
    return functools.reduce(operator.mul, barlows, 1)

  @staticmethod
  def compute_zoom(telescope, barlows, output):
    magnification = OpticsUtils.barlows_multiplications(barlows)
    return telescope.focal_length * magnification / output._zoom_divider()

  @staticmethod
  def compute_field_of_view(telescope, barlows, output):
    magnification = OpticsUtils.barlows_multiplications(barlows)
    zoom = OpticsUtils.compute_zoom(telescope, barlows, output)
    # TODO: this is not best way to do it
    return output.field_of_view(telescope, zoom, magnification)


class OpticalPath:
  """
  Class representing an optical path in a telescope setup.
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

  def effective_barlow(self):
    return OpticsUtils.barlows_multiplications(self.barlows)

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
