import ast

def verify_askar_reducers():
    filepath = 'apts/opticalequipment/reducer/vendors/askar.py'
    with open(filepath, 'r') as f:
        tree = ast.parse(f.read())

    askar_reducer_db = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'AskarReducer':
            for item in node.body:
                if isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name) and target.id == '_DATABASE':
                            askar_reducer_db = ast.literal_eval(item.value)
                            break

    if not askar_reducer_db:
        print("FAILED: AskarReducer _DATABASE not found")
        return False

    expected_entries = {
        'Askar_103APO_Reducer_0_6x': {'mass': 980, 'tside_thread': 'M68', 'cside_thread': 'M48', 'cside_gender': 'Male', 'required_backfocus': 55},
        'Askar_151PHQ_Reducer_0_7x': {'mass': 600, 'tside_thread': 'M68', 'cside_thread': 'M48', 'cside_gender': 'Male', 'required_backfocus': 55},
        'Askar_120APO_Reducer_0_8x': {'mass': 750, 'tside_thread': 'M68', 'cside_thread': 'M54', 'cside_gender': 'Male', 'required_backfocus': 55},
        'Askar_140APO_Reducer_0_8x': {'mass': 750, 'tside_thread': 'M68', 'cside_thread': 'M54', 'cside_gender': 'Male', 'required_backfocus': 55},
        'Askar_185APO_Reducer_0_8x': {'mass': 950, 'tside_thread': 'M68', 'cside_thread': 'M54', 'cside_gender': 'Male', 'required_backfocus': 55},
    }

    for key, expected in expected_entries.items():
        if key not in askar_reducer_db:
            print(f"FAILED: {key} not found in _DATABASE")
            return False
        entry = askar_reducer_db[key]
        for field, value in expected.items():
            if entry.get(field) != value:
                print(f"FAILED: {key} field '{field}' expected {value}, got {entry.get(field)}")
                return False
        print(f"VERIFIED: {key}")

    # Verify factory methods exist in AskarReducer
    methods = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'AskarReducer':
            methods = [item.name for item in node.body if isinstance(item, ast.FunctionDef)]
            break

    for key in ['Askar_120APO_Reducer_0_8x', 'Askar_140APO_Reducer_0_8x', 'Askar_185APO_Reducer_0_8x']:
        if key not in methods:
            print(f"FAILED: Factory method {key} not found in AskarReducer")
            return False
        print(f"VERIFIED: Factory method {key}")

    print("ALL VERIFICATIONS PASSED")
    return True

if __name__ == "__main__":
    if not verify_askar_reducers():
        exit(1)
