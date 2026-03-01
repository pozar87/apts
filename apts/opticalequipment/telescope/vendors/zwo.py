from ..base import Telescope

class ZwoTelescope(Telescope):
    _DATABASE = {
        'ZWO_Seestar_S50': {
            'brand': 'ZWO',
            'name': 'Seestar S50',
            'type': 'type_smart_telescope',
            'aperture': 50,
            'focal_length': 250,
            'sensor_width': 5.6,
            'sensor_height': 3.2,
            'width': 1920,
            'height': 1080,
            'mass': 2500
        }
    }

    @classmethod
    def ZWO_Seestar_S50(cls):
        from ...smart_telescope import SmartTelescope
        return SmartTelescope.from_database(cls._DATABASE['ZWO_Seestar_S50'])
