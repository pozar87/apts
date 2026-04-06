import ast
import json

def extract_database(filepath):
    with open(filepath, 'r') as f:
        tree = ast.parse(f.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'AskarTelescope':
            for body_node in node.body:
                if isinstance(body_node, ast.Assign):
                    for target in body_node.targets:
                        if isinstance(target, ast.Name) and target.id == '_DATABASE':
                            return ast.literal_eval(body_node.value)
    return None

def verify_askar():
    database = extract_database('apts/opticalequipment/telescope/vendors/askar.py')
    if not database:
        print("Could not find _DATABASE in AskarTelescope class.")
        return

    print("Current Askar Telescope Database Content (via AST):")
    for key, specs in database.items():
        print(f"Key: {key}")
        print(f"  Brand: {specs.get('brand')}")
        print(f"  Name: {specs.get('name')}")
        print(f"  Aperture: {specs.get('aperture_mm')} mm")
        print(f"  Focal Length: {specs.get('focal_length_mm')} mm")
        print(f"  Mass: {specs.get('mass')} g")
        print(f"  Central Obstruction: {specs.get('central_obstruction_mm')} mm")
        print("-" * 20)

if __name__ == "__main__":
    verify_askar()
