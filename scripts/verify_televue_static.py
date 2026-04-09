import ast
import sys

def verify_televue_specs():
    filepath = 'apts/opticalequipment/telescope/vendors/televue.py'
    with open(filepath, 'r') as f:
        tree = ast.parse(f.read())

    database = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == '_DATABASE':
                    database = ast.literal_eval(node.value)
                    break
        if database:
            break

    if not database:
        print("Error: _DATABASE not found in televue.py")
        sys.exit(1)

    expected = {
        'TeleVue_NP101is': {'aperture_mm': 101, 'focal_length_mm': 540, 'mass': 4853, 'central_obstruction_mm': 0},
        'TeleVue_NP127fli': {'aperture_mm': 127, 'focal_length_mm': 660, 'mass': 6577, 'central_obstruction_mm': 0},
        'TeleVue_TV_60': {'aperture_mm': 60, 'focal_length_mm': 360, 'mass': 1361, 'central_obstruction_mm': 0},
        'TeleVue_TV_76': {'aperture_mm': 76, 'focal_length_mm': 480, 'mass': 2313, 'central_obstruction_mm': 0},
        'TeleVue_TV_85': {'aperture_mm': 85, 'focal_length_mm': 600, 'mass': 2767, 'central_obstruction_mm': 0},
        'TeleVue_TV_102': {'aperture_mm': 102, 'focal_length_mm': 880, 'mass': 4173, 'central_obstruction_mm': 0},
        'TeleVue_TV_NP127is': {'aperture_mm': 127, 'focal_length_mm': 660, 'mass': 6577, 'central_obstruction_mm': 0},
        'TeleVue_TV_NP101': {'aperture_mm': 101, 'focal_length_mm': 540, 'mass': 4853, 'central_obstruction_mm': 0},
    }

    errors = []
    for key, specs in expected.items():
        if key not in database:
            errors.append(f"Missing model: {key}")
            continue

        db_entry = database[key]
        for field, value in specs.items():
            if db_entry.get(field) != value:
                errors.append(f"Mismatch for {key} field {field}: expected {value}, got {db_entry.get(field)}")

    if errors:
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("All TeleVue specifications verified successfully!")

if __name__ == "__main__":
    verify_televue_specs()
