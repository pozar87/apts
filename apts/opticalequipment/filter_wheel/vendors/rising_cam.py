from ..base import FilterWheel


class RisingCamFilterWheel(FilterWheel):
    _DATABASE = {'Rising_Cam_Filter_Wheel_5x1_25_M42': {'brand':
        'Rising Cam', 'name': 'Filter Wheel 5x1.25" (M42)', 'type':
        'type_filter_wheel', 'optical_length': 18, 'mass': 310,
        'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread':
        'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Rising_Cam_Filter_Wheel_5x_M42': {'brand': 'Rising Cam', 'name':
        'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel',
        'optical_length': 18, 'mass': 300, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Rising_Cam_Filter_Wheel_7x_M48': {'brand': 'Rising Cam', 'name':
        'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel',
        'optical_length': 20, 'mass': 450, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Rising_Cam_Filter_Wheel_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE[
            'Rising_Cam_Filter_Wheel_5x1_25_M42'])

    @classmethod
    def Rising_Cam_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE[
            'Rising_Cam_Filter_Wheel_5x_M42'])

    @classmethod
    def Rising_Cam_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE[
            'Rising_Cam_Filter_Wheel_7x_M48'])
