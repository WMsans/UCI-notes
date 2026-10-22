from connectfour import (EMPTY, MAX_COLUMNS, MAX_ROWS, MIN_COLUMNS, MIN_ROWS,
                         GameState, InvalidMoveError, columns, drop, new_game,
                         pop, rows, winner)


def get_full_side_name(side: int) -> str:
    '''Returns the name of the given player, or 'EMPTY' for an empty cell'''
    return ['EMPTY', 'RED', 'YELLOW'][side]


def get_symbol(side: int) -> str:
    '''Returns the single character that stands for the given player on the board'''
    return ['.', 'R', 'Y'][side]


def format_board(game_state: GameState) -> str:
    '''
    Returns a string showing the board of the given game state, with the
    column numbers written above it.
    '''
    column_numbers = ''.join(f'{column_number + 1:<3}' for column_number in range(columns(game_state)))
    lines = [column_numbers.rstrip()]

    for row in range(rows(game_state)):
        lines.append(''.join(f'{get_symbol(game_state.board[column][row]):<3}'
                             for column in range(columns(game_state))).rstrip())

    return '\n'.join(lines)


def is_board_full(game_state: GameState) -> bool:
    '''Returns True if every cell on the board is filled with a piece'''
    for column in range(columns(game_state)):
        for row in range(rows(game_state)):
            if game_state.board[column][row] == EMPTY:
                return False

    return True


def show_turn(game_state: GameState) -> None:
    '''Prints whose turn it is, followed by the current board'''
    print()
    print(f"It is {get_full_side_name(game_state.turn)}'s turn.")
    print(format_board(game_state))


def show_result(game_state: GameState) -> None:
    '''Prints the final board, followed by who won or that the game was a draw'''
    print()
    print(format_board(game_state))

    if winner(game_state) == EMPTY:
        print('The board is full, so the game is a draw.')
    else:
        print(f'{get_full_side_name(winner(game_state))} wins!')


def ask_for_number(question: str) -> int:
    '''Asks the user for a whole number, asking again until one is typed'''
    while True:
        try:
            return int(input(question))
        except ValueError:
            print('That is not a whole number. Please try again.')
        except EOFError:
            raise SystemExit()


def ask_for_board_size() -> GameState:
    '''Asks the user for the board's size, asking again until it is valid'''
    while True:
        columns_cnt = ask_for_number(f'How many columns (between {MIN_COLUMNS} and {MAX_COLUMNS})? ')
        rows_cnt = ask_for_number(f'How many rows (between {MIN_ROWS} and {MAX_ROWS})? ')

        try:
            return new_game(columns_cnt, rows_cnt)
        except ValueError as error:
            print(f'{error}. Please try again.')


def ask_for_move(game_state: GameState) -> tuple[str, int]:
    '''
    Asks the current player for a legal move, returning the kind of move
    (either 'drop' or 'pop') and a column number counting from 1.  Input that
    isn't a column number, and moves that the rules don't allow, are explained
    to the player, who is then asked again.
    '''
    while True:
        try:
            answer = input(f'Enter a column number from 1 to {columns(game_state)} to drop a piece, '
                           f'or p plus the number (e.g. p3) to pop that column: ').strip().lower()
        except EOFError:
            raise SystemExit()

        kind = 'drop'
        if answer.startswith('p'):
            kind = 'pop'
            answer = answer[1:].removeprefix('op').strip()

        try:
            column_number = int(answer)
        except ValueError:
            print('That is not a column number. Please try again.')
            continue

        try:
            if kind == 'pop':
                pop(game_state, column_number - 1)
            else:
                drop(game_state, column_number - 1)
        except ValueError:
            print(f'There is no column {column_number}. Please try again.')
        except InvalidMoveError:
            if kind == 'pop':
                print(f'Column {column_number} cannot be popped: it is empty, or its bottom piece is not '
                      f'{get_full_side_name(game_state.turn)}. Please try again.')
            else:
                print(f'Column {column_number} is full. Please try again.')
        else:
            return kind, column_number
