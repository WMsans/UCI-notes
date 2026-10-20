from collections import namedtuple
from pathlib import Path

Student = namedtuple('Student', ['scores', 'grade'])
GradeRanges = dict[str, tuple[float, ...]]

def parse_line(line: str):
    '''Parse one line of a scores file.'''
    # Everything from a '#' on is a comment
    stripped = line.split('#')[0].strip()

    if stripped == '':
        return None

    parts = stripped.split()

    return parts[0], [float(score) for score in parts[1:]]


def total_score(scores: list[float]):
    '''Return the sum of the given raw scores.'''
    return sum(scores)


def grade_for_score(score: float, ranges: GradeRanges):
    '''Return the letter grade for the given total score, or None if the
    score falls in none of the given ranges.
    '''
    for grade, bounds in ranges.items():
        if len(bounds) == 1:
            if score >= bounds[0]:
                return grade
        elif len(bounds) == 2:
            if bounds[0] <= score < bounds[1]:
                return grade

    return None


def build_grade_report(path: Path, ranges: GradeRanges):
    '''Return a dictionary mapping each UCInetID in the file at the given
    path to a Student namedtuple holding that student's scores and grade.
    '''
    report: dict[str, Student] = {}

    with open(path, 'r') as score_file:
        lines = score_file.readlines()

    for line in lines:
        parsed = parse_line(line)

        if parsed is None:
            continue

        ucinetid, scores = parsed
        report[ucinetid] = Student(scores=scores,
                                   grade=grade_for_score(total_score(scores),
                                                         ranges))

    return report


assert parse_line('thornton 30 40 50') == ('thornton', [30.0, 40.0, 50.0])
assert parse_line('didnothing') == ('didnothing', [])

# Extra spaces between the fields are allowed.
assert parse_line('  thornton   30    40  ') == ('thornton', [30.0, 40.0])
assert parse_line('\tboo\t100\t') == ('boo', [100.0])

# Non-integer scores keep their value.
assert parse_line('a 1.5 2') == ('a', [1.5, 2.0])
assert parse_line('a -3') == ('a', [-3.0])

# Blank lines, whitespace-only lines, and comments are ignored.
assert parse_line('') is None
assert parse_line('   ') is None
assert parse_line('\t \n') is None
assert parse_line('# a comment') is None
assert parse_line('    # an indented comment') is None
assert parse_line('#') is None

assert parse_line('a # 5') == ('a', [])

assert total_score([]) == 0
assert total_score([10.0]) == 10.0
assert total_score([30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0]) == 420.0
assert total_score([1.5, 2.5]) == 4.0
assert total_score([-5.0, 5.0]) == 0

RANGES: GradeRanges = {'A': (600,), 'B': (500, 600), 'C': (400, 500),
                        'D': (300, 400), 'F': (0, 300)}

assert grade_for_score(600, RANGES) == 'A'
assert grade_for_score(1000, RANGES) == 'A'
assert grade_for_score(500, RANGES) == 'B'
assert grade_for_score(599.9, RANGES) == 'B'
assert grade_for_score(400, RANGES) == 'C'
assert grade_for_score(300, RANGES) == 'D'
assert grade_for_score(0, RANGES) == 'F'
assert grade_for_score(299, RANGES) == 'F'

# A score below every range gets no grade.
assert grade_for_score(-1, RANGES) is None

# A gap in the ranges also gets no grade.
assert grade_for_score(450, {'A': (600,), 'B': (500, 600)}) is None

# The grades need not be single letters.
assert grade_for_score(10, {'Pass': (5, 20), 'Fail': (0, 5)}) == 'Pass'
assert grade_for_score(3, {'Pass': (5, 20), 'Fail': (0, 5)}) == 'Fail'

# An empty set of ranges grades nothing.
assert grade_for_score(100, {}) is None
