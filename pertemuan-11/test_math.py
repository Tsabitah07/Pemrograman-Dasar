import unittest

import math_operation as math_op

class TestMathOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_op.add(2, 3), 5)
        self.assertEqual(math_op.add(-1, 1), 0)
        self.assertEqual(math_op.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(math_op.subtract(5, 3), 2)
        self.assertEqual(math_op.subtract(0, 0), 0)
        self.assertEqual(math_op.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(math_op.multiply(4, 5), 20)
        self.assertEqual(math_op.multiply(-1, 1), -1)
        self.assertEqual(math_op.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(math_op.divide(10, 2), 5)
        self.assertEqual(math_op.divide(-6, -2), 3)
        with self.assertRaises(ValueError):
            math_op.divide(5, 0)