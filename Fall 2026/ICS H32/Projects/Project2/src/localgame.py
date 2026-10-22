from connectfour import EMPTY, GameState, drop, pop, winner
from gamerenderer import ask_for_board_size, ask_for_move, is_board_full, show_result, show_turn


def _run_turn(game_state: GameState) -> GameState:
    '''Shows the current player the board, asks for a move, and returns the state that results'''
    show_turn(game_state)
    kind, column_number = ask_for_move(game_state)

    if kind == 'pop':
        return pop(game_state, column_number - 1)
    else:
        return drop(game_state, column_number - 1)


def _game_loop() -> None:
    '''Plays one game from beginning to end'''
    print('Welcome to Connect Four!')
    print('Choose a column by typing its number; the far-left column is 1.')
    print('Type p before the number (e.g. p3) to pop the bottom piece of that column instead.')

    game_state = ask_for_board_size()

    while winner(game_state) == EMPTY and not is_board_full(game_state):
        game_state = _run_turn(game_state)

    show_result(game_state)


if __name__ == '__main__':
    _game_loop()
