from ..telescope import Telescope
from ...constants import OpticalType
from ...utils import ConnectionType, Gender


class GuideScope(Telescope):
    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender, guess_optical_properties

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        ct = map_conn(entry.get("cside_thread"))
        cg = map_gender(entry.get("cside_gender"))
        aperture, focal_length = guess_optical_properties(name)
        bf_val = entry.get("bf_role") == "start"
        outputs = [(ct, cg)] if ct else []
        return cls(
            aperture or 30,
            focal_length or 120,
            vendor=vendor,
            outputs=outputs,
            backfocus=ol if bf_val else None,
            mass=mass,
            optical_length=ol,
        )

    def __init__(
        self,
        aperture,
        focal_length,
        vendor="unknown guide scope",
        outputs=None,
        backfocus=None,
        mass=0,
        optical_length=0,
    ):
        super(GuideScope, self).__init__(
            aperture,
            focal_length,
            vendor,
            outputs=outputs,
            backfocus=backfocus,
            mass=mass,
            optical_length=optical_length,
        )
        self._type = OpticalType.GUIDE_SCOPE

    _DATABASE = {}
