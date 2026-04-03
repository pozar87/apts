import sys
import os
import ast

def verify_stellarvue_static():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'apts', 'opticalequipment', 'telescope', 'vendors', 'stellarvue.py'))

    with open(file_path, 'r') as f:
        content = f.read()

    tree = ast.parse(content)

    database = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'StellarvueTelescope':
            for item in node.body:
                if isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name) and target.id == '_DATABASE':
                            database = ast.literal_eval(item.value)
                            break

    if database is None:
        print("[FAIL] Could not find _DATABASE in StellarvueTelescope class.")
        sys.exit(1)

    success = True
    for key, specs in database.items():
        print(f"Verifying {key}...")

        required_keys = ['aperture_mm', 'focal_length_mm', 'mass', 'central_obstruction_mm']
        for k in required_keys:
            if k not in specs:
                print(f"  [FAIL] Missing required key '{k}' in {key}")
                success = False

        if success:
            # Check for logical values
            if specs['aperture_mm'] <= 0:
                print(f"  [FAIL] Aperture must be positive, got {specs['aperture_mm']}")
                success = False
            if specs['focal_length_mm'] <= 0:
                print(f"  [FAIL] Focal length must be positive, got {specs['focal_length_mm']}")
                success = False
            if specs['mass'] <= 0:
                print(f"  [FAIL] Mass must be positive, got {specs['mass']}")
                success = False
            if specs['central_obstruction_mm'] != 0:
                print(f"  [FAIL] Central obstruction must be 0 for refractors, got {specs['central_obstruction_mm']}")
                success = False

        if success:
            print(f"  [OK] {key} verified.")

    if success:
        print("\nAll Stellarvue models verified successfully (static check)!")
    else:
        print("\nVerification failed for one or more Stellarvue models.")
        sys.exit(1)

if __name__ == "__main__":
    verify_stellarvue_static()
