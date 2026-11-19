from collections.abc import Sequence

COLORS = frozenset('STVWXYZ')

EMPTY = 'empty'
EMPTY_COLOR = ' '
FROZEN = 'frozen'
MATCHED = 'matched'
FALLER = 'faller'
LANDED = 'landed'

_DIRECTIONS = ((0, 1), (1, 0), (1, 1), (1, -1))


class ColumnsError(Exception):
    pass


class _Jewel:
    __slots__ = ('color', 'matched')

    def __init__(self, color: str):
        self.color = color
        self.matched = False


class ColumnsGame:
    def __init__(self, rows: int, cols: int, contents: Sequence[str] = ()):
        if not isinstance(rows, int) or not isinstance(cols, int):
            raise ColumnsError('The number of rows and columns must be integers.')
        if rows < 1 or cols < 1:
            raise ColumnsError('The field must have at least one row and one column.')

        self._rows = rows
        self._cols = cols
        self._grid: list[list[_Jewel | None]] = [[None] * cols for _ in range(rows)]
        self._faller: list[str] = []
        self._faller_col = 0
        self._faller_bottom = 0
        self._game_over = False
        self._partial_freeze = False
        self._frozen_col = 0

        if contents:
            self._load(contents)

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def game_over(self) -> bool:
        return self._game_over

    def cell(self, row: int, col: int) -> tuple[str, str]:
        if not (0 <= row < self._rows and 0 <= col < self._cols):
            raise ColumnsError(f'There is no cell at row {row}, column {col}.')

        jewel = self._grid[row][col]

        if jewel is not None:
            return jewel.color, MATCHED if jewel.matched else FROZEN

        index = self._faller_bottom - row

        if col == self._faller_col and 0 <= index < len(self._faller):
            return self._faller[index], FALLER if self._can_move_down() else LANDED

        return EMPTY_COLOR, EMPTY

    def create_faller(self, col: int, colors: list[str]) -> None:
        if self._game_over:
            raise ColumnsError('The game is over.')
        if self._faller:
            raise ColumnsError('There is already a faller.')
        if not 0 <= col < self._cols:
            raise ColumnsError(f'There is no column {col}.')
        if len(colors) != 3 or any(color not in COLORS for color in colors):
            raise ColumnsError('A faller needs exactly three valid colors.')

        if self._grid[0][col] is not None:
            self._game_over = True
            return

        self._faller = list(reversed(colors))
        self._faller_col = col
        self._faller_bottom = 0

    def rotate(self) -> None:
        if self._game_over:
            raise ColumnsError('The game is over.')
        if not self._faller:
            raise ColumnsError('There is no faller to rotate.')

        self._faller = [self._faller[1], self._faller[2], self._faller[0]]

    def move_left(self) -> None:
        self._move(-1)

    def move_right(self) -> None:
        self._move(1)

    def time_passes(self) -> None:
        if self._game_over:
            raise ColumnsError('The game is over.')

        if self._has_matched():
            self._remove_matches()
            self._mark_matches()
        elif self._faller:
            if self._can_move_down():
                self._faller_bottom += 1
            else:
                self._freeze()
        else:
            return

        self._evaluate_game_over()

    def _move(self, offset: int) -> None:
        if self._game_over:
            raise ColumnsError('The game is over.')
        if not self._faller:
            raise ColumnsError('There is no faller to move.')

        col = self._faller_col + offset

        if not 0 <= col < self._cols:
            raise ColumnsError('The faller would move off the field.')

        for row in self._faller_rows():
            if row >= 0 and self._grid[row][col] is not None:
                raise ColumnsError('The faller is blocked.')

        self._faller_col = col

    def _faller_rows(self):
        return [self._faller_bottom - index for index in range(3)]

    def _can_move_down(self) -> bool:
        return (self._faller_bottom + 1 < self._rows
                and self._grid[self._faller_bottom + 1][self._faller_col] is None)

    def _freeze(self) -> None:
        placed = 0

        for index, color in enumerate(self._faller):
            row = self._faller_bottom - index

            if row >= 0:
                self._grid[row][self._faller_col] = _Jewel(color)
                placed += 1

        self._partial_freeze = placed < 3
        self._frozen_col = self._faller_col
        self._faller = []
        self._mark_matches()

    def _evaluate_game_over(self) -> None:
        if not self._partial_freeze or self._has_matched():
            return

        if all(self._grid[row][self._frozen_col] is not None for row in range(self._rows)):
            self._game_over = True

        self._partial_freeze = False

    def _load(self, contents: Sequence[str]) -> None:
        if len(contents) != self._rows:
            raise ColumnsError(f'Expected {self._rows} rows of contents.')

        for row, line in enumerate(contents):
            if len(line) != self._cols:
                raise ColumnsError(f'Expected {self._cols} characters in row {row}.')

            for col, character in enumerate(line):
                if character == ' ':
                    continue
                if character not in COLORS:
                    raise ColumnsError(f'{character!r} is not a color.')

                self._grid[row][col] = _Jewel(character)

        for col in range(self._cols):
            self._apply_gravity(col)

        self._mark_matches()

    def _has_matched(self) -> bool:
        return any(jewel is not None and jewel.matched
                   for row in self._grid for jewel in row)

    def _matching_positions(self) -> set[tuple[int, int]]:
        positions: set[tuple[int, int]] = set()

        for row in range(self._rows):
            for col in range(self._cols):
                jewel = self._grid[row][col]

                if jewel is None:
                    continue

                for row_step, col_step in _DIRECTIONS:
                    previous = row - row_step, col - col_step

                    if self._is_same_color(*previous, jewel.color):
                        continue

                    length = 1
                    next_row, next_col = row + row_step, col + col_step

                    while self._is_same_color(next_row, next_col, jewel.color):
                        length += 1
                        next_row += row_step
                        next_col += col_step

                    if length >= 3:
                        for index in range(length):
                            positions.add((row + row_step * index, col + col_step * index))

        return positions

    def _is_same_color(self, row: int, col: int, color: str) -> bool:
        if not (0 <= row < self._rows and 0 <= col < self._cols):
            return False

        jewel = self._grid[row][col]

        return jewel is not None and jewel.color == color

    def _mark_matches(self) -> None:
        for row, col in self._matching_positions():
            self._grid[row][col].matched = True

    def _remove_matches(self) -> None:
        emptied = set()

        for row in range(self._rows):
            for col in range(self._cols):
                jewel = self._grid[row][col]

                if jewel is not None and jewel.matched:
                    self._grid[row][col] = None
                    emptied.add(col)

        for col in emptied:
            self._apply_gravity(col)

    def _apply_gravity(self, col: int) -> None:
        jewels = [self._grid[row][col] for row in range(self._rows)
                  if self._grid[row][col] is not None]

        for row in range(self._rows):
            self._grid[row][col] = None

        for index, jewel in enumerate(reversed(jewels)):
            self._grid[self._rows - 1 - index][col] = jewel
