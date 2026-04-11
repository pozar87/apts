from ..telescope import Telescope
from ...constants import OpticalType
from ...utils import ConnectionType, Gender


class GuideScope(Telescope):
    @classmethod
    def from_database(cls, entry):
        from ...utils import Utils, Gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        ct = Utils.map_conn(entry.get("cside_thread"))
        cg = Utils.map_gender(entry.get("cside_gender"))
        aperture, focal_length = Utils.guess_optical_properties(name)
        bf_val = entry.get("bf_role") == "start"
        return cls(
            aperture or 30,
            focal_length or 120,
            vendor=vendor,
            connection_type=ct,
            connection_gender=cg or Gender.FEMALE,
            backfocus=ol if bf_val else None,
            mass=mass,
            optical_length=ol,
        )

    def __init__(
        self,
        aperture,
        focal_length,
        vendor="unknown guide scope",
        connection_type=ConnectionType.F_1_25,
        connection_gender=Gender.FEMALE,
        backfocus=None,
        mass=0,
        optical_length=0,
    ):
        super(GuideScope, self).__init__(
            aperture,
            focal_length,
            vendor,
            connection_type=connection_type,
            connection_gender=connection_gender,
            backfocus=backfocus,
            mass=mass,
            optical_length=optical_length,
        )
        self._type = OpticalType.GUIDE_SCOPE

    _DATABASE = {}
