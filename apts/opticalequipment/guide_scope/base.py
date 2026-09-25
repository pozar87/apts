from ...constants import OpticalType
from ..telescope import Telescope
from .calculations import normalize_guide_scope_database_entry


class GuideScope(Telescope):
    @classmethod
    def from_database(cls, entry):
        normalized = normalize_guide_scope_database_entry(entry)
        return cls(
            normalized["aperture"],
            normalized["focal_length"],
            vendor=normalized["vendor"],
            outputs=normalized["outputs"],
            backfocus=normalized["backfocus"],
            mass=normalized["mass"],
            optical_length=normalized["optical_length"],
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
        super().__init__(
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
