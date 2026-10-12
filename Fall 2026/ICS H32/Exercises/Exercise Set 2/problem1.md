# Problem 1

## Recursive version of `find_max`

```python
def find_max(nums: list[int]) -> int:
    '''
    Finds the maximum value in the given list of integers,
    or None if the list is empty
    '''
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums[0]
    else:
        largest_of_rest = find_max(nums[1:])

        if nums[0] > largest_of_rest:
            return nums[0]
        else:
            return largest_of_rest
```

## Was recursion an appropriate solution here?

No, this is not a problem that is well-suited to recursion in Python, and
the loop version is the better solution.

The reason is that a flat list of integers is not a recursive data
structure. We can iterate throught it better in a plain loop. 

