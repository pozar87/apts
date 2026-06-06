from ..base import FilterWheel


class StarlightXpressFilterWheel(FilterWheel):
    _DATABASE = {'Starlight_Xpress_SX_Mini_Wheel': {'brand':
        'Starlight Xpress', 'name': 'SX Mini Wheel', 'type':
        'type_filter_wheel', 'optical_length': 20, 'mass': 300,
        'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread':
        'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Starlight_Xpress_SX_USB_Wheel_M54': {'brand': 'Starlight Xpress',
        'name': 'SX USB Wheel (M54)', 'type': 'type_filter_wheel',
        'optical_length': 21, 'mass': 600, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Starlight_Xpress_SX_Maxi_Wheel_M68': {'brand': 'Starlight Xpress',
        'name': 'SX Maxi Wheel (M68)', 'type': 'type_filter_wheel',
        'optical_length': 22, 'mass': 700, 'tside_thread': 'M68',
        'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Starlight_Xpress_SX_Mini_Wheel(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Xpress_SX_Mini_Wheel'])

    @classmethod
    def Starlight_Xpress_SX_USB_Wheel_M54(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Xpress_SX_USB_Wheel_M54'])

    @classmethod
    def Starlight_Xpress_SX_Maxi_Wheel_M68(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Xpress_SX_Maxi_Wheel_M68'])
