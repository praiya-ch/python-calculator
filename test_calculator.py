import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 2), 2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 3), 4)
        self.assertEqual(self.calc.divide(0, 1), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 7), 3)
        self.assertEqual(self.calc.modulo(10, 2), 0)

if __name__ == '__main__':
    unittest.main()