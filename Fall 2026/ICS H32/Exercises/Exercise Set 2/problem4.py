import random
import socket
from typing import TextIO


SHAKESPEARE_HOST = 'circinus-32.ics.uci.edu'
SHAKESPEARE_PORT = 1564

COUNTS_MESSAGE = 'SHAKESPEARE_COUNTS'
INSULT_MESSAGE = 'SHAKESPEARE_INSULT'
GOODBYE_MESSAGE = 'SHAKESPEARE_GOODBYE'

END_OF_LINE = '\r\n'


def run() -> None:
    server = socket.socket()

    try:
        server.connect((SHAKESPEARE_HOST, SHAKESPEARE_PORT))
        input_stream = server.makefile('r')
        output_stream = server.makefile('w')

        try:
            counts = _read_counts(input_stream, output_stream)
            print(_read_insult(input_stream, output_stream, counts))
            print(_read_goodbye(input_stream, output_stream))
        finally:
            input_stream.close()
            output_stream.close()
    finally:
        server.close()


def _read_counts(input_stream: TextIO, output_stream: TextIO) -> list[int]:
    _send_line(output_stream, COUNTS_MESSAGE)
    return [int(count) for count in input_stream.readline().split()]


def _read_insult(input_stream: TextIO, output_stream: TextIO,
                 counts: list[int]) -> str:
    choices = [str(random.randint(1, count)) for count in counts]
    _send_line(output_stream, f'{INSULT_MESSAGE} {" ".join(choices)}')
    return input_stream.readline().strip()


def _read_goodbye(input_stream: TextIO, output_stream: TextIO) -> str:
    _send_line(output_stream, GOODBYE_MESSAGE)
    return input_stream.readline().strip()


def _send_line(output_stream: TextIO, text: str) -> None:
    output_stream.write(text + END_OF_LINE)
    output_stream.flush()


if __name__ == '__main__':
    run()
