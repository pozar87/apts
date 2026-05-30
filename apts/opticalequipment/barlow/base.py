from ..abstract import OpticalEquipment
from ...utils import ConnectionType, Gender


class Barlow(OpticalEquipment):
    @classmethod 
    def normalize_database_entry(cls, entry: dict) -> dict: 
        from ...utils import extract_number
        entry = entry.copy() 
        name = entry.get("name", "") 
        if "magnification" not in entry:
            mag = extract_number(name, prefix="x")
            if mag:
                entry["magnification"] = mag
        return super(Barlow, cls).normalize_database_entry(entry)

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender, extract_number, Gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        tt = map_conn(entry.get("tside_thread"))
        tg = map_gender(entry.get("tside_gender"))
        map_conn(entry.get("cside_thread"))
        cg = map_gender(entry.get("cside_gender"))
        mag = extract_number(name, prefix="x") or 2.0
        t2_out = entry.get("t2_output", False)
        return cls(
            mag,
            vendor=vendor,
            connection_type=tt,
            in_gender=tg or Gender.MALE,
            out_gender=cg or Gender.FEMALE,
            t2_output=t2_out,
            mass=mass,
            optical_length=ol,
        )

    """
  Class representing Barlow lenses
  """

    path_layer = 2

    def __init__(
        self,
        magnification,
        vendor="unknown barlow",
        connection_type=ConnectionType.F_1_25,
        in_gender=Gender.MALE,
        out_gender=Gender.FEMALE,
        t2_output=False,
        mass=0.0,
        optical_length=0.0,
    ):
        super(Barlow, self).__init__(
            0, vendor, mass=mass, optical_length=optical_length
        )
        self.connection_type = connection_type
        self.in_gender = in_gender
        self.out_gender = out_gender
        self.t2_output = t2_output
        self.magnification = magnification

        self.add_input(self.connection_type, self.in_gender)
        self.add_output(self.connection_type, self.out_gender)
        if self.t2_output:
            self.add_output(ConnectionType.T2, Gender.MALE)

    def register(self, equipment):
        """
        Register barlow lens in optical equipment graph. Barlow node is build out of three vertices:
        barlow node its input and output. Barlow node is automatically connected with them.
        """
        # Add barlow lens node
        super(Barlow, self).register(equipment)

    def __str__(self):
        # Format: <vendor> x<magnification>
        return "{} x{}".format(self.get_vendor(), self.magnification)

    _DATABASE = {}
