try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '../src'
            )
        )
    )
except ImportError:
    raise


import unittest
import src.calculator as calculator


class TestCalculator(unittest.TestCase):
    def test_sum_five_plus_five_must_return_ten(self):
        self.assertEqual(calculator.sum(5, 5), 10)

    def test_sum_with_many_inputs(self):
        x_y_outputs = ((1, 1, 1+1), (2, 2, 2+2), (3, 3, 3+3), (4, 4, 4+4),
                       (5, 5, 5+5), (6, 6, 6+6), (7, 7, 7+7), (8, 8, 8+8),
                       (9, 9, 9+9), (10, 10, 10+10), (11, 11, 11+11),
                       (12, 12, 12+12), (13, 13, 13+13), (14, 14, 14+14),
                       (15, 15, 15+15))

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(calculator.sum(x, y), output)

    def test_sum_x_should_return_type_error(self):
        with self.assertRaises(TypeError):
            calculator.sum('1', 1)

    def test_sum_y_should_return_type_error(self):
        with self.assertRaises(TypeError):
            calculator.sum(1, '1')


if __name__ == "__main__":
    unittest.main(verbosity=2)
