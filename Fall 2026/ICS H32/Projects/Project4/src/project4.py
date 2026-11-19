from columns import (EMPTY, FALLER, FROZEN, LANDED, MATCHED, ColumnsError,
                     ColumnsGame)

_STYLES = {
    EMPTY: '   ',
    FROZEN: ' {} ',
    MATCHED: '*{}*',
    FALLER: '[{}]',
    LANDED: '|{}|',
}


def render_field(game: ColumnsGame) -> None:
    for row in range(game.rows):
        line = '|'

        for col in range(game.cols):
            color, style = game.cell(row, col)
            line += _STYLES[style].format(color)

        print(line + '|')

    print(' ' + '-' * (3 * game.cols) + ' ')


def read_field() -> ColumnsGame:
    rows = int(input())
    cols = int(input())

    if input() == 'CONTENTS':
        return ColumnsGame(rows, cols, [input().ljust(cols) for _ in range(rows)])

    return ColumnsGame(rows, cols)


def game_loop(game: ColumnsGame) -> None:
    while True:
        render_field(game)

        if game.game_over:
            print('GAME OVER')
            return

        command = input()

        if command == 'Q':
            return

        try:
            handle_command(game, command)
        except ColumnsError:
            pass


def handle_command(game: ColumnsGame, command: str) -> None:
    if command == '':
        game.time_passes()
    elif command == 'R':
        game.rotate()
    elif command == '<':
        game.move_left()
    elif command == '>':
        game.move_right()
    elif command.startswith('F '):
        _, col, top, middle, bottom = command.split()
        game.create_faller(int(col) - 1, [top, middle, bottom])


def main() -> None:
    game_loop(read_field())


if __name__ == '__main__':
    main()
