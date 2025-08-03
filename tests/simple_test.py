import unittest

class SimpleTest(unittest.TestCase):
    def test_simple(self):
        print("Running simple test")
        self.assertEqual(1, 1)
        print("Finished simple test")
