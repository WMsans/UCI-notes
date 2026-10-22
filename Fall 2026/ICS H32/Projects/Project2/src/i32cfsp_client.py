import socket
from collections import namedtuple


DROP = 'DROP'
POP = 'POP'

OKAY = 'OKAY'
INVALID = 'INVALID'
READY = 'READY'
WINNER_RED = 'WINNER_RED'
WINNER_YELLOW = 'WINNER_YELLOW'

WINNERS = (WINNER_RED, WINNER_YELLOW)


I32CFSPConnection = namedtuple('I32CFSPConnection', ['socket', 'input', 'output'])


I32CFSPMove = namedtuple('I32CFSPMove', ['operation', 'column'])


# Errors

class I32CFSPError(Exception):
    '''Raised for any way that a I32CFSP conversation can go wrong'''


class I32CFSPProtocolError(I32CFSPError):
    '''Raised when the server says something the protocol does not allow'''


class I32CFSPInvalidMoveError(I32CFSPError):
    '''Raised when the server rejects a move that we made'''


# Methods

def connect(host: str, port: int) -> I32CFSPConnection:
    '''
    Connects to a I32CFSP server running on the given host and listening on
    the given port, returning a I32CFSPConnection describing that connection.
    '''
    connection_socket = socket.socket()

    try:
        connection_socket.connect((host, port))
    except OSError:
        connection_socket.close()
        raise

    return I32CFSPConnection(
        socket = connection_socket,
        input = connection_socket.makefile('r'),
        output = connection_socket.makefile('w'))


def hello(connection: I32CFSPConnection, username: str) -> None:
    '''Logs a user into the I32CFSP service.'''
    # The _write_line and _expect_line functions are written below.  Their goal
    # is to hide the details of interacting with the socket (e.g., putting the
    # correct newline sequence on the end of the line, remembering to flush the
    # output after writing it, etc.).  Notice how, given those tools, the code
    # we've written here is terse and clear, relative to what it would look like
    # if we had these details interspersed throughout this function.
    _write_line(connection, f'I32CFSP_HELLO {username}')

    _expect_line(connection, f'WELCOME {username}')


def setup_board(connection: I32CFSPConnection, columns: int, rows: int) -> None:
    '''
    Requests a game against the server's artificial intelligence on a board
    with the given number of columns and rows.
    '''
    _write_line(connection, f'AI_GAME {columns} {rows}')

    _expect_line(connection, READY)


def play_move(connection: I32CFSPConnection, operation: str, column: int) -> tuple[I32CFSPMove | None, str | None]:
    '''
    Sends the given move (either DROP or POP, with a column number counting
    from 1 at the far left) and returns a tuple describing the server's
    answer: the server's own move, and the status line that ended the exchange.

    Raises I32CFSPInvalidMoveError if the server rejected our move, or
    I32CFSPProtocolError if the server said anything the protocol disallows.
    '''
    if operation not in (DROP, POP):
        raise ValueError(f'operation must be {DROP} or {POP}')

    _write_line(connection, f'{operation} {column}')

    reply = _read_line(connection)

    if reply == INVALID:
        raise I32CFSPInvalidMoveError()
    if reply in WINNERS:
        return None, reply
    if reply != OKAY:
        raise I32CFSPProtocolError(f'expecting {OKAY}, received {reply!r}')

    server_move = _read_move(connection)
    status = _read_line(connection)

    if status == READY or status in WINNERS:
        return server_move, status

    raise I32CFSPProtocolError(f'expecting {READY} or a winner, received {status!r}')


def close(connection: I32CFSPConnection) -> None:
    '''Closes the connection to the I32CFSP server'''
    # To close the connection, we'll need to close the two pseudo-file objects
    # and the socket object.  We'll need to close the pseudo-file objects first
    # -- though, in practice, it doesn't matter whether we close the input or
    # the output one first -- and then the socket.
    connection.input.close()
    connection.output.close()
    connection.socket.close()


def _read_move(connection: I32CFSPConnection) -> I32CFSPMove:
    '''Reads the server's move, raising an exception unless it is well formed'''
    line = _read_line(connection)
    parts = line.split(' ')

    if len(parts) != 2 or parts[0] not in (DROP, POP) or not parts[1].isdigit() or int(parts[1]) < 1:
        raise I32CFSPProtocolError(f'illegal move from server: {line!r}')

    return I32CFSPMove(operation = parts[0], column = int(parts[1]))


def _read_line(connection: I32CFSPConnection) -> str:
    '''Reads a line of text sent from the server and returns it without the
    end-of-line sequence on the end of it'''
    line = connection.input.readline()

    if line.endswith('\r\n'):
        return line[:-2]
    if line.endswith('\n'):
        return line[:-1]

    raise I32CFSPProtocolError(f'connection closed unexpectedly: {line!r}')


def _expect_line(connection: I32CFSPConnection, expected: str) -> None:
    '''Reads a line of text sent from the server, expecting it to contain a
    particular text.  If the line of text received is different, this function
    raises an exception; otherwise, the function has no effect.'''
    line = _read_line(connection)

    if line != expected:
        raise I32CFSPProtocolError(f'expecting {expected!r}, received {line!r}')


def _write_line(connection: I32CFSPConnection, line: str) -> None:
    '''Writes a line of text to the server, including the appropriate newline
    sequence, and ensures that it is sent immediately.'''
    connection.output.write(line + '\r\n')
    connection.output.flush()
