import unittest

from columns import ColumnsError, ColumnsGame


def colors(game):
    return [[game.cell(row, col)[0] for col in range(game.cols)] for row in range(game.rows)]


def styles(game):
    return [[game.cell(row, col)[1] for col in range(game.cols)] for row in range(game.rows)]


class TestStartingPosition(unittest.TestCase):
    def test_empty_field_has_the_right_size(self):
        game = ColumnsGame(4, 3)
        self.assertEqual((4, 3), (game.rows, game.cols))
        self.assertEqual([[' '] * 3] * 4, colors(game))
        self.assertFalse(game.game_over)

    def test_contents_are_used_as_given_when_nothing_moves(self):
        game = ColumnsGame(3, 3, ['XYZ', 'XYZ', 'XYZ'])
        self.assertEqual([['X', 'Y', 'Z']] * 3, colors(game))

    def test_contents_fall_immediately(self):
        game = ColumnsGame(3, 3, ['X  ', '   ', '   '])
        self.assertEqual([' ', ' ', 'X'], [colors(game)[row][0] for row in range(3)])

    def test_contents_falling_can_trigger_matching(self):
        game = ColumnsGame(3, 3, ['X  ', 'X  ', 'XY '])
        self.assertEqual(['matched'] * 3, [styles(game)[row][0] for row in range(3)])

    def test_initial_matches_are_marked(self):
        game = ColumnsGame(3, 3, ['   ', '   ', 'XXX'])
        self.assertEqual(['matched'] * 3, styles(game)[2])

    def test_bad_dimensions_are_rejected(self):
        self.assertRaises(ColumnsError, ColumnsGame, 0, 3)
        self.assertRaises(ColumnsError, ColumnsGame, 3, 0)

    def test_bad_contents_are_rejected(self):
        self.assertRaises(ColumnsError, ColumnsGame, 2, 3, ['XXX'])
        self.assertRaises(ColumnsError, ColumnsGame, 2, 3, ['XX', 'XXX'])
        self.assertRaises(ColumnsError, ColumnsGame, 2, 3, ['AA ', '   '])


class TestFaller(unittest.TestCase):
    def test_only_the_bottom_jewel_is_visible_at_first(self):
        game = ColumnsGame(4, 3)
        game.create_faller(2, ['X', 'Y', 'Z'])
        self.assertEqual(['Z', ' ', ' ', ' '], [colors(game)[row][2] for row in range(4)])
        self.assertEqual('faller', styles(game)[0][2])

    def test_faller_falls_one_row_per_tick(self):
        game = ColumnsGame(4, 3)
        game.create_faller(0, ['X', 'Y', 'Z'])
        game.time_passes()
        self.assertEqual(['Y', 'Z', ' ', ' '], [colors(game)[row][0] for row in range(4)])

    def test_faller_lands_then_freezes(self):
        game = ColumnsGame(4, 3)
        game.create_faller(0, ['X', 'Y', 'Z'])

        for _ in range(3):
            game.time_passes()

        self.assertEqual([' ', 'X', 'Y', 'Z'], [colors(game)[row][0] for row in range(4)])
        self.assertEqual(['landed'] * 3, [styles(game)[row][0] for row in range(1, 4)])

        game.time_passes()
        self.assertEqual(['frozen'] * 3, [styles(game)[row][0] for row in range(1, 4)])

    def test_second_faller_is_rejected_while_one_is_falling(self):
        game = ColumnsGame(4, 3)
        game.create_faller(0, ['X', 'Y', 'Z'])
        self.assertRaises(ColumnsError, game.create_faller, 1, ['X', 'Y', 'Z'])

    def test_creating_a_faller_in_a_full_column_ends_the_game(self):
        game = ColumnsGame(4, 1, ['X', 'Y', 'Z', 'S'])
        game.create_faller(0, ['X', 'Y', 'Z'])
        self.assertTrue(game.game_over)

    def test_bad_faller_parameters_are_rejected(self):
        game = ColumnsGame(4, 3)
        self.assertRaises(ColumnsError, game.create_faller, 3, ['X', 'Y', 'Z'])
        self.assertRaises(ColumnsError, game.create_faller, 0, ['X', 'Y'])
        self.assertRaises(ColumnsError, game.create_faller, 0, ['X', 'Y', 'A'])


