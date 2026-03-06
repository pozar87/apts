from ..base import Telescope

class DwarfLabTelescope(Telescope):
    _DATABASE = {
        'DwarfLab_Dwarf_II': {
            'brand': 'DwarfLab',
            'name': 'Dwarf II',
            'type': 'type_smart_telescope',
            'aperture': 24,
            'focal_length': 100,
            'sensor_width': 5.568,
            'sensor_height': 3.132,
            'width': 3840,
            'height': 2160,
            'mass': 1200,
            'pixel_size_um': 1.45,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0
        },
        'DwarfLab_Dwarf_3': {
            'brand': 'DwarfLab',
            'name': 'Dwarf 3',
            'type': 'type_smart_telescope',
            'aperture': 35,
            'focal_length': 150,
            'sensor_width': 7.68,
            'sensor_height': 4.32,
            'width': 3840,
            'height': 2160,
            'mass': 1350,
            'pixel_size_um': 2.0,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 0.6
        }
    }

    @classmethod
    def DwarfLab_Dwarf_II(cls):
        from ...smart_telescope import SmartTelescope
        return SmartTelescope.from_database(cls._DATABASE['DwarfLab_Dwarf_II'])

    @classmethod
    def DwarfLab_Dwarf_3(cls):
        from ...smart_telescope import SmartTelescope
        return SmartTelescope.from_database(cls._DATABASE['DwarfLab_Dwarf_3'])
