from typing import TYPE_CHECKING, Any, Sequence

if TYPE_CHECKING:
    pass

from .models.atmospheric import AtmosphericMixIn
from .models.exposure import ExposureMixIn
from .models.geometric import GeometricMixIn
from .models.mechanical import MechanicalMixIn
from .models.photometry import PhotometryMixIn
from .models.planetary import PlanetaryMixIn
from .models.resolution import ResolutionMixIn
from .utils import OpticsUtils


class OpticalPath(
    AtmosphericMixIn,
    PhotometryMixIn,
    ExposureMixIn,
    PlanetaryMixIn,
    GeometricMixIn,
    ResolutionMixIn,
    MechanicalMixIn,
):
    """
    Class representing an optical path in a telescope setup.
    """

    def __init__(
        self,
        telescope,
        barlows: Sequence[Any],
        diagonals,
        filters: Sequence[Any],
        others,
        output=None,
        path=None,
    ):
        self.telescope = telescope
        self.barlows = list(barlows)
        self.diagonals = diagonals
        self.filters = list(filters)
        if output is None:
            # Handle 5-argument constructor calls for backward compatibility
            self.others = []
            self.output = others
        else:
            self.others = others
            self.output = output
        # Store original path to preserve physical order
        self._path = list(path) if path is not None else None
        # Cache for expensive calculations
        self._cache = {}

    @classmethod
    def from_path(cls, path):
        telescope, barlows, diagonals, filters, others, output = OpticsUtils.expand(
            path
        )
        return cls(telescope, barlows, diagonals, filters, others, output, path=path)

    def elements(self) -> frozenset[Any]:
        """
        Return immutable set of elements - used for removing redundant optical paths
        """
        return frozenset(self.component_list())

    def component_list(self) -> list[Any]:
        """
        Return ordered list of all optical components in the path.
        """
        from ..opticalequipment.binoculars import Binoculars
        from ..opticalequipment.naked_eye import NakedEye
        from ..opticalequipment.smart_telescope import SmartTelescope

        if self._path is not None:
            return self._path

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return [self.telescope]

        return (
            [self.telescope]
            + self.barlows
            + self.diagonals
            + self.filters
            + self.others
            + [self.output]
        )
