import ast
import unittest

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

class TestAskarSpecsStatic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = extract_database('apts/opticalequipment/telescope/vendors/askar.py')

    def test_fra300_pro(self):
        specs = self.db['Askar_FRA300_Pro']
        self.assertEqual(specs['aperture_mm'], 60)
        self.assertEqual(specs['focal_length_mm'], 300)
        self.assertEqual(specs['mass'], 2260)
        self.assertEqual(specs['central_obstruction_mm'], 0)

    def test_fra400(self):
        specs = self.db['Askar_FRA400']
        self.assertEqual(specs['aperture_mm'], 72)
        self.assertEqual(specs['focal_length_mm'], 400)
        self.assertEqual(specs['mass'], 2560)
        self.assertEqual(specs['central_obstruction_mm'], 0)

    def test_103apo(self):
        specs = self.db['Askar_103APO']
        self.assertEqual(specs['aperture_mm'], 103)
        self.assertEqual(specs['focal_length_mm'], 700.4)
        self.assertEqual(specs['mass'], 4750)

    def test_v60q(self):
        specs = self.db['Askar_V_60Q']
        self.assertEqual(specs['focal_length_mm'], 360)
        self.assertEqual(specs['mass'], 2860)

    def test_fma230(self):
        specs = self.db['Askar_FMA_230']
        self.assertEqual(specs['focal_length_mm'], 275)
        self.assertEqual(specs['mass'], 1200)

    def test_203apo(self):
        specs = self.db['Askar_203APO']
        self.assertEqual(specs['aperture_mm'], 203)
        self.assertEqual(specs['focal_length_mm'], 1421)
        self.assertEqual(specs['mass'], 14900)

    def test_all_have_co(self):
        for key, specs in self.db.items():
            self.assertIn('central_obstruction_mm', specs, f"{key} is missing central_obstruction_mm")
            self.assertEqual(specs['central_obstruction_mm'], 0, f"{key} should have 0 central obstruction")

if __name__ == '__main__':
    unittest.main()
