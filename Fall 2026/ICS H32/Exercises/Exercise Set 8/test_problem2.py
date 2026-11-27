import math
import unittest

import problem2


class TestZeroCalc(unittest.TestCase):
    def test_returns_zero_for_number(self):
        self.assertEqual(problem2.zero_calc(7), 0)

    def test_returns_zero_for_string(self):
        self.assertEqual(problem2.zero_calc('anything'), 0)

    def test_returns_zero_for_list(self):
        self.assertEqual(problem2.zero_calc([1, 2, 3]), 0)


class TestSquareCalc(unittest.TestCase):
    def test_squares_positive_integer(self):
        self.assertEqual(problem2.square_calc(4), 16)

    def test_squares_negative_integer(self):
        self.assertEqual(problem2.square_calc(-4), 16)

    def test_squares_zero(self):
        self.assertEqual(problem2.square_calc(0), 0)

    def test_squares_float(self):
        self.assertAlmostEqual(problem2.square_calc(2.5), 6.25)

    def test_squaring_a_string_fails(self):
        with self.assertRaises(TypeError):
            problem2.square_calc('Boo')


class TestCubeCalc(unittest.TestCase):
    def test_cubes_positive_integer(self):
        self.assertEqual(problem2.cube_calc(3), 27)

    def test_cubes_negative_integer(self):
        self.assertEqual(problem2.cube_calc(-3), -27)

    def test_cubes_zero(self):
        self.assertEqual(problem2.cube_calc(0), 0)

    def test_cubes_float(self):
        self.assertAlmostEqual(problem2.cube_calc(1.5), 3.375)


class TestLengthCalc(unittest.TestCase):
    def test_length_of_string(self):
        self.assertEqual(problem2.length_calc('Boo'), 3)

    def test_length_of_empty_string(self):
        self.assertEqual(problem2.length_calc(''), 0)

    def test_length_of_list(self):
        self.assertEqual(problem2.length_calc([1, 2, 3, 4]), 4)

    def test_length_of_tuple(self):
        self.assertEqual(problem2.length_calc((1, 2)), 2)

    def test_length_of_integer_fails(self):
        with self.assertRaises(TypeError):
            problem2.length_calc(17)


class TestSquareRootCalc(unittest.TestCase):
    def test_root_of_perfect_square(self):
        self.assertAlmostEqual(problem2.square_root_calc(81), 9.0)

    def test_root_of_zero(self):
        self.assertAlmostEqual(problem2.square_root_calc(0), 0.0)

    def test_root_of_imperfect_square(self):
        self.assertAlmostEqual(problem2.square_root_calc(2), math.sqrt(2))

    def test_root_of_negative_fails(self):
        with self.assertRaises(ValueError):
            problem2.square_root_calc(-1)


class TestMultiplyByCalc(unittest.TestCase):
    def test_multiplies_by_positive(self):
        self.assertEqual(problem2.multiply_by_calc(3, 7), 21)

    def test_multiplies_by_zero(self):
        self.assertEqual(problem2.multiply_by_calc(0, 7), 0)

    def test_multiplies_by_negative(self):
        self.assertEqual(problem2.multiply_by_calc(-2, 7), -14)

    def test_multiplies_float(self):
        self.assertAlmostEqual(problem2.multiply_by_calc(2.5, 4), 10.0)

    def test_repeats_a_string(self):
        self.assertEqual(problem2.multiply_by_calc(3, 'ab'), 'ababab')


class TestRunCalcs(unittest.TestCase):
    def test_no_calcs_returns_starting_value(self):
        self.assertEqual(problem2.run_calcs([], 80), 80)

    def test_single_calc(self):
        self.assertEqual(problem2.run_calcs([problem2.square_calc], 4), 16)

    def test_applies_calcs_in_sequence(self):
        self.assertEqual(
            problem2.run_calcs([problem2.square_calc, problem2.square_calc], 4),
            256,
        )

    def test_order_matters(self):
        def add_one(n):
            return n + 1

        def double(n):
            return n * 2

        self.assertEqual(problem2.run_calcs([add_one, double], 3), 8)
        self.assertEqual(problem2.run_calcs([double, add_one], 3), 7)

    def test_incompatible_chain_fails(self):
        with self.assertRaises(TypeError):
            problem2.run_calcs(
                [problem2.square_root_calc, problem2.length_calc], 81
            )

    def test_accepts_a_plain_function(self):
        def double(n):
            return n * 2

        self.assertEqual(problem2.run_calcs([double, double], 3), 12)

    def test_accepts_a_closure_carrying_state(self):
        def multiply_by(multiplier):
            def calc(n):
                return n * multiplier
            return calc

        self.assertEqual(problem2.run_calcs([multiply_by(3)], 7), 21)


if __name__ == '__main__':
    unittest.main()
