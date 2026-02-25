from ..base import Camera

class ZwoCamera(Camera):
    _DATABASE = {'ZWO_ASI_183MC_Pro': {'brand': 'ZWO', 'name': 'ASI 183MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 410, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MM_Pro': {'brand': 'ZWO', 'name': 'ASI 183MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 410, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MC_Pro': {'brand': 'ZWO', 'name': 'ASI 294MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 478, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MM_Pro': {'brand': 'ZWO', 'name': 'ASI 294MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 478, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MC_Pro': {'brand': 'ZWO', 'name': 'ASI 533MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MM_Pro': {'brand': 'ZWO', 'name': 'ASI 533MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600MC_Pro': {'brand': 'ZWO', 'name': 'ASI 1600MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 410, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600MM_Pro': {'brand': 'ZWO', 'name': 'ASI 1600MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 410, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_071MC_Pro': {'brand': 'ZWO', 'name': 'ASI 071MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_071MM_Pro': {'brand': 'ZWO', 'name': 'ASI 071MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_094MC_Pro': {'brand': 'ZWO', 'name': 'ASI 094MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_094MM_Pro': {'brand': 'ZWO', 'name': 'ASI 094MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MC_Pro': {'brand': 'ZWO', 'name': 'ASI 2600MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 720, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MM_Pro': {'brand': 'ZWO', 'name': 'ASI 2600MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 720, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MC_Duo': {'brand': 'ZWO', 'name': 'ASI 2600MC Duo', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 730, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MM_Duo': {'brand': 'ZWO', 'name': 'ASI 2600MM Duo', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 730, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200MC_Pro': {'brand': 'ZWO', 'name': 'ASI 6200MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1010, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200MM_Pro': {'brand': 'ZWO', 'name': 'ASI 6200MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1010, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2400MC_Pro': {'brand': 'ZWO', 'name': 'ASI 2400MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2400MM_Pro': {'brand': 'ZWO', 'name': 'ASI 2400MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_128MC_Pro': {'brand': 'ZWO', 'name': 'ASI 128MC Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_128MM_Pro': {'brand': 'ZWO', 'name': 'ASI 128MM Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MC': {'brand': 'ZWO', 'name': 'ASI 533MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MM': {'brand': 'ZWO', 'name': 'ASI 533MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MC': {'brand': 'ZWO', 'name': 'ASI 294MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MM': {'brand': 'ZWO', 'name': 'ASI 294MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MC': {'brand': 'ZWO', 'name': 'ASI 183MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MM': {'brand': 'ZWO', 'name': 'ASI 183MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600MC': {'brand': 'ZWO', 'name': 'ASI 1600MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600MM': {'brand': 'ZWO', 'name': 'ASI 1600MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 2600 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 6200 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 294 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_071_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 071 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 533 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 183 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 1600 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2400_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 2400 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_128_M54_Adapter': {'brand': 'ZWO', 'name': 'ASI 128 + M54 Adapter', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600_Tilt_Adj_M54': {'brand': 'ZWO', 'name': 'ASI 2600 + Tilt Adj. (M54)', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200_Tilt_Adj_M54': {'brand': 'ZWO', 'name': 'ASI 6200 + Tilt Adj. (M54)', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294_Tilt_Adj_M54': {'brand': 'ZWO', 'name': 'ASI 294 + Tilt Adj. (M54)', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533_Tilt_Adj_M54': {'brand': 'ZWO', 'name': 'ASI 533 + Tilt Adj. (M54)', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_585MC': {'brand': 'ZWO', 'name': 'ASI 585MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_585MM': {'brand': 'ZWO', 'name': 'ASI 585MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_678MC': {'brand': 'ZWO', 'name': 'ASI 678MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_678MM': {'brand': 'ZWO', 'name': 'ASI 678MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_662MC': {'brand': 'ZWO', 'name': 'ASI 662MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_662MM': {'brand': 'ZWO', 'name': 'ASI 662MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_482MC': {'brand': 'ZWO', 'name': 'ASI 482MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_482MM': {'brand': 'ZWO', 'name': 'ASI 482MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_485MC': {'brand': 'ZWO', 'name': 'ASI 485MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_485MM': {'brand': 'ZWO', 'name': 'ASI 485MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_462MC': {'brand': 'ZWO', 'name': 'ASI 462MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_462MM': {'brand': 'ZWO', 'name': 'ASI 462MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_715MC': {'brand': 'ZWO', 'name': 'ASI 715MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_715MM': {'brand': 'ZWO', 'name': 'ASI 715MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_676MC': {'brand': 'ZWO', 'name': 'ASI 676MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_676MM': {'brand': 'ZWO', 'name': 'ASI 676MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_120MM_Mini': {'brand': 'ZWO', 'name': 'ASI 120MM Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_120MC_S': {'brand': 'ZWO', 'name': 'ASI 120MC-S', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_224MC': {'brand': 'ZWO', 'name': 'ASI 224MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_290MM_Mini': {'brand': 'ZWO', 'name': 'ASI 290MM Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_290MC': {'brand': 'ZWO', 'name': 'ASI 290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_178MC': {'brand': 'ZWO', 'name': 'ASI 178MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_178MM': {'brand': 'ZWO', 'name': 'ASI 178MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_385MC': {'brand': 'ZWO', 'name': 'ASI 385MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_385MM': {'brand': 'ZWO', 'name': 'ASI 385MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_220MM_Mini': {'brand': 'ZWO', 'name': 'ASI 220MM Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_174MC': {'brand': 'ZWO', 'name': 'ASI 174MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 60, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_174MM': {'brand': 'ZWO', 'name': 'ASI 174MM', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 60, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_174MM_Mini': {'brand': 'ZWO', 'name': 'ASI 174MM Mini', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 60, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 2600MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 2600MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 6200MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 6200MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 294MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 294MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 533MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 533MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 183MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 183MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 1600MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 1600MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_071MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 071MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_128MM_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 128MM Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2400MC_Pro_6_bolt_mount': {'brand': 'ZWO', 'name': 'ASI 2400MC Pro (6-bolt mount)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MC_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 2600MC Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MM_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 2600MM Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200MC_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 6200MC Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200MM_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 6200MM Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MC_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 294MC Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MC_Pro_4_bolt_no_tilt_plate': {'brand': 'ZWO', 'name': 'ASI 533MC Pro (4-bolt, no tilt plate)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 50, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_120MM_S_for_ASIAir': {'brand': 'ZWO', 'name': 'ASI 120MM-S (for ASIAir)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_220MM_Mini_for_ASIAir': {'brand': 'ZWO', 'name': 'ASI 220MM Mini (for ASIAir)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_034MC': {'brand': 'ZWO', 'name': 'ASI 034MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_035MC': {'brand': 'ZWO', 'name': 'ASI 035MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_120MC': {'brand': 'ZWO', 'name': 'ASI 120MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_120MM': {'brand': 'ZWO', 'name': 'ASI 120MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_130MM': {'brand': 'ZWO', 'name': 'ASI 130MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 65, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_035MM': {'brand': 'ZWO', 'name': 'ASI 035MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_174MC_Mini': {'brand': 'ZWO', 'name': 'ASI 174MC Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 65, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_290MC_Mini': {'brand': 'ZWO', 'name': 'ASI 290MC Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_290MM': {'brand': 'ZWO', 'name': 'ASI 290MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600MC_Cool': {'brand': 'ZWO', 'name': 'ASI 1600MC Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 380, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_1600MM_Cool': {'brand': 'ZWO', 'name': 'ASI 1600MM Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 380, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MC_Cool': {'brand': 'ZWO', 'name': 'ASI 183MC Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MM_Cool': {'brand': 'ZWO', 'name': 'ASI 183MM Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 340, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_071MC_Cool': {'brand': 'ZWO', 'name': 'ASI 071MC Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_094MC_Cool': {'brand': 'ZWO', 'name': 'ASI 094MC Cool', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 780, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 533MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_533MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 533MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 2600MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 730, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_2600MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 2600MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 730, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 6200MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1020, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_6200MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 6200MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1020, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 294MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_294MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 294MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MC_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 183MC Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_183MM_Pro_v2': {'brand': 'ZWO', 'name': 'ASI 183MM Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_715MC_V2': {'brand': 'ZWO', 'name': 'ASI 715MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_715MM_V2': {'brand': 'ZWO', 'name': 'ASI 715MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_585MC_V2': {'brand': 'ZWO', 'name': 'ASI 585MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_585MM_V2': {'brand': 'ZWO', 'name': 'ASI 585MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_662MC_V2': {'brand': 'ZWO', 'name': 'ASI 662MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_662MM_V2': {'brand': 'ZWO', 'name': 'ASI 662MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_678MC_V2': {'brand': 'ZWO', 'name': 'ASI 678MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_678MM_V2': {'brand': 'ZWO', 'name': 'ASI 678MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_482MC_V2': {'brand': 'ZWO', 'name': 'ASI 482MC V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ZWO_ASI_482MM_V2': {'brand': 'ZWO', 'name': 'ASI 482MM V2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 155, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def ZWO_ASI294MC_PRO(cls):
        """
        Factory method for ZWO ASI294MC Pro camera.
        Sensor: Sony IMX294 (4/3")
        """
        return cls(19.1, 13.0, 4144, 2822, 'ZWO ASI294MC Pro', pixel_size=4.63, read_noise=1.2, full_well=63700, quantum_efficiency=75)

    @classmethod
    def ZWO_ASI294MM_PRO(cls):
        """
        Factory method for ZWO ASI294MM Pro camera.
        Sensor: Sony IMX492 (4/3")
        Defaulting to Bin2 mode.
        """
        return cls(19.1, 13.0, 4144, 2822, 'ZWO ASI294MM Pro', pixel_size=4.63, read_noise=1.2, full_well=66000, quantum_efficiency=90)

    @classmethod
    def ZWO_ASI585MC(cls):
        """
        Factory method for ZWO ASI585MC camera.
        Sensor: Sony IMX585 (1/1.2")
        """
        return cls(11.13, 6.26, 3840, 2160, 'ZWO ASI585MC', pixel_size=2.9, read_noise=0.8, full_well=40000, quantum_efficiency=91)

    @classmethod
    def ZWO_ASI2600MC_PRO(cls):
        """
        Factory method for ZWO ASI2600MC Pro camera.
        Sensor: Sony IMX571 (APS-C)
        """
        return cls(23.5, 15.7, 6248, 4176, 'ZWO ASI2600MC Pro', pixel_size=3.76, read_noise=1.0, full_well=50000, quantum_efficiency=80)

    @classmethod
    def ZWO_ASI2600MM_PRO(cls):
        """
        Factory method for ZWO ASI2600MM Pro camera.
        Sensor: Sony IMX571 (Mono APS-C)
        """
        return cls(23.5, 15.7, 6248, 4176, 'ZWO ASI2600MM Pro', pixel_size=3.76, read_noise=1.0, full_well=50000, quantum_efficiency=91)

    @classmethod
    def ZWO_ASI1600MM_PRO(cls):
        """
        Factory method for ZWO ASI1600MM Pro camera.
        Sensor: Panasonic MN34230 (4/3")
        """
        return cls(17.7, 13.4, 4656, 3520, 'ZWO ASI1600MM Pro', pixel_size=3.8, read_noise=1.2, full_well=20000, quantum_efficiency=60)

    @classmethod
    def ZWO_ASI533MC_PRO(cls):
        """
        Factory method for ZWO ASI533MC Pro camera.
        Sensor: Sony IMX533 (1" Square)
        """
        return cls(11.31, 11.31, 3008, 3008, 'ZWO ASI533MC Pro', pixel_size=3.76, read_noise=1.0, full_well=50000, quantum_efficiency=80)

    @classmethod
    def ZWO_ASI_183MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MC_Pro'])

    @classmethod
    def ZWO_ASI_183MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MM_Pro'])

    @classmethod
    def ZWO_ASI_294MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MC_Pro'])

    @classmethod
    def ZWO_ASI_294MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MM_Pro'])

    @classmethod
    def ZWO_ASI_533MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MC_Pro'])

    @classmethod
    def ZWO_ASI_533MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MM_Pro'])

    @classmethod
    def ZWO_ASI_1600MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600MC_Pro'])

    @classmethod
    def ZWO_ASI_1600MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600MM_Pro'])

    @classmethod
    def ZWO_ASI_071MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_071MC_Pro'])

    @classmethod
    def ZWO_ASI_071MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_071MM_Pro'])

    @classmethod
    def ZWO_ASI_094MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_094MC_Pro'])

    @classmethod
    def ZWO_ASI_094MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_094MM_Pro'])

    @classmethod
    def ZWO_ASI_2600MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Pro'])

    @classmethod
    def ZWO_ASI_2600MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Pro'])

    @classmethod
    def ZWO_ASI_2600MC_Duo(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Duo'])

    @classmethod
    def ZWO_ASI_2600MM_Duo(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Duo'])

    @classmethod
    def ZWO_ASI_6200MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200MC_Pro'])

    @classmethod
    def ZWO_ASI_6200MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200MM_Pro'])

    @classmethod
    def ZWO_ASI_2400MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2400MC_Pro'])

    @classmethod
    def ZWO_ASI_2400MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2400MM_Pro'])

    @classmethod
    def ZWO_ASI_128MC_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_128MC_Pro'])

    @classmethod
    def ZWO_ASI_128MM_Pro(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_128MM_Pro'])

    @classmethod
    def ZWO_ASI_533MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MC'])

    @classmethod
    def ZWO_ASI_533MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MM'])

    @classmethod
    def ZWO_ASI_294MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MC'])

    @classmethod
    def ZWO_ASI_294MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MM'])

    @classmethod
    def ZWO_ASI_183MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MC'])

    @classmethod
    def ZWO_ASI_183MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MM'])

    @classmethod
    def ZWO_ASI_1600MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600MC'])

    @classmethod
    def ZWO_ASI_1600MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600MM'])

    @classmethod
    def ZWO_ASI_2600_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600_M54_Adapter'])

    @classmethod
    def ZWO_ASI_6200_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200_M54_Adapter'])

    @classmethod
    def ZWO_ASI_294_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294_M54_Adapter'])

    @classmethod
    def ZWO_ASI_071_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_071_M54_Adapter'])

    @classmethod
    def ZWO_ASI_533_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533_M54_Adapter'])

    @classmethod
    def ZWO_ASI_183_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183_M54_Adapter'])

    @classmethod
    def ZWO_ASI_1600_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600_M54_Adapter'])

    @classmethod
    def ZWO_ASI_2400_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2400_M54_Adapter'])

    @classmethod
    def ZWO_ASI_128_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_128_M54_Adapter'])

    @classmethod
    def ZWO_ASI_2600_Tilt_Adj_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600_Tilt_Adj_M54'])

    @classmethod
    def ZWO_ASI_6200_Tilt_Adj_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200_Tilt_Adj_M54'])

    @classmethod
    def ZWO_ASI_294_Tilt_Adj_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294_Tilt_Adj_M54'])

    @classmethod
    def ZWO_ASI_533_Tilt_Adj_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533_Tilt_Adj_M54'])

    @classmethod
    def ZWO_ASI_585MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_585MC'])

    @classmethod
    def ZWO_ASI_585MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_585MM'])

    @classmethod
    def ZWO_ASI_678MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_678MC'])

    @classmethod
    def ZWO_ASI_678MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_678MM'])

    @classmethod
    def ZWO_ASI_662MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_662MC'])

    @classmethod
    def ZWO_ASI_662MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_662MM'])

    @classmethod
    def ZWO_ASI_482MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_482MC'])

    @classmethod
    def ZWO_ASI_482MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_482MM'])

    @classmethod
    def ZWO_ASI_485MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_485MC'])

    @classmethod
    def ZWO_ASI_485MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_485MM'])

    @classmethod
    def ZWO_ASI_462MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_462MC'])

    @classmethod
    def ZWO_ASI_462MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_462MM'])

    @classmethod
    def ZWO_ASI_715MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_715MC'])

    @classmethod
    def ZWO_ASI_715MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_715MM'])

    @classmethod
    def ZWO_ASI_676MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_676MC'])

    @classmethod
    def ZWO_ASI_676MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_676MM'])

    @classmethod
    def ZWO_ASI_120MM_Mini(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_120MM_Mini'])

    @classmethod
    def ZWO_ASI_120MC_S(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_120MC_S'])

    @classmethod
    def ZWO_ASI_224MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_224MC'])

    @classmethod
    def ZWO_ASI_290MM_Mini(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_290MM_Mini'])

    @classmethod
    def ZWO_ASI_290MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_290MC'])

    @classmethod
    def ZWO_ASI_178MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_178MC'])

    @classmethod
    def ZWO_ASI_178MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_178MM'])

    @classmethod
    def ZWO_ASI_385MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_385MC'])

    @classmethod
    def ZWO_ASI_385MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_385MM'])

    @classmethod
    def ZWO_ASI_220MM_Mini(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_220MM_Mini'])

    @classmethod
    def ZWO_ASI_174MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_174MC'])

    @classmethod
    def ZWO_ASI_174MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_174MM'])

    @classmethod
    def ZWO_ASI_174MM_Mini(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_174MM_Mini'])

    @classmethod
    def ZWO_ASI_2600MC_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_2600MM_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_6200MC_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200MC_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_6200MM_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200MM_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_294MC_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MC_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_294MM_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MM_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_533MC_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MC_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_533MM_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MM_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_183MC_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MC_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_183MM_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MM_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_1600MC_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600MC_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_1600MM_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600MM_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_071MC_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_071MC_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_128MM_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_128MM_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_2400MC_Pro_6_bolt_mount(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2400MC_Pro_6_bolt_mount'])

    @classmethod
    def ZWO_ASI_2600MC_Pro_4_bolt_no_tilt_plate(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Pro_4_bolt_no_tilt_plate'])

    @classmethod
    def ZWO_ASI_2600MM_Pro_4_bolt_no_tilt_plate(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Pro_4_bolt_no_tilt_plate'])

    @classmethod
    def ZWO_ASI_6200MC_Pro_4_bolt_no_tilt_plate(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200MC_Pro_4_bolt_no_tilt_plate'])

    @classmethod
    def ZWO_ASI_6200MM_Pro_4_bolt_no_tilt_plate(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200MM_Pro_4_bolt_no_tilt_plate'])

    @classmethod
    def ZWO_ASI_294MC_Pro_4_bolt_no_tilt_plate(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MC_Pro_4_bolt_no_tilt_plate'])

    @classmethod
    def ZWO_ASI_533MC_Pro_4_bolt_no_tilt_plate(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MC_Pro_4_bolt_no_tilt_plate'])

    @classmethod
    def ZWO_ASI_120MM_S_for_ASIAir(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_120MM_S_for_ASIAir'])

    @classmethod
    def ZWO_ASI_220MM_Mini_for_ASIAir(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_220MM_Mini_for_ASIAir'])

    @classmethod
    def ZWO_ASI_034MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_034MC'])

    @classmethod
    def ZWO_ASI_035MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_035MC'])

    @classmethod
    def ZWO_ASI_120MC(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_120MC'])

    @classmethod
    def ZWO_ASI_120MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_120MM'])

    @classmethod
    def ZWO_ASI_130MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_130MM'])

    @classmethod
    def ZWO_ASI_035MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_035MM'])

    @classmethod
    def ZWO_ASI_174MC_Mini(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_174MC_Mini'])

    @classmethod
    def ZWO_ASI_290MC_Mini(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_290MC_Mini'])

    @classmethod
    def ZWO_ASI_290MM(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_290MM'])

    @classmethod
    def ZWO_ASI_1600MC_Cool(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600MC_Cool'])

    @classmethod
    def ZWO_ASI_1600MM_Cool(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600MM_Cool'])

    @classmethod
    def ZWO_ASI_183MC_Cool(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MC_Cool'])

    @classmethod
    def ZWO_ASI_183MM_Cool(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MM_Cool'])

    @classmethod
    def ZWO_ASI_071MC_Cool(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_071MC_Cool'])

    @classmethod
    def ZWO_ASI_094MC_Cool(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_094MC_Cool'])

    @classmethod
    def ZWO_ASI_533MC_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MC_Pro_v2'])

    @classmethod
    def ZWO_ASI_533MM_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533MM_Pro_v2'])

    @classmethod
    def ZWO_ASI_2600MC_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MC_Pro_v2'])

    @classmethod
    def ZWO_ASI_2600MM_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600MM_Pro_v2'])

    @classmethod
    def ZWO_ASI_6200MC_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200MC_Pro_v2'])

    @classmethod
    def ZWO_ASI_6200MM_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200MM_Pro_v2'])

    @classmethod
    def ZWO_ASI_294MC_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MC_Pro_v2'])

    @classmethod
    def ZWO_ASI_294MM_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294MM_Pro_v2'])

    @classmethod
    def ZWO_ASI_183MC_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MC_Pro_v2'])

    @classmethod
    def ZWO_ASI_183MM_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183MM_Pro_v2'])

    @classmethod
    def ZWO_ASI_715MC_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_715MC_V2'])

    @classmethod
    def ZWO_ASI_715MM_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_715MM_V2'])

    @classmethod
    def ZWO_ASI_585MC_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_585MC_V2'])

    @classmethod
    def ZWO_ASI_585MM_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_585MM_V2'])

    @classmethod
    def ZWO_ASI_662MC_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_662MC_V2'])

    @classmethod
    def ZWO_ASI_662MM_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_662MM_V2'])

    @classmethod
    def ZWO_ASI_678MC_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_678MC_V2'])

    @classmethod
    def ZWO_ASI_678MM_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_678MM_V2'])

    @classmethod
    def ZWO_ASI_482MC_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_482MC_V2'])

    @classmethod
    def ZWO_ASI_482MM_V2(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_482MM_V2'])