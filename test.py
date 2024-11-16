import unittest
from add import add

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result1 = add(6, 4)
        result2 = add(-1, 2)
        self.assertEqual(result1, 10)
        self.assertEqual(result2, 1)

if _name_ == "_main_":
    unittest.main()
