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
        from ...utils import map_conn, map_gender, extract_number

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        tt = map_conn(entry.get("tside_thread"))
        tg = map_gender(entry.get("tside_gender"))
        ct = map_conn(entry.get("cside_thread"))
        cg = map_gender(entry.get("cside_gender"))
        mag = extract_number(name, prefix="x") or 2.0

        inputs = entry.get("inputs")
        if inputs is None:
            inputs = [(tt, tg)] if tt else []
        else:
            from ...utils import map_conn, map_gender
            inputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in inputs]

        outputs = entry.get("outputs")
        if outputs is None:
            outputs = [(ct, cg)] if ct else []
            if entry.get("t2_output", False):
                from ...utils import Gender
                outputs.append((ConnectionType.T2, Gender.MALE))
        else:
            from ...utils import map_conn, map_gender
            outputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in outputs]

        return cls(
            mag,
            vendor=vendor,
            inputs=inputs,
            outputs=outputs,
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
        inputs=None,
        outputs=None,
        mass=0.0,
        optical_length=0.0,
        connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        if inputs is None:
            if connection_type:
                inputs = [(connection_type, in_gender)]
            else:
                inputs = [ConnectionType.F_1_25]
        if outputs is None:
            if connection_type:
                outputs = [(connection_type, out_gender)]
            else:
                outputs = [ConnectionType.F_1_25]

        super(Barlow, self).__init__(
            0,
            vendor,
            mass=mass,
            optical_length=optical_length,
            inputs=inputs,
            outputs=outputs,
        )
        self.magnification = magnification

    @property
    def connection_type(self):
        return self._inputs[0][0] if self._inputs else None

    @property
    def in_gender(self):
        return self._inputs[0][1] if self._inputs else None

    @property
    def out_gender(self):
        return self._outputs[0][1] if self._outputs else None

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
