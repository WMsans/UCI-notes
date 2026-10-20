from collections import namedtuple

def formatted_lines(value: namedtuple) -> list[str]:
    '''Return the lines pretty_print would print for the given namedtuple.'''
    if len(value._fields) == 0:
        return []

    width = max(len(name) for name in value._fields)

    return [f'{name.rjust(width)}: {getattr(value, name)}'
            for name in value._fields]

def pretty_print(value: namedtuple) -> None:
    '''Print each field of the given namedtuple as a "name: value" line.'''
    for line in formatted_lines(value):
        print(line)


Point = namedtuple('Point', ['x', 'y', 'z'])
Person = namedtuple('Person', ['name', 'age', 'favorite'])
Empty = namedtuple('Empty', [])


assert formatted_lines(Point(z=5, x=9, y=13)) == ['x: 9', 'y: 13', 'z: 5']
assert formatted_lines(Point(1, 2, 3)) == ['x: 1', 'y: 2', 'z: 3']

assert formatted_lines(Person(name='Alex', age=47, favorite='Boo')) == [
    '    name: Alex',
    '     age: 47',
    'favorite: Boo',
]

# The longest name alone gets no padding; ties all get none.
assert formatted_lines(namedtuple('Two', ['ab', 'cd'])(1, 2)) == [
    'ab: 1', 'cd: 2']
assert formatted_lines(namedtuple('Pads', ['a', 'bbb'])(1, 2)) == [
    '  a: 1', 'bbb: 2']

# Values are converted with str
assert formatted_lines(Point(1.5, None, [2, 3])) == [
    'x: 1.5', 'y: None', 'z: [2, 3]']
assert formatted_lines(Person('', 0, False)) == [
    '    name: ', '     age: 0', 'favorite: False']

assert formatted_lines(Empty()) == []
pretty_print(Empty())