class TestMovingAndRotating(unittest.TestCase):
    def setUp(self):
        self.game = ColumnsGame(4, 4)
        self.game.create_faller(1, ['X', 'Y', 'Z'])

    def test_moves_left_and_right(self):
        self.game.move_left()
        self.assertEqual('Z', colors(self.game)[0][0])
        self.game.move_right()
        self.game.move_right()
        self.assertEqual('Z', colors(self.game)[0][2])

    def test_cannot_move_off_the_field(self):
        game = ColumnsGame(4, 3)
        game.create_faller(1, ['X', 'Y', 'Z'])
        game.move_left()
        self.assertRaises(ColumnsError, game.move_left)
        game.move_right()
        game.move_right()
        self.assertRaises(ColumnsError, game.move_right)

    def test_cannot_move_into_frozen_jewels(self):
        game = ColumnsGame(4, 4, ['    ', '    ', '    ', 'X   '])
        game.create_faller(1, ['X', 'Y', 'Z'])

        for _ in range(3):
            game.time_passes()

        self.assertRaises(ColumnsError, game.move_left)

    def test_rotation_moves_the_bottom_jewel_to_the_top(self):
        self.game.rotate()

        for _ in range(3):
            self.game.time_passes()

        self.assertEqual([' ', 'Z', 'X', 'Y'],
                         [colors(self.game)[row][1] for row in range(4)])

    def test_rotation_without_a_faller_is_rejected(self):
        self.assertRaises(ColumnsError, ColumnsGame(4, 4).rotate)

    def test_moving_off_a_landing_spot_makes_the_faller_fall_again(self):
        game = ColumnsGame(4, 3, ['   ', '   ', '   ', ' X '])
        game.create_faller(1, ['X', 'Y', 'Z'])
        game.time_passes()
        game.time_passes()
        self.assertEqual('landed', styles(game)[1][1])
        game.move_right()
        self.assertEqual('faller', styles(game)[1][2])


class TestMatching(unittest.TestCase):
    def test_horizontal_match(self):
        game = ColumnsGame(1, 3, ['XXX'])
        self.assertEqual(['matched'] * 3, styles(game)[0])
        game.time_passes()
        self.assertEqual([' '] * 3, colors(game)[0])

    def test_vertical_match(self):
        game = ColumnsGame(3, 1, ['X', 'X', 'X'])
        self.assertEqual(['matched'] * 3, [styles(game)[row][0] for row in range(3)])

    def test_diagonal_matches_in_both_directions(self):
        down_right = ColumnsGame(4, 4, ['    ', 'X   ', 'YX  ', 'ZYXT'])
        self.assertEqual(['matched'] * 3,
                         [down_right.cell(row, row - 1)[1] for row in range(1, 4)])

        down_left = ColumnsGame(4, 4, ['    ', 'T  X', 'V XY', 'WXSZ'])
        self.assertEqual(['matched'] * 3,
                         [down_left.cell(row, 4 - row)[1] for row in range(1, 4)])

    def test_runs_longer_than_three(self):
        game = ColumnsGame(1, 4, ['XXXX'])
        self.assertEqual(['matched'] * 4, styles(game)[0])

    def test_two_matches_at_once(self):
        game = ColumnsGame(2, 3, ['XXX', 'YYY'])
        self.assertEqual(['matched'] * 3, styles(game)[0])
        self.assertEqual(['matched'] * 3, styles(game)[1])

    def test_two_jewels_do_not_match(self):
        game = ColumnsGame(1, 3, ['XX '])
        self.assertNotIn('matched', styles(game)[0])

    def test_jewels_above_a_match_drop_into_the_gap(self):
        game = ColumnsGame(3, 3, ['   ', '  S', 'XXX'])
        self.assertEqual(['matched'] * 3, styles(game)[2])
        game.time_passes()
        self.assertEqual([' ', ' ', 'S'], [colors(game)[row][2] for row in range(3)])

    def test_matched_jewels_are_gone_after_a_tick(self):
        game = ColumnsGame(3, 3, ['   ', 'S S', 'XXX'])
        game.time_passes()
        self.assertNotIn('matched', [style for row in styles(game) for style in row])


class TestEndOfGame(unittest.TestCase):
    def test_freezing_without_room_ends_the_game(self):
        game = ColumnsGame(4, 2, ['  ', '  ', 'X ', 'Y '])
        game.create_faller(0, ['S', 'X', 'Y'])
        game.time_passes()
        game.time_passes()
        self.assertTrue(game.game_over)

    def test_matching_can_postpone_the_end_of_the_game(self):
        game = ColumnsGame(4, 4, ['    ', ' SSY', 'XTWZ', 'ZVXT'])
        game.create_faller(0, ['Y', 'W', 'S'])
        game.time_passes()
        game.time_passes()   # the middle jewel is left outside the field
        self.assertFalse(game.game_over)
        game.time_passes()   # the Ss disappear, so the column has room again
        self.assertFalse(game.game_over)

    def test_no_play_after_the_game_is_over(self):
        game = ColumnsGame(4, 1, ['X', 'Y', 'Z', 'S'])
        game.create_faller(0, ['X', 'Y', 'Z'])
        self.assertRaises(ColumnsError, game.time_passes)
        self.assertRaises(ColumnsError, game.rotate)


if __name__ == '__main__':
    unittest.main()
