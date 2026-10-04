from pathlib import Path


def lines_of_code(path: Path) -> int:
    with open(path, "r") as f:
        lines = f.read().splitlines()

    count = 0

    in_string = False
    quote_char = ""
    is_triple = False

    for line in lines:
        i = 0
        has_code = False

        while i < len(line):
            c = line[i]

            if in_string:
                if c not in " \t":
                    has_code = True

                if is_triple:
                    if c == quote_char and line[i : i + 3] == quote_char * 3:
                        in_string = False
                        i += 3
                    elif c == "\\":
                        i += 2
                    else:
                        i += 1
                else:
                    if c == quote_char:
                        in_string = False
                        i += 1
                    elif c == "\\":
                        i += 2
                    else:
                        i += 1

            else:
                if c == "#":
                    break
                elif c in "\"'":
                    if c not in " \t":
                        has_code = True

                    if line[i : i + 3] == c * 3:
                        in_string = True
                        is_triple = True
                        quote_char = c
                        i += 3
                    else:
                        in_string = True
                        is_triple = False
                        quote_char = c
                        i += 1
                else:
                    if c not in " \t":
                        has_code = True
                    i += 1

        if has_code:
            count += 1

    return count
