import sys
import os

# Update Sky-Watcher Quattro specs
quattro_updates = {
    'Sky_Watcher_Quattro_150P': {'brand': 'Sky-Watcher', 'name': 'Quattro 150P', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 5700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 150, 'focal_length_mm': 600, 'central_obstruction_mm': 52},
    'Sky_Watcher_Quattro_200P': {'brand': 'Sky-Watcher', 'name': 'Quattro 200P', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 9500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 800, 'central_obstruction_mm': 70},
    'Sky_Watcher_Quattro_250P': {'brand': 'Sky-Watcher', 'name': 'Quattro 250P', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 250, 'focal_length_mm': 1000, 'central_obstruction_mm': 82},
    'Sky_Watcher_Quattro_300P': {'brand': 'Sky-Watcher', 'name': 'Quattro 300P', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 23000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 300, 'focal_length_mm': 1200, 'central_obstruction_mm': 100},
}

sw_path = 'apts/opticalequipment/telescope/vendors/sky_watcher.py'
with open(sw_path, 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '_DATABASE =' in line:
        # Extract the dictionary
        start = line.find('{')
        end = line.rfind('}') + 1
        db_str = line[start:end]
        import ast
        db = ast.literal_eval(db_str)
        db.update(quattro_updates)
        new_lines.append(f"    _DATABASE = {repr(db)}\n")
    else:
        new_lines.append(line)

with open(sw_path, 'w') as f:
    f.writelines(new_lines)

# Update ZWO Duo specs
duo_updates = {
    'ZWO_ASI_2600MC_Duo': {'brand': 'ZWO', 'name': 'ASI 2600MC Duo', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'start', 'sensor_width_mm': 23.5, 'sensor_height_mm': 15.7, 'width': 6248, 'height': 4176, 'pixel_size_um': 3.76, 'quantum_efficiency': 80, 'full_well_e': 50000, 'read_noise_e': 1.0},
    'ZWO_ASI_2600MM_Duo': {'brand': 'ZWO', 'name': 'ASI 2600MM Duo', 'type': 'type_camera', 'optical_length': 17.5, 'mass': 800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'start', 'sensor_width_mm': 23.5, 'sensor_height_mm': 15.7, 'width': 6248, 'height': 4176, 'pixel_size_um': 3.76, 'quantum_efficiency': 91, 'full_well_e': 50000, 'read_noise_e': 1.0},
}

zwo_path = 'apts/opticalequipment/camera/vendors/zwo.py'
with open(zwo_path, 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '_DATABASE =' in line:
        start = line.find('{')
        end = line.rfind('}') + 1
        db_str = line[start:end]
        import ast
        db = ast.literal_eval(db_str)
        db.update(duo_updates)
        new_lines.append(f"    _DATABASE = {repr(db)}\n")
    else:
        new_lines.append(line)

with open(zwo_path, 'w') as f:
    f.writelines(new_lines)
