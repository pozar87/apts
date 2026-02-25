from ..base import Reducer, Flattener

class Astro_physicsReducer(Reducer):
    _DATABASE = {'Astro_Physics_CCDT67_Telecompressor': {'brand': 'Astro-Physics', 'name': 'CCDT67 Telecompressor', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Astro_Physics_0_67x_Reducer_130GTX': {'brand': 'Astro-Physics', 'name': '0.67x Reducer (130GTX)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Astro_Physics_0_72x_Reducer': {'brand': 'Astro-Physics', 'name': '0.72x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 320, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Astro_Physics_92mm_Reducer_0_72x': {'brand': 'Astro-Physics', 'name': '92mm Reducer 0.72x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Astro_Physics_Quad_TCC_4_Reducer': {'brand': 'Astro-Physics', 'name': 'Quad TCC (4" Reducer)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 700, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Astro_Physics_27TVPH_Reducer_0_75x': {'brand': 'Astro-Physics', 'name': '27TVPH Reducer 0.75x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Astro_Physics_CCDT67_Telecompressor(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_CCDT67_Telecompressor'])

    @classmethod
    def Astro_Physics_0_67x_Reducer_130GTX(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_0_67x_Reducer_130GTX'])

    @classmethod
    def Astro_Physics_0_72x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_0_72x_Reducer'])

    @classmethod
    def Astro_Physics_92mm_Reducer_0_72x(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_92mm_Reducer_0_72x'])

    @classmethod
    def Astro_Physics_Quad_TCC_4_Reducer(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_Quad_TCC_4_Reducer'])

    @classmethod
    def Astro_Physics_27TVPH_Reducer_0_75x(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_27TVPH_Reducer_0_75x'])

class Astro_physicsFlattener(Flattener):
    _DATABASE = {'Astro_Physics_160FFAPO5_Flattener': {'brand': 'Astro-Physics', 'name': '160FFAPO5 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Astro_Physics_130GTX_Flattener': {'brand': 'Astro-Physics', 'name': '130GTX Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Astro_Physics_160FFAPO5_Flattener(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_160FFAPO5_Flattener'])

    @classmethod
    def Astro_Physics_130GTX_Flattener(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_130GTX_Flattener'])