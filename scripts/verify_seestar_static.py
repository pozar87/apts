import sys
import ast

def verify_seestar_static():
    print("--- Verifying ZWO Seestar Series Data Integrity (Static) ---")

    # Path to the vendors/zwo.py in telescope and camera
    telescope_zwo_path = 'apts/opticalequipment/telescope/vendors/zwo.py'
    camera_zwo_path = 'apts/opticalequipment/camera/vendors/zwo.py'

    with open(telescope_zwo_path, 'r') as f:
        tree = ast.parse(f.read())

    db = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == '_DATABASE':
                    db = ast.literal_eval(node.value)
                    break

    # Verify S50
    print("\n[Seestar S50]")
    s50 = db['ZWO_Seestar_S50']
    print(f"Full Well: {s50['full_well_e']}e-")
    assert s50['full_well_e'] == 11200
    assert s50['focal_length'] == 250
    assert s50['aperture'] == 50
    assert s50['sensor_width'] == 5.6
    assert s50['pixel_size_um'] == 2.9

    # Verify S30
    print("\n[Seestar S30]")
    s30 = db['ZWO_Seestar_S30']
    print(f"Full Well: {s30['full_well_e']}e-")
    assert s30['full_well_e'] == 38200
    assert s30['focal_length'] == 150
    assert s30['aperture'] == 30
    assert s30['sensor_width'] == 5.57
    assert s30['pixel_size_um'] == 2.9

    # Verify S30 Pro
    print("\n[Seestar S30 Pro]")
    s30pro = db['ZWO_Seestar_S30_Pro']
    print(f"Focal Length: {s30pro['focal_length']}")
    print(f"Sensor: {s30pro['sensor_width']} x {s30pro['sensor_height']}")
    print(f"Pixel Size: {s30pro['pixel_size_um']}")
    print(f"Full Well: {s30pro['full_well_e']}e-")

    assert s30pro['focal_length'] == 160
    assert s30pro['sensor_width'] == 11.13
    assert s30pro['pixel_size_um'] == 2.9
    assert s30pro['full_well_e'] == 40000

    # Verify Sensors in Camera Database
    with open(camera_zwo_path, 'r') as f:
        tree_cam = ast.parse(f.read())

    db_cam = {}
    for node in ast.walk(tree_cam):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == '_DATABASE':
                    db_cam = ast.literal_eval(node.value)
                    break

    print("\n[Seestar Sensors - Camera Database]")
    s30pro_sensor = db_cam['ZWO_Seestar_S30_Pro_Sensor']
    print(f"S30 Pro Sensor Full Well: {s30pro_sensor['full_well_e']}e-")
    assert s30pro_sensor['full_well_e'] == 40000
    assert s30pro_sensor['sensor_width_mm'] == 11.13

    s50_sensor = db_cam['ZWO_Seestar_S50_Sensor']
    print(f"S50 Sensor Full Well: {s50_sensor['full_well_e']}e-")
    assert s50_sensor['full_well_e'] == 11200

    print("\n✅ All Seestar static data integrity checks passed!")

if __name__ == "__main__":
    try:
        verify_seestar_static()
    except AssertionError:
        print("\n❌ Static Data Integrity Check FAILED")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)
