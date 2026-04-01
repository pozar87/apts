import ast
import os

def verify():
    filepath = 'apts/opticalequipment/telescope/vendors/sky_watcher.py'
    with open(filepath, 'r') as f:
        tree = ast.parse(f.read())

    database = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == '_DATABASE':
                    database = ast.literal_eval(node.value)
                    break

    expected = {
        'Sky_Watcher_Evolux_62ED': {'aperture_mm': 62, 'focal_length_mm': 400, 'mass': 2500, 'central_obstruction_mm': 0},
        'Sky_Watcher_Evolux_82ED': {'aperture_mm': 82, 'focal_length_mm': 530, 'mass': 2920, 'central_obstruction_mm': 0},
        'Sky_Watcher_Explorer_200P': {'aperture_mm': 200, 'focal_length_mm': 1000, 'mass': 8800, 'central_obstruction_mm': 52},
        'Sky_Watcher_Quattro_200P': {'aperture_mm': 205, 'focal_length_mm': 800, 'mass': 9500, 'central_obstruction_mm': 70}
    }

    for model, specs in expected.items():
        if model not in database:
            print(f"FAILED: {model} not found in database")
            return False

        actual = database[model]
        for key, value in specs.items():
            if actual.get(key) != value:
                print(f"FAILED: {model} {key} expected {value}, got {actual.get(key)}")
                return False
        print(f"PASSED: {model}")

    return True

if __name__ == '__main__':
    if verify():
        print("Static verification successful!")
        exit(0)
    else:
        print("Static verification failed!")
        exit(1)
