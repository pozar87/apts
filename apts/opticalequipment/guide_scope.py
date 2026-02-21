from .telescope import Telescope
from ..constants import OpticalType

class GuideScope(Telescope):
    def __init__(self, aperture, focal_length, vendor="unknown guide scope", connection_type=None, connection_gender=None, mass=0, optical_length=0):
        super(GuideScope, self).__init__(aperture, focal_length, vendor, connection_type=connection_type, connection_gender=connection_gender, mass=mass, optical_length=optical_length)
        self._type = OpticalType.GUIDE_SCOPE
