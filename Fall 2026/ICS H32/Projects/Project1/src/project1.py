import re
import shutil
from collections.abc import Iterator
from pathlib import Path


def parse_directory_from_input(input_string: str) -> tuple[bool, Path]:
    '''Parses a directory line into (recursive, path).'''
    if len(input_string) >= 3 and input_string[0] in ('D', 'R') and input_string[1] == ' ':
        recursive = input_string[0] == 'R'
        directory_path = Path(input_string[2:])

        if directory_path.is_dir():
            return (recursive, directory_path)

        raise LookupError("The provided directory does not exist.")

    raise ValueError("The provided string failed to parse.")


def iterating_directory(path: Path, recursive: bool) -> Iterator[Path]:
    '''Yields every eligible file under path, in the required order.'''
    entries = sorted(path.iterdir(), key=lambda entry: entry.name)
    files = [entry for entry in entries if entry.is_file()]
    subdirectories = [entry for entry in entries if entry.is_dir()]

    for file in files:
        yield file

    if recursive:
        for subdirectory in subdirectories:
            yield from iterating_directory(subdirectory, recursive)


def parse_search_from_input(input_string: str) -> tuple[str, str]:
    '''Parses a search-characteristic line into (kind, argument).'''
    if input_string == 'A':
        return ('A', '')

    if len(input_string) >= 3 and input_string[1] == ' ':
        kind = input_string[0]
        argument = input_string[2:]

        if kind in ('N', 'E', 'T'):
            return (kind, argument)

        if kind in ('<', '>') and re.fullmatch(r'\d+', argument):
            return (kind, argument)

    raise ValueError("The provided string failed to parse.")


def read_text(path: Path) -> str | None:
    '''Returns the contents of a text file, or None if it is not text.'''
    try:
        return path.read_text()
    except (OSError, UnicodeDecodeError):
        return None


def matches_search(path: Path, kind: str, argument: str) -> bool:
    '''Returns whether a file satisfies a parsed search characteristic.'''
    if kind == 'A':
        return True

    if kind == 'N':
        return path.name == argument

    if kind == 'E':
        extension = argument[1:] if argument.startswith('.') else argument
        return path.suffix[1:] == extension

    if kind == 'T':
        text = read_text(path)
        return text is not None and argument in text

    if kind == '<':
        return path.stat().st_size < int(argument)

    if kind == '>':
        return path.stat().st_size > int(argument)

    return False


def take_action(path: Path, action: str) -> None:
    '''Performs the chosen action on a single interesting file.'''
    if action == 'F':
        text = read_text(path)

        if text is None:
            print('NOT TEXT')
        else:
            print(text.split('\n', 1)[0].rstrip('\r'))

    elif action == 'D':
        shutil.copy2(path, path.with_name(path.name + '.dup'))

    elif action == 'T':
        path.touch()


def read_directory_line() -> tuple[bool, Path]:
    '''Reads directory lines until a valid one is entered.'''
    while True:
        try:
            return parse_directory_from_input(input())
        except (ValueError, LookupError):
            print('ERROR')


def read_search_line() -> tuple[str, str]:
    '''Reads search lines until a valid one is entered.'''
    while True:
        try:
            return parse_search_from_input(input())
        except ValueError:
            print('ERROR')


def read_action_line() -> str:
    '''Reads action lines until a valid one is entered.'''
    while True:
        action = input()

        if action in ('F', 'D', 'T'):
            return action

        print('ERROR')


def main() -> None:
    '''Runs the file search, narrowing, and action-taking program.'''
    recursive, directory = read_directory_line()

    files = list(iterating_directory(directory, recursive))

    for file in files:
        print(file)

    kind, argument = read_search_line()

    interesting = [file for file in files if matches_search(file, kind, argument)]

    for file in interesting:
        print(file)

    if not interesting:
        return

    action = read_action_line()

    for file in interesting:
        take_action(file, action)


if __name__ == '__main__':
    main()
