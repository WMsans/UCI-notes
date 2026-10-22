import i32cfsp_client
from connectfour import GameState, InvalidMoveError, columns, drop, pop, rows
from gamerenderer import ask_for_board_size, ask_for_move, ask_for_number, show_result, show_turn


def _ask_for_host() -> str:
    '''Asks for the host name or IP address where a server is running'''
    while True:
        try:
            host = input('Host name or IP address of the Connect Four server: ').strip()
        except EOFError:
            raise SystemExit()

        if host != '':
            return host

        print('Please type the host name or IP address of the server.')


def _ask_for_username() -> str:
    '''Asks for a username, which the protocol does not allow to contain whitespace'''
    while True:
        try:
            username = input('Username (no spaces or tabs): ').strip()
        except EOFError:
            raise SystemExit()

        if username != '' and not any(character.isspace() for character in username):
            return username

        print('A username cannot be empty or contain whitespace.')


def _apply_move(game_state: GameState, operation: str, column_number: int) -> GameState:
    '''
    Returns the game state that results from making the given move, where the
    operation is either DROP or POP and the column number counts from 1 at the
    far left.  Raises InvalidMoveError or ValueError if the move is not legal
    '''
    if operation == i32cfsp_client.POP:
        return pop(game_state, column_number - 1)
    elif operation == i32cfsp_client.DROP:
        return drop(game_state, column_number - 1)
    else:
        raise ValueError(f'unknown operation: {operation!r}')


def _game_loop(connection: i32cfsp_client.I32CFSPConnection, username: str) -> None:
    '''Plays one game against the server, from the greeting to the last move'''
    i32cfsp_client.hello(connection, username)

    game_state = ask_for_board_size()
    i32cfsp_client.setup_board(connection, columns(game_state), rows(game_state))

    while True:
        show_turn(game_state)
        kind, column_number = ask_for_move(game_state)
        game_state = _apply_move(game_state, kind.upper(), column_number)

        try:
            server_move, status = i32cfsp_client.play_move(connection, kind.upper(), column_number)
        except i32cfsp_client.I32CFSPInvalidMoveError:
            print('The server rejected a move that the rules allow, so the game is over.')
            return

        if server_move is not None:
            print(f'The server moves: {server_move.operation} {server_move.column}')

            try:
                game_state = _apply_move(game_state, server_move.operation, server_move.column)
            except (InvalidMoveError, ValueError):
                print('The server made an illegal move, so the game is over.')
                return

        if status != i32cfsp_client.READY:
            show_result(game_state)
            return


def _run() -> None:
    '''Asks where to connect, connects, and plays one game'''
    print('Welcome to Connect Four!')
    print('You are the red player and move first; the server plays yellow.')
    print()

    host = _ask_for_host()
    port = ask_for_number('Port number the server is listening on: ')
    username = _ask_for_username()

    try:
        connection = i32cfsp_client.connect(host, port)
    except (OSError, OverflowError) as error:
        print(f'Could not connect to {host} on port {port}: {error}')
        return

    try:
        _game_loop(connection, username)
    except (i32cfsp_client.I32CFSPError, OSError) as error:
        print(f'The conversation with the server ended early: {error}')
    finally:
        i32cfsp_client.close(connection)


if __name__ == '__main__':
    _run()
