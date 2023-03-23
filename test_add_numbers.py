import unittest
from add_numbers import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(10, 10), 20)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)
        self.assertEqual(add_numbers(-10, 5), -5)
        self.assertEqual(add_numbers(-5, -5), -10)
    
    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add_numbers(1.5, 2.5), 4.0)
    
    def test_add_string_numbers(self):
        with self.assertRaises(TypeError):
            add_numbers('2', 3)
            add_numbers(2, '3')
            add_numbers('2', '3')

if __name__ == '__main__':
    unittest.main()
