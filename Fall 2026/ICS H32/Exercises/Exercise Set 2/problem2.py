def first_chars(items: list) -> str:
    result = ''

    for item in items:
        if type(item) == list:
            result += first_chars(item)
        elif type(item) == str and item != '':
            result += item[0]

    return result


def count_bigger(items: list, threshold: float) -> int:
    count = 0

    for item in items:
        if type(item) == list:
            count += count_bigger(item, threshold)
        elif (type(item) == int or type(item) == float) and item > threshold:
            count += 1

    return count


assert first_chars(['Boo', 'is', 'happy', 'today']) == 'Biht'
assert first_chars(['boo', 'was', ['sleeping', 'deeply'], 'that', 'night',
                    ['as', ['usual']]]) == 'bwsdtnau'

assert first_chars([]) == ''
assert first_chars(['', [], [[]], '']) == ''
assert first_chars(['a']) == 'a'
assert first_chars([[['x']]]) == 'x'

assert first_chars(['', 'abc', ['', ['def', '']], 'g']) == 'adg'

assert count_bigger([1, 2, 3, 4, 5, 6], 2.5) == 4
assert count_bigger(['boo', [3.0, 'is', 'perfect'], 'today', 5], 3) == 1

assert count_bigger([], 0) == 0
assert count_bigger([1, 2, 3], 10) == 0
assert count_bigger([3, 3.0], 3) == 0
assert count_bigger([-1, -2.5, 0], -3) == 3

assert count_bigger(['a', None, 'b'], 0) == 0
assert count_bigger([[10, [20, 30]], 5], 15) == 2
assert count_bigger([[[[4.5]]]], 4) == 1
