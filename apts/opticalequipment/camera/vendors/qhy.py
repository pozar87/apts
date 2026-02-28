from ..base import Camera

class QhyCamera(Camera):
    _DATABASE = {'QHY_QHY_600M_Pro': {'brand': 'QHY', 'name': 'QHY 600M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1100, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_600M': {'brand': 'QHY', 'name': 'QHY 600M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1050, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_268M_Pro': {'brand': 'QHY', 'name': 'QHY 268M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 860, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_268M': {'brand': 'QHY', 'name': 'QHY 268M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_533M_Pro': {'brand': 'QHY', 'name': 'QHY 533M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 740, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_533M': {'brand': 'QHY', 'name': 'QHY 533M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_294M_Pro': {'brand': 'QHY', 'name': 'QHY 294M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 680, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_294M': {'brand': 'QHY', 'name': 'QHY 294M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 620, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_183M_Pro': {'brand': 'QHY', 'name': 'QHY 183M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 520, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_183M': {'brand': 'QHY', 'name': 'QHY 183M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_163M': {'brand': 'QHY', 'name': 'QHY 163M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_168M': {'brand': 'QHY', 'name': 'QHY 168M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_367M_Pro': {'brand': 'QHY', 'name': 'QHY 367M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_410M': {'brand': 'QHY', 'name': 'QHY 410M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 950, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_411M': {'brand': 'QHY', 'name': 'QHY 411M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_461M': {'brand': 'QHY', 'name': 'QHY 461M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_492M': {'brand': 'QHY', 'name': 'QHY 492M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 750, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_128M_Pro': {'brand': 'QHY', 'name': 'QHY 128M Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_247M': {'brand': 'QHY', 'name': 'QHY 247M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_600C_Pro': {'brand': 'QHY', 'name': 'QHY 600C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1100, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_600C': {'brand': 'QHY', 'name': 'QHY 600C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1050, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_268C_Pro': {'brand': 'QHY', 'name': 'QHY 268C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 860, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_268C': {'brand': 'QHY', 'name': 'QHY 268C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_533C_Pro': {'brand': 'QHY', 'name': 'QHY 533C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 740, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_533C': {'brand': 'QHY', 'name': 'QHY 533C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_294C_Pro': {'brand': 'QHY', 'name': 'QHY 294C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 680, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_294C': {'brand': 'QHY', 'name': 'QHY 294C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 620, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_183C_Pro': {'brand': 'QHY', 'name': 'QHY 183C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 520, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_183C': {'brand': 'QHY', 'name': 'QHY 183C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_163C': {'brand': 'QHY', 'name': 'QHY 163C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_168C': {'brand': 'QHY', 'name': 'QHY 168C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_367C_Pro': {'brand': 'QHY', 'name': 'QHY 367C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_410C': {'brand': 'QHY', 'name': 'QHY 410C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 950, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_411C': {'brand': 'QHY', 'name': 'QHY 411C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_461C': {'brand': 'QHY', 'name': 'QHY 461C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_492C': {'brand': 'QHY', 'name': 'QHY 492C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 750, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_128C_Pro': {'brand': 'QHY', 'name': 'QHY 128C Pro', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_247C': {'brand': 'QHY', 'name': 'QHY 247C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_178M': {'brand': 'QHY', 'name': 'QHY 5III 178M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_178C': {'brand': 'QHY', 'name': 'QHY 5III 178C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_290M': {'brand': 'QHY', 'name': 'QHY 5III 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_290C': {'brand': 'QHY', 'name': 'QHY 5III 290C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_462C': {'brand': 'QHY', 'name': 'QHY 5III 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_485C': {'brand': 'QHY', 'name': 'QHY 5III 485C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_715C': {'brand': 'QHY', 'name': 'QHY 5III 715C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_533M': {'brand': 'QHY', 'name': 'QHY 5III 533M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_533C': {'brand': 'QHY', 'name': 'QHY 5III 533C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_224C': {'brand': 'QHY', 'name': 'QHY 5III 224C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_174M': {'brand': 'QHY', 'name': 'QHY 5III 174M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_585C': {'brand': 'QHY', 'name': 'QHY 5III 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_662C': {'brand': 'QHY', 'name': 'QHY 5III 662C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_600M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 600M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 1130, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_268M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 268M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 890, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_533M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 533M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 770, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_294M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 294M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 710, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_183M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 183M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_410M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 410M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 980, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_461M_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 461M + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 1230, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_600C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 600C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 1130, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_268C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 268C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 890, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_533C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 533C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 770, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_294C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 294C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 710, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_183C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 183C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_410C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 410C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 980, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_461C_M42_Adapter': {'brand': 'QHY', 'name': 'QHY 461C + M42 Adapter', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 1230, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_PoleMaster': {'brand': 'QHY', 'name': 'PoleMaster', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_MiniGuideScope_5III': {'brand': 'QHY', 'name': 'MiniGuideScope + 5III', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 210, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_120M': {'brand': 'QHY', 'name': 'QHY 5III 120M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_200M': {'brand': 'QHY', 'name': 'QHY 5III 200M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_385M': {'brand': 'QHY', 'name': 'QHY 5III 385M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_678M': {'brand': 'QHY', 'name': 'QHY 5III 678M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_482M': {'brand': 'QHY', 'name': 'QHY 5III 482M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_120C': {'brand': 'QHY', 'name': 'QHY 5III 120C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_200C': {'brand': 'QHY', 'name': 'QHY 5III 200C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_385C': {'brand': 'QHY', 'name': 'QHY 5III 385C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_678C': {'brand': 'QHY', 'name': 'QHY 5III 678C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_482C': {'brand': 'QHY', 'name': 'QHY 5III 482C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_462M': {'brand': 'QHY', 'name': 'QHY 5III 462M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_568M': {'brand': 'QHY', 'name': 'QHY 5III 568M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 110, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_600M': {'brand': 'QHY', 'name': 'QHY 5III 600M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_568C': {'brand': 'QHY', 'name': 'QHY 5III 568C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 110, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5III_600C': {'brand': 'QHY', 'name': 'QHY 5III 600C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_990M': {'brand': 'QHY', 'name': 'QHY 990M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_600LM': {'brand': 'QHY', 'name': 'QHY 600LM', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1150, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5200M': {'brand': 'QHY', 'name': 'QHY 5200M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_2020M': {'brand': 'QHY', 'name': 'QHY 2020M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_550M': {'brand': 'QHY', 'name': 'QHY 550M', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 650, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_174M': {'brand': 'QHY', 'name': 'QHY 174M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_990C': {'brand': 'QHY', 'name': 'QHY 990C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_600LC': {'brand': 'QHY', 'name': 'QHY 600LC', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1150, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_5200C': {'brand': 'QHY', 'name': 'QHY 5200C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_2020C': {'brand': 'QHY', 'name': 'QHY 2020C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_550C': {'brand': 'QHY', 'name': 'QHY 550C', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 650, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QHY_QHY_174C': {'brand': 'QHY', 'name': 'QHY 174C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def QHY_QHY_600M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600M_Pro'])

    @classmethod
    def QHY_QHY_600M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600M'])

    @classmethod
    def QHY_QHY_268M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268M_Pro'])

    @classmethod
    def QHY_QHY_268M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268M'])

    @classmethod
    def QHY_QHY_533M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533M_Pro'])

    @classmethod
    def QHY_QHY_533M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533M'])

    @classmethod
    def QHY_QHY_294M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294M_Pro'])

    @classmethod
    def QHY_QHY_294M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294M'])

    @classmethod
    def QHY_QHY_183M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183M_Pro'])

    @classmethod
    def QHY_QHY_183M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183M'])

    @classmethod
    def QHY_QHY_163M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_163M'])

    @classmethod
    def QHY_QHY_168M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_168M'])

    @classmethod
    def QHY_QHY_367M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_367M_Pro'])

    @classmethod
    def QHY_QHY_410M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_410M'])

    @classmethod
    def QHY_QHY_411M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_411M'])

    @classmethod
    def QHY_QHY_461M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_461M'])

    @classmethod
    def QHY_QHY_492M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_492M'])

    @classmethod
    def QHY_QHY_128M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_128M_Pro'])

    @classmethod
    def QHY_QHY_247M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_247M'])

    @classmethod
    def QHY_QHY_600C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600C_Pro'])

    @classmethod
    def QHY_QHY_600C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600C'])

    @classmethod
    def QHY_QHY_268C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268C_Pro'])

    @classmethod
    def QHY_QHY_268C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268C'])

    @classmethod
    def QHY_QHY_533C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533C_Pro'])

    @classmethod
    def QHY_QHY_533C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533C'])

    @classmethod
    def QHY_QHY_294C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294C_Pro'])

    @classmethod
    def QHY_QHY_294C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294C'])

    @classmethod
    def QHY_QHY_183C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183C_Pro'])

    @classmethod
    def QHY_QHY_183C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183C'])

    @classmethod
    def QHY_QHY_163C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_163C'])

    @classmethod
    def QHY_QHY_168C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_168C'])

    @classmethod
    def QHY_QHY_367C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_367C_Pro'])

    @classmethod
    def QHY_QHY_410C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_410C'])

    @classmethod
    def QHY_QHY_411C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_411C'])

    @classmethod
    def QHY_QHY_461C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_461C'])

    @classmethod
    def QHY_QHY_492C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_492C'])

    @classmethod
    def QHY_QHY_128C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_128C_Pro'])

    @classmethod
    def QHY_QHY_247C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_247C'])

    @classmethod
    def QHY_QHY_5III_178M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_178M'])

    @classmethod
    def QHY_QHY_5III_178C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_178C'])

    @classmethod
    def QHY_QHY_5III_290M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_290M'])

    @classmethod
    def QHY_QHY_5III_290C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_290C'])

    @classmethod
    def QHY_QHY_5III_462C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_462C'])

    @classmethod
    def QHY_QHY_5III_485C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_485C'])

    @classmethod
    def QHY_QHY_5III_715C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_715C'])

    @classmethod
    def QHY_QHY_5III_533M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_533M'])

    @classmethod
    def QHY_QHY_5III_533C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_533C'])

    @classmethod
    def QHY_QHY_5III_224C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_224C'])

    @classmethod
    def QHY_QHY_5III_174M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_174M'])

    @classmethod
    def QHY_QHY_5III_585C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_585C'])

    @classmethod
    def QHY_QHY_5III_662C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_662C'])

    @classmethod
    def QHY_QHY_600M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600M_M42_Adapter'])

    @classmethod
    def QHY_QHY_268M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268M_M42_Adapter'])

    @classmethod
    def QHY_QHY_533M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533M_M42_Adapter'])

    @classmethod
    def QHY_QHY_294M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294M_M42_Adapter'])

    @classmethod
    def QHY_QHY_183M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183M_M42_Adapter'])

    @classmethod
    def QHY_QHY_410M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_410M_M42_Adapter'])

    @classmethod
    def QHY_QHY_461M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_461M_M42_Adapter'])

    @classmethod
    def QHY_QHY_600C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600C_M42_Adapter'])

    @classmethod
    def QHY_QHY_268C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268C_M42_Adapter'])

    @classmethod
    def QHY_QHY_533C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533C_M42_Adapter'])

    @classmethod
    def QHY_QHY_294C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294C_M42_Adapter'])

    @classmethod
    def QHY_QHY_183C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183C_M42_Adapter'])

    @classmethod
    def QHY_QHY_410C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_410C_M42_Adapter'])

    @classmethod
    def QHY_QHY_461C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_461C_M42_Adapter'])

    @classmethod
    def QHY_PoleMaster(cls):
        return cls.from_database(cls._DATABASE['QHY_PoleMaster'])

    @classmethod
    def QHY_MiniGuideScope_5III(cls):
        return cls.from_database(cls._DATABASE['QHY_MiniGuideScope_5III'])

    @classmethod
    def QHY_QHY_5III_120M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_120M'])

    @classmethod
    def QHY_QHY_5III_200M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_200M'])

    @classmethod
    def QHY_QHY_5III_385M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_385M'])

    @classmethod
    def QHY_QHY_5III_678M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_678M'])

    @classmethod
    def QHY_QHY_5III_482M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_482M'])

    @classmethod
    def QHY_QHY_5III_120C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_120C'])

    @classmethod
    def QHY_QHY_5III_200C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_200C'])

    @classmethod
    def QHY_QHY_5III_385C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_385C'])

    @classmethod
    def QHY_QHY_5III_678C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_678C'])

    @classmethod
    def QHY_QHY_5III_482C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_482C'])

    @classmethod
    def QHY_QHY_5III_462M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_462M'])

    @classmethod
    def QHY_QHY_5III_568M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_568M'])

    @classmethod
    def QHY_QHY_5III_600M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_600M'])

    @classmethod
    def QHY_QHY_5III_568C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_568C'])

    @classmethod
    def QHY_QHY_5III_600C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_600C'])

    @classmethod
    def QHY_QHY_990M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_990M'])

    @classmethod
    def QHY_QHY_600LM(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600LM'])

    @classmethod
    def QHY_QHY_5200M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5200M'])

    @classmethod
    def QHY_QHY_2020M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_2020M'])

    @classmethod
    def QHY_QHY_550M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_550M'])

    @classmethod
    def QHY_QHY_174M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_174M'])

    @classmethod
    def QHY_QHY_990C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_990C'])

    @classmethod
    def QHY_QHY_600LC(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600LC'])

    @classmethod
    def QHY_QHY_5200C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5200C'])

    @classmethod
    def QHY_QHY_2020C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_2020C'])

    @classmethod
    def QHY_QHY_550C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_550C'])

    @classmethod
    def QHY_QHY_174C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_174C'])