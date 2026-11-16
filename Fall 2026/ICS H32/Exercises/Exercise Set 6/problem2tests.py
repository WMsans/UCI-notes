from problem2 import reverse_transpose, calculate_sums
import unittest


class ReverseTransposeTest(unittest.TestCase):
    def test_three_by_three_matrix(self):
        a = [['x', 'y', 'z'], ['w', 'v', 't'], ['p', 'r', 's']]

        self.assertEqual(reverse_transpose(a),
                         [['s', 't', 'z'], ['r', 'v', 'y'], ['p', 'w', 'x']])


    def test_single_cell_matrix(self):
        self.assertEqual(reverse_transpose([[42]]), [[42]])


    def test_single_row_becomes_single_column_reversed(self):
        self.assertEqual(reverse_transpose([[1, 2, 3]]), [[3], [2], [1]])


    def test_single_column_becomes_single_row_reversed(self):
        self.assertEqual(reverse_transpose([[1], [2], [3]]), [[3, 2, 1]])


    def test_rectangle_has_swapped_dimensions(self):
        a = [[1, 2, 3], [4, 5, 6]]

        self.assertEqual(reverse_transpose(a), [[6, 3], [5, 2], [4, 1]])


    def test_original_matrix_is_not_modified(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        separate_copy_of_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        reverse_transpose(a)

        self.assertEqual(a, separate_copy_of_a)


    def test_result_does_not_share_rows_with_original(self):
        a = [[1, 2], [3, 4]]
        b = reverse_transpose(a)

        b[0][0] = 'changed'

        self.assertEqual(a, [[1, 2], [3, 4]])


    def test_values_need_not_be_comparable(self):
        a = [[None, 'a'], [3.5, object()]]

        self.assertEqual(reverse_transpose(a), [[a[1][1], a[0][1]],
                                                [a[1][0], a[0][0]]])



class CalculateSumsTest(unittest.TestCase):
    def test_three_by_three_matrix(self):
        c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        calculate_sums(c)

        self.assertEqual(c, [[45, 33, 18], [39, 28, 15], [24, 17, 9]])


    def test_single_cell_matrix_is_unchanged(self):
        c = [[7]]

        calculate_sums(c)

        self.assertEqual(c, [[7]])


    def test_single_row_becomes_suffix_sums(self):
        c = [[1, 2, 3, 4]]

        calculate_sums(c)

        self.assertEqual(c, [[10, 9, 7, 4]])


    def test_single_column_becomes_suffix_sums(self):
        c = [[1], [2], [3]]

        calculate_sums(c)

        self.assertEqual(c, [[6], [5], [3]])


    def test_negative_numbers_are_included_in_the_sums(self):
        c = [[-1, -2], [-3, -4]]

        calculate_sums(c)

        self.assertEqual(c, [[-10, -6], [-7, -4]])


    def test_sums_use_only_cells_below_and_to_the_right(self):
        c = [[2, 5], [1, 10]]

        calculate_sums(c)

        self.assertEqual(c[0][1], 15)


    def test_modifies_the_given_list_in_place(self):
        c = [[1, 2], [3, 4]]
        returned = calculate_sums(c)

        self.assertIsNone(returned)
        self.assertEqual(c, [[10, 6], [7, 4]])



if __name__ == '__main__':
    unittest.main()
