from ..base import Telescope

class VixenTelescope(Telescope):
    _DATABASE = {
        'Vixen_VC200L': {'brand': 'Vixen', 'name': 'VC200L', 'type': 'catadioptric', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M60', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 1800, 'central_obstruction_mm': 75},
        'Vixen_VSD100_F3_8': {'brand': 'Vixen', 'name': 'VSD100 F3.8', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 100, 'focal_length_mm': 380},
        'Vixen_SD81S': {'brand': 'Vixen', 'name': 'SD81S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M60', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 81, 'focal_length_mm': 625},
        'Vixen_SD103S': {'brand': 'Vixen', 'name': 'SD103S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M60', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 103, 'focal_length_mm': 795},
        'Vixen_SD115S': {'brand': 'Vixen', 'name': 'SD115S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M60', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 115, 'focal_length_mm': 890},
        'Vixen_AX103S': {'brand': 'Vixen', 'name': 'AX103S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M60', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 103, 'focal_length_mm': 825},
        'Vixen_FL55SS': {'brand': 'Vixen', 'name': 'FL55SS', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M60', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 55, 'focal_length_mm': 303},
        'Vixen_R200SS': {'brand': 'Vixen', 'name': 'R200SS', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 5300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M60', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 800, 'central_obstruction_mm': 65},
        'Vixen_VMC200L': {'brand': 'Vixen', 'name': 'VMC200L', 'type': 'catadioptric', 'optical_length': 0, 'mass': 5900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M60', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 1950, 'central_obstruction_mm': 80},
    }

    @classmethod
    def Vixen_VC200L(cls):
        return cls.from_database(cls._DATABASE['Vixen_VC200L'])

    @classmethod
    def Vixen_VSD100_F3_8(cls):
        return cls.from_database(cls._DATABASE['Vixen_VSD100_F3_8'])

    @classmethod
    def Vixen_SD81S(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD81S'])

    @classmethod
    def Vixen_SD103S(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD103S'])

    @classmethod
    def Vixen_SD115S(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD115S'])

    @classmethod
    def Vixen_AX103S(cls):
        return cls.from_database(cls._DATABASE['Vixen_AX103S'])

    @classmethod
    def Vixen_FL55SS(cls):
        return cls.from_database(cls._DATABASE['Vixen_FL55SS'])

    @classmethod
    def Vixen_R200SS(cls):
        return cls.from_database(cls._DATABASE['Vixen_R200SS'])

    @classmethod
    def Vixen_VMC200L(cls):
        return cls.from_database(cls._DATABASE['Vixen_VMC200L'])
