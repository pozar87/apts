from .abstract import OpticalEquipment
from ..utils import ConnectionType, Gender


class Barlow(OpticalEquipment):
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
    ct = Utils.map_conn(entry.get("cside_thread"))
    cg = Utils.map_gender(entry.get("cside_gender"))
    mag = Utils.extract_number(name, prefix="x") or 2.0
    return cls(
      mag, vendor=vendor, connection_type=tt,
      in_gender=tg or Gender.MALE, out_gender=cg or Gender.FEMALE,
      mass=mass, optical_length=ol
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
    ct = Utils.map_conn(entry.get("cside_thread"))
    cg = Utils.map_gender(entry.get("cside_gender"))
    mag = Utils.extract_number(name, prefix="x") or 2.0
    return cls(
      mag, vendor=vendor, connection_type=tt,
      in_gender=tg or Gender.MALE, out_gender=cg or Gender.FEMALE,
      mass=mass, optical_length=ol
    )
  """
  Class representing Barlow lenses
  """

  def __init__(self, magnification, vendor="unknown barlow", connection_type=ConnectionType.F_1_25, in_gender=Gender.MALE, out_gender=Gender.FEMALE, t2_output=False, mass=0, optical_length=0):
    super(Barlow, self).__init__(0, vendor, mass=mass, optical_length=optical_length)
    self.connection_type = connection_type
    self.in_gender = in_gender
    self.out_gender = out_gender
    self.t2_output = t2_output
    self.magnification = magnification

  def register(self, equipment):
    """
    Register barlow lens in optical equipment graph. Barlow node is build out of three vertices:
    barlow node its input and output. Barlow node is automatically connected with them.
    """
    # Add barlow lens node
    super(Barlow, self)._register(equipment)
    # Add barlow lens output node and connect it to barlow lens
    self._register_output(equipment, self.connection_type, self.out_gender)
    # Add barlow lens input node and connect it to barlow lens
    self._register_input(equipment, self.connection_type, self.in_gender)
    # Handling optional T2 output
    if self.t2_output:
      self._register_output(equipment, ConnectionType.T2)

  def __str__(self):
    # Format: <vendor> x<magnification>
    return "{} x{}".format(self.get_vendor(), self.magnification)

  _DATABASE = {
    'Takahashi_Extender_Q_1_6x': {'brand': 'Takahashi', 'name': 'Extender-Q 1.6x', 'type': 'type_extender', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
    'Takahashi_Extender_CQ_1_7x': {'brand': 'Takahashi', 'name': 'Extender-CQ 1.7x', 'type': 'type_extender', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_Powermate_2x_1_25': {'brand': 'TeleVue', 'name': 'Powermate 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_Powermate_2_5x_1_25': {'brand': 'TeleVue', 'name': 'Powermate 2.5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_Powermate_4x_1_25': {'brand': 'TeleVue', 'name': 'Powermate 4x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_Powermate_5x_1_25': {'brand': 'TeleVue', 'name': 'Powermate 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_Big_Barlow_2x_2': {'brand': 'TeleVue', 'name': 'Big Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 310, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_Powermate_2x_2': {'brand': 'TeleVue', 'name': 'Powermate 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 310, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_Powermate_4x_2': {'brand': 'TeleVue', 'name': 'Powermate 4x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 310, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Baader_VIP_Barlow_2_25x': {'brand': 'Baader', 'name': 'VIP Barlow 2.25x', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Baader_1_3x_GPC_M48': {'brand': 'Baader', 'name': '1.3x GPC (M48)', 'type': 'type_barlow', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Baader_Q_Barlow_2_25x_1_25': {'brand': 'Baader', 'name': 'Q-Barlow 2.25x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Explore_Scientific_Focal_Extender_2x_1_25': {'brand': 'Explore Scientific', 'name': 'Focal Extender 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Explore_Scientific_Focal_Extender_3x_1_25': {'brand': 'Explore Scientific', 'name': 'Focal Extender 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Explore_Scientific_Focal_Extender_5x_1_25': {'brand': 'Explore Scientific', 'name': 'Focal Extender 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Explore_Scientific_2x_Focal_Extender_2': {'brand': 'Explore Scientific', 'name': '2x Focal Extender (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 300, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Celestron_Ultima_Barlow_2x_1_25': {'brand': 'Celestron', 'name': 'Ultima Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Celestron_Ultima_Barlow_3x_1_25': {'brand': 'Celestron', 'name': 'Ultima Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Celestron_Ultima_Barlow_5x_1_25': {'brand': 'Celestron', 'name': 'Ultima Barlow 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Celestron_Ultima_Barlow_2x_2': {'brand': 'Celestron', 'name': 'Ultima Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 250, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Celestron_X_Cel_LX_2x_Barlow': {'brand': 'Celestron', 'name': 'X-Cel LX 2x Barlow', 'type': 'type_barlow', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Celestron_X_Cel_LX_3x_Barlow': {'brand': 'Celestron', 'name': 'X-Cel LX 3x Barlow', 'type': 'type_barlow', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Meade_126_2x_Barlow': {'brand': 'Meade', 'name': '#126 2x Barlow', 'type': 'type_barlow', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Meade_140_2x_Barlow_2': {'brand': 'Meade', 'name': '#140 2x Barlow (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 250, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Sky_Watcher_2x_Deluxe_Barlow_1_25': {'brand': 'Sky-Watcher', 'name': '2x Deluxe Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Sky_Watcher_2x_Deluxe_Barlow_2': {'brand': 'Sky-Watcher', 'name': '2x Deluxe Barlow (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 240, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Orion_Shorty_2x_Barlow': {'brand': 'Orion', 'name': 'Shorty 2x Barlow', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Orion_2x_Shorty_Plus_Barlow_2': {'brand': 'Orion', 'name': '2x Shorty Plus Barlow (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 230, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'SVBony_SV137_2x_Barlow': {'brand': 'SVBony', 'name': 'SV137 2x Barlow', 'type': 'type_barlow', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'GSO_2x_Barlow_1_25': {'brand': 'GSO', 'name': '2x Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'GSO_2x_Barlow_2': {'brand': 'GSO', 'name': '2x Barlow (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 200, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Generic_Barlow_2x_1_25': {'brand': 'Generic', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Generic_Barlow_3x_1_25': {'brand': 'Generic', 'name': 'Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Generic_Barlow_5x_1_25': {'brand': 'Generic', 'name': 'Barlow 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Generic_Barlow_2x_2': {'brand': 'Generic', 'name': 'Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 200, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Omegon_2x_ED_Barlow_1_25': {'brand': 'Omegon', 'name': '2x ED Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Bresser_2x_Barlow_1_25': {'brand': 'Bresser', 'name': '2x Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'William_Optics_Barlow_2x_1_25': {'brand': 'William Optics', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'APM_Comacorr_2x_Barlow_M48': {'brand': 'APM', 'name': 'Comacorr 2x Barlow (M48)', 'type': 'type_barlow', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Lacerta_2x_ED_Barlow_1_25': {'brand': 'Lacerta', 'name': '2x ED Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Saxon_2x_Barlow_1_25': {'brand': 'Saxon', 'name': '2x Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'National_Geographic_2x_Barlow_1_25': {'brand': 'National Geographic', 'name': '2x Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 70, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Vixen_2x_Barlow_1_25': {'brand': 'Vixen', 'name': '2x Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Vixen_2x_Barlow_2': {'brand': 'Vixen', 'name': '2x Barlow (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 220, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Takahashi_2x_Extender_Q_1_25': {'brand': 'Takahashi', 'name': '2x Extender-Q (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'APM_2x_ED_Barlow_1_25': {'brand': 'APM', 'name': '2x ED Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Omegon_3x_Barlow_1_25': {'brand': 'Omegon', 'name': '3x Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Bresser_3x_Barlow_1_25': {'brand': 'Bresser', 'name': '3x Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TS_Optics_2_5x_ED_Barlow_1_25': {'brand': 'TS-Optics', 'name': '2.5x ED Barlow (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TS_Optics_2x_Barlow_2': {'brand': 'TS-Optics', 'name': '2x Barlow (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 230, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Takahashi_Extender_C_2_27x': {'brand': 'Takahashi', 'name': 'Extender C 2.27x', 'type': 'type_extender', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
    'Takahashi_Extender_EX_1_5x': {'brand': 'Takahashi', 'name': 'Extender EX 1.5x', 'type': 'type_extender', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_2x_Extender_1_25': {'brand': 'TeleVue', 'name': '2x Extender (1.25")', 'type': 'type_extender', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TeleVue_2x_Extender_2': {'brand': 'TeleVue', 'name': '2x Extender (2")', 'type': 'type_extender', 'optical_length': 0, 'mass': 310, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Celestron_2x_Extender': {'brand': 'Celestron', 'name': '2x Extender', 'type': 'type_extender', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Sky_Watcher_2x_ED_Extender': {'brand': 'Sky-Watcher', 'name': '2x ED Extender', 'type': 'type_extender', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Antares_Barlow_1_5x_1_25': {'brand': 'Antares', 'name': 'Barlow 1.5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Antares_Barlow_2x_1_25': {'brand': 'Antares', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Antares_Barlow_3x_1_25': {'brand': 'Antares', 'name': 'Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Antares_Barlow_5x_1_25': {'brand': 'Antares', 'name': 'Barlow 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Lacerta_Barlow_2x_1_25': {'brand': 'Lacerta', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Lacerta_Barlow_2_5x_1_25': {'brand': 'Lacerta', 'name': 'Barlow 2.5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Lacerta_Barlow_3x_1_25': {'brand': 'Lacerta', 'name': 'Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Lacerta_Barlow_5x_1_25': {'brand': 'Lacerta', 'name': 'Barlow 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Lacerta_Barlow_2x_2': {'brand': 'Lacerta', 'name': 'Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 220, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Vixen_Barlow_2x_1_25': {'brand': 'Vixen', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Vixen_Barlow_2_5x_1_25': {'brand': 'Vixen', 'name': 'Barlow 2.5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Takahashi_Barlow_2x_1_25': {'brand': 'Takahashi', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Takahashi_Barlow_1_6x_M42': {'brand': 'Takahashi', 'name': 'Barlow 1.6x (M42)', 'type': 'type_barlow', 'optical_length': 0, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'APM_ED_Barlow_1_5x_1_25': {'brand': 'APM', 'name': 'ED Barlow 1.5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'APM_ED_Barlow_2x_1_25': {'brand': 'APM', 'name': 'ED Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'APM_ED_Barlow_2_5x_1_25': {'brand': 'APM', 'name': 'ED Barlow 2.5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'APM_ED_Barlow_3x_1_25': {'brand': 'APM', 'name': 'ED Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'APM_ED_Barlow_2x_2': {'brand': 'APM', 'name': 'ED Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 260, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Stellarvue_Barlow_2x_1_25': {'brand': 'Stellarvue', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Stellarvue_Barlow_2x_2': {'brand': 'Stellarvue', 'name': 'Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 250, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TS_Optics_Barlow_2x_1_25': {'brand': 'TS-Optics', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TS_Optics_Barlow_2_5x_1_25': {'brand': 'TS-Optics', 'name': 'Barlow 2.5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TS_Optics_Barlow_3x_1_25': {'brand': 'TS-Optics', 'name': 'Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TS_Optics_Barlow_5x_1_25': {'brand': 'TS-Optics', 'name': 'Barlow 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'TS_Optics_Barlow_2x_2': {'brand': 'TS-Optics', 'name': 'Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 230, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Datyson_Barlow_2x_1_25': {'brand': 'Datyson', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Datyson_Barlow_3x_1_25': {'brand': 'Datyson', 'name': 'Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Datyson_Barlow_5x_1_25': {'brand': 'Datyson', 'name': 'Barlow 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Altair_ED_Barlow_2x_1_25': {'brand': 'Altair', 'name': 'ED Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Altair_ED_Barlow_2x_2': {'brand': 'Altair', 'name': 'ED Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 240, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Altair_Barlow_3x_1_25': {'brand': 'Altair', 'name': 'Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Omegon_Barlow_2x_1_25': {'brand': 'Omegon', 'name': 'Barlow 2x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Omegon_Barlow_3x_1_25': {'brand': 'Omegon', 'name': 'Barlow 3x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Omegon_Barlow_5x_1_25': {'brand': 'Omegon', 'name': 'Barlow 5x (1.25")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Omegon_Barlow_2x_2': {'brand': 'Omegon', 'name': 'Barlow 2x (2")', 'type': 'type_barlow', 'optical_length': 0, 'mass': 220, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Baader_Mark_III_2x_Shorty_Barlow': {'brand': 'Baader', 'name': 'Mark III 2x Shorty Barlow', 'type': 'type_barlow', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
    'Baader_2x_Barlow_M48': {'brand': 'Baader', 'name': '2x Barlow (M48)', 'type': 'type_barlow', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': 'start'},
  }

  @classmethod
  def Takahashi_Extender_Q_1_6x(cls):
    return cls.from_database(cls._DATABASE['Takahashi_Extender_Q_1_6x'])

  @classmethod
  def Takahashi_Extender_CQ_1_7x(cls):
    return cls.from_database(cls._DATABASE['Takahashi_Extender_CQ_1_7x'])

  @classmethod
  def TeleVue_Powermate_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['TeleVue_Powermate_2x_1_25'])

  @classmethod
  def TeleVue_Powermate_2_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['TeleVue_Powermate_2_5x_1_25'])

  @classmethod
  def TeleVue_Powermate_4x_1_25(cls):
    return cls.from_database(cls._DATABASE['TeleVue_Powermate_4x_1_25'])

  @classmethod
  def TeleVue_Powermate_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['TeleVue_Powermate_5x_1_25'])

  @classmethod
  def TeleVue_Big_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['TeleVue_Big_Barlow_2x_2'])

  @classmethod
  def TeleVue_Powermate_2x_2(cls):
    return cls.from_database(cls._DATABASE['TeleVue_Powermate_2x_2'])

  @classmethod
  def TeleVue_Powermate_4x_2(cls):
    return cls.from_database(cls._DATABASE['TeleVue_Powermate_4x_2'])

  @classmethod
  def Baader_VIP_Barlow_2_25x(cls):
    return cls.from_database(cls._DATABASE['Baader_VIP_Barlow_2_25x'])

  @classmethod
  def Baader_1_3x_GPC_M48(cls):
    return cls.from_database(cls._DATABASE['Baader_1_3x_GPC_M48'])

  @classmethod
  def Baader_Q_Barlow_2_25x_1_25(cls):
    return cls.from_database(cls._DATABASE['Baader_Q_Barlow_2_25x_1_25'])

  @classmethod
  def Explore_Scientific_Focal_Extender_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_Focal_Extender_2x_1_25'])

  @classmethod
  def Explore_Scientific_Focal_Extender_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_Focal_Extender_3x_1_25'])

  @classmethod
  def Explore_Scientific_Focal_Extender_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_Focal_Extender_5x_1_25'])

  @classmethod
  def Explore_Scientific_2x_Focal_Extender_2(cls):
    return cls.from_database(cls._DATABASE['Explore_Scientific_2x_Focal_Extender_2'])

  @classmethod
  def Celestron_Ultima_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Celestron_Ultima_Barlow_2x_1_25'])

  @classmethod
  def Celestron_Ultima_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['Celestron_Ultima_Barlow_3x_1_25'])

  @classmethod
  def Celestron_Ultima_Barlow_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Celestron_Ultima_Barlow_5x_1_25'])

  @classmethod
  def Celestron_Ultima_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['Celestron_Ultima_Barlow_2x_2'])

  @classmethod
  def Celestron_X_Cel_LX_2x_Barlow(cls):
    return cls.from_database(cls._DATABASE['Celestron_X_Cel_LX_2x_Barlow'])

  @classmethod
  def Celestron_X_Cel_LX_3x_Barlow(cls):
    return cls.from_database(cls._DATABASE['Celestron_X_Cel_LX_3x_Barlow'])

  @classmethod
  def Meade_126_2x_Barlow(cls):
    return cls.from_database(cls._DATABASE['Meade_126_2x_Barlow'])

  @classmethod
  def Meade_140_2x_Barlow_2(cls):
    return cls.from_database(cls._DATABASE['Meade_140_2x_Barlow_2'])

  @classmethod
  def Sky_Watcher_2x_Deluxe_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['Sky_Watcher_2x_Deluxe_Barlow_1_25'])

  @classmethod
  def Sky_Watcher_2x_Deluxe_Barlow_2(cls):
    return cls.from_database(cls._DATABASE['Sky_Watcher_2x_Deluxe_Barlow_2'])

  @classmethod
  def Orion_Shorty_2x_Barlow(cls):
    return cls.from_database(cls._DATABASE['Orion_Shorty_2x_Barlow'])

  @classmethod
  def Orion_2x_Shorty_Plus_Barlow_2(cls):
    return cls.from_database(cls._DATABASE['Orion_2x_Shorty_Plus_Barlow_2'])

  @classmethod
  def SVBony_SV137_2x_Barlow(cls):
    return cls.from_database(cls._DATABASE['SVBony_SV137_2x_Barlow'])

  @classmethod
  def GSO_2x_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['GSO_2x_Barlow_1_25'])

  @classmethod
  def GSO_2x_Barlow_2(cls):
    return cls.from_database(cls._DATABASE['GSO_2x_Barlow_2'])

  @classmethod
  def Generic_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Generic_Barlow_2x_1_25'])

  @classmethod
  def Generic_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['Generic_Barlow_3x_1_25'])

  @classmethod
  def Generic_Barlow_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Generic_Barlow_5x_1_25'])

  @classmethod
  def Generic_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['Generic_Barlow_2x_2'])

  @classmethod
  def Omegon_2x_ED_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['Omegon_2x_ED_Barlow_1_25'])

  @classmethod
  def Bresser_2x_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['Bresser_2x_Barlow_1_25'])

  @classmethod
  def William_Optics_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['William_Optics_Barlow_2x_1_25'])

  @classmethod
  def APM_Comacorr_2x_Barlow_M48(cls):
    return cls.from_database(cls._DATABASE['APM_Comacorr_2x_Barlow_M48'])

  @classmethod
  def Lacerta_2x_ED_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['Lacerta_2x_ED_Barlow_1_25'])

  @classmethod
  def Saxon_2x_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['Saxon_2x_Barlow_1_25'])

  @classmethod
  def National_Geographic_2x_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['National_Geographic_2x_Barlow_1_25'])

  @classmethod
  def Vixen_2x_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['Vixen_2x_Barlow_1_25'])

  @classmethod
  def Vixen_2x_Barlow_2(cls):
    return cls.from_database(cls._DATABASE['Vixen_2x_Barlow_2'])

  @classmethod
  def Takahashi_2x_Extender_Q_1_25(cls):
    return cls.from_database(cls._DATABASE['Takahashi_2x_Extender_Q_1_25'])

  @classmethod
  def APM_2x_ED_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['APM_2x_ED_Barlow_1_25'])

  @classmethod
  def Omegon_3x_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['Omegon_3x_Barlow_1_25'])

  @classmethod
  def Bresser_3x_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['Bresser_3x_Barlow_1_25'])

  @classmethod
  def TS_Optics_2_5x_ED_Barlow_1_25(cls):
    return cls.from_database(cls._DATABASE['TS_Optics_2_5x_ED_Barlow_1_25'])

  @classmethod
  def TS_Optics_2x_Barlow_2(cls):
    return cls.from_database(cls._DATABASE['TS_Optics_2x_Barlow_2'])

  @classmethod
  def Takahashi_Extender_C_2_27x(cls):
    return cls.from_database(cls._DATABASE['Takahashi_Extender_C_2_27x'])

  @classmethod
  def Takahashi_Extender_EX_1_5x(cls):
    return cls.from_database(cls._DATABASE['Takahashi_Extender_EX_1_5x'])

  @classmethod
  def TeleVue_2x_Extender_1_25(cls):
    return cls.from_database(cls._DATABASE['TeleVue_2x_Extender_1_25'])

  @classmethod
  def TeleVue_2x_Extender_2(cls):
    return cls.from_database(cls._DATABASE['TeleVue_2x_Extender_2'])

  @classmethod
  def Celestron_2x_Extender(cls):
    return cls.from_database(cls._DATABASE['Celestron_2x_Extender'])

  @classmethod
  def Sky_Watcher_2x_ED_Extender(cls):
    return cls.from_database(cls._DATABASE['Sky_Watcher_2x_ED_Extender'])

  @classmethod
  def Antares_Barlow_1_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Antares_Barlow_1_5x_1_25'])

  @classmethod
  def Antares_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Antares_Barlow_2x_1_25'])

  @classmethod
  def Antares_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['Antares_Barlow_3x_1_25'])

  @classmethod
  def Antares_Barlow_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Antares_Barlow_5x_1_25'])

  @classmethod
  def Lacerta_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Lacerta_Barlow_2x_1_25'])

  @classmethod
  def Lacerta_Barlow_2_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Lacerta_Barlow_2_5x_1_25'])

  @classmethod
  def Lacerta_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['Lacerta_Barlow_3x_1_25'])

  @classmethod
  def Lacerta_Barlow_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Lacerta_Barlow_5x_1_25'])

  @classmethod
  def Lacerta_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['Lacerta_Barlow_2x_2'])

  @classmethod
  def Vixen_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Vixen_Barlow_2x_1_25'])

  @classmethod
  def Vixen_Barlow_2_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Vixen_Barlow_2_5x_1_25'])

  @classmethod
  def Takahashi_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Takahashi_Barlow_2x_1_25'])

  @classmethod
  def Takahashi_Barlow_1_6x_M42(cls):
    return cls.from_database(cls._DATABASE['Takahashi_Barlow_1_6x_M42'])

  @classmethod
  def APM_ED_Barlow_1_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['APM_ED_Barlow_1_5x_1_25'])

  @classmethod
  def APM_ED_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['APM_ED_Barlow_2x_1_25'])

  @classmethod
  def APM_ED_Barlow_2_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['APM_ED_Barlow_2_5x_1_25'])

  @classmethod
  def APM_ED_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['APM_ED_Barlow_3x_1_25'])

  @classmethod
  def APM_ED_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['APM_ED_Barlow_2x_2'])

  @classmethod
  def Stellarvue_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Stellarvue_Barlow_2x_1_25'])

  @classmethod
  def Stellarvue_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['Stellarvue_Barlow_2x_2'])

  @classmethod
  def TS_Optics_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['TS_Optics_Barlow_2x_1_25'])

  @classmethod
  def TS_Optics_Barlow_2_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['TS_Optics_Barlow_2_5x_1_25'])

  @classmethod
  def TS_Optics_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['TS_Optics_Barlow_3x_1_25'])

  @classmethod
  def TS_Optics_Barlow_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['TS_Optics_Barlow_5x_1_25'])

  @classmethod
  def TS_Optics_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['TS_Optics_Barlow_2x_2'])

  @classmethod
  def Datyson_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Datyson_Barlow_2x_1_25'])

  @classmethod
  def Datyson_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['Datyson_Barlow_3x_1_25'])

  @classmethod
  def Datyson_Barlow_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Datyson_Barlow_5x_1_25'])

  @classmethod
  def Altair_ED_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Altair_ED_Barlow_2x_1_25'])

  @classmethod
  def Altair_ED_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['Altair_ED_Barlow_2x_2'])

  @classmethod
  def Altair_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['Altair_Barlow_3x_1_25'])

  @classmethod
  def Omegon_Barlow_2x_1_25(cls):
    return cls.from_database(cls._DATABASE['Omegon_Barlow_2x_1_25'])

  @classmethod
  def Omegon_Barlow_3x_1_25(cls):
    return cls.from_database(cls._DATABASE['Omegon_Barlow_3x_1_25'])

  @classmethod
  def Omegon_Barlow_5x_1_25(cls):
    return cls.from_database(cls._DATABASE['Omegon_Barlow_5x_1_25'])

  @classmethod
  def Omegon_Barlow_2x_2(cls):
    return cls.from_database(cls._DATABASE['Omegon_Barlow_2x_2'])

  @classmethod
  def Baader_Mark_III_2x_Shorty_Barlow(cls):
    return cls.from_database(cls._DATABASE['Baader_Mark_III_2x_Shorty_Barlow'])

  @classmethod
  def Baader_2x_Barlow_M48(cls):
    return cls.from_database(cls._DATABASE['Baader_2x_Barlow_M48'])
