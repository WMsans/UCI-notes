from connectfour import *


def _get_full_side_name(side : int) -> str:
    return ["EMPTY", "RED", "YELLOW"][side]

def _get_symbol(side : int) -> str:
    return ['.', 'R', 'Y'][side]



def _format_board(game_state : GameState) -> str:
    '''
    Returns a string showing the board of the given game state, with the
    column numbers written above it.
    '''
    column_numbers = ''.join(f'{column_number + 1:<3}' for column_number in range(columns(game_state)))
    lines = [column_numbers.rstrip()]

    for row in range(rows(game_state)):
        lines.append(''.join(f'{_get_symbol(game_state.board[column][row]):<3}'
                             for column in range(columns(game_state))).rstrip())

    return '\n'.join(lines)



def _is_board_full(game_state : GameState) -> bool:
    '''Returns True if every cell on the board is filled with a piece'''
    for column in range(columns(game_state)):
        for row in range(rows(game_state)):
            if game_state.board[column][row] == EMPTY:
                return False

    return True



def _ask_for_number(question : str) -> int:
    '''Asks the user for a whole number, asking again until one is typed'''
    while True:
        try:
            return int(input(question))
        except ValueError:
            print('That is not a whole number. Please try again.')
        except EOFError:
            raise SystemExit()



def _ask_for_board_size() -> GameState:
    '''Asks the user for the board's size, asking again until it is valid'''
    while True:
        columns_cnt = _ask_for_number(f'How many columns (between {MIN_COLUMNS} and {MAX_COLUMNS})? ')
        rows_cnt = _ask_for_number(f'How many rows (between {MIN_ROWS} and {MAX_ROWS})? ')

        try:
            return new_game(columns_cnt, rows_cnt)
        except ValueError as error:
            print(f'{error}. Please try again.')



def _ask_for_move(game_state : GameState) -> tuple[str, int]:
    '''
    Asks the user for a move, returning the kind of move (either 'drop' or
    'pop') and a column number counting from 1; asks again until both are
    well formed.
    '''
    while True:
        try:
            answer = input(f'Enter a column number from 1 to {columns(game_state)} to drop a piece, '
                           f'or p plus the number (e.g. p3) to pop that column: ').strip().lower()
        except EOFError:
            raise SystemExit()

        move_kind = 'drop'
        if answer.startswith('p'):
            move_kind = 'pop'
            answer = answer[1:].removeprefix('op').strip()

        try:
            column_number = int(answer)
        except ValueError:
            print('That is not a column number. Please try again.')
            continue

        if not 1 <= column_number <= columns(game_state):
            print(f'There is no column {column_number}. Please try again.')
            continue

        return move_kind, column_number



def _run_turn(current_state : GameState) -> GameState:
    '''Asks the current player for a move and returns the resulting game state'''
    print()
    print("It is " + str(_get_full_side_name(current_state.turn)) + "\'s turn.")
    print(_format_board(current_state))

    while True:
        move_kind, column_number = _ask_for_move(current_state)

        try:
            if move_kind == 'pop':
                return pop(current_state, column_number - 1)
            else:
                return drop(current_state, column_number - 1)
        except InvalidMoveError:
            if move_kind == 'pop':
                print(f'Column {column_number} cannot be popped: it is empty, or its bottom piece is not '
                      + str(_get_full_side_name(current_state.turn)) + '. Please try again.')
            else:
                print(f'Column {column_number} is full. Please try again.')



def _game_loop():
    try:
        print('Welcome to Connect Four!')
        print('Choose a column by typing its number; the far-left column is 1.')
        print('Type p before the number (e.g. p3) to pop the bottom piece of that column instead.')
        print()

        current_state : GameState = _ask_for_board_size()

        while winner(current_state) == EMPTY and not _is_board_full(current_state):
            current_state = _run_turn(current_state)

        print()
        print(_format_board(current_state))

        if winner(current_state) == EMPTY:
            print('The board is full, so the game is a draw.')
        else:
            print(str(_get_full_side_name(winner(current_state))) + ' wins!')
    finally:
        print("Game Over")



if __name__ == "__main__":
    _game_loop()
