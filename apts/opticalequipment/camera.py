import math

import numpy

from .abstract import OutputOpticalEqipment
from ..constants import GraphConstants, OpticalType
from ..units import get_unit_registry
from ..utils import ConnectionType, Gender


class Camera(OutputOpticalEqipment):
  @classmethod
  def from_database(cls, entry):
    from ..utils import Utils, Gender
    brand = entry["brand"]
    name = entry["name"]
    vendor = f"{brand} {name}"
    ol = entry.get("optical_length", 0)
    mass = entry.get("mass", 0)
    tt = Utils.map_conn(entry.get("tside_thread"))
    tg = Utils.map_gender(entry.get("tside_gender"))
    sw, sh = 23.5, 15.7
    w, h = 6000, 4000
    if "full frame" in name.lower() or "36x24" in name.lower():
      sw, sh = 35.9, 23.9
      w, h = 8256, 5504
    elif "4/3" in name.lower() or "micro four thirds" in name.lower():
      sw, sh = 17.3, 13.0
      w, h = 4656, 3520
    return cls(
      sw, sh, w, h, vendor=vendor,
      connection_type=tt, connection_gender=tg or Gender.FEMALE,
      backfocus=ol, mass=mass, optical_length=ol
    )
  @classmethod
  def from_database(cls, entry):
    from ..utils import Utils, Gender
    brand = entry["brand"]
    name = entry["name"]
    vendor = f"{brand} {name}"
    ol = entry.get("optical_length", 0)
    mass = entry.get("mass", 0)
    tt = Utils.map_conn(entry.get("tside_thread"))
    tg = Utils.map_gender(entry.get("tside_gender"))
    sw, sh = 23.5, 15.7
    w, h = 6000, 4000
    if "full frame" in name.lower() or "36x24" in name.lower():
      sw, sh = 35.9, 23.9
      w, h = 8256, 5504
    elif "4/3" in name.lower() or "micro four thirds" in name.lower():
      sw, sh = 17.3, 13.0
      w, h = 4656, 3520
    return cls(
      sw, sh, w, h, vendor=vendor,
      connection_type=tt, connection_gender=tg or Gender.FEMALE,
      backfocus=ol, mass=mass, optical_length=ol
    )
  """
  Class representing DSLR camera mounted via T2 adapter
  """

  def __init__(self, sensor_width, sensor_height, width, height, vendor="unknown camera",
               connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE, pixel_size=None, read_noise=None,
               full_well=None, quantum_efficiency=None, backfocus=None, mass=0, optical_length=0):
    super(Camera, self).__init__(0, vendor, mass=mass, optical_length=optical_length)
    self.connection_type = connection_type
    self.connection_gender = connection_gender
    self.sensor_width = sensor_width * get_unit_registry().mm
    self.sensor_height = sensor_height * get_unit_registry().mm
    self.width = width
    self.height = height
    self.read_noise = read_noise
    self.full_well = full_well
    self.quantum_efficiency = quantum_efficiency
    self.backfocus = backfocus * get_unit_registry().mm if backfocus is not None else None
    if pixel_size is not None:
      self._pixel_size = pixel_size * get_unit_registry().micrometer
    else:
      self._pixel_size = None

  def pixel_size(self):
    if self._pixel_size is not None:
      return self._pixel_size
    return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2) / math.sqrt(
      self.width ** 2 + self.height ** 2)

  def _zoom_divider(self):
    return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2)

  def field_of_view(self, telescop, zoom, barlow_magnification):
    return self.sensor_height * 3438 / (telescop.focal_length * barlow_magnification) / 60 * get_unit_registry().deg

  def output_type(self):
    return OpticalType.IMAGE

  def register(self, equipment):
    # Add camera node
    super(Camera, self)._register(equipment)
    # Add camera input node and connect it to camera
    self._register_input(equipment, self.connection_type, self.connection_gender)
    # Connect camera with output image node
    equipment.add_edge(self.id(), GraphConstants.IMAGE_ID)

  def is_visual_output(self):
    return False

  def __str__(self):
    # Format: <vendor> <width>x<height>
    return "{} {}x{}".format(self.vendor, self.sensor_width.magnitude, self.sensor_height.magnitude)

  @classmethod
  def ZWO_ASI2600MC_PRO(cls):
    """
    Factory method for ZWO ASI2600MC Pro camera.
    Sensor: Sony IMX571 (APS-C)
    """
    return cls(
      23.5, 15.7, 6248, 4176, "ZWO ASI2600MC Pro",
      pixel_size=3.76, read_noise=1.0, full_well=50000, quantum_efficiency=80
    )

  @classmethod
  def ZWO_ASI1600MM_PRO(cls):
    """
    Factory method for ZWO ASI1600MM Pro camera.
    Sensor: Panasonic MN34230 (4/3")
    """
    return cls(
      17.7, 13.4, 4656, 3520, "ZWO ASI1600MM Pro",
      pixel_size=3.8, read_noise=1.2, full_well=20000, quantum_efficiency=60
    )

  @classmethod
  def Nikon_D850(cls):
    """
    Factory method for Nikon D850 camera.
    Sensor: Full Frame
    """
    return cls(
      35.9, 23.9, 8256, 5504, "Nikon D850",
      pixel_size=4.35, read_noise=1.1, full_well=48000, quantum_efficiency=54
    )

  @classmethod
  def ZWO_ASI533MC_PRO(cls):
    """
    Factory method for ZWO ASI533MC Pro camera.
    Sensor: Sony IMX533 (1" Square)
    """
    return cls(
      11.31, 11.31, 3008, 3008, "ZWO ASI533MC Pro",
      pixel_size=3.76, read_noise=1.0, full_well=50000, quantum_efficiency=80
    )

  _DATABASE = {
    'ZWO_ASI_183MC_Pro': {'brand': 'ZWO', 'name': 'ASI 183MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 410, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MM_Pro': {'brand': 'ZWO', 'name': 'ASI 183MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 410, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MC_Pro': {'brand': 'ZWO', 'name': 'ASI 294MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 478, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MM_Pro': {'brand': 'ZWO', 'name': 'ASI 294MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 478, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MC_Pro': {'brand': 'ZWO', 'name': 'ASI 533MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MM_Pro': {'brand': 'ZWO', 'name': 'ASI 533MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600MC_Pro': {'brand': 'ZWO', 'name': 'ASI 1600MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 410, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600MM_Pro': {'brand': 'ZWO', 'name': 'ASI 1600MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 410, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_071MC_Pro': {'brand': 'ZWO', 'name': 'ASI 071MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_071MM_Pro': {'brand': 'ZWO', 'name': 'ASI 071MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_094MC_Pro': {'brand': 'ZWO', 'name': 'ASI 094MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_094MM_Pro': {'brand': 'ZWO', 'name': 'ASI 094MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MC_Pro': {'brand': 'ZWO', 'name': 'ASI 2600MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 720, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MM_Pro': {'brand': 'ZWO', 'name': 'ASI 2600MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 720, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MC_Duo': {'brand': 'ZWO', 'name': 'ASI 2600MC Duo', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 730, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MM_Duo': {'brand': 'ZWO', 'name': 'ASI 2600MM Duo', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 730, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200MC_Pro': {'brand': 'ZWO', 'name': 'ASI 6200MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1010, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200MM_Pro': {'brand': 'ZWO', 'name': 'ASI 6200MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1010, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2400MC_Pro': {'brand': 'ZWO', 'name': 'ASI 2400MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2400MM_Pro': {'brand': 'ZWO', 'name': 'ASI 2400MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_128MC_Pro': {'brand': 'ZWO', 'name': 'ASI 128MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_128MM_Pro': {'brand': 'ZWO', 'name': 'ASI 128MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MC': {'brand': 'ZWO', 'name': 'ASI 533MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MM': {'brand': 'ZWO', 'name': 'ASI 533MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MC': {'brand': 'ZWO', 'name': 'ASI 294MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MM': {'brand': 'ZWO', 'name': 'ASI 294MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MC': {'brand': 'ZWO', 'name': 'ASI 183MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MM': {'brand': 'ZWO', 'name': 'ASI 183MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600MC': {'brand': 'ZWO', 'name': 'ASI 1600MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600MM': {'brand': 'ZWO', 'name': 'ASI 1600MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 2600 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 6200 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 294 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_071_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 071 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 533 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 183 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 1600 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2400_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 2400 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_128_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 128 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600_Tilt_Adj_M54': {'brand': 'ZWO', 'name': 'ASI 2600 + Tilt Adj. (M54)', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200_Tilt_Adj_M54': {'brand': 'ZWO', 'name': 'ASI 6200 + Tilt Adj. (M54)', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294_Tilt_Adj_M54': {'brand': 'ZWO', 'name': 'ASI 294 + Tilt Adj. (M54)', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533_Tilt_Adj_M54': {'brand': 'ZWO', 'name': 'ASI 533 + Tilt Adj. (M54)', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_585MC': {'brand': 'ZWO', 'name': 'ASI 585MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_585MM': {'brand': 'ZWO', 'name': 'ASI 585MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_678MC': {'brand': 'ZWO', 'name': 'ASI 678MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_678MM': {'brand': 'ZWO', 'name': 'ASI 678MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_662MC': {'brand': 'ZWO', 'name': 'ASI 662MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_662MM': {'brand': 'ZWO', 'name': 'ASI 662MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_482MC': {'brand': 'ZWO', 'name': 'ASI 482MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_482MM': {'brand': 'ZWO', 'name': 'ASI 482MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_485MC': {'brand': 'ZWO', 'name': 'ASI 485MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_485MM': {'brand': 'ZWO', 'name': 'ASI 485MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_462MC': {'brand': 'ZWO', 'name': 'ASI 462MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_462MM': {'brand': 'ZWO', 'name': 'ASI 462MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_715MC': {'brand': 'ZWO', 'name': 'ASI 715MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_715MM': {'brand': 'ZWO', 'name': 'ASI 715MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_676MC': {'brand': 'ZWO', 'name': 'ASI 676MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_676MM': {'brand': 'ZWO', 'name': 'ASI 676MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_120MM_Mini': {'brand': 'ZWO', 'name': 'ASI 120MM Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_120MC_S': {'brand': 'ZWO', 'name': 'ASI 120MC-S', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_224MC': {'brand': 'ZWO', 'name': 'ASI 224MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_290MM_Mini': {'brand': 'ZWO', 'name': 'ASI 290MM Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_290MC': {'brand': 'ZWO', 'name': 'ASI 290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_178MC': {'brand': 'ZWO', 'name': 'ASI 178MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_178MM': {'brand': 'ZWO', 'name': 'ASI 178MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_385MC': {'brand': 'ZWO', 'name': 'ASI 385MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_385MM': {'brand': 'ZWO', 'name': 'ASI 385MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_220MM_Mini': {'brand': 'ZWO', 'name': 'ASI 220MM Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_174MC': {'brand': 'ZWO', 'name': 'ASI 174MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 60, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_174MM': {'brand': 'ZWO', 'name': 'ASI 174MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 60, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_174MM_Mini': {'brand': 'ZWO', 'name': 'ASI 174MM Mini', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 60, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_600M_Pro': {'brand': 'QHY', 'name': 'QHY 600M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1100, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_600M': {'brand': 'QHY', 'name': 'QHY 600M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1050, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_268M_Pro': {'brand': 'QHY', 'name': 'QHY 268M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 860, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_268M': {'brand': 'QHY', 'name': 'QHY 268M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_533M_Pro': {'brand': 'QHY', 'name': 'QHY 533M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 740, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_533M': {'brand': 'QHY', 'name': 'QHY 533M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_294M_Pro': {'brand': 'QHY', 'name': 'QHY 294M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 680, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_294M': {'brand': 'QHY', 'name': 'QHY 294M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 620, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_183M_Pro': {'brand': 'QHY', 'name': 'QHY 183M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 520, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_183M': {'brand': 'QHY', 'name': 'QHY 183M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_163M': {'brand': 'QHY', 'name': 'QHY 163M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_168M': {'brand': 'QHY', 'name': 'QHY 168M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_367M_Pro': {'brand': 'QHY', 'name': 'QHY 367M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_410M': {'brand': 'QHY', 'name': 'QHY 410M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 950, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_411M': {'brand': 'QHY', 'name': 'QHY 411M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_461M': {'brand': 'QHY', 'name': 'QHY 461M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_492M': {'brand': 'QHY', 'name': 'QHY 492M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 750, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_128M_Pro': {'brand': 'QHY', 'name': 'QHY 128M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_247M': {'brand': 'QHY', 'name': 'QHY 247M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_600C_Pro': {'brand': 'QHY', 'name': 'QHY 600C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1100, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_600C': {'brand': 'QHY', 'name': 'QHY 600C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1050, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_268C_Pro': {'brand': 'QHY', 'name': 'QHY 268C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 860, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_268C': {'brand': 'QHY', 'name': 'QHY 268C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_533C_Pro': {'brand': 'QHY', 'name': 'QHY 533C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 740, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_533C': {'brand': 'QHY', 'name': 'QHY 533C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_294C_Pro': {'brand': 'QHY', 'name': 'QHY 294C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 680, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_294C': {'brand': 'QHY', 'name': 'QHY 294C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 620, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_183C_Pro': {'brand': 'QHY', 'name': 'QHY 183C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 520, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_183C': {'brand': 'QHY', 'name': 'QHY 183C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_163C': {'brand': 'QHY', 'name': 'QHY 163C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_168C': {'brand': 'QHY', 'name': 'QHY 168C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_367C_Pro': {'brand': 'QHY', 'name': 'QHY 367C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_410C': {'brand': 'QHY', 'name': 'QHY 410C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 950, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_411C': {'brand': 'QHY', 'name': 'QHY 411C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_461C': {'brand': 'QHY', 'name': 'QHY 461C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_492C': {'brand': 'QHY', 'name': 'QHY 492C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 750, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_128C_Pro': {'brand': 'QHY', 'name': 'QHY 128C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_247C': {'brand': 'QHY', 'name': 'QHY 247C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_178M': {'brand': 'QHY', 'name': 'QHY 5III 178M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_178C': {'brand': 'QHY', 'name': 'QHY 5III 178C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_290M': {'brand': 'QHY', 'name': 'QHY 5III 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_290C': {'brand': 'QHY', 'name': 'QHY 5III 290C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_462C': {'brand': 'QHY', 'name': 'QHY 5III 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_485C': {'brand': 'QHY', 'name': 'QHY 5III 485C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_715C': {'brand': 'QHY', 'name': 'QHY 5III 715C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_533M': {'brand': 'QHY', 'name': 'QHY 5III 533M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_533C': {'brand': 'QHY', 'name': 'QHY 5III 533C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_224C': {'brand': 'QHY', 'name': 'QHY 5III 224C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_174M': {'brand': 'QHY', 'name': 'QHY 5III 174M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_585C': {'brand': 'QHY', 'name': 'QHY 5III 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_662C': {'brand': 'QHY', 'name': 'QHY 5III 662C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Poseidon_C_Pro': {'brand': 'Player One', 'name': 'Poseidon-C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Artemis_C_Pro': {'brand': 'Player One', 'name': 'Artemis-C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ares_C_Pro': {'brand': 'Player One', 'name': 'Ares-C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Apollo_MAX_C_Pro': {'brand': 'Player One', 'name': 'Apollo-MAX-C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Zeus_C_Pro': {'brand': 'Player One', 'name': 'Zeus-C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Hades_C_Pro': {'brand': 'Player One', 'name': 'Hades-C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 470, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Athena_C_Pro': {'brand': 'Player One', 'name': 'Athena-C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 430, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ceres_C_Pro': {'brand': 'Player One', 'name': 'Ceres-C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Poseidon_M_Pro': {'brand': 'Player One', 'name': 'Poseidon-M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Artemis_M_Pro': {'brand': 'Player One', 'name': 'Artemis-M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ares_M_Pro': {'brand': 'Player One', 'name': 'Ares-M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Apollo_MAX_M_Pro': {'brand': 'Player One', 'name': 'Apollo-MAX-M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Zeus_M_Pro': {'brand': 'Player One', 'name': 'Zeus-M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Hades_M_Pro': {'brand': 'Player One', 'name': 'Hades-M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 470, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Athena_M_Pro': {'brand': 'Player One', 'name': 'Athena-M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 430, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ceres_M_Pro': {'brand': 'Player One', 'name': 'Ceres-M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ceres_C': {'brand': 'Player One', 'name': 'Ceres-C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Neptune_II_C': {'brand': 'Player One', 'name': 'Neptune-II-C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 120, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Saturn_C': {'brand': 'Player One', 'name': 'Saturn-C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 130, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Uranus_C': {'brand': 'Player One', 'name': 'Uranus-C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 140, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Mars_II_C': {'brand': 'Player One', 'name': 'Mars-II-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Mercury_C': {'brand': 'Player One', 'name': 'Mercury-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 55, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ceres_M': {'brand': 'Player One', 'name': 'Ceres-M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Neptune_II_M': {'brand': 'Player One', 'name': 'Neptune-II-M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 120, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Saturn_M': {'brand': 'Player One', 'name': 'Saturn-M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 130, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Uranus_M': {'brand': 'Player One', 'name': 'Uranus-M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 140, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Mars_II_M': {'brand': 'Player One', 'name': 'Mars-II-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Mercury_M': {'brand': 'Player One', 'name': 'Mercury-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 55, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV305': {'brand': 'SVBony', 'name': 'SV305', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV305M_Pro': {'brand': 'SVBony', 'name': 'SV305M Pro', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV305C_Pro': {'brand': 'SVBony', 'name': 'SV305C Pro', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV205': {'brand': 'SVBony', 'name': 'SV205', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV405CC': {'brand': 'SVBony', 'name': 'SV405CC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV505C': {'brand': 'SVBony', 'name': 'SV505C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV605CC': {'brand': 'SVBony', 'name': 'SV605CC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV705C': {'brand': 'SVBony', 'name': 'SV705C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV905C': {'brand': 'SVBony', 'name': 'SV905C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV305_Pro': {'brand': 'SVBony', 'name': 'SV305 Pro', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV105': {'brand': 'SVBony', 'name': 'SV105', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV205C': {'brand': 'SVBony', 'name': 'SV205C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 75, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS26000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS26000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS16000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS16000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS02000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS02000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS06300KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS06300KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS26000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS26000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 720, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS07100KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS07100KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS21000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS21000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GP_CMOS02000KMA': {'brand': 'ToupTek', 'name': 'GP-CMOS02000KMA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GP_CMOS02900KPA': {'brand': 'ToupTek', 'name': 'GP-CMOS02900KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GP_CMOS04600KPA': {'brand': 'ToupTek', 'name': 'GP-CMOS04600KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_269C_Pro': {'brand': 'Altair', 'name': 'Hypercam 269C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_183M_Pro': {'brand': 'Altair', 'name': 'Hypercam 183M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_533C_Pro': {'brand': 'Altair', 'name': 'Hypercam 533C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_294C_Pro': {'brand': 'Altair', 'name': 'Hypercam 294C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 680, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_571C_Pro': {'brand': 'Altair', 'name': 'Hypercam 571C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_26000C_Pro': {'brand': 'Altair', 'name': 'Hypercam 26000C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_585C': {'brand': 'Altair', 'name': 'Hypercam 585C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_462C': {'brand': 'Altair', 'name': 'Hypercam 462C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_678C': {'brand': 'Altair', 'name': 'Hypercam 678C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 160, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_174M': {'brand': 'Altair', 'name': 'Hypercam 174M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_Horizon': {'brand': 'Atik', 'name': 'Horizon', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_383L': {'brand': 'Atik', 'name': '383L+', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_460EX': {'brand': 'Atik', 'name': '460EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_ONE_6_0': {'brand': 'Atik', 'name': 'ONE 6.0', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_Infinity': {'brand': 'Atik', 'name': 'Infinity', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_414EX': {'brand': 'Atik', 'name': '414EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_490EX': {'brand': 'Atik', 'name': '490EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_ONE_9_0': {'brand': 'Atik', 'name': 'ONE 9.0', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_16200': {'brand': 'Atik', 'name': '16200', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C3_61000_Pro': {'brand': 'Moravian', 'name': 'C3-61000 Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C1_12000': {'brand': 'Moravian', 'name': 'C1-12000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C4_16000': {'brand': 'Moravian', 'name': 'C4-16000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C3_26000_Pro': {'brand': 'Moravian', 'name': 'C3-26000 Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C1_5000': {'brand': 'Moravian', 'name': 'C1-5000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C5_100000': {'brand': 'Moravian', 'name': 'C5-100000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STF_8300M': {'brand': 'SBIG', 'name': 'STF-8300M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STT_8300M': {'brand': 'SBIG', 'name': 'STT-8300M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STX_16803': {'brand': 'SBIG', 'name': 'STX-16803', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STXL_11002': {'brand': 'SBIG', 'name': 'STXL-11002', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STF_8050M': {'brand': 'SBIG', 'name': 'STF-8050M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STT_1603M': {'brand': 'SBIG', 'name': 'STT-1603M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_Aluma_AC694': {'brand': 'SBIG', 'name': 'Aluma AC694', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ML16200': {'brand': 'FLI', 'name': 'ML16200', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_Kepler_KL400': {'brand': 'FLI', 'name': 'Kepler KL400', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ProLine_16803': {'brand': 'FLI', 'name': 'ProLine 16803', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ML50100': {'brand': 'FLI', 'name': 'ML50100', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 2000, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_Kepler_KL4040': {'brand': 'FLI', 'name': 'Kepler KL4040', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ML8300': {'brand': 'FLI', 'name': 'ML8300', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Trius_SX_694': {'brand': 'Starlight Xpress', 'name': 'Trius SX-694', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Trius_SX_814': {'brand': 'Starlight Xpress', 'name': 'Trius SX-814', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Trius_SX_825': {'brand': 'Starlight Xpress', 'name': 'Trius SX-825', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Trius_SX_46': {'brand': 'Starlight Xpress', 'name': 'Trius SX-46', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Ultrastar': {'brand': 'Starlight Xpress', 'name': 'Ultrastar', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Lodestar_X2': {'brand': 'Starlight Xpress', 'name': 'Lodestar X2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_CoStar': {'brand': 'Starlight Xpress', 'name': 'CoStar', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 120, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX571_ATR': {'brand': 'Rising Cam', 'name': 'IMX571 (ATR)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX533_ATR': {'brand': 'Rising Cam', 'name': 'IMX533 (ATR)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX294_ATR': {'brand': 'Rising Cam', 'name': 'IMX294 (ATR)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX585_ATR': {'brand': 'Rising Cam', 'name': 'IMX585 (ATR)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_571C': {'brand': 'Omegon', 'name': 'veTEC 571C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_533C': {'brand': 'Omegon', 'name': 'veTEC 533C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_294C': {'brand': 'Omegon', 'name': 'veTEC 294C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_183C': {'brand': 'Omegon', 'name': 'veTEC 183C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_2600C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 2600C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_533C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 533C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_294C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 294C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Wanderer_Astro_WanderCam_585C': {'brand': 'Wanderer Astro', 'name': 'WanderCam 585C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 160, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_533C_Pro': {'brand': 'OGMA', 'name': 'OGC-533C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_294C_Pro': {'brand': 'OGMA', 'name': 'OGC-294C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iOptron_iGuider_174M': {'brand': 'iOptron', 'name': 'iGuider 174M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_Ra': {'brand': 'Canon', 'name': 'EOS Ra', 'type': 'type_dslr', 'optical_length': 44, 'mass': 660, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_6D_II': {'brand': 'Canon', 'name': 'EOS 6D II', 'type': 'type_dslr', 'optical_length': 44, 'mass': 765, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_5D_IV': {'brand': 'Canon', 'name': 'EOS 5D IV', 'type': 'type_dslr', 'optical_length': 44, 'mass': 890, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_5D_III': {'brand': 'Canon', 'name': 'EOS 5D III', 'type': 'type_dslr', 'optical_length': 44, 'mass': 860, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_60Da': {'brand': 'Canon', 'name': 'EOS 60Da', 'type': 'type_dslr', 'optical_length': 44, 'mass': 675, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_1000Da': {'brand': 'Canon', 'name': 'EOS 1000Da', 'type': 'type_dslr', 'optical_length': 44, 'mass': 480, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_2000D': {'brand': 'Canon', 'name': 'EOS 2000D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 475, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_850D': {'brand': 'Canon', 'name': 'EOS 850D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 515, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_90D': {'brand': 'Canon', 'name': 'EOS 90D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 619, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_80D': {'brand': 'Canon', 'name': 'EOS 80D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 650, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_77D': {'brand': 'Canon', 'name': 'EOS 77D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 540, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_4000D': {'brand': 'Canon', 'name': 'EOS 4000D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 436, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_750D': {'brand': 'Canon', 'name': 'EOS 750D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 510, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_700D': {'brand': 'Canon', 'name': 'EOS 700D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 525, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_650D': {'brand': 'Canon', 'name': 'EOS 650D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 520, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_600D': {'brand': 'Canon', 'name': 'EOS 600D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 515, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_550D': {'brand': 'Canon', 'name': 'EOS 550D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 530, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_450D': {'brand': 'Canon', 'name': 'EOS 450D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 475, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_350D': {'brand': 'Canon', 'name': 'EOS 350D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 485, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_1100D': {'brand': 'Canon', 'name': 'EOS 1100D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 440, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_7D_II': {'brand': 'Canon', 'name': 'EOS 7D II', 'type': 'type_dslr', 'optical_length': 44, 'mass': 820, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_6D': {'brand': 'Canon', 'name': 'EOS 6D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 755, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_5D_II': {'brand': 'Canon', 'name': 'EOS 5D II', 'type': 'type_dslr', 'optical_length': 44, 'mass': 810, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_1200D': {'brand': 'Canon', 'name': 'EOS 1200D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 435, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R': {'brand': 'Canon', 'name': 'EOS R', 'type': 'type_dslr', 'optical_length': 20, 'mass': 660, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R5': {'brand': 'Canon', 'name': 'EOS R5', 'type': 'type_dslr', 'optical_length': 20, 'mass': 738, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R5_II': {'brand': 'Canon', 'name': 'EOS R5 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 746, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R6': {'brand': 'Canon', 'name': 'EOS R6', 'type': 'type_dslr', 'optical_length': 20, 'mass': 680, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R6_II': {'brand': 'Canon', 'name': 'EOS R6 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 670, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R7': {'brand': 'Canon', 'name': 'EOS R7', 'type': 'type_dslr', 'optical_length': 20, 'mass': 612, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R8': {'brand': 'Canon', 'name': 'EOS R8', 'type': 'type_dslr', 'optical_length': 20, 'mass': 461, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R10': {'brand': 'Canon', 'name': 'EOS R10', 'type': 'type_dslr', 'optical_length': 20, 'mass': 429, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R50': {'brand': 'Canon', 'name': 'EOS R50', 'type': 'type_dslr', 'optical_length': 20, 'mass': 375, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R100': {'brand': 'Canon', 'name': 'EOS R100', 'type': 'type_dslr', 'optical_length': 20, 'mass': 356, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_RP': {'brand': 'Canon', 'name': 'EOS RP', 'type': 'type_dslr', 'optical_length': 20, 'mass': 485, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R3': {'brand': 'Canon', 'name': 'EOS R3', 'type': 'type_dslr', 'optical_length': 20, 'mass': 1015, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D810A': {'brand': 'Nikon', 'name': 'D810A', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 980, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D750': {'brand': 'Nikon', 'name': 'D750', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 840, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D5600': {'brand': 'Nikon', 'name': 'D5600', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 465, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D7500': {'brand': 'Nikon', 'name': 'D7500', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 640, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D3400': {'brand': 'Nikon', 'name': 'D3400', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 395, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D5300': {'brand': 'Nikon', 'name': 'D5300', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 480, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D7200': {'brand': 'Nikon', 'name': 'D7200', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 675, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D810': {'brand': 'Nikon', 'name': 'D810', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 880, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D850': {'brand': 'Nikon', 'name': 'D850', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 1005, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D610': {'brand': 'Nikon', 'name': 'D610', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 760, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D5500': {'brand': 'Nikon', 'name': 'D5500', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 470, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D3300': {'brand': 'Nikon', 'name': 'D3300', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 410, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D500': {'brand': 'Nikon', 'name': 'D500', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 860, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z5': {'brand': 'Nikon', 'name': 'Z5', 'type': 'type_dslr', 'optical_length': 16, 'mass': 675, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z6': {'brand': 'Nikon', 'name': 'Z6', 'type': 'type_dslr', 'optical_length': 16, 'mass': 675, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z6_II': {'brand': 'Nikon', 'name': 'Z6 II', 'type': 'type_dslr', 'optical_length': 16, 'mass': 705, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z6_III': {'brand': 'Nikon', 'name': 'Z6 III', 'type': 'type_dslr', 'optical_length': 16, 'mass': 760, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z7': {'brand': 'Nikon', 'name': 'Z7', 'type': 'type_dslr', 'optical_length': 16, 'mass': 675, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z7_II': {'brand': 'Nikon', 'name': 'Z7 II', 'type': 'type_dslr', 'optical_length': 16, 'mass': 705, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z8': {'brand': 'Nikon', 'name': 'Z8', 'type': 'type_dslr', 'optical_length': 16, 'mass': 910, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z9': {'brand': 'Nikon', 'name': 'Z9', 'type': 'type_dslr', 'optical_length': 16, 'mass': 1340, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z30': {'brand': 'Nikon', 'name': 'Z30', 'type': 'type_dslr', 'optical_length': 16, 'mass': 405, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Z50': {'brand': 'Nikon', 'name': 'Z50', 'type': 'type_dslr', 'optical_length': 16, 'mass': 450, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Zf': {'brand': 'Nikon', 'name': 'Zf', 'type': 'type_dslr', 'optical_length': 16, 'mass': 710, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Zfc': {'brand': 'Nikon', 'name': 'Zfc', 'type': 'type_dslr', 'optical_length': 16, 'mass': 445, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7_III': {'brand': 'Sony', 'name': 'A7 III', 'type': 'type_dslr', 'optical_length': 18, 'mass': 650, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7_IV': {'brand': 'Sony', 'name': 'A7 IV', 'type': 'type_dslr', 'optical_length': 18, 'mass': 658, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7R_IV': {'brand': 'Sony', 'name': 'A7R IV', 'type': 'type_dslr', 'optical_length': 18, 'mass': 665, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7R_V': {'brand': 'Sony', 'name': 'A7R V', 'type': 'type_dslr', 'optical_length': 18, 'mass': 723, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7S_III': {'brand': 'Sony', 'name': 'A7S III', 'type': 'type_dslr', 'optical_length': 18, 'mass': 699, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7CR': {'brand': 'Sony', 'name': 'A7CR', 'type': 'type_dslr', 'optical_length': 18, 'mass': 515, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7C': {'brand': 'Sony', 'name': 'A7C', 'type': 'type_dslr', 'optical_length': 18, 'mass': 509, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7C_II': {'brand': 'Sony', 'name': 'A7C II', 'type': 'type_dslr', 'optical_length': 18, 'mass': 514, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A6700': {'brand': 'Sony', 'name': 'A6700', 'type': 'type_dslr', 'optical_length': 18, 'mass': 493, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A6400': {'brand': 'Sony', 'name': 'A6400', 'type': 'type_dslr', 'optical_length': 18, 'mass': 403, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A6300': {'brand': 'Sony', 'name': 'A6300', 'type': 'type_dslr', 'optical_length': 18, 'mass': 404, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A6100': {'brand': 'Sony', 'name': 'A6100', 'type': 'type_dslr', 'optical_length': 18, 'mass': 396, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A6000': {'brand': 'Sony', 'name': 'A6000', 'type': 'type_dslr', 'optical_length': 18, 'mass': 344, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A1': {'brand': 'Sony', 'name': 'A1', 'type': 'type_dslr', 'optical_length': 18, 'mass': 737, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A9_III': {'brand': 'Sony', 'name': 'A9 III', 'type': 'type_dslr', 'optical_length': 18, 'mass': 703, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7_II': {'brand': 'Sony', 'name': 'A7 II', 'type': 'type_dslr', 'optical_length': 18, 'mass': 599, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7R_III': {'brand': 'Sony', 'name': 'A7R III', 'type': 'type_dslr', 'optical_length': 18, 'mass': 657, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_T4': {'brand': 'Fuji', 'name': 'X-T4', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 607, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_T5': {'brand': 'Fuji', 'name': 'X-T5', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 557, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_T3': {'brand': 'Fuji', 'name': 'X-T3', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 539, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_T2': {'brand': 'Fuji', 'name': 'X-T2', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 507, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_T30_II': {'brand': 'Fuji', 'name': 'X-T30 II', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 378, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_H2': {'brand': 'Fuji', 'name': 'X-H2', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 660, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_H2S': {'brand': 'Fuji', 'name': 'X-H2S', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 660, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_S20': {'brand': 'Fuji', 'name': 'X-S20', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 491, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_S10': {'brand': 'Fuji', 'name': 'X-S10', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 465, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_E4': {'brand': 'Fuji', 'name': 'X-E4', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 364, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_T50': {'brand': 'Fuji', 'name': 'X-T50', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 438, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Pentax_K_1_II': {'brand': 'Pentax', 'name': 'K-1 II', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 1010, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Pentax_K_1': {'brand': 'Pentax', 'name': 'K-1', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 1010, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Pentax_K_3_III': {'brand': 'Pentax', 'name': 'K-3 III', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 820, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Pentax_KP': {'brand': 'Pentax', 'name': 'KP', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 703, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Pentax_K_70': {'brand': 'Pentax', 'name': 'K-70', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 688, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OM_System_Olympus_OM_1': {'brand': 'OM System/Olympus', 'name': 'OM-1', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 599, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OM_System_Olympus_OM_1_II': {'brand': 'OM System/Olympus', 'name': 'OM-1 II', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 599, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OM_System_Olympus_E_M1_III': {'brand': 'OM System/Olympus', 'name': 'E-M1 III', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 580, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OM_System_Olympus_E_M1_II': {'brand': 'OM System/Olympus', 'name': 'E-M1 II', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 574, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OM_System_Olympus_E_M5_III': {'brand': 'OM System/Olympus', 'name': 'E-M5 III', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 414, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OM_System_Olympus_E_M10_IV': {'brand': 'OM System/Olympus', 'name': 'E-M10 IV', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 383, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OM_System_Olympus_E_PL10': {'brand': 'OM System/Olympus', 'name': 'E-PL10', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 332, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_GH6': {'brand': 'Panasonic', 'name': 'GH6', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 823, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_GH5_II': {'brand': 'Panasonic', 'name': 'GH5 II', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 727, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_GH5': {'brand': 'Panasonic', 'name': 'GH5', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 725, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_G9_II': {'brand': 'Panasonic', 'name': 'G9 II', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 658, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_G9': {'brand': 'Panasonic', 'name': 'G9', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 586, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_G85': {'brand': 'Panasonic', 'name': 'G85', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 505, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_GX85': {'brand': 'Panasonic', 'name': 'GX85', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 426, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_G100': {'brand': 'Panasonic', 'name': 'G100', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 412, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 2600MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 2600MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 6200MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 6200MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 294MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 294MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 533MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 533MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 183MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 183MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 1600MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 1600MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_071MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 071MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_128MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 128MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2400MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 2400MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MC_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 2600MC Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MM_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 2600MM Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200MC_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 6200MC Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200MM_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 6200MM Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MC_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 294MC Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MC_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 533MC Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_600M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 600M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 1130, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_268M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 268M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 890, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_533M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 533M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 770, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_294M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 294M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 710, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_183M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 183M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_410M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 410M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 980, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_461M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 461M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 1230, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_600C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 600C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 1130, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_268C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 268C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 890, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_533C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 533C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 770, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_294C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 294C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 710, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_183C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 183C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_410C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 410C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 980, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_461C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 461C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 1230, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS09440KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS09440KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 520, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS04600KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS04600KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS12000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS12000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS09120KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS09120KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS02100KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS02100KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 360, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS08000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS08000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GCMOS01200KPA': {'brand': 'ToupTek', 'name': 'GCMOS01200KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GCMOS01200KMA': {'brand': 'ToupTek', 'name': 'GCMOS01200KMA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C3_12000_Pro': {'brand': 'Moravian', 'name': 'C3-12000 Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C2_3000': {'brand': 'Moravian', 'name': 'C2-3000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C3_16000_Pro': {'brand': 'Moravian', 'name': 'C3-16000 Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C4_9000': {'brand': 'Moravian', 'name': 'C4-9000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C1_3000': {'brand': 'Moravian', 'name': 'C1-3000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R6_III': {'brand': 'Canon', 'name': 'EOS R6 III', 'type': 'type_dslr', 'optical_length': 20, 'mass': 690, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_R1': {'brand': 'Canon', 'name': 'EOS R1', 'type': 'type_dslr', 'optical_length': 20, 'mass': 1000, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_M50_II': {'brand': 'Canon', 'name': 'EOS M50 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 387, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D780': {'brand': 'Nikon', 'name': 'D780', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 840, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D7000': {'brand': 'Nikon', 'name': 'D7000', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 690, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D5100': {'brand': 'Nikon', 'name': 'D5100', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 510, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D3500': {'brand': 'Nikon', 'name': 'D3500', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 415, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A7_V': {'brand': 'Sony', 'name': 'A7 V', 'type': 'type_dslr', 'optical_length': 18, 'mass': 700, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A6500': {'brand': 'Sony', 'name': 'A6500', 'type': 'type_dslr', 'optical_length': 18, 'mass': 453, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A5100': {'brand': 'Sony', 'name': 'A5100', 'type': 'type_dslr', 'optical_length': 18, 'mass': 283, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_T1': {'brand': 'Fuji', 'name': 'X-T1', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 440, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_T20': {'brand': 'Fuji', 'name': 'X-T20', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 383, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_A7': {'brand': 'Fuji', 'name': 'X-A7', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 320, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_571C_Pro': {'brand': 'OGMA', 'name': 'OGC-571C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_183C_Pro': {'brand': 'OGMA', 'name': 'OGC-183C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_585C': {'brand': 'OGMA', 'name': 'OGC-585C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_462C': {'brand': 'OGMA', 'name': 'OGC-462C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_678C': {'brand': 'OGMA', 'name': 'OGC-678C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 170, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_178C': {'brand': 'OGMA', 'name': 'OGC-178C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iNova_PLB_Cx2_178C': {'brand': 'iNova', 'name': 'PLB-Cx2 178C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iNova_PLB_Cx2_290C': {'brand': 'iNova', 'name': 'PLB-Cx2 290C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iNova_PLB_Cx2_462C': {'brand': 'iNova', 'name': 'PLB-Cx2 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iNova_PLB_Cx2_585C': {'brand': 'iNova', 'name': 'PLB-Cx2 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_SkyRaider_DS26000C': {'brand': 'Mallincam', 'name': 'SkyRaider DS26000C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_SkyRaider_DS16000C': {'brand': 'Mallincam', 'name': 'SkyRaider DS16000C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_SkyRaider_DS2100C': {'brand': 'Mallincam', 'name': 'SkyRaider DS2100C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_SkyRaider_DS287C': {'brand': 'Mallincam', 'name': 'SkyRaider DS287C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_Xtreme_Solar_System_Imager': {'brand': 'Mallincam', 'name': 'Xtreme Solar System Imager', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_PoleMaster': {'brand': 'QHY', 'name': 'PoleMaster', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_MiniGuideScope_5III': {'brand': 'QHY', 'name': 'MiniGuideScope + 5III', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 210, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Lodestar_PRO': {'brand': 'Starlight Xpress', 'name': 'Lodestar PRO', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_SXVR_H694': {'brand': 'Starlight Xpress', 'name': 'SXVR-H694', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_SXVR_H814': {'brand': 'Starlight Xpress', 'name': 'SXVR-H814', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_SXVR_H9': {'brand': 'Starlight Xpress', 'name': 'SXVR-H9', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_SXVR_H18': {'brand': 'Starlight Xpress', 'name': 'SXVR-H18', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_SXVR_H35': {'brand': 'Starlight Xpress', 'name': 'SXVR-H35', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_SXVR_H36': {'brand': 'Starlight Xpress', 'name': 'SXVR-H36', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_120MM_S_for_ASIAir': {'brand': 'ZWO', 'name': 'ASI 120MM-S (for ASIAir)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_220MM_Mini_for_ASIAir': {'brand': 'ZWO', 'name': 'ASI 220MM Mini (for ASIAir)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ProLine_PL09000': {'brand': 'FLI', 'name': 'ProLine PL09000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ProLine_PL4710': {'brand': 'FLI', 'name': 'ProLine PL4710', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ProLine_PL11002': {'brand': 'FLI', 'name': 'ProLine PL11002', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_Kepler_KL4040M': {'brand': 'FLI', 'name': 'Kepler KL4040M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_Kepler_KL16070': {'brand': 'FLI', 'name': 'Kepler KL16070', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1800, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_MicroLine_ML4710': {'brand': 'FLI', 'name': 'MicroLine ML4710', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_MicroLine_ML1109': {'brand': 'FLI', 'name': 'MicroLine ML1109', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_MicroLine_ML29050': {'brand': 'FLI', 'name': 'MicroLine ML29050', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STT_1603ME': {'brand': 'SBIG', 'name': 'STT-1603ME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STT_3200ME': {'brand': 'SBIG', 'name': 'STT-3200ME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_ST_i': {'brand': 'SBIG', 'name': 'ST-i', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_ST_402ME': {'brand': 'SBIG', 'name': 'ST-402ME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_ST_8300M': {'brand': 'SBIG', 'name': 'ST-8300M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STF_4070M': {'brand': 'SBIG', 'name': 'STF-4070M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_Aluma_AC4040': {'brand': 'SBIG', 'name': 'Aluma AC4040', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_Aluma_AC2020': {'brand': 'SBIG', 'name': 'Aluma AC2020', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_20Da': {'brand': 'Canon', 'name': 'EOS 20Da', 'type': 'type_dslr', 'optical_length': 44, 'mass': 685, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_300D': {'brand': 'Canon', 'name': 'EOS 300D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 560, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_400D': {'brand': 'Canon', 'name': 'EOS 400D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 510, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_500D': {'brand': 'Canon', 'name': 'EOS 500D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 520, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_1000D': {'brand': 'Canon', 'name': 'EOS 1000D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 450, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_1300D': {'brand': 'Canon', 'name': 'EOS 1300D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 440, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_M6_II': {'brand': 'Canon', 'name': 'EOS M6 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 408, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D40': {'brand': 'Nikon', 'name': 'D40', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 475, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D60': {'brand': 'Nikon', 'name': 'D60', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 580, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D70': {'brand': 'Nikon', 'name': 'D70', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 600, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D80': {'brand': 'Nikon', 'name': 'D80', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 625, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D90': {'brand': 'Nikon', 'name': 'D90', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 620, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D200': {'brand': 'Nikon', 'name': 'D200', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 830, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D300': {'brand': 'Nikon', 'name': 'D300', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 825, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D7100': {'brand': 'Nikon', 'name': 'D7100', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 675, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_034MC': {'brand': 'ZWO', 'name': 'ASI 034MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_035MC': {'brand': 'ZWO', 'name': 'ASI 035MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_120MC': {'brand': 'ZWO', 'name': 'ASI 120MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_120MM': {'brand': 'ZWO', 'name': 'ASI 120MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_130MM': {'brand': 'ZWO', 'name': 'ASI 130MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 65, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_035MM': {'brand': 'ZWO', 'name': 'ASI 035MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_174MC_Mini': {'brand': 'ZWO', 'name': 'ASI 174MC Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 65, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_290MC_Mini': {'brand': 'ZWO', 'name': 'ASI 290MC Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_290MM': {'brand': 'ZWO', 'name': 'ASI 290MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600MC_Cool': {'brand': 'ZWO', 'name': 'ASI 1600MC Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 380, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_1600MM_Cool': {'brand': 'ZWO', 'name': 'ASI 1600MM Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 380, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MC_Cool': {'brand': 'ZWO', 'name': 'ASI 183MC Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MM_Cool': {'brand': 'ZWO', 'name': 'ASI 183MM Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_071MC_Cool': {'brand': 'ZWO', 'name': 'ASI 071MC Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_094MC_Cool': {'brand': 'ZWO', 'name': 'ASI 094MC Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 780, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_120M': {'brand': 'QHY', 'name': 'QHY 5III 120M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_200M': {'brand': 'QHY', 'name': 'QHY 5III 200M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_385M': {'brand': 'QHY', 'name': 'QHY 5III 385M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_678M': {'brand': 'QHY', 'name': 'QHY 5III 678M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_482M': {'brand': 'QHY', 'name': 'QHY 5III 482M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_120C': {'brand': 'QHY', 'name': 'QHY 5III 120C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_200C': {'brand': 'QHY', 'name': 'QHY 5III 200C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_385C': {'brand': 'QHY', 'name': 'QHY 5III 385C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_678C': {'brand': 'QHY', 'name': 'QHY 5III 678C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_482C': {'brand': 'QHY', 'name': 'QHY 5III 482C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_462M': {'brand': 'QHY', 'name': 'QHY 5III 462M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_568M': {'brand': 'QHY', 'name': 'QHY 5III 568M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 110, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_600M': {'brand': 'QHY', 'name': 'QHY 5III 600M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_568C': {'brand': 'QHY', 'name': 'QHY 5III 568C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 110, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5III_600C': {'brand': 'QHY', 'name': 'QHY 5III 600C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Jupiter_C': {'brand': 'Player One', 'name': 'Jupiter-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Luna_C': {'brand': 'Player One', 'name': 'Luna-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Pluto_C': {'brand': 'Player One', 'name': 'Pluto-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Callisto_C': {'brand': 'Player One', 'name': 'Callisto-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Io_C': {'brand': 'Player One', 'name': 'Io-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 95, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ganymede_C': {'brand': 'Player One', 'name': 'Ganymede-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 110, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Titan_C': {'brand': 'Player One', 'name': 'Titan-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Triton_C': {'brand': 'Player One', 'name': 'Triton-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 125, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Charon_C': {'brand': 'Player One', 'name': 'Charon-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Oberon_C': {'brand': 'Player One', 'name': 'Oberon-C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 115, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Jupiter_M': {'brand': 'Player One', 'name': 'Jupiter-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Luna_M': {'brand': 'Player One', 'name': 'Luna-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Pluto_M': {'brand': 'Player One', 'name': 'Pluto-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Callisto_M': {'brand': 'Player One', 'name': 'Callisto-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Io_M': {'brand': 'Player One', 'name': 'Io-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 95, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ganymede_M': {'brand': 'Player One', 'name': 'Ganymede-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 110, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Titan_M': {'brand': 'Player One', 'name': 'Titan-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Triton_M': {'brand': 'Player One', 'name': 'Triton-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 125, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Charon_M': {'brand': 'Player One', 'name': 'Charon-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Oberon_M': {'brand': 'Player One', 'name': 'Oberon-M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 115, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_290M': {'brand': 'Altair', 'name': 'Hypercam 290M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_290C': {'brand': 'Altair', 'name': 'Hypercam 290C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_178M': {'brand': 'Altair', 'name': 'Hypercam 178M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_178C': {'brand': 'Altair', 'name': 'Hypercam 178C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_224C': {'brand': 'Altair', 'name': 'Hypercam 224C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_120M': {'brand': 'Altair', 'name': 'Hypercam 120M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_385C': {'brand': 'Altair', 'name': 'Hypercam 385C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_174C': {'brand': 'Altair', 'name': 'Hypercam 174C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_2600C_Pro': {'brand': 'Altair', 'name': 'Hypercam 2600C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_16000M_Pro': {'brand': 'Altair', 'name': 'Hypercam 16000M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_GPCAM3_290M': {'brand': 'Altair', 'name': 'GPCAM3 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_GPCAM3_178M': {'brand': 'Altair', 'name': 'GPCAM3 178M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_GPCAM3_462C': {'brand': 'Altair', 'name': 'GPCAM3 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_GPCAM3_385C': {'brand': 'Altair', 'name': 'GPCAM3 385C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_678C': {'brand': 'Rising Cam', 'name': 'IMX 678C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_462MC': {'brand': 'Rising Cam', 'name': 'IMX 462MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_174MM': {'brand': 'Rising Cam', 'name': 'IMX 174MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_290MM': {'brand': 'Rising Cam', 'name': 'IMX 290MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 170, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_290MC': {'brand': 'Rising Cam', 'name': 'IMX 290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 170, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_120MM': {'brand': 'Rising Cam', 'name': 'IMX 120MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_482MC': {'brand': 'Rising Cam', 'name': 'IMX 482MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_385MC': {'brand': 'Rising Cam', 'name': 'IMX 385MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_224MC': {'brand': 'Rising Cam', 'name': 'IMX 224MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_178MM': {'brand': 'Rising Cam', 'name': 'IMX 178MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Rising_Cam_IMX_178MC': {'brand': 'Rising Cam', 'name': 'IMX 178MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_26000C_Pro': {'brand': 'Omegon', 'name': 'veTEC 26000C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_2600MC': {'brand': 'Omegon', 'name': 'veTEC 2600MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_571M': {'brand': 'Omegon', 'name': 'veTEC 571M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 620, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_16000C': {'brand': 'Omegon', 'name': 'veTEC 16000C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_585C': {'brand': 'Omegon', 'name': 'veTEC 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_462C': {'brand': 'Omegon', 'name': 'veTEC 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_178M': {'brand': 'Omegon', 'name': 'veTEC 178M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_veTEC_290M': {'brand': 'Omegon', 'name': 'veTEC 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_vePROBE_462C': {'brand': 'Omegon', 'name': 'vePROBE 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Omegon_vePROBE_290MC': {'brand': 'Omegon', 'name': 'vePROBE 290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_533M_Pro': {'brand': 'OGMA', 'name': 'OGC-533M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_2600C_Pro': {'brand': 'OGMA', 'name': 'OGC-2600C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_2600M_Pro': {'brand': 'OGMA', 'name': 'OGC-2600M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 710, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_290MC': {'brand': 'OGMA', 'name': 'OGC-290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_178MM': {'brand': 'OGMA', 'name': 'OGC-178MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_571C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 571C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 580, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_2600M': {'brand': 'Lacerta', 'name': 'DeepSkyPro 2600M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 720, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_183C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 183C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_183M': {'brand': 'Lacerta', 'name': 'DeepSkyPro 183M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 430, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_585C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_462C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_290MC': {'brand': 'Lacerta', 'name': 'DeepSkyPro 290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Lacerta_DeepSkyPro_178MM': {'brand': 'Lacerta', 'name': 'DeepSkyPro 178MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV305M_II': {'brand': 'SVBony', 'name': 'SV305M II', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV405CC_Pro': {'brand': 'SVBony', 'name': 'SV405CC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV505C_Pro': {'brand': 'SVBony', 'name': 'SV505C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 320, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV605CC_Pro': {'brand': 'SVBony', 'name': 'SV605CC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 520, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV805C': {'brand': 'SVBony', 'name': 'SV805C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 380, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV130': {'brand': 'SVBony', 'name': 'SV130', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 55, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV135M': {'brand': 'SVBony', 'name': 'SV135M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV305_II': {'brand': 'SVBony', 'name': 'SV305 II', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 82, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV505M': {'brand': 'SVBony', 'name': 'SV505M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 310, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV905M': {'brand': 'SVBony', 'name': 'SV905M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 560, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS16000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS16000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 510, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS02900KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS02900KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 370, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS04600KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS04600KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 430, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS09440KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS09440KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS12000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS12000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 560, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS09120KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS09120KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 510, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS02100KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS02100KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 365, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_ATR3CMOS08000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS08000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 490, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GP_CMOS01200KPA': {'brand': 'ToupTek', 'name': 'GP-CMOS01200KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 65, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GP_CMOS01200KMA': {'brand': 'ToupTek', 'name': 'GP-CMOS01200KMA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 65, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GP_CMOS05780KPA': {'brand': 'ToupTek', 'name': 'GP-CMOS05780KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ToupTek_GP_CMOS05780KMA': {'brand': 'ToupTek', 'name': 'GP-CMOS05780KMA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Trius_SX_56': {'brand': 'Starlight Xpress', 'name': 'Trius SX-56', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Trius_SX_36': {'brand': 'Starlight Xpress', 'name': 'Trius SX-36', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Trius_SX_26': {'brand': 'Starlight Xpress', 'name': 'Trius SX-26', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_Trius_SX_16': {'brand': 'Starlight Xpress', 'name': 'Trius SX-16', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_MiniStar': {'brand': 'Starlight Xpress', 'name': 'MiniStar', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Starlight_Xpress_SuperStar': {'brand': 'Starlight Xpress', 'name': 'SuperStar', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_Horizon_II': {'brand': 'Atik', 'name': 'Horizon II', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_414EX_Mono': {'brand': 'Atik', 'name': '414EX Mono', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_428EX': {'brand': 'Atik', 'name': '428EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_450EX': {'brand': 'Atik', 'name': '450EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_ONE_2_0': {'brand': 'Atik', 'name': 'ONE 2.0', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_ACIS_7_1': {'brand': 'Atik', 'name': 'ACIS 7.1', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_ACIS_12_1': {'brand': 'Atik', 'name': 'ACIS 12.1', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1100, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ML16070': {'brand': 'FLI', 'name': 'ML16070', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ML8050': {'brand': 'FLI', 'name': 'ML8050', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ML4710': {'brand': 'FLI', 'name': 'ML4710', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_ProLine_PL16803': {'brand': 'FLI', 'name': 'ProLine PL16803', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLI_Kepler_KL4040_FG': {'brand': 'FLI', 'name': 'Kepler KL4040 FG', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_STF_8050': {'brand': 'SBIG', 'name': 'STF-8050', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_ST_10XME': {'brand': 'SBIG', 'name': 'ST-10XME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_ST_8XME': {'brand': 'SBIG', 'name': 'ST-8XME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SBIG_ST_7XME': {'brand': 'SBIG', 'name': 'ST-7XME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_200D': {'brand': 'Canon', 'name': 'EOS 200D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 453, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_250D': {'brand': 'Canon', 'name': 'EOS 250D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 449, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_M200': {'brand': 'Canon', 'name': 'EOS M200', 'type': 'type_dslr', 'optical_length': 18, 'mass': 299, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_70D': {'brand': 'Canon', 'name': 'EOS 70D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 755, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_5DS_R': {'brand': 'Canon', 'name': 'EOS 5DS R', 'type': 'type_dslr', 'optical_length': 44, 'mass': 930, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_5DS': {'brand': 'Canon', 'name': 'EOS 5DS', 'type': 'type_dslr', 'optical_length': 44, 'mass': 845, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_1DX_III': {'brand': 'Canon', 'name': 'EOS 1DX III', 'type': 'type_dslr', 'optical_length': 44, 'mass': 1440, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_1DX_II': {'brand': 'Canon', 'name': 'EOS 1DX II', 'type': 'type_dslr', 'optical_length': 44, 'mass': 1340, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_5D': {'brand': 'Canon', 'name': 'EOS 5D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 810, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D5000': {'brand': 'Nikon', 'name': 'D5000', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 560, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D3200': {'brand': 'Nikon', 'name': 'D3200', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 455, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D5200': {'brand': 'Nikon', 'name': 'D5200', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 505, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D600': {'brand': 'Nikon', 'name': 'D600', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 760, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D4': {'brand': 'Nikon', 'name': 'D4', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 1340, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D4S': {'brand': 'Nikon', 'name': 'D4S', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 1350, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D5': {'brand': 'Nikon', 'name': 'D5', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 1405, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A6600': {'brand': 'Sony', 'name': 'A6600', 'type': 'type_dslr', 'optical_length': 18, 'mass': 503, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A77_II': {'brand': 'Sony', 'name': 'A77 II', 'type': 'type_dslr', 'optical_length': 18, 'mass': 647, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A99_II': {'brand': 'Sony', 'name': 'A99 II', 'type': 'type_dslr', 'optical_length': 18, 'mass': 849, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_A5000': {'brand': 'Sony', 'name': 'A5000', 'type': 'type_dslr', 'optical_length': 18, 'mass': 269, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_NEX_7': {'brand': 'Sony', 'name': 'NEX-7', 'type': 'type_dslr', 'optical_length': 18, 'mass': 353, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_NEX_6': {'brand': 'Sony', 'name': 'NEX-6', 'type': 'type_dslr', 'optical_length': 18, 'mass': 345, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sony_NEX_5T': {'brand': 'Sony', 'name': 'NEX-5T', 'type': 'type_dslr', 'optical_length': 18, 'mass': 276, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_Pro3': {'brand': 'Fuji', 'name': 'X-Pro3', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 497, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_Pro2': {'brand': 'Fuji', 'name': 'X-Pro2', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 495, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_E3': {'brand': 'Fuji', 'name': 'X-E3', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 337, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_E2': {'brand': 'Fuji', 'name': 'X-E2', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 350, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X100V': {'brand': 'Fuji', 'name': 'X100V', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 478, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_A5': {'brand': 'Fuji', 'name': 'X-A5', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 311, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Fuji_X_A3': {'brand': 'Fuji', 'name': 'X-A3', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 339, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_Lumix_S5': {'brand': 'Panasonic', 'name': 'Lumix S5', 'type': 'type_dslr', 'optical_length': 20, 'mass': 714, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_Lumix_S5_II': {'brand': 'Panasonic', 'name': 'Lumix S5 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 740, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_Lumix_S1': {'brand': 'Panasonic', 'name': 'Lumix S1', 'type': 'type_dslr', 'optical_length': 20, 'mass': 899, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_Lumix_S1R': {'brand': 'Panasonic', 'name': 'Lumix S1R', 'type': 'type_dslr', 'optical_length': 20, 'mass': 898, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Panasonic_Lumix_S1H': {'brand': 'Panasonic', 'name': 'Lumix S1H', 'type': 'type_dslr', 'optical_length': 20, 'mass': 1164, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Samsung_NX1': {'brand': 'Samsung', 'name': 'NX1', 'type': 'type_dslr', 'optical_length': 25.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Samsung_NX500': {'brand': 'Samsung', 'name': 'NX500', 'type': 'type_dslr', 'optical_length': 25.5, 'mass': 292, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Samsung_NX300': {'brand': 'Samsung', 'name': 'NX300', 'type': 'type_dslr', 'optical_length': 25.5, 'mass': 284, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Samsung_NX3000': {'brand': 'Samsung', 'name': 'NX3000', 'type': 'type_dslr', 'optical_length': 25.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Hasselblad_X2D_100C': {'brand': 'Hasselblad', 'name': 'X2D 100C', 'type': 'type_dslr', 'optical_length': 26.7, 'mass': 895, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Hasselblad_X1D_II_50C': {'brand': 'Hasselblad', 'name': 'X1D II 50C', 'type': 'type_dslr', 'optical_length': 26.7, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Hasselblad_907X_50C': {'brand': 'Hasselblad', 'name': '907X 50C', 'type': 'type_dslr', 'optical_length': 26.7, 'mass': 740, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_SkyRaider_DS26C': {'brand': 'Mallincam', 'name': 'SkyRaider DS26C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_SkyRaider_DS10C': {'brand': 'Mallincam', 'name': 'SkyRaider DS10C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_Xtreme': {'brand': 'Mallincam', 'name': 'Xtreme', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_Universe': {'brand': 'Mallincam', 'name': 'Universe', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Mallincam_Micro': {'brand': 'Mallincam', 'name': 'Micro', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Celestron_NexImage_10': {'brand': 'Celestron', 'name': 'NexImage 10', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Celestron_NexImage_Burst': {'brand': 'Celestron', 'name': 'NexImage Burst', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Celestron_NexImage_5': {'brand': 'Celestron', 'name': 'NexImage 5', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Celestron_Skyris_132M': {'brand': 'Celestron', 'name': 'Skyris 132M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Celestron_Skyris_236M': {'brand': 'Celestron', 'name': 'Skyris 236M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Celestron_Skyris_618M': {'brand': 'Celestron', 'name': 'Skyris 618M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 200, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Celestron_Skyris_445M': {'brand': 'Celestron', 'name': 'Skyris 445M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Celestron_Skyris_274M': {'brand': 'Celestron', 'name': 'Skyris 274M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 170, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Meade_LPI_G_Color': {'brand': 'Meade', 'name': 'LPI-G (Color)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Meade_LPI_G_Mono': {'brand': 'Meade', 'name': 'LPI-G (Mono)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Meade_LPI_G_Advanced_Color': {'brand': 'Meade', 'name': 'LPI-G Advanced (Color)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Meade_Deep_Sky_Imager_IV_Color': {'brand': 'Meade', 'name': 'Deep Sky Imager IV (Color)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Meade_Deep_Sky_Imager_IV_Mono': {'brand': 'Meade', 'name': 'Deep Sky Imager IV (Mono)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Meade_Deep_Sky_Imager_Pro': {'brand': 'Meade', 'name': 'Deep Sky Imager Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Orion_StarShoot_G21': {'brand': 'Orion', 'name': 'StarShoot G21', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Orion_StarShoot_G26_Deep_Space': {'brand': 'Orion', 'name': 'StarShoot G26 Deep Space', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Orion_StarShoot_Solar_System_V': {'brand': 'Orion', 'name': 'StarShoot Solar System V', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Orion_StarShoot_Autoguider': {'brand': 'Orion', 'name': 'StarShoot Autoguider', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Orion_StarShoot_Deep_Space_3': {'brand': 'Orion', 'name': 'StarShoot Deep Space 3', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Orion_StarShoot_Mini': {'brand': 'Orion', 'name': 'StarShoot Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Bresser_MikroCamII_5MP': {'brand': 'Bresser', 'name': 'MikroCamII 5MP', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Bresser_MikroCamII_10MP': {'brand': 'Bresser', 'name': 'MikroCamII 10MP', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Bresser_Full_HD_Deep_Sky': {'brand': 'Bresser', 'name': 'Full HD Deep Sky', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Bresser_Astro_2MP_Guide': {'brand': 'Bresser', 'name': 'Astro 2MP Guide', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Explore_Scientific_5MP_Guide_Camera': {'brand': 'Explore Scientific', 'name': '5MP Guide Camera', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Explore_Scientific_3MP_USB3_Planetary': {'brand': 'Explore Scientific', 'name': '3MP USB3 Planetary', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Explore_Scientific_Starlight_571C': {'brand': 'Explore Scientific', 'name': 'Starlight 571C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Explore_Scientific_Starlight_533C': {'brand': 'Explore Scientific', 'name': 'Starlight 533C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Explore_Scientific_Starlight_585C': {'brand': 'Explore Scientific', 'name': 'Starlight 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_100D': {'brand': 'Canon', 'name': 'EOS 100D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 407, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_40D': {'brand': 'Canon', 'name': 'EOS 40D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 740, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_50D': {'brand': 'Canon', 'name': 'EOS 50D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 730, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_30D': {'brand': 'Canon', 'name': 'EOS 30D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 700, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Canon_EOS_20D': {'brand': 'Canon', 'name': 'EOS 20D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 685, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D70s': {'brand': 'Nikon', 'name': 'D70s', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 610, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D50': {'brand': 'Nikon', 'name': 'D50', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 540, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D3100': {'brand': 'Nikon', 'name': 'D3100', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 455, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_D3000': {'brand': 'Nikon', 'name': 'D3000', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 485, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Nikon_Df': {'brand': 'Nikon', 'name': 'Df', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 765, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sigma_fp': {'brand': 'Sigma', 'name': 'fp', 'type': 'type_dslr', 'optical_length': 20, 'mass': 427, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sigma_fp_L': {'brand': 'Sigma', 'name': 'fp L', 'type': 'type_dslr', 'optical_length': 20, 'mass': 427, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sigma_sd_Quattro': {'brand': 'Sigma', 'name': 'sd Quattro', 'type': 'type_dslr', 'optical_length': 20, 'mass': 625, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Sigma_sd_Quattro_H': {'brand': 'Sigma', 'name': 'sd Quattro H', 'type': 'type_dslr', 'optical_length': 20, 'mass': 625, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Leica_SL2': {'brand': 'Leica', 'name': 'SL2', 'type': 'type_dslr', 'optical_length': 20, 'mass': 835, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Leica_SL2_S': {'brand': 'Leica', 'name': 'SL2-S', 'type': 'type_dslr', 'optical_length': 20, 'mass': 850, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Leica_M11': {'brand': 'Leica', 'name': 'M11', 'type': 'type_dslr', 'optical_length': 20, 'mass': 530, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Leica_Q2': {'brand': 'Leica', 'name': 'Q2', 'type': 'type_dslr', 'optical_length': 20, 'mass': 718, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Leica_CL': {'brand': 'Leica', 'name': 'CL', 'type': 'type_dslr', 'optical_length': 20, 'mass': 390, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Logitech_C920_Webcam_afocal': {'brand': 'Logitech', 'name': 'C920 Webcam (afocal)', 'type': 'type_camera', 'optical_length': 0, 'mass': 162, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Logitech_C930e_Webcam_afocal': {'brand': 'Logitech', 'name': 'C930e Webcam (afocal)', 'type': 'type_camera', 'optical_length': 0, 'mass': 175, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Microsoft_LifeCam_HD_3000_afocal': {'brand': 'Microsoft', 'name': 'LifeCam HD-3000 (afocal)', 'type': 'type_camera', 'optical_length': 0, 'mass': 110, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DMK_21AU04_AS': {'brand': 'The Imaging Source', 'name': 'DMK 21AU04.AS', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DMK_41AU02_AS': {'brand': 'The Imaging Source', 'name': 'DMK 41AU02.AS', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DMK_51AU02_AS': {'brand': 'The Imaging Source', 'name': 'DMK 51AU02.AS', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DFK_21AU04_AS': {'brand': 'The Imaging Source', 'name': 'DFK 21AU04.AS', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DFK_41AU02_AS': {'brand': 'The Imaging Source', 'name': 'DFK 41AU02.AS', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DFK_51AU02_AS': {'brand': 'The Imaging Source', 'name': 'DFK 51AU02.AS', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DMK_33UX290': {'brand': 'The Imaging Source', 'name': 'DMK 33UX290', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 200, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DFK_33UX290': {'brand': 'The Imaging Source', 'name': 'DFK 33UX290', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 200, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DMK_33UX178': {'brand': 'The Imaging Source', 'name': 'DMK 33UX178', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'The_Imaging_Source_DFK_33UX585': {'brand': 'The Imaging Source', 'name': 'DFK 33UX585', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 220, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLIR_Point_Grey_Chameleon3_USB3': {'brand': 'FLIR/Point Grey', 'name': 'Chameleon3 USB3', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 200, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLIR_Point_Grey_Grasshopper3_USB3': {'brand': 'FLIR/Point Grey', 'name': 'Grasshopper3 USB3', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 350, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLIR_Point_Grey_Blackfly_S_IMX290': {'brand': 'FLIR/Point Grey', 'name': 'Blackfly S (IMX290)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 250, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLIR_Point_Grey_Blackfly_S_IMX178': {'brand': 'FLIR/Point Grey', 'name': 'Blackfly S (IMX178)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 220, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'FLIR_Point_Grey_Firefly_S': {'brand': 'FLIR/Point Grey', 'name': 'Firefly S', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QSI_690ws': {'brand': 'QSI', 'name': '690ws', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QSI_690wsg': {'brand': 'QSI', 'name': '690wsg', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 850, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QSI_660ws': {'brand': 'QSI', 'name': '660ws', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QSI_660wsg': {'brand': 'QSI', 'name': '660wsg', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QSI_583ws': {'brand': 'QSI', 'name': '583ws', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QSI_583wsg': {'brand': 'QSI', 'name': '583wsg', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QSI_616ws': {'brand': 'QSI', 'name': '616ws', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_11000': {'brand': 'Atik', 'name': '11000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_16HR': {'brand': 'Atik', 'name': '16HR', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_320E': {'brand': 'Atik', 'name': '320E', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_4000': {'brand': 'Atik', 'name': '4000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_Titan_Mono': {'brand': 'Atik', 'name': 'Titan Mono', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_GP_CAM3_290M': {'brand': 'Atik', 'name': 'GP-CAM3 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_GP_CAM2_290M': {'brand': 'Atik', 'name': 'GP-CAM2 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_VS14': {'brand': 'Atik', 'name': 'VS14', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Atik_Apx60': {'brand': 'Atik', 'name': 'Apx60', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C1x_61000': {'brand': 'Moravian', 'name': 'C1x-61000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C1x_26000': {'brand': 'Moravian', 'name': 'C1x-26000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C1_5500': {'brand': 'Moravian', 'name': 'C1-5500', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C2_7000': {'brand': 'Moravian', 'name': 'C2-7000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C3_61000_Pro_v2': {'brand': 'Moravian', 'name': 'C3-61000 Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C4_20000': {'brand': 'Moravian', 'name': 'C4-20000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1100, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Moravian_C5_100000_v2': {'brand': 'Moravian', 'name': 'C5-100000 v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1600, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_990M': {'brand': 'QHY', 'name': 'QHY 990M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_600LM': {'brand': 'QHY', 'name': 'QHY 600LM', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1150, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5200M': {'brand': 'QHY', 'name': 'QHY 5200M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_2020M': {'brand': 'QHY', 'name': 'QHY 2020M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_550M': {'brand': 'QHY', 'name': 'QHY 550M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 650, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_174M': {'brand': 'QHY', 'name': 'QHY 174M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_990C': {'brand': 'QHY', 'name': 'QHY 990C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_600LC': {'brand': 'QHY', 'name': 'QHY 600LC', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1150, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_5200C': {'brand': 'QHY', 'name': 'QHY 5200C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_2020C': {'brand': 'QHY', 'name': 'QHY 2020C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_550C': {'brand': 'QHY', 'name': 'QHY 550C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 650, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'QHY_QHY_174C': {'brand': 'QHY', 'name': 'QHY 174C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 533MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_533MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 533MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 2600MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 730, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_2600MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 2600MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 730, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 6200MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1020, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_6200MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 6200MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1020, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 294MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_294MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 294MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 183MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_183MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 183MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Poseidon_C_Pro_v2': {'brand': 'Player One', 'name': 'Poseidon-C Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 470, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Artemis_C_Pro_v2': {'brand': 'Player One', 'name': 'Artemis-C Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 760, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ares_C_Pro_v2': {'brand': 'Player One', 'name': 'Ares-C Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 810, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Zeus_C_Pro_v2': {'brand': 'Player One', 'name': 'Zeus-C Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 510, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Hades_C_Pro_v2': {'brand': 'Player One', 'name': 'Hades-C Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Athena_C_Pro_v2': {'brand': 'Player One', 'name': 'Athena-C Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 440, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Poseidon_M_Pro_v2': {'brand': 'Player One', 'name': 'Poseidon-M Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 470, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Artemis_M_Pro_v2': {'brand': 'Player One', 'name': 'Artemis-M Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 760, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Ares_M_Pro_v2': {'brand': 'Player One', 'name': 'Ares-M Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 810, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Zeus_M_Pro_v2': {'brand': 'Player One', 'name': 'Zeus-M Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 510, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Hades_M_Pro_v2': {'brand': 'Player One', 'name': 'Hades-M Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Player_One_Athena_M_Pro_v2': {'brand': 'Player One', 'name': 'Athena-M Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 440, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV705M': {'brand': 'SVBony', 'name': 'SV705M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV805M': {'brand': 'SVBony', 'name': 'SV805M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 390, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV905CC': {'brand': 'SVBony', 'name': 'SV905CC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 560, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV405CC_v2': {'brand': 'SVBony', 'name': 'SV405CC v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 430, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV505M_Pro': {'brand': 'SVBony', 'name': 'SV505M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 330, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV605CC_v2': {'brand': 'SVBony', 'name': 'SV605CC v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV205M': {'brand': 'SVBony', 'name': 'SV205M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 72, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'SVBony_SV305M_Pro_v2': {'brand': 'SVBony', 'name': 'SV305M Pro v2', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 82, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_26000M_Pro': {'brand': 'Altair', 'name': 'Hypercam 26000M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 770, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_571M_Pro': {'brand': 'Altair', 'name': 'Hypercam 571M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 660, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_533M_Pro': {'brand': 'Altair', 'name': 'Hypercam 533M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_294M_Pro': {'brand': 'Altair', 'name': 'Hypercam 294M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 690, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_183M_Pro_v2': {'brand': 'Altair', 'name': 'Hypercam 183M Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 510, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'Altair_Hypercam_2600M_Pro': {'brand': 'Altair', 'name': 'Hypercam 2600M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 760, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_571M_Pro': {'brand': 'OGMA', 'name': 'OGC-571M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 610, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_2600C': {'brand': 'OGMA', 'name': 'OGC-2600C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 690, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_2600M': {'brand': 'OGMA', 'name': 'OGC-2600M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_571C': {'brand': 'OGMA', 'name': 'OGC-571C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 590, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'OGMA_OGC_183M_Pro': {'brand': 'OGMA', 'name': 'OGC-183M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 440, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iNova_PLB_Mx2_IMX290': {'brand': 'iNova', 'name': 'PLB-Mx2 (IMX290)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iNova_PLB_Cx2_IMX290': {'brand': 'iNova', 'name': 'PLB-Cx2 (IMX290)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iNova_PLB_Mx2_IMX178': {'brand': 'iNova', 'name': 'PLB-Mx2 (IMX178)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'iNova_PLB_Cx2_IMX178': {'brand': 'iNova', 'name': 'PLB-Cx2 (IMX178)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_715MC_V2': {'brand': 'ZWO', 'name': 'ASI 715MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_715MM_V2': {'brand': 'ZWO', 'name': 'ASI 715MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_585MC_V2': {'brand': 'ZWO', 'name': 'ASI 585MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_585MM_V2': {'brand': 'ZWO', 'name': 'ASI 585MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_662MC_V2': {'brand': 'ZWO', 'name': 'ASI 662MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_662MM_V2': {'brand': 'ZWO', 'name': 'ASI 662MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_678MC_V2': {'brand': 'ZWO', 'name': 'ASI 678MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_678MM_V2': {'brand': 'ZWO', 'name': 'ASI 678MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_482MC_V2': {'brand': 'ZWO', 'name': 'ASI 482MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
    'ZWO_ASI_482MM_V2': {'brand': 'ZWO', 'name': 'ASI 482MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'},
  }

  @classmethod
  def ZWO_ASI_183MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MC_Pro'])

  @classmethod
  def ZWO_ASI_183MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MM_Pro'])

  @classmethod
  def ZWO_ASI_294MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MC_Pro'])

  @classmethod
  def ZWO_ASI_294MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MM_Pro'])

  @classmethod
  def ZWO_ASI_533MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MC_Pro'])

  @classmethod
  def ZWO_ASI_533MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MM_Pro'])

  @classmethod
  def ZWO_ASI_1600MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600MC_Pro'])

  @classmethod
  def ZWO_ASI_1600MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600MM_Pro'])

  @classmethod
  def ZWO_ASI_071MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_071MC_Pro'])

  @classmethod
  def ZWO_ASI_071MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_071MM_Pro'])

  @classmethod
  def ZWO_ASI_094MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_094MC_Pro'])

  @classmethod
  def ZWO_ASI_094MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_094MM_Pro'])

  @classmethod
  def ZWO_ASI_2600MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Pro'])

  @classmethod
  def ZWO_ASI_2600MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Pro'])

  @classmethod
  def ZWO_ASI_2600MC_Duo(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Duo'])

  @classmethod
  def ZWO_ASI_2600MM_Duo(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Duo'])

  @classmethod
  def ZWO_ASI_6200MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200MC_Pro'])

  @classmethod
  def ZWO_ASI_6200MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200MM_Pro'])

  @classmethod
  def ZWO_ASI_2400MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2400MC_Pro'])

  @classmethod
  def ZWO_ASI_2400MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2400MM_Pro'])

  @classmethod
  def ZWO_ASI_128MC_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_128MC_Pro'])

  @classmethod
  def ZWO_ASI_128MM_Pro(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_128MM_Pro'])

  @classmethod
  def ZWO_ASI_533MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MC'])

  @classmethod
  def ZWO_ASI_533MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MM'])

  @classmethod
  def ZWO_ASI_294MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MC'])

  @classmethod
  def ZWO_ASI_294MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MM'])

  @classmethod
  def ZWO_ASI_183MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MC'])

  @classmethod
  def ZWO_ASI_183MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MM'])

  @classmethod
  def ZWO_ASI_1600MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600MC'])

  @classmethod
  def ZWO_ASI_1600MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600MM'])

  @classmethod
  def ZWO_ASI_2600_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600_M54_Adapter'])

  @classmethod
  def ZWO_ASI_6200_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200_M54_Adapter'])

  @classmethod
  def ZWO_ASI_294_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294_M54_Adapter'])

  @classmethod
  def ZWO_ASI_071_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_071_M54_Adapter'])

  @classmethod
  def ZWO_ASI_533_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533_M54_Adapter'])

  @classmethod
  def ZWO_ASI_183_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183_M54_Adapter'])

  @classmethod
  def ZWO_ASI_1600_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600_M54_Adapter'])

  @classmethod
  def ZWO_ASI_2400_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2400_M54_Adapter'])

  @classmethod
  def ZWO_ASI_128_M54_Adapter(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_128_M54_Adapter'])

  @classmethod
  def ZWO_ASI_2600_Tilt_Adj_M54(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600_Tilt_Adj_M54'])

  @classmethod
  def ZWO_ASI_6200_Tilt_Adj_M54(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200_Tilt_Adj_M54'])

  @classmethod
  def ZWO_ASI_294_Tilt_Adj_M54(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294_Tilt_Adj_M54'])

  @classmethod
  def ZWO_ASI_533_Tilt_Adj_M54(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533_Tilt_Adj_M54'])

  @classmethod
  def ZWO_ASI_585MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_585MC'])

  @classmethod
  def ZWO_ASI_585MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_585MM'])

  @classmethod
  def ZWO_ASI_678MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_678MC'])

  @classmethod
  def ZWO_ASI_678MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_678MM'])

  @classmethod
  def ZWO_ASI_662MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_662MC'])

  @classmethod
  def ZWO_ASI_662MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_662MM'])

  @classmethod
  def ZWO_ASI_482MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_482MC'])

  @classmethod
  def ZWO_ASI_482MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_482MM'])

  @classmethod
  def ZWO_ASI_485MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_485MC'])

  @classmethod
  def ZWO_ASI_485MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_485MM'])

  @classmethod
  def ZWO_ASI_462MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_462MC'])

  @classmethod
  def ZWO_ASI_462MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_462MM'])

  @classmethod
  def ZWO_ASI_715MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_715MC'])

  @classmethod
  def ZWO_ASI_715MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_715MM'])

  @classmethod
  def ZWO_ASI_676MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_676MC'])

  @classmethod
  def ZWO_ASI_676MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_676MM'])

  @classmethod
  def ZWO_ASI_120MM_Mini(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_120MM_Mini'])

  @classmethod
  def ZWO_ASI_120MC_S(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_120MC_S'])

  @classmethod
  def ZWO_ASI_224MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_224MC'])

  @classmethod
  def ZWO_ASI_290MM_Mini(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_290MM_Mini'])

  @classmethod
  def ZWO_ASI_290MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_290MC'])

  @classmethod
  def ZWO_ASI_178MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_178MC'])

  @classmethod
  def ZWO_ASI_178MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_178MM'])

  @classmethod
  def ZWO_ASI_385MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_385MC'])

  @classmethod
  def ZWO_ASI_385MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_385MM'])

  @classmethod
  def ZWO_ASI_220MM_Mini(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_220MM_Mini'])

  @classmethod
  def ZWO_ASI_174MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_174MC'])

  @classmethod
  def ZWO_ASI_174MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_174MM'])

  @classmethod
  def ZWO_ASI_174MM_Mini(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_174MM_Mini'])

  @classmethod
  def QHY_QHY_600M_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_600M_Pro'])

  @classmethod
  def QHY_QHY_600M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_600M'])

  @classmethod
  def QHY_QHY_268M_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_268M_Pro'])

  @classmethod
  def QHY_QHY_268M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_268M'])

  @classmethod
  def QHY_QHY_533M_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_533M_Pro'])

  @classmethod
  def QHY_QHY_533M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_533M'])

  @classmethod
  def QHY_QHY_294M_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_294M_Pro'])

  @classmethod
  def QHY_QHY_294M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_294M'])

  @classmethod
  def QHY_QHY_183M_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_183M_Pro'])

  @classmethod
  def QHY_QHY_183M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_183M'])

  @classmethod
  def QHY_QHY_163M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_163M'])

  @classmethod
  def QHY_QHY_168M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_168M'])

  @classmethod
  def QHY_QHY_367M_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_367M_Pro'])

  @classmethod
  def QHY_QHY_410M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_410M'])

  @classmethod
  def QHY_QHY_411M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_411M'])

  @classmethod
  def QHY_QHY_461M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_461M'])

  @classmethod
  def QHY_QHY_492M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_492M'])

  @classmethod
  def QHY_QHY_128M_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_128M_Pro'])

  @classmethod
  def QHY_QHY_247M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_247M'])

  @classmethod
  def QHY_QHY_600C_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_600C_Pro'])

  @classmethod
  def QHY_QHY_600C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_600C'])

  @classmethod
  def QHY_QHY_268C_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_268C_Pro'])

  @classmethod
  def QHY_QHY_268C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_268C'])

  @classmethod
  def QHY_QHY_533C_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_533C_Pro'])

  @classmethod
  def QHY_QHY_533C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_533C'])

  @classmethod
  def QHY_QHY_294C_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_294C_Pro'])

  @classmethod
  def QHY_QHY_294C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_294C'])

  @classmethod
  def QHY_QHY_183C_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_183C_Pro'])

  @classmethod
  def QHY_QHY_183C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_183C'])

  @classmethod
  def QHY_QHY_163C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_163C'])

  @classmethod
  def QHY_QHY_168C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_168C'])

  @classmethod
  def QHY_QHY_367C_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_367C_Pro'])

  @classmethod
  def QHY_QHY_410C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_410C'])

  @classmethod
  def QHY_QHY_411C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_411C'])

  @classmethod
  def QHY_QHY_461C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_461C'])

  @classmethod
  def QHY_QHY_492C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_492C'])

  @classmethod
  def QHY_QHY_128C_Pro(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_128C_Pro'])

  @classmethod
  def QHY_QHY_247C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_247C'])

  @classmethod
  def QHY_QHY_5III_178M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_178M'])

  @classmethod
  def QHY_QHY_5III_178C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_178C'])

  @classmethod
  def QHY_QHY_5III_290M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_290M'])

  @classmethod
  def QHY_QHY_5III_290C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_290C'])

  @classmethod
  def QHY_QHY_5III_462C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_462C'])

  @classmethod
  def QHY_QHY_5III_485C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_485C'])

  @classmethod
  def QHY_QHY_5III_715C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_715C'])

  @classmethod
  def QHY_QHY_5III_533M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_533M'])

  @classmethod
  def QHY_QHY_5III_533C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_533C'])

  @classmethod
  def QHY_QHY_5III_224C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_224C'])

  @classmethod
  def QHY_QHY_5III_174M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_174M'])

  @classmethod
  def QHY_QHY_5III_585C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_585C'])

  @classmethod
  def QHY_QHY_5III_662C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_662C'])

  @classmethod
  def Player_One_Poseidon_C_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Poseidon_C_Pro'])

  @classmethod
  def Player_One_Artemis_C_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Artemis_C_Pro'])

  @classmethod
  def Player_One_Ares_C_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ares_C_Pro'])

  @classmethod
  def Player_One_Apollo_MAX_C_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Apollo_MAX_C_Pro'])

  @classmethod
  def Player_One_Zeus_C_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Zeus_C_Pro'])

  @classmethod
  def Player_One_Hades_C_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Hades_C_Pro'])

  @classmethod
  def Player_One_Athena_C_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Athena_C_Pro'])

  @classmethod
  def Player_One_Ceres_C_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ceres_C_Pro'])

  @classmethod
  def Player_One_Poseidon_M_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Poseidon_M_Pro'])

  @classmethod
  def Player_One_Artemis_M_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Artemis_M_Pro'])

  @classmethod
  def Player_One_Ares_M_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ares_M_Pro'])

  @classmethod
  def Player_One_Apollo_MAX_M_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Apollo_MAX_M_Pro'])

  @classmethod
  def Player_One_Zeus_M_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Zeus_M_Pro'])

  @classmethod
  def Player_One_Hades_M_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Hades_M_Pro'])

  @classmethod
  def Player_One_Athena_M_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Athena_M_Pro'])

  @classmethod
  def Player_One_Ceres_M_Pro(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ceres_M_Pro'])

  @classmethod
  def Player_One_Ceres_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ceres_C'])

  @classmethod
  def Player_One_Neptune_II_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Neptune_II_C'])

  @classmethod
  def Player_One_Saturn_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Saturn_C'])

  @classmethod
  def Player_One_Uranus_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Uranus_C'])

  @classmethod
  def Player_One_Mars_II_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Mars_II_C'])

  @classmethod
  def Player_One_Mercury_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Mercury_C'])

  @classmethod
  def Player_One_Ceres_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ceres_M'])

  @classmethod
  def Player_One_Neptune_II_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Neptune_II_M'])

  @classmethod
  def Player_One_Saturn_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Saturn_M'])

  @classmethod
  def Player_One_Uranus_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Uranus_M'])

  @classmethod
  def Player_One_Mars_II_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Mars_II_M'])

  @classmethod
  def Player_One_Mercury_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Mercury_M'])

  @classmethod
  def SVBony_SV305(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV305'])

  @classmethod
  def SVBony_SV305M_Pro(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV305M_Pro'])

  @classmethod
  def SVBony_SV305C_Pro(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV305C_Pro'])

  @classmethod
  def SVBony_SV205(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV205'])

  @classmethod
  def SVBony_SV405CC(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV405CC'])

  @classmethod
  def SVBony_SV505C(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV505C'])

  @classmethod
  def SVBony_SV605CC(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV605CC'])

  @classmethod
  def SVBony_SV705C(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV705C'])

  @classmethod
  def SVBony_SV905C(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV905C'])

  @classmethod
  def SVBony_SV305_Pro(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV305_Pro'])

  @classmethod
  def SVBony_SV105(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV105'])

  @classmethod
  def SVBony_SV205C(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV205C'])

  @classmethod
  def ToupTek_ATR3CMOS26000KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS26000KPA'])

  @classmethod
  def ToupTek_ATR3CMOS16000KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS16000KPA'])

  @classmethod
  def ToupTek_ATR3CMOS02000KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS02000KMA'])

  @classmethod
  def ToupTek_ATR3CMOS06300KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS06300KPA'])

  @classmethod
  def ToupTek_ATR3CMOS26000KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS26000KMA'])

  @classmethod
  def ToupTek_ATR3CMOS07100KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS07100KPA'])

  @classmethod
  def ToupTek_ATR3CMOS21000KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS21000KPA'])

  @classmethod
  def ToupTek_GP_CMOS02000KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS02000KMA'])

  @classmethod
  def ToupTek_GP_CMOS02900KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS02900KPA'])

  @classmethod
  def ToupTek_GP_CMOS04600KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS04600KPA'])

  @classmethod
  def Altair_Hypercam_269C_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_269C_Pro'])

  @classmethod
  def Altair_Hypercam_183M_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_183M_Pro'])

  @classmethod
  def Altair_Hypercam_533C_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_533C_Pro'])

  @classmethod
  def Altair_Hypercam_294C_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_294C_Pro'])

  @classmethod
  def Altair_Hypercam_571C_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_571C_Pro'])

  @classmethod
  def Altair_Hypercam_26000C_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_26000C_Pro'])

  @classmethod
  def Altair_Hypercam_585C(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_585C'])

  @classmethod
  def Altair_Hypercam_462C(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_462C'])

  @classmethod
  def Altair_Hypercam_678C(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_678C'])

  @classmethod
  def Altair_Hypercam_174M(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_174M'])

  @classmethod
  def Atik_Horizon(cls):
    return cls.from_database(cls._DATABASE['Atik_Horizon'])

  @classmethod
  def Atik_383L(cls):
    return cls.from_database(cls._DATABASE['Atik_383L'])

  @classmethod
  def Atik_460EX(cls):
    return cls.from_database(cls._DATABASE['Atik_460EX'])

  @classmethod
  def Atik_ONE_6_0(cls):
    return cls.from_database(cls._DATABASE['Atik_ONE_6_0'])

  @classmethod
  def Atik_Infinity(cls):
    return cls.from_database(cls._DATABASE['Atik_Infinity'])

  @classmethod
  def Atik_414EX(cls):
    return cls.from_database(cls._DATABASE['Atik_414EX'])

  @classmethod
  def Atik_490EX(cls):
    return cls.from_database(cls._DATABASE['Atik_490EX'])

  @classmethod
  def Atik_ONE_9_0(cls):
    return cls.from_database(cls._DATABASE['Atik_ONE_9_0'])

  @classmethod
  def Atik_16200(cls):
    return cls.from_database(cls._DATABASE['Atik_16200'])

  @classmethod
  def Moravian_C3_61000_Pro(cls):
    return cls.from_database(cls._DATABASE['Moravian_C3_61000_Pro'])

  @classmethod
  def Moravian_C1_12000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C1_12000'])

  @classmethod
  def Moravian_C4_16000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C4_16000'])

  @classmethod
  def Moravian_C3_26000_Pro(cls):
    return cls.from_database(cls._DATABASE['Moravian_C3_26000_Pro'])

  @classmethod
  def Moravian_C1_5000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C1_5000'])

  @classmethod
  def Moravian_C5_100000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C5_100000'])

  @classmethod
  def SBIG_STF_8300M(cls):
    return cls.from_database(cls._DATABASE['SBIG_STF_8300M'])

  @classmethod
  def SBIG_STT_8300M(cls):
    return cls.from_database(cls._DATABASE['SBIG_STT_8300M'])

  @classmethod
  def SBIG_STX_16803(cls):
    return cls.from_database(cls._DATABASE['SBIG_STX_16803'])

  @classmethod
  def SBIG_STXL_11002(cls):
    return cls.from_database(cls._DATABASE['SBIG_STXL_11002'])

  @classmethod
  def SBIG_STF_8050M(cls):
    return cls.from_database(cls._DATABASE['SBIG_STF_8050M'])

  @classmethod
  def SBIG_STT_1603M(cls):
    return cls.from_database(cls._DATABASE['SBIG_STT_1603M'])

  @classmethod
  def SBIG_Aluma_AC694(cls):
    return cls.from_database(cls._DATABASE['SBIG_Aluma_AC694'])

  @classmethod
  def FLI_ML16200(cls):
    return cls.from_database(cls._DATABASE['FLI_ML16200'])

  @classmethod
  def FLI_Kepler_KL400(cls):
    return cls.from_database(cls._DATABASE['FLI_Kepler_KL400'])

  @classmethod
  def FLI_ProLine_16803(cls):
    return cls.from_database(cls._DATABASE['FLI_ProLine_16803'])

  @classmethod
  def FLI_ML50100(cls):
    return cls.from_database(cls._DATABASE['FLI_ML50100'])

  @classmethod
  def FLI_Kepler_KL4040(cls):
    return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040'])

  @classmethod
  def FLI_ML8300(cls):
    return cls.from_database(cls._DATABASE['FLI_ML8300'])

  @classmethod
  def Starlight_Xpress_Trius_SX_694(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_694'])

  @classmethod
  def Starlight_Xpress_Trius_SX_814(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_814'])

  @classmethod
  def Starlight_Xpress_Trius_SX_825(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_825'])

  @classmethod
  def Starlight_Xpress_Trius_SX_46(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_46'])

  @classmethod
  def Starlight_Xpress_Ultrastar(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Ultrastar'])

  @classmethod
  def Starlight_Xpress_Lodestar_X2(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Lodestar_X2'])

  @classmethod
  def Starlight_Xpress_CoStar(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_CoStar'])

  @classmethod
  def Rising_Cam_IMX571_ATR(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX571_ATR'])

  @classmethod
  def Rising_Cam_IMX533_ATR(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX533_ATR'])

  @classmethod
  def Rising_Cam_IMX294_ATR(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX294_ATR'])

  @classmethod
  def Rising_Cam_IMX585_ATR(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX585_ATR'])

  @classmethod
  def Omegon_veTEC_571C(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_571C'])

  @classmethod
  def Omegon_veTEC_533C(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_533C'])

  @classmethod
  def Omegon_veTEC_294C(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_294C'])

  @classmethod
  def Omegon_veTEC_183C(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_183C'])

  @classmethod
  def Lacerta_DeepSkyPro_2600C(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_2600C'])

  @classmethod
  def Lacerta_DeepSkyPro_533C(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_533C'])

  @classmethod
  def Lacerta_DeepSkyPro_294C(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_294C'])

  @classmethod
  def Wanderer_Astro_WanderCam_585C(cls):
    return cls.from_database(cls._DATABASE['Wanderer_Astro_WanderCam_585C'])

  @classmethod
  def OGMA_OGC_533C_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_533C_Pro'])

  @classmethod
  def OGMA_OGC_294C_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_294C_Pro'])

  @classmethod
  def iOptron_iGuider_174M(cls):
    return cls.from_database(cls._DATABASE['iOptron_iGuider_174M'])

  @classmethod
  def Canon_EOS_Ra(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_Ra'])

  @classmethod
  def Canon_EOS_6D_II(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_6D_II'])

  @classmethod
  def Canon_EOS_5D_IV(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_5D_IV'])

  @classmethod
  def Canon_EOS_5D_III(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_5D_III'])

  @classmethod
  def Canon_EOS_60Da(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_60Da'])

  @classmethod
  def Canon_EOS_1000Da(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_1000Da'])

  @classmethod
  def Canon_EOS_2000D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_2000D'])

  @classmethod
  def Canon_EOS_850D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_850D'])

  @classmethod
  def Canon_EOS_90D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_90D'])

  @classmethod
  def Canon_EOS_80D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_80D'])

  @classmethod
  def Canon_EOS_77D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_77D'])

  @classmethod
  def Canon_EOS_4000D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_4000D'])

  @classmethod
  def Canon_EOS_750D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_750D'])

  @classmethod
  def Canon_EOS_700D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_700D'])

  @classmethod
  def Canon_EOS_650D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_650D'])

  @classmethod
  def Canon_EOS_600D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_600D'])

  @classmethod
  def Canon_EOS_550D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_550D'])

  @classmethod
  def Canon_EOS_450D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_450D'])

  @classmethod
  def Canon_EOS_350D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_350D'])

  @classmethod
  def Canon_EOS_1100D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_1100D'])

  @classmethod
  def Canon_EOS_7D_II(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_7D_II'])

  @classmethod
  def Canon_EOS_6D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_6D'])

  @classmethod
  def Canon_EOS_5D_II(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_5D_II'])

  @classmethod
  def Canon_EOS_1200D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_1200D'])

  @classmethod
  def Canon_EOS_R(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R'])

  @classmethod
  def Canon_EOS_R5(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R5'])

  @classmethod
  def Canon_EOS_R5_II(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R5_II'])

  @classmethod
  def Canon_EOS_R6(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R6'])

  @classmethod
  def Canon_EOS_R6_II(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R6_II'])

  @classmethod
  def Canon_EOS_R7(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R7'])

  @classmethod
  def Canon_EOS_R8(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R8'])

  @classmethod
  def Canon_EOS_R10(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R10'])

  @classmethod
  def Canon_EOS_R50(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R50'])

  @classmethod
  def Canon_EOS_R100(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R100'])

  @classmethod
  def Canon_EOS_RP(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_RP'])

  @classmethod
  def Canon_EOS_R3(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R3'])

  @classmethod
  def Nikon_D810A(cls):
    return cls.from_database(cls._DATABASE['Nikon_D810A'])

  @classmethod
  def Nikon_D750(cls):
    return cls.from_database(cls._DATABASE['Nikon_D750'])

  @classmethod
  def Nikon_D5600(cls):
    return cls.from_database(cls._DATABASE['Nikon_D5600'])

  @classmethod
  def Nikon_D7500(cls):
    return cls.from_database(cls._DATABASE['Nikon_D7500'])

  @classmethod
  def Nikon_D3400(cls):
    return cls.from_database(cls._DATABASE['Nikon_D3400'])

  @classmethod
  def Nikon_D5300(cls):
    return cls.from_database(cls._DATABASE['Nikon_D5300'])

  @classmethod
  def Nikon_D7200(cls):
    return cls.from_database(cls._DATABASE['Nikon_D7200'])

  @classmethod
  def Nikon_D810(cls):
    return cls.from_database(cls._DATABASE['Nikon_D810'])

  @classmethod
  def Nikon_D850(cls):
    return cls.from_database(cls._DATABASE['Nikon_D850'])

  @classmethod
  def Nikon_D610(cls):
    return cls.from_database(cls._DATABASE['Nikon_D610'])

  @classmethod
  def Nikon_D5500(cls):
    return cls.from_database(cls._DATABASE['Nikon_D5500'])

  @classmethod
  def Nikon_D3300(cls):
    return cls.from_database(cls._DATABASE['Nikon_D3300'])

  @classmethod
  def Nikon_D500(cls):
    return cls.from_database(cls._DATABASE['Nikon_D500'])

  @classmethod
  def Nikon_Z5(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z5'])

  @classmethod
  def Nikon_Z6(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z6'])

  @classmethod
  def Nikon_Z6_II(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z6_II'])

  @classmethod
  def Nikon_Z6_III(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z6_III'])

  @classmethod
  def Nikon_Z7(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z7'])

  @classmethod
  def Nikon_Z7_II(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z7_II'])

  @classmethod
  def Nikon_Z8(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z8'])

  @classmethod
  def Nikon_Z9(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z9'])

  @classmethod
  def Nikon_Z30(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z30'])

  @classmethod
  def Nikon_Z50(cls):
    return cls.from_database(cls._DATABASE['Nikon_Z50'])

  @classmethod
  def Nikon_Zf(cls):
    return cls.from_database(cls._DATABASE['Nikon_Zf'])

  @classmethod
  def Nikon_Zfc(cls):
    return cls.from_database(cls._DATABASE['Nikon_Zfc'])

  @classmethod
  def Sony_A7_III(cls):
    return cls.from_database(cls._DATABASE['Sony_A7_III'])

  @classmethod
  def Sony_A7_IV(cls):
    return cls.from_database(cls._DATABASE['Sony_A7_IV'])

  @classmethod
  def Sony_A7R_IV(cls):
    return cls.from_database(cls._DATABASE['Sony_A7R_IV'])

  @classmethod
  def Sony_A7R_V(cls):
    return cls.from_database(cls._DATABASE['Sony_A7R_V'])

  @classmethod
  def Sony_A7S_III(cls):
    return cls.from_database(cls._DATABASE['Sony_A7S_III'])

  @classmethod
  def Sony_A7CR(cls):
    return cls.from_database(cls._DATABASE['Sony_A7CR'])

  @classmethod
  def Sony_A7C(cls):
    return cls.from_database(cls._DATABASE['Sony_A7C'])

  @classmethod
  def Sony_A7C_II(cls):
    return cls.from_database(cls._DATABASE['Sony_A7C_II'])

  @classmethod
  def Sony_A6700(cls):
    return cls.from_database(cls._DATABASE['Sony_A6700'])

  @classmethod
  def Sony_A6400(cls):
    return cls.from_database(cls._DATABASE['Sony_A6400'])

  @classmethod
  def Sony_A6300(cls):
    return cls.from_database(cls._DATABASE['Sony_A6300'])

  @classmethod
  def Sony_A6100(cls):
    return cls.from_database(cls._DATABASE['Sony_A6100'])

  @classmethod
  def Sony_A6000(cls):
    return cls.from_database(cls._DATABASE['Sony_A6000'])

  @classmethod
  def Sony_A1(cls):
    return cls.from_database(cls._DATABASE['Sony_A1'])

  @classmethod
  def Sony_A9_III(cls):
    return cls.from_database(cls._DATABASE['Sony_A9_III'])

  @classmethod
  def Sony_A7_II(cls):
    return cls.from_database(cls._DATABASE['Sony_A7_II'])

  @classmethod
  def Sony_A7R_III(cls):
    return cls.from_database(cls._DATABASE['Sony_A7R_III'])

  @classmethod
  def Fuji_X_T4(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_T4'])

  @classmethod
  def Fuji_X_T5(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_T5'])

  @classmethod
  def Fuji_X_T3(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_T3'])

  @classmethod
  def Fuji_X_T2(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_T2'])

  @classmethod
  def Fuji_X_T30_II(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_T30_II'])

  @classmethod
  def Fuji_X_H2(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_H2'])

  @classmethod
  def Fuji_X_H2S(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_H2S'])

  @classmethod
  def Fuji_X_S20(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_S20'])

  @classmethod
  def Fuji_X_S10(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_S10'])

  @classmethod
  def Fuji_X_E4(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_E4'])

  @classmethod
  def Fuji_X_T50(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_T50'])

  @classmethod
  def Pentax_K_1_II(cls):
    return cls.from_database(cls._DATABASE['Pentax_K_1_II'])

  @classmethod
  def Pentax_K_1(cls):
    return cls.from_database(cls._DATABASE['Pentax_K_1'])

  @classmethod
  def Pentax_K_3_III(cls):
    return cls.from_database(cls._DATABASE['Pentax_K_3_III'])

  @classmethod
  def Pentax_KP(cls):
    return cls.from_database(cls._DATABASE['Pentax_KP'])

  @classmethod
  def Pentax_K_70(cls):
    return cls.from_database(cls._DATABASE['Pentax_K_70'])

  @classmethod
  def OM_System_Olympus_OM_1(cls):
    return cls.from_database(cls._DATABASE['OM_System_Olympus_OM_1'])

  @classmethod
  def OM_System_Olympus_OM_1_II(cls):
    return cls.from_database(cls._DATABASE['OM_System_Olympus_OM_1_II'])

  @classmethod
  def OM_System_Olympus_E_M1_III(cls):
    return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M1_III'])

  @classmethod
  def OM_System_Olympus_E_M1_II(cls):
    return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M1_II'])

  @classmethod
  def OM_System_Olympus_E_M5_III(cls):
    return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M5_III'])

  @classmethod
  def OM_System_Olympus_E_M10_IV(cls):
    return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M10_IV'])

  @classmethod
  def OM_System_Olympus_E_PL10(cls):
    return cls.from_database(cls._DATABASE['OM_System_Olympus_E_PL10'])

  @classmethod
  def Panasonic_GH6(cls):
    return cls.from_database(cls._DATABASE['Panasonic_GH6'])

  @classmethod
  def Panasonic_GH5_II(cls):
    return cls.from_database(cls._DATABASE['Panasonic_GH5_II'])

  @classmethod
  def Panasonic_GH5(cls):
    return cls.from_database(cls._DATABASE['Panasonic_GH5'])

  @classmethod
  def Panasonic_G9_II(cls):
    return cls.from_database(cls._DATABASE['Panasonic_G9_II'])

  @classmethod
  def Panasonic_G9(cls):
    return cls.from_database(cls._DATABASE['Panasonic_G9'])

  @classmethod
  def Panasonic_G85(cls):
    return cls.from_database(cls._DATABASE['Panasonic_G85'])

  @classmethod
  def Panasonic_GX85(cls):
    return cls.from_database(cls._DATABASE['Panasonic_GX85'])

  @classmethod
  def Panasonic_G100(cls):
    return cls.from_database(cls._DATABASE['Panasonic_G100'])

  @classmethod
  def ZWO_ASI_2600MC_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_2600MM_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_6200MC_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200MC_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_6200MM_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200MM_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_294MC_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MC_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_294MM_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MM_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_533MC_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MC_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_533MM_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MM_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_183MC_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MC_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_183MM_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MM_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_1600MC_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600MC_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_1600MM_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600MM_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_071MC_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_071MC_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_128MM_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_128MM_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_2400MC_Pro_6_bolt_mount(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2400MC_Pro_6_bolt_mount'])

  @classmethod
  def ZWO_ASI_2600MC_Pro_4_bolt_no_tilt_plate(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Pro_4_bolt_no_tilt_plate'])

  @classmethod
  def ZWO_ASI_2600MM_Pro_4_bolt_no_tilt_plate(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Pro_4_bolt_no_tilt_plate'])

  @classmethod
  def ZWO_ASI_6200MC_Pro_4_bolt_no_tilt_plate(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200MC_Pro_4_bolt_no_tilt_plate'])

  @classmethod
  def ZWO_ASI_6200MM_Pro_4_bolt_no_tilt_plate(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200MM_Pro_4_bolt_no_tilt_plate'])

  @classmethod
  def ZWO_ASI_294MC_Pro_4_bolt_no_tilt_plate(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MC_Pro_4_bolt_no_tilt_plate'])

  @classmethod
  def ZWO_ASI_533MC_Pro_4_bolt_no_tilt_plate(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MC_Pro_4_bolt_no_tilt_plate'])

  @classmethod
  def QHY_QHY_600M_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_600M_M42_Adapter'])

  @classmethod
  def QHY_QHY_268M_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_268M_M42_Adapter'])

  @classmethod
  def QHY_QHY_533M_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_533M_M42_Adapter'])

  @classmethod
  def QHY_QHY_294M_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_294M_M42_Adapter'])

  @classmethod
  def QHY_QHY_183M_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_183M_M42_Adapter'])

  @classmethod
  def QHY_QHY_410M_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_410M_M42_Adapter'])

  @classmethod
  def QHY_QHY_461M_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_461M_M42_Adapter'])

  @classmethod
  def QHY_QHY_600C_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_600C_M42_Adapter'])

  @classmethod
  def QHY_QHY_268C_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_268C_M42_Adapter'])

  @classmethod
  def QHY_QHY_533C_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_533C_M42_Adapter'])

  @classmethod
  def QHY_QHY_294C_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_294C_M42_Adapter'])

  @classmethod
  def QHY_QHY_183C_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_183C_M42_Adapter'])

  @classmethod
  def QHY_QHY_410C_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_410C_M42_Adapter'])

  @classmethod
  def QHY_QHY_461C_M42_Adapter(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_461C_M42_Adapter'])

  @classmethod
  def ToupTek_ATR3CMOS09440KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS09440KPA'])

  @classmethod
  def ToupTek_ATR3CMOS04600KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS04600KPA'])

  @classmethod
  def ToupTek_ATR3CMOS12000KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS12000KPA'])

  @classmethod
  def ToupTek_ATR3CMOS09120KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS09120KPA'])

  @classmethod
  def ToupTek_ATR3CMOS02100KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS02100KPA'])

  @classmethod
  def ToupTek_ATR3CMOS08000KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS08000KPA'])

  @classmethod
  def ToupTek_GCMOS01200KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GCMOS01200KPA'])

  @classmethod
  def ToupTek_GCMOS01200KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GCMOS01200KMA'])

  @classmethod
  def Moravian_C3_12000_Pro(cls):
    return cls.from_database(cls._DATABASE['Moravian_C3_12000_Pro'])

  @classmethod
  def Moravian_C2_3000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C2_3000'])

  @classmethod
  def Moravian_C3_16000_Pro(cls):
    return cls.from_database(cls._DATABASE['Moravian_C3_16000_Pro'])

  @classmethod
  def Moravian_C4_9000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C4_9000'])

  @classmethod
  def Moravian_C1_3000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C1_3000'])

  @classmethod
  def Canon_EOS_R6_III(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R6_III'])

  @classmethod
  def Canon_EOS_R1(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_R1'])

  @classmethod
  def Canon_EOS_M50_II(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_M50_II'])

  @classmethod
  def Nikon_D780(cls):
    return cls.from_database(cls._DATABASE['Nikon_D780'])

  @classmethod
  def Nikon_D7000(cls):
    return cls.from_database(cls._DATABASE['Nikon_D7000'])

  @classmethod
  def Nikon_D5100(cls):
    return cls.from_database(cls._DATABASE['Nikon_D5100'])

  @classmethod
  def Nikon_D3500(cls):
    return cls.from_database(cls._DATABASE['Nikon_D3500'])

  @classmethod
  def Sony_A7_V(cls):
    return cls.from_database(cls._DATABASE['Sony_A7_V'])

  @classmethod
  def Sony_A6500(cls):
    return cls.from_database(cls._DATABASE['Sony_A6500'])

  @classmethod
  def Sony_A5100(cls):
    return cls.from_database(cls._DATABASE['Sony_A5100'])

  @classmethod
  def Fuji_X_T1(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_T1'])

  @classmethod
  def Fuji_X_T20(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_T20'])

  @classmethod
  def Fuji_X_A7(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_A7'])

  @classmethod
  def OGMA_OGC_571C_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_571C_Pro'])

  @classmethod
  def OGMA_OGC_183C_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_183C_Pro'])

  @classmethod
  def OGMA_OGC_585C(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_585C'])

  @classmethod
  def OGMA_OGC_462C(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_462C'])

  @classmethod
  def OGMA_OGC_678C(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_678C'])

  @classmethod
  def OGMA_OGC_178C(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_178C'])

  @classmethod
  def iNova_PLB_Cx2_178C(cls):
    return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_178C'])

  @classmethod
  def iNova_PLB_Cx2_290C(cls):
    return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_290C'])

  @classmethod
  def iNova_PLB_Cx2_462C(cls):
    return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_462C'])

  @classmethod
  def iNova_PLB_Cx2_585C(cls):
    return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_585C'])

  @classmethod
  def Mallincam_SkyRaider_DS26000C(cls):
    return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS26000C'])

  @classmethod
  def Mallincam_SkyRaider_DS16000C(cls):
    return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS16000C'])

  @classmethod
  def Mallincam_SkyRaider_DS2100C(cls):
    return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS2100C'])

  @classmethod
  def Mallincam_SkyRaider_DS287C(cls):
    return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS287C'])

  @classmethod
  def Mallincam_Xtreme_Solar_System_Imager(cls):
    return cls.from_database(cls._DATABASE['Mallincam_Xtreme_Solar_System_Imager'])

  @classmethod
  def QHY_PoleMaster(cls):
    return cls.from_database(cls._DATABASE['QHY_PoleMaster'])

  @classmethod
  def QHY_MiniGuideScope_5III(cls):
    return cls.from_database(cls._DATABASE['QHY_MiniGuideScope_5III'])

  @classmethod
  def Starlight_Xpress_Lodestar_PRO(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Lodestar_PRO'])

  @classmethod
  def Starlight_Xpress_SXVR_H694(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H694'])

  @classmethod
  def Starlight_Xpress_SXVR_H814(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H814'])

  @classmethod
  def Starlight_Xpress_SXVR_H9(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H9'])

  @classmethod
  def Starlight_Xpress_SXVR_H18(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H18'])

  @classmethod
  def Starlight_Xpress_SXVR_H35(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H35'])

  @classmethod
  def Starlight_Xpress_SXVR_H36(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H36'])

  @classmethod
  def ZWO_ASI_120MM_S_for_ASIAir(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_120MM_S_for_ASIAir'])

  @classmethod
  def ZWO_ASI_220MM_Mini_for_ASIAir(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_220MM_Mini_for_ASIAir'])

  @classmethod
  def FLI_ProLine_PL09000(cls):
    return cls.from_database(cls._DATABASE['FLI_ProLine_PL09000'])

  @classmethod
  def FLI_ProLine_PL4710(cls):
    return cls.from_database(cls._DATABASE['FLI_ProLine_PL4710'])

  @classmethod
  def FLI_ProLine_PL11002(cls):
    return cls.from_database(cls._DATABASE['FLI_ProLine_PL11002'])

  @classmethod
  def FLI_Kepler_KL4040M(cls):
    return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040M'])

  @classmethod
  def FLI_Kepler_KL16070(cls):
    return cls.from_database(cls._DATABASE['FLI_Kepler_KL16070'])

  @classmethod
  def FLI_MicroLine_ML4710(cls):
    return cls.from_database(cls._DATABASE['FLI_MicroLine_ML4710'])

  @classmethod
  def FLI_MicroLine_ML1109(cls):
    return cls.from_database(cls._DATABASE['FLI_MicroLine_ML1109'])

  @classmethod
  def FLI_MicroLine_ML29050(cls):
    return cls.from_database(cls._DATABASE['FLI_MicroLine_ML29050'])

  @classmethod
  def SBIG_STT_1603ME(cls):
    return cls.from_database(cls._DATABASE['SBIG_STT_1603ME'])

  @classmethod
  def SBIG_STT_3200ME(cls):
    return cls.from_database(cls._DATABASE['SBIG_STT_3200ME'])

  @classmethod
  def SBIG_ST_i(cls):
    return cls.from_database(cls._DATABASE['SBIG_ST_i'])

  @classmethod
  def SBIG_ST_402ME(cls):
    return cls.from_database(cls._DATABASE['SBIG_ST_402ME'])

  @classmethod
  def SBIG_ST_8300M(cls):
    return cls.from_database(cls._DATABASE['SBIG_ST_8300M'])

  @classmethod
  def SBIG_STF_4070M(cls):
    return cls.from_database(cls._DATABASE['SBIG_STF_4070M'])

  @classmethod
  def SBIG_Aluma_AC4040(cls):
    return cls.from_database(cls._DATABASE['SBIG_Aluma_AC4040'])

  @classmethod
  def SBIG_Aluma_AC2020(cls):
    return cls.from_database(cls._DATABASE['SBIG_Aluma_AC2020'])

  @classmethod
  def Canon_EOS_20Da(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_20Da'])

  @classmethod
  def Canon_EOS_300D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_300D'])

  @classmethod
  def Canon_EOS_400D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_400D'])

  @classmethod
  def Canon_EOS_500D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_500D'])

  @classmethod
  def Canon_EOS_1000D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_1000D'])

  @classmethod
  def Canon_EOS_1300D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_1300D'])

  @classmethod
  def Canon_EOS_M6_II(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_M6_II'])

  @classmethod
  def Nikon_D40(cls):
    return cls.from_database(cls._DATABASE['Nikon_D40'])

  @classmethod
  def Nikon_D60(cls):
    return cls.from_database(cls._DATABASE['Nikon_D60'])

  @classmethod
  def Nikon_D70(cls):
    return cls.from_database(cls._DATABASE['Nikon_D70'])

  @classmethod
  def Nikon_D80(cls):
    return cls.from_database(cls._DATABASE['Nikon_D80'])

  @classmethod
  def Nikon_D90(cls):
    return cls.from_database(cls._DATABASE['Nikon_D90'])

  @classmethod
  def Nikon_D200(cls):
    return cls.from_database(cls._DATABASE['Nikon_D200'])

  @classmethod
  def Nikon_D300(cls):
    return cls.from_database(cls._DATABASE['Nikon_D300'])

  @classmethod
  def Nikon_D7100(cls):
    return cls.from_database(cls._DATABASE['Nikon_D7100'])

  @classmethod
  def ZWO_ASI_034MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_034MC'])

  @classmethod
  def ZWO_ASI_035MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_035MC'])

  @classmethod
  def ZWO_ASI_120MC(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_120MC'])

  @classmethod
  def ZWO_ASI_120MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_120MM'])

  @classmethod
  def ZWO_ASI_130MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_130MM'])

  @classmethod
  def ZWO_ASI_035MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_035MM'])

  @classmethod
  def ZWO_ASI_174MC_Mini(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_174MC_Mini'])

  @classmethod
  def ZWO_ASI_290MC_Mini(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_290MC_Mini'])

  @classmethod
  def ZWO_ASI_290MM(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_290MM'])

  @classmethod
  def ZWO_ASI_1600MC_Cool(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600MC_Cool'])

  @classmethod
  def ZWO_ASI_1600MM_Cool(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_1600MM_Cool'])

  @classmethod
  def ZWO_ASI_183MC_Cool(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MC_Cool'])

  @classmethod
  def ZWO_ASI_183MM_Cool(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MM_Cool'])

  @classmethod
  def ZWO_ASI_071MC_Cool(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_071MC_Cool'])

  @classmethod
  def ZWO_ASI_094MC_Cool(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_094MC_Cool'])

  @classmethod
  def QHY_QHY_5III_120M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_120M'])

  @classmethod
  def QHY_QHY_5III_200M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_200M'])

  @classmethod
  def QHY_QHY_5III_385M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_385M'])

  @classmethod
  def QHY_QHY_5III_678M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_678M'])

  @classmethod
  def QHY_QHY_5III_482M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_482M'])

  @classmethod
  def QHY_QHY_5III_120C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_120C'])

  @classmethod
  def QHY_QHY_5III_200C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_200C'])

  @classmethod
  def QHY_QHY_5III_385C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_385C'])

  @classmethod
  def QHY_QHY_5III_678C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_678C'])

  @classmethod
  def QHY_QHY_5III_482C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_482C'])

  @classmethod
  def QHY_QHY_5III_462M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_462M'])

  @classmethod
  def QHY_QHY_5III_568M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_568M'])

  @classmethod
  def QHY_QHY_5III_600M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_600M'])

  @classmethod
  def QHY_QHY_5III_568C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_568C'])

  @classmethod
  def QHY_QHY_5III_600C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5III_600C'])

  @classmethod
  def Player_One_Jupiter_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Jupiter_C'])

  @classmethod
  def Player_One_Luna_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Luna_C'])

  @classmethod
  def Player_One_Pluto_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Pluto_C'])

  @classmethod
  def Player_One_Callisto_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Callisto_C'])

  @classmethod
  def Player_One_Io_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Io_C'])

  @classmethod
  def Player_One_Ganymede_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ganymede_C'])

  @classmethod
  def Player_One_Titan_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Titan_C'])

  @classmethod
  def Player_One_Triton_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Triton_C'])

  @classmethod
  def Player_One_Charon_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Charon_C'])

  @classmethod
  def Player_One_Oberon_C(cls):
    return cls.from_database(cls._DATABASE['Player_One_Oberon_C'])

  @classmethod
  def Player_One_Jupiter_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Jupiter_M'])

  @classmethod
  def Player_One_Luna_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Luna_M'])

  @classmethod
  def Player_One_Pluto_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Pluto_M'])

  @classmethod
  def Player_One_Callisto_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Callisto_M'])

  @classmethod
  def Player_One_Io_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Io_M'])

  @classmethod
  def Player_One_Ganymede_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ganymede_M'])

  @classmethod
  def Player_One_Titan_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Titan_M'])

  @classmethod
  def Player_One_Triton_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Triton_M'])

  @classmethod
  def Player_One_Charon_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Charon_M'])

  @classmethod
  def Player_One_Oberon_M(cls):
    return cls.from_database(cls._DATABASE['Player_One_Oberon_M'])

  @classmethod
  def Altair_Hypercam_290M(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_290M'])

  @classmethod
  def Altair_Hypercam_290C(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_290C'])

  @classmethod
  def Altair_Hypercam_178M(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_178M'])

  @classmethod
  def Altair_Hypercam_178C(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_178C'])

  @classmethod
  def Altair_Hypercam_224C(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_224C'])

  @classmethod
  def Altair_Hypercam_120M(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_120M'])

  @classmethod
  def Altair_Hypercam_385C(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_385C'])

  @classmethod
  def Altair_Hypercam_174C(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_174C'])

  @classmethod
  def Altair_Hypercam_2600C_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_2600C_Pro'])

  @classmethod
  def Altair_Hypercam_16000M_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_16000M_Pro'])

  @classmethod
  def Altair_GPCAM3_290M(cls):
    return cls.from_database(cls._DATABASE['Altair_GPCAM3_290M'])

  @classmethod
  def Altair_GPCAM3_178M(cls):
    return cls.from_database(cls._DATABASE['Altair_GPCAM3_178M'])

  @classmethod
  def Altair_GPCAM3_462C(cls):
    return cls.from_database(cls._DATABASE['Altair_GPCAM3_462C'])

  @classmethod
  def Altair_GPCAM3_385C(cls):
    return cls.from_database(cls._DATABASE['Altair_GPCAM3_385C'])

  @classmethod
  def Rising_Cam_IMX_678C(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_678C'])

  @classmethod
  def Rising_Cam_IMX_462MC(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_462MC'])

  @classmethod
  def Rising_Cam_IMX_174MM(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_174MM'])

  @classmethod
  def Rising_Cam_IMX_290MM(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_290MM'])

  @classmethod
  def Rising_Cam_IMX_290MC(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_290MC'])

  @classmethod
  def Rising_Cam_IMX_120MM(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_120MM'])

  @classmethod
  def Rising_Cam_IMX_482MC(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_482MC'])

  @classmethod
  def Rising_Cam_IMX_385MC(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_385MC'])

  @classmethod
  def Rising_Cam_IMX_224MC(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_224MC'])

  @classmethod
  def Rising_Cam_IMX_178MM(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_178MM'])

  @classmethod
  def Rising_Cam_IMX_178MC(cls):
    return cls.from_database(cls._DATABASE['Rising_Cam_IMX_178MC'])

  @classmethod
  def Omegon_veTEC_26000C_Pro(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_26000C_Pro'])

  @classmethod
  def Omegon_veTEC_2600MC(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_2600MC'])

  @classmethod
  def Omegon_veTEC_571M(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_571M'])

  @classmethod
  def Omegon_veTEC_16000C(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_16000C'])

  @classmethod
  def Omegon_veTEC_585C(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_585C'])

  @classmethod
  def Omegon_veTEC_462C(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_462C'])

  @classmethod
  def Omegon_veTEC_178M(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_178M'])

  @classmethod
  def Omegon_veTEC_290M(cls):
    return cls.from_database(cls._DATABASE['Omegon_veTEC_290M'])

  @classmethod
  def Omegon_vePROBE_462C(cls):
    return cls.from_database(cls._DATABASE['Omegon_vePROBE_462C'])

  @classmethod
  def Omegon_vePROBE_290MC(cls):
    return cls.from_database(cls._DATABASE['Omegon_vePROBE_290MC'])

  @classmethod
  def OGMA_OGC_533M_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_533M_Pro'])

  @classmethod
  def OGMA_OGC_2600C_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_2600C_Pro'])

  @classmethod
  def OGMA_OGC_2600M_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_2600M_Pro'])

  @classmethod
  def OGMA_OGC_290MC(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_290MC'])

  @classmethod
  def OGMA_OGC_178MM(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_178MM'])

  @classmethod
  def Lacerta_DeepSkyPro_571C(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_571C'])

  @classmethod
  def Lacerta_DeepSkyPro_2600M(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_2600M'])

  @classmethod
  def Lacerta_DeepSkyPro_183C(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_183C'])

  @classmethod
  def Lacerta_DeepSkyPro_183M(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_183M'])

  @classmethod
  def Lacerta_DeepSkyPro_585C(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_585C'])

  @classmethod
  def Lacerta_DeepSkyPro_462C(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_462C'])

  @classmethod
  def Lacerta_DeepSkyPro_290MC(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_290MC'])

  @classmethod
  def Lacerta_DeepSkyPro_178MM(cls):
    return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_178MM'])

  @classmethod
  def SVBony_SV305M_II(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV305M_II'])

  @classmethod
  def SVBony_SV405CC_Pro(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV405CC_Pro'])

  @classmethod
  def SVBony_SV505C_Pro(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV505C_Pro'])

  @classmethod
  def SVBony_SV605CC_Pro(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV605CC_Pro'])

  @classmethod
  def SVBony_SV805C(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV805C'])

  @classmethod
  def SVBony_SV130(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV130'])

  @classmethod
  def SVBony_SV135M(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV135M'])

  @classmethod
  def SVBony_SV305_II(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV305_II'])

  @classmethod
  def SVBony_SV505M(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV505M'])

  @classmethod
  def SVBony_SV905M(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV905M'])

  @classmethod
  def ToupTek_ATR3CMOS16000KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS16000KMA'])

  @classmethod
  def ToupTek_ATR3CMOS02900KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS02900KPA'])

  @classmethod
  def ToupTek_ATR3CMOS04600KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS04600KMA'])

  @classmethod
  def ToupTek_ATR3CMOS09440KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS09440KMA'])

  @classmethod
  def ToupTek_ATR3CMOS12000KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS12000KMA'])

  @classmethod
  def ToupTek_ATR3CMOS09120KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS09120KMA'])

  @classmethod
  def ToupTek_ATR3CMOS02100KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS02100KMA'])

  @classmethod
  def ToupTek_ATR3CMOS08000KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS08000KMA'])

  @classmethod
  def ToupTek_GP_CMOS01200KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS01200KPA'])

  @classmethod
  def ToupTek_GP_CMOS01200KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS01200KMA'])

  @classmethod
  def ToupTek_GP_CMOS05780KPA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS05780KPA'])

  @classmethod
  def ToupTek_GP_CMOS05780KMA(cls):
    return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS05780KMA'])

  @classmethod
  def Starlight_Xpress_Trius_SX_56(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_56'])

  @classmethod
  def Starlight_Xpress_Trius_SX_36(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_36'])

  @classmethod
  def Starlight_Xpress_Trius_SX_26(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_26'])

  @classmethod
  def Starlight_Xpress_Trius_SX_16(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_16'])

  @classmethod
  def Starlight_Xpress_MiniStar(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_MiniStar'])

  @classmethod
  def Starlight_Xpress_SuperStar(cls):
    return cls.from_database(cls._DATABASE['Starlight_Xpress_SuperStar'])

  @classmethod
  def Atik_Horizon_II(cls):
    return cls.from_database(cls._DATABASE['Atik_Horizon_II'])

  @classmethod
  def Atik_414EX_Mono(cls):
    return cls.from_database(cls._DATABASE['Atik_414EX_Mono'])

  @classmethod
  def Atik_428EX(cls):
    return cls.from_database(cls._DATABASE['Atik_428EX'])

  @classmethod
  def Atik_450EX(cls):
    return cls.from_database(cls._DATABASE['Atik_450EX'])

  @classmethod
  def Atik_ONE_2_0(cls):
    return cls.from_database(cls._DATABASE['Atik_ONE_2_0'])

  @classmethod
  def Atik_ACIS_7_1(cls):
    return cls.from_database(cls._DATABASE['Atik_ACIS_7_1'])

  @classmethod
  def Atik_ACIS_12_1(cls):
    return cls.from_database(cls._DATABASE['Atik_ACIS_12_1'])

  @classmethod
  def FLI_ML16070(cls):
    return cls.from_database(cls._DATABASE['FLI_ML16070'])

  @classmethod
  def FLI_ML8050(cls):
    return cls.from_database(cls._DATABASE['FLI_ML8050'])

  @classmethod
  def FLI_ML4710(cls):
    return cls.from_database(cls._DATABASE['FLI_ML4710'])

  @classmethod
  def FLI_ProLine_PL16803(cls):
    return cls.from_database(cls._DATABASE['FLI_ProLine_PL16803'])

  @classmethod
  def FLI_Kepler_KL4040_FG(cls):
    return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040_FG'])

  @classmethod
  def SBIG_STF_8050(cls):
    return cls.from_database(cls._DATABASE['SBIG_STF_8050'])

  @classmethod
  def SBIG_ST_10XME(cls):
    return cls.from_database(cls._DATABASE['SBIG_ST_10XME'])

  @classmethod
  def SBIG_ST_8XME(cls):
    return cls.from_database(cls._DATABASE['SBIG_ST_8XME'])

  @classmethod
  def SBIG_ST_7XME(cls):
    return cls.from_database(cls._DATABASE['SBIG_ST_7XME'])

  @classmethod
  def Canon_EOS_200D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_200D'])

  @classmethod
  def Canon_EOS_250D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_250D'])

  @classmethod
  def Canon_EOS_M200(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_M200'])

  @classmethod
  def Canon_EOS_70D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_70D'])

  @classmethod
  def Canon_EOS_5DS_R(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_5DS_R'])

  @classmethod
  def Canon_EOS_5DS(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_5DS'])

  @classmethod
  def Canon_EOS_1DX_III(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_1DX_III'])

  @classmethod
  def Canon_EOS_1DX_II(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_1DX_II'])

  @classmethod
  def Canon_EOS_5D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_5D'])

  @classmethod
  def Nikon_D5000(cls):
    return cls.from_database(cls._DATABASE['Nikon_D5000'])

  @classmethod
  def Nikon_D3200(cls):
    return cls.from_database(cls._DATABASE['Nikon_D3200'])

  @classmethod
  def Nikon_D5200(cls):
    return cls.from_database(cls._DATABASE['Nikon_D5200'])

  @classmethod
  def Nikon_D600(cls):
    return cls.from_database(cls._DATABASE['Nikon_D600'])

  @classmethod
  def Nikon_D4(cls):
    return cls.from_database(cls._DATABASE['Nikon_D4'])

  @classmethod
  def Nikon_D4S(cls):
    return cls.from_database(cls._DATABASE['Nikon_D4S'])

  @classmethod
  def Nikon_D5(cls):
    return cls.from_database(cls._DATABASE['Nikon_D5'])

  @classmethod
  def Sony_A6600(cls):
    return cls.from_database(cls._DATABASE['Sony_A6600'])

  @classmethod
  def Sony_A77_II(cls):
    return cls.from_database(cls._DATABASE['Sony_A77_II'])

  @classmethod
  def Sony_A99_II(cls):
    return cls.from_database(cls._DATABASE['Sony_A99_II'])

  @classmethod
  def Sony_A5000(cls):
    return cls.from_database(cls._DATABASE['Sony_A5000'])

  @classmethod
  def Sony_NEX_7(cls):
    return cls.from_database(cls._DATABASE['Sony_NEX_7'])

  @classmethod
  def Sony_NEX_6(cls):
    return cls.from_database(cls._DATABASE['Sony_NEX_6'])

  @classmethod
  def Sony_NEX_5T(cls):
    return cls.from_database(cls._DATABASE['Sony_NEX_5T'])

  @classmethod
  def Fuji_X_Pro3(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_Pro3'])

  @classmethod
  def Fuji_X_Pro2(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_Pro2'])

  @classmethod
  def Fuji_X_E3(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_E3'])

  @classmethod
  def Fuji_X_E2(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_E2'])

  @classmethod
  def Fuji_X100V(cls):
    return cls.from_database(cls._DATABASE['Fuji_X100V'])

  @classmethod
  def Fuji_X_A5(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_A5'])

  @classmethod
  def Fuji_X_A3(cls):
    return cls.from_database(cls._DATABASE['Fuji_X_A3'])

  @classmethod
  def Panasonic_Lumix_S5(cls):
    return cls.from_database(cls._DATABASE['Panasonic_Lumix_S5'])

  @classmethod
  def Panasonic_Lumix_S5_II(cls):
    return cls.from_database(cls._DATABASE['Panasonic_Lumix_S5_II'])

  @classmethod
  def Panasonic_Lumix_S1(cls):
    return cls.from_database(cls._DATABASE['Panasonic_Lumix_S1'])

  @classmethod
  def Panasonic_Lumix_S1R(cls):
    return cls.from_database(cls._DATABASE['Panasonic_Lumix_S1R'])

  @classmethod
  def Panasonic_Lumix_S1H(cls):
    return cls.from_database(cls._DATABASE['Panasonic_Lumix_S1H'])

  @classmethod
  def Samsung_NX1(cls):
    return cls.from_database(cls._DATABASE['Samsung_NX1'])

  @classmethod
  def Samsung_NX500(cls):
    return cls.from_database(cls._DATABASE['Samsung_NX500'])

  @classmethod
  def Samsung_NX300(cls):
    return cls.from_database(cls._DATABASE['Samsung_NX300'])

  @classmethod
  def Samsung_NX3000(cls):
    return cls.from_database(cls._DATABASE['Samsung_NX3000'])

  @classmethod
  def Hasselblad_X2D_100C(cls):
    return cls.from_database(cls._DATABASE['Hasselblad_X2D_100C'])

  @classmethod
  def Hasselblad_X1D_II_50C(cls):
    return cls.from_database(cls._DATABASE['Hasselblad_X1D_II_50C'])

  @classmethod
  def Hasselblad_907X_50C(cls):
    return cls.from_database(cls._DATABASE['Hasselblad_907X_50C'])

  @classmethod
  def Mallincam_SkyRaider_DS26C(cls):
    return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS26C'])

  @classmethod
  def Mallincam_SkyRaider_DS10C(cls):
    return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS10C'])

  @classmethod
  def Mallincam_Xtreme(cls):
    return cls.from_database(cls._DATABASE['Mallincam_Xtreme'])

  @classmethod
  def Mallincam_Universe(cls):
    return cls.from_database(cls._DATABASE['Mallincam_Universe'])

  @classmethod
  def Mallincam_Micro(cls):
    return cls.from_database(cls._DATABASE['Mallincam_Micro'])

  @classmethod
  def Celestron_NexImage_10(cls):
    return cls.from_database(cls._DATABASE['Celestron_NexImage_10'])

  @classmethod
  def Celestron_NexImage_Burst(cls):
    return cls.from_database(cls._DATABASE['Celestron_NexImage_Burst'])

  @classmethod
  def Celestron_NexImage_5(cls):
    return cls.from_database(cls._DATABASE['Celestron_NexImage_5'])

  @classmethod
  def Celestron_Skyris_132M(cls):
    return cls.from_database(cls._DATABASE['Celestron_Skyris_132M'])

  @classmethod
  def Celestron_Skyris_236M(cls):
    return cls.from_database(cls._DATABASE['Celestron_Skyris_236M'])

  @classmethod
  def Celestron_Skyris_618M(cls):
    return cls.from_database(cls._DATABASE['Celestron_Skyris_618M'])

  @classmethod
  def Celestron_Skyris_445M(cls):
    return cls.from_database(cls._DATABASE['Celestron_Skyris_445M'])

  @classmethod
  def Celestron_Skyris_274M(cls):
    return cls.from_database(cls._DATABASE['Celestron_Skyris_274M'])

  @classmethod
  def Meade_LPI_G_Color(cls):
    return cls.from_database(cls._DATABASE['Meade_LPI_G_Color'])

  @classmethod
  def Meade_LPI_G_Mono(cls):
    return cls.from_database(cls._DATABASE['Meade_LPI_G_Mono'])

  @classmethod
  def Meade_LPI_G_Advanced_Color(cls):
    return cls.from_database(cls._DATABASE['Meade_LPI_G_Advanced_Color'])

  @classmethod
  def Meade_Deep_Sky_Imager_IV_Color(cls):
    return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_IV_Color'])

  @classmethod
  def Meade_Deep_Sky_Imager_IV_Mono(cls):
    return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_IV_Mono'])

  @classmethod
  def Meade_Deep_Sky_Imager_Pro(cls):
    return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_Pro'])

  @classmethod
  def Orion_StarShoot_G21(cls):
    return cls.from_database(cls._DATABASE['Orion_StarShoot_G21'])

  @classmethod
  def Orion_StarShoot_G26_Deep_Space(cls):
    return cls.from_database(cls._DATABASE['Orion_StarShoot_G26_Deep_Space'])

  @classmethod
  def Orion_StarShoot_Solar_System_V(cls):
    return cls.from_database(cls._DATABASE['Orion_StarShoot_Solar_System_V'])

  @classmethod
  def Orion_StarShoot_Autoguider(cls):
    return cls.from_database(cls._DATABASE['Orion_StarShoot_Autoguider'])

  @classmethod
  def Orion_StarShoot_Deep_Space_3(cls):
    return cls.from_database(cls._DATABASE['Orion_StarShoot_Deep_Space_3'])

  @classmethod
  def Orion_StarShoot_Mini(cls):
    return cls.from_database(cls._DATABASE['Orion_StarShoot_Mini'])

  @classmethod
  def Bresser_MikroCamII_5MP(cls):
    return cls.from_database(cls._DATABASE['Bresser_MikroCamII_5MP'])

  @classmethod
  def Bresser_MikroCamII_10MP(cls):
    return cls.from_database(cls._DATABASE['Bresser_MikroCamII_10MP'])

  @classmethod
  def Bresser_Full_HD_Deep_Sky(cls):
    return cls.from_database(cls._DATABASE['Bresser_Full_HD_Deep_Sky'])

  @classmethod
  def Bresser_Astro_2MP_Guide(cls):
    return cls.from_database(cls._DATABASE['Bresser_Astro_2MP_Guide'])

  @classmethod
  def Explore_Scientific_5MP_Guide_Camera(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_5MP_Guide_Camera'])

  @classmethod
  def Explore_Scientific_3MP_USB3_Planetary(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_3MP_USB3_Planetary'])

  @classmethod
  def Explore_Scientific_Starlight_571C(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_571C'])

  @classmethod
  def Explore_Scientific_Starlight_533C(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_533C'])

  @classmethod
  def Explore_Scientific_Starlight_585C(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_585C'])

  @classmethod
  def Canon_EOS_100D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_100D'])

  @classmethod
  def Canon_EOS_40D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_40D'])

  @classmethod
  def Canon_EOS_50D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_50D'])

  @classmethod
  def Canon_EOS_30D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_30D'])

  @classmethod
  def Canon_EOS_20D(cls):
    return cls.from_database(cls._DATABASE['Canon_EOS_20D'])

  @classmethod
  def Nikon_D70s(cls):
    return cls.from_database(cls._DATABASE['Nikon_D70s'])

  @classmethod
  def Nikon_D50(cls):
    return cls.from_database(cls._DATABASE['Nikon_D50'])

  @classmethod
  def Nikon_D3100(cls):
    return cls.from_database(cls._DATABASE['Nikon_D3100'])

  @classmethod
  def Nikon_D3000(cls):
    return cls.from_database(cls._DATABASE['Nikon_D3000'])

  @classmethod
  def Nikon_Df(cls):
    return cls.from_database(cls._DATABASE['Nikon_Df'])

  @classmethod
  def Sigma_fp(cls):
    return cls.from_database(cls._DATABASE['Sigma_fp'])

  @classmethod
  def Sigma_fp_L(cls):
    return cls.from_database(cls._DATABASE['Sigma_fp_L'])

  @classmethod
  def Sigma_sd_Quattro(cls):
    return cls.from_database(cls._DATABASE['Sigma_sd_Quattro'])

  @classmethod
  def Sigma_sd_Quattro_H(cls):
    return cls.from_database(cls._DATABASE['Sigma_sd_Quattro_H'])

  @classmethod
  def Leica_SL2(cls):
    return cls.from_database(cls._DATABASE['Leica_SL2'])

  @classmethod
  def Leica_SL2_S(cls):
    return cls.from_database(cls._DATABASE['Leica_SL2_S'])

  @classmethod
  def Leica_M11(cls):
    return cls.from_database(cls._DATABASE['Leica_M11'])

  @classmethod
  def Leica_Q2(cls):
    return cls.from_database(cls._DATABASE['Leica_Q2'])

  @classmethod
  def Leica_CL(cls):
    return cls.from_database(cls._DATABASE['Leica_CL'])

  @classmethod
  def Logitech_C920_Webcam_afocal(cls):
    return cls.from_database(cls._DATABASE['Logitech_C920_Webcam_afocal'])

  @classmethod
  def Logitech_C930e_Webcam_afocal(cls):
    return cls.from_database(cls._DATABASE['Logitech_C930e_Webcam_afocal'])

  @classmethod
  def Microsoft_LifeCam_HD_3000_afocal(cls):
    return cls.from_database(cls._DATABASE['Microsoft_LifeCam_HD_3000_afocal'])

  @classmethod
  def The_Imaging_Source_DMK_21AU04_AS(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DMK_21AU04_AS'])

  @classmethod
  def The_Imaging_Source_DMK_41AU02_AS(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DMK_41AU02_AS'])

  @classmethod
  def The_Imaging_Source_DMK_51AU02_AS(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DMK_51AU02_AS'])

  @classmethod
  def The_Imaging_Source_DFK_21AU04_AS(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DFK_21AU04_AS'])

  @classmethod
  def The_Imaging_Source_DFK_41AU02_AS(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DFK_41AU02_AS'])

  @classmethod
  def The_Imaging_Source_DFK_51AU02_AS(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DFK_51AU02_AS'])

  @classmethod
  def The_Imaging_Source_DMK_33UX290(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DMK_33UX290'])

  @classmethod
  def The_Imaging_Source_DFK_33UX290(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DFK_33UX290'])

  @classmethod
  def The_Imaging_Source_DMK_33UX178(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DMK_33UX178'])

  @classmethod
  def The_Imaging_Source_DFK_33UX585(cls):
    return cls.from_database(cls._DATABASE['The_Imaging_Source_DFK_33UX585'])

  @classmethod
  def FLIR_Point_Grey_Chameleon3_USB3(cls):
    return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Chameleon3_USB3'])

  @classmethod
  def FLIR_Point_Grey_Grasshopper3_USB3(cls):
    return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Grasshopper3_USB3'])

  @classmethod
  def FLIR_Point_Grey_Blackfly_S_IMX290(cls):
    return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Blackfly_S_IMX290'])

  @classmethod
  def FLIR_Point_Grey_Blackfly_S_IMX178(cls):
    return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Blackfly_S_IMX178'])

  @classmethod
  def FLIR_Point_Grey_Firefly_S(cls):
    return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Firefly_S'])

  @classmethod
  def QSI_690ws(cls):
    return cls.from_database(cls._DATABASE['QSI_690ws'])

  @classmethod
  def QSI_690wsg(cls):
    return cls.from_database(cls._DATABASE['QSI_690wsg'])

  @classmethod
  def QSI_660ws(cls):
    return cls.from_database(cls._DATABASE['QSI_660ws'])

  @classmethod
  def QSI_660wsg(cls):
    return cls.from_database(cls._DATABASE['QSI_660wsg'])

  @classmethod
  def QSI_583ws(cls):
    return cls.from_database(cls._DATABASE['QSI_583ws'])

  @classmethod
  def QSI_583wsg(cls):
    return cls.from_database(cls._DATABASE['QSI_583wsg'])

  @classmethod
  def QSI_616ws(cls):
    return cls.from_database(cls._DATABASE['QSI_616ws'])

  @classmethod
  def Atik_11000(cls):
    return cls.from_database(cls._DATABASE['Atik_11000'])

  @classmethod
  def Atik_16HR(cls):
    return cls.from_database(cls._DATABASE['Atik_16HR'])

  @classmethod
  def Atik_320E(cls):
    return cls.from_database(cls._DATABASE['Atik_320E'])

  @classmethod
  def Atik_4000(cls):
    return cls.from_database(cls._DATABASE['Atik_4000'])

  @classmethod
  def Atik_Titan_Mono(cls):
    return cls.from_database(cls._DATABASE['Atik_Titan_Mono'])

  @classmethod
  def Atik_GP_CAM3_290M(cls):
    return cls.from_database(cls._DATABASE['Atik_GP_CAM3_290M'])

  @classmethod
  def Atik_GP_CAM2_290M(cls):
    return cls.from_database(cls._DATABASE['Atik_GP_CAM2_290M'])

  @classmethod
  def Atik_VS14(cls):
    return cls.from_database(cls._DATABASE['Atik_VS14'])

  @classmethod
  def Atik_Apx60(cls):
    return cls.from_database(cls._DATABASE['Atik_Apx60'])

  @classmethod
  def Moravian_C1x_61000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C1x_61000'])

  @classmethod
  def Moravian_C1x_26000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C1x_26000'])

  @classmethod
  def Moravian_C1_5500(cls):
    return cls.from_database(cls._DATABASE['Moravian_C1_5500'])

  @classmethod
  def Moravian_C2_7000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C2_7000'])

  @classmethod
  def Moravian_C3_61000_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Moravian_C3_61000_Pro_v2'])

  @classmethod
  def Moravian_C4_20000(cls):
    return cls.from_database(cls._DATABASE['Moravian_C4_20000'])

  @classmethod
  def Moravian_C5_100000_v2(cls):
    return cls.from_database(cls._DATABASE['Moravian_C5_100000_v2'])

  @classmethod
  def QHY_QHY_990M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_990M'])

  @classmethod
  def QHY_QHY_600LM(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_600LM'])

  @classmethod
  def QHY_QHY_5200M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5200M'])

  @classmethod
  def QHY_QHY_2020M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_2020M'])

  @classmethod
  def QHY_QHY_550M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_550M'])

  @classmethod
  def QHY_QHY_174M(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_174M'])

  @classmethod
  def QHY_QHY_990C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_990C'])

  @classmethod
  def QHY_QHY_600LC(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_600LC'])

  @classmethod
  def QHY_QHY_5200C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_5200C'])

  @classmethod
  def QHY_QHY_2020C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_2020C'])

  @classmethod
  def QHY_QHY_550C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_550C'])

  @classmethod
  def QHY_QHY_174C(cls):
    return cls.from_database(cls._DATABASE['QHY_QHY_174C'])

  @classmethod
  def ZWO_ASI_533MC_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MC_Pro_v2'])

  @classmethod
  def ZWO_ASI_533MM_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_533MM_Pro_v2'])

  @classmethod
  def ZWO_ASI_2600MC_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Pro_v2'])

  @classmethod
  def ZWO_ASI_2600MM_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Pro_v2'])

  @classmethod
  def ZWO_ASI_6200MC_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200MC_Pro_v2'])

  @classmethod
  def ZWO_ASI_6200MM_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_6200MM_Pro_v2'])

  @classmethod
  def ZWO_ASI_294MC_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MC_Pro_v2'])

  @classmethod
  def ZWO_ASI_294MM_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_294MM_Pro_v2'])

  @classmethod
  def ZWO_ASI_183MC_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MC_Pro_v2'])

  @classmethod
  def ZWO_ASI_183MM_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_183MM_Pro_v2'])

  @classmethod
  def Player_One_Poseidon_C_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Poseidon_C_Pro_v2'])

  @classmethod
  def Player_One_Artemis_C_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Artemis_C_Pro_v2'])

  @classmethod
  def Player_One_Ares_C_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ares_C_Pro_v2'])

  @classmethod
  def Player_One_Zeus_C_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Zeus_C_Pro_v2'])

  @classmethod
  def Player_One_Hades_C_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Hades_C_Pro_v2'])

  @classmethod
  def Player_One_Athena_C_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Athena_C_Pro_v2'])

  @classmethod
  def Player_One_Poseidon_M_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Poseidon_M_Pro_v2'])

  @classmethod
  def Player_One_Artemis_M_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Artemis_M_Pro_v2'])

  @classmethod
  def Player_One_Ares_M_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Ares_M_Pro_v2'])

  @classmethod
  def Player_One_Zeus_M_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Zeus_M_Pro_v2'])

  @classmethod
  def Player_One_Hades_M_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Hades_M_Pro_v2'])

  @classmethod
  def Player_One_Athena_M_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Player_One_Athena_M_Pro_v2'])

  @classmethod
  def SVBony_SV705M(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV705M'])

  @classmethod
  def SVBony_SV805M(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV805M'])

  @classmethod
  def SVBony_SV905CC(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV905CC'])

  @classmethod
  def SVBony_SV405CC_v2(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV405CC_v2'])

  @classmethod
  def SVBony_SV505M_Pro(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV505M_Pro'])

  @classmethod
  def SVBony_SV605CC_v2(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV605CC_v2'])

  @classmethod
  def SVBony_SV205M(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV205M'])

  @classmethod
  def SVBony_SV305M_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV305M_Pro_v2'])

  @classmethod
  def Altair_Hypercam_26000M_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_26000M_Pro'])

  @classmethod
  def Altair_Hypercam_571M_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_571M_Pro'])

  @classmethod
  def Altair_Hypercam_533M_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_533M_Pro'])

  @classmethod
  def Altair_Hypercam_294M_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_294M_Pro'])

  @classmethod
  def Altair_Hypercam_183M_Pro_v2(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_183M_Pro_v2'])

  @classmethod
  def Altair_Hypercam_2600M_Pro(cls):
    return cls.from_database(cls._DATABASE['Altair_Hypercam_2600M_Pro'])

  @classmethod
  def OGMA_OGC_571M_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_571M_Pro'])

  @classmethod
  def OGMA_OGC_2600C(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_2600C'])

  @classmethod
  def OGMA_OGC_2600M(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_2600M'])

  @classmethod
  def OGMA_OGC_571C(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_571C'])

  @classmethod
  def OGMA_OGC_183M_Pro(cls):
    return cls.from_database(cls._DATABASE['OGMA_OGC_183M_Pro'])

  @classmethod
  def iNova_PLB_Mx2_IMX290(cls):
    return cls.from_database(cls._DATABASE['iNova_PLB_Mx2_IMX290'])

  @classmethod
  def iNova_PLB_Cx2_IMX290(cls):
    return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_IMX290'])

  @classmethod
  def iNova_PLB_Mx2_IMX178(cls):
    return cls.from_database(cls._DATABASE['iNova_PLB_Mx2_IMX178'])

  @classmethod
  def iNova_PLB_Cx2_IMX178(cls):
    return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_IMX178'])

  @classmethod
  def ZWO_ASI_715MC_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_715MC_V2'])

  @classmethod
  def ZWO_ASI_715MM_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_715MM_V2'])

  @classmethod
  def ZWO_ASI_585MC_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_585MC_V2'])

  @classmethod
  def ZWO_ASI_585MM_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_585MM_V2'])

  @classmethod
  def ZWO_ASI_662MC_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_662MC_V2'])

  @classmethod
  def ZWO_ASI_662MM_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_662MM_V2'])

  @classmethod
  def ZWO_ASI_678MC_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_678MC_V2'])

  @classmethod
  def ZWO_ASI_678MM_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_678MM_V2'])

  @classmethod
  def ZWO_ASI_482MC_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_482MC_V2'])

  @classmethod
  def ZWO_ASI_482MM_V2(cls):
    return cls.from_database(cls._DATABASE['ZWO_ASI_482MM_V2'])
