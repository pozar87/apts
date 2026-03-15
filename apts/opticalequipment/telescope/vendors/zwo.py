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
            'mass': 2500,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 12000
        },
        'ZWO_Seestar_S30': {
            'brand': 'ZWO',
            'name': 'Seestar S30',
            'type': 'type_smart_telescope',
            'aperture': 30,
            'focal_length': 150,
            'sensor_width': 5.57,
            'sensor_height': 3.13,
            'width': 1920,
            'height': 1080,
            'mass': 1650,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.8,
            'full_well_e': 54000
        },
        'ZWO_Seestar_S30_Pro': {
            'brand': 'ZWO',
            'name': 'Seestar S30 Pro',
            'type': 'type_smart_telescope',
            'aperture': 30,
            'focal_length': 160,
            'sensor_width': 11.14,
            'sensor_height': 6.26,
            'width': 3840,
            'height': 2160,
            'mass': 1650,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.7,
            'full_well_e': 54000
        }
    }

    @classmethod
    def ZWO_Seestar_S50(cls):
        from ...smart_telescope import SmartTelescope
        return SmartTelescope.from_database(cls._DATABASE['ZWO_Seestar_S50'])

    @classmethod
    def ZWO_Seestar_S30(cls):
        from ...smart_telescope import SmartTelescope
        return SmartTelescope.from_database(cls._DATABASE['ZWO_Seestar_S30'])

    @classmethod
    def ZWO_Seestar_S30_Pro(cls):
        from ...smart_telescope import SmartTelescope
        return SmartTelescope.from_database(cls._DATABASE['ZWO_Seestar_S30_Pro'])
