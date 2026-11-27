import math

def zero_calc(n):
    return 0

def square_calc(n):
    return n * n

def cube_calc(n):
    return n * n * n

def length_calc(n):
    return len(n)

def square_root_calc(n):
    return math.sqrt(n)

def multiply_by_calc(multiplier, n):
    return n * multiplier

def run_calcs(calcs, starting_value):
    current_value = starting_value

    for calc in calcs:
        current_value = calc(current_value)

    return current_value
