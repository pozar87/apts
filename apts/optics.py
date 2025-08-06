import functools
import operator
from .opticalequipment.binoculars import Binoculars
from .units import ureg


class OpticsUtils:

  @staticmethod
  def expand(path):
    # First item in the path should be the telescope or binoculars
    main_optic = path[0]
    if isinstance(main_optic, Binoculars):
        # Treat binoculars as the 'output' as well for path structure consistency
        return (main_optic, [], main_optic)

    # Original logic for telescopes
    telescope = main_optic
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
    if isinstance(telescope, Binoculars):
        return telescope.magnification * ureg.dimensionless

    # Original logic
    magnification = OpticsUtils.barlows_multiplications(barlows)
    return telescope.focal_length * magnification / output._zoom_divider()

  @staticmethod
  def compute_field_of_view(telescope, barlows, output):
    if isinstance(telescope, Binoculars):
        return telescope.fov()

    # Original logic
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
    if isinstance(self.telescope, Binoculars):
        return str(self.telescope)
    return ", ".join([str(self.telescope)] + [str(item) for item in self.barlows] + [str(self.output)])

  def length(self):
    # For binoculars, path is [Binoculars], expanded to (Binoculars, [], Binoculars)
    # So self.barlows is []. Length should be 1 for a direct binocular path.
    # Original: return 2 + len(self.barlows) (Telescope + Output + Barlows)
    if isinstance(self.telescope, Binoculars):
        return 1 # Just the binoculars itself
    return 2 + len(self.barlows)


  def fov(self):
    return OpticsUtils.compute_field_of_view(self.telescope, self.barlows, self.output)

  def brightness(self):
    if isinstance(self.telescope, Binoculars):
        # self.telescope.brightness() returns a float like 75.0 (for 75%)
        # OutputOpticalEquipment.brightness returns a value like <Quantity(75.0, 'dimensionless')>
        # To be consistent so that .magnitude can be called later:
        return self.telescope.brightness() * ureg.dimensionless
    # This already returns a pint Quantity from OutputOpticalEquipment's method
    return self.output.brightness(self.telescope, self.zoom())

  def exit_pupil(self):
      if isinstance(self.telescope, Binoculars):
          return self.telescope.exit_pupil() # This returns a Quantity

      # Original logic for telescopes:
      # telescope.aperture should be a Quantity (e.g., mm)
      # self.zoom() returns a dimensionless Quantity
      # The result will be in units of aperture (e.g., mm)
      if hasattr(self.telescope, 'aperture'):
          zoom_value = self.zoom()
          if zoom_value.magnitude == 0: # Avoid division by zero
              return 0 * ureg.mm
          return self.telescope.aperture / zoom_value

      # If it's not Binoculars and telescope has no aperture (should not happen for Telescopes)
      # return a zero quantity to avoid crashes, though this indicates a data problem.
      return 0 * ureg.mm

  def elements(self):
    """
    Return immutable set of elements - used for removing redundant optical paths
    """
    elements = set((self.telescope, self.output))
    elements |= set(self.barlows)
    return frozenset(elements)
