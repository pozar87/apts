from ..base import Telescope

class StellarvueTelescope(Telescope):
    _DATABASE = {
        'Stellarvue_SVX080T': {
            'brand': 'Stellarvue',
            'name': 'SVX080T',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 2950, # 6.5 lbs (OTA only)
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 80,
            'focal_length_mm': 480,
            'central_obstruction_mm': 0
        }, # Source: http://www.stellarvue.com/manuals/SVX80T-3SV_manual.pdf
        'Stellarvue_SVX102T': {
            'brand': 'Stellarvue',
            'name': 'SVX102T',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 4500, # 9.9 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 101.5,
            'focal_length_mm': 714,
            'central_obstruction_mm': 0
        }, # Source: https://www.stellarvue.com/product/svx102t
        'Stellarvue_SVX102T_R': {
            'brand': 'Stellarvue',
            'name': 'SVX102T-R',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 4500,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M54',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 101.5,
            'focal_length_mm': 714,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SVX130T': {
            'brand': 'Stellarvue',
            'name': 'SVX130T',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 7620, # 16.8 lbs with 3.5" focuser
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M68',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 130,
            'focal_length_mm': 910,
            'central_obstruction_mm': 0
        }, # Source: https://www.stellarvue.com/manuals/SVX130T_manual.pdf
        'Stellarvue_SVX152T': {
            'brand': 'Stellarvue',
            'name': 'SVX152T',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 10520, # 23.2 lbs (OTA)
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M68',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 152,
            'focal_length_mm': 1200,
            'central_obstruction_mm': 0
        }, # Source: https://telescope.fandom.com/wiki/Stellarvue_SVX152T
        'Stellarvue_SV60EDS': {
            'brand': 'Stellarvue',
            'name': 'SV60EDS',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 1130, # 2.5 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M42',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 60,
            'focal_length_mm': 330,
            'central_obstruction_mm': 0
        }, # Source: https://stargazerslounge.com/topic/234836-stellarvue-sv-60eds-unbox-mini-review/
        'Stellarvue_SV70T': {
            'brand': 'Stellarvue',
            'name': 'SV70T',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 2500,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 70,
            'focal_length_mm': 420,
            'central_obstruction_mm': 0
        }, # Source: https://ssr.app.astrobin.com/equipment/explorer/telescope/333/stellarvue-sv70t
        'Stellarvue_SVX80T_IS': {
            'brand': 'Stellarvue',
            'name': 'SVX80T-IS',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 2950,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 80,
            'focal_length_mm': 480,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SVX090T': {
            'brand': 'Stellarvue',
            'name': 'SVX090T',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 3200,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 90,
            'focal_length_mm': 540,
            'central_obstruction_mm': 0
        }, # Source: https://www.stellarvue.com/product/svx090t
        'Stellarvue_Access_80': {
            'brand': 'Stellarvue',
            'name': 'Access 80',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 2720, # 6 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 80,
            'focal_length_mm': 560,
            'central_obstruction_mm': 0
        }, # Source: https://galileotelescope.com/telescopes/stellarvue-access-80mm-super-ed-2-5-sv-focuser-with-d1029ed-and-case.html
        'Stellarvue_Access_102': {
            'brand': 'Stellarvue',
            'name': 'Access 102',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 4310, # 9.5 lbs (est)
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 102,
            'focal_length_mm': 714,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SV48_Access': {
            'brand': 'Stellarvue',
            'name': 'SV48 Access',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 2720,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M42',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 80,
            'focal_length_mm': 560,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SV60EDS_v2': {
            'brand': 'Stellarvue',
            'name': 'SV60EDS v2',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 1130,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M42',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 60,
            'focal_length_mm': 330,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SV70T_v2': {
            'brand': 'Stellarvue',
            'name': 'SV70T v2',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 2500,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 70,
            'focal_length_mm': 420,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SVX080T_v2': {
            'brand': 'Stellarvue',
            'name': 'SVX080T v2',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 2950,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 80,
            'focal_length_mm': 480,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SVX090T_v2': {
            'brand': 'Stellarvue',
            'name': 'SVX090T v2',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 3200,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 90,
            'focal_length_mm': 540,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SVX102T_v2': {
            'brand': 'Stellarvue',
            'name': 'SVX102T v2',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 4500,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 101.5,
            'focal_length_mm': 714,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SVX130T_v2': {
            'brand': 'Stellarvue',
            'name': 'SVX130T v2',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 7620,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M68',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 130,
            'focal_length_mm': 910,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SVX152T_v2': {
            'brand': 'Stellarvue',
            'name': 'SVX152T v2',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 10520,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M68',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 152,
            'focal_length_mm': 1200,
            'central_obstruction_mm': 0
        },
        'Stellarvue_SVX070T_Raptor': {
            'brand': 'Stellarvue',
            'name': 'SVX070T Raptor',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 1810, # 4 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 70,
            'focal_length_mm': 420,
            'central_obstruction_mm': 0
        }
    }

    @classmethod
    def Stellarvue_SVX080T(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX080T'])

    @classmethod
    def Stellarvue_SVX102T(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX102T'])

    @classmethod
    def Stellarvue_SVX102T_R(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX102T_R'])

    @classmethod
    def Stellarvue_SVX130T(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX130T'])

    @classmethod
    def Stellarvue_SVX152T(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX152T'])

    @classmethod
    def Stellarvue_SV60EDS(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SV60EDS'])

    @classmethod
    def Stellarvue_SV70T(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SV70T'])

    @classmethod
    def Stellarvue_SVX80T_IS(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX80T_IS'])

    @classmethod
    def Stellarvue_SVX090T(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX090T'])

    @classmethod
    def Stellarvue_Access_80(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Access_80'])

    @classmethod
    def Stellarvue_Access_102(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Access_102'])

    @classmethod
    def Stellarvue_SV48_Access(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SV48_Access'])

    @classmethod
    def Stellarvue_SV60EDS_v2(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SV60EDS_v2'])

    @classmethod
    def Stellarvue_SV70T_v2(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SV70T_v2'])

    @classmethod
    def Stellarvue_SVX080T_v2(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX080T_v2'])

    @classmethod
    def Stellarvue_SVX090T_v2(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX090T_v2'])

    @classmethod
    def Stellarvue_SVX102T_v2(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX102T_v2'])

    @classmethod
    def Stellarvue_SVX130T_v2(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX130T_v2'])

    @classmethod
    def Stellarvue_SVX152T_v2(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX152T_v2'])

    @classmethod
    def Stellarvue_SVX070T_Raptor(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVX070T_Raptor'])
