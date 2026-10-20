# Problem 1

## What is an advantage of namedtuples over dictionaries?

A namedtuple has a fixed set of fields decided when the class is defined,
so a misspelled name is an error instead of a new entry. For instance, suppose we want to change `xcoord` instead of `xcord` which doesn't exist in the data. Writing
`point.xcord` raises `AttributeError` and thus stops the user from doing the wrong operation. On the other hand, the dictionary equivalents
`d["xcord"] = 3` silently creates a new key instead of failing, so the
record ends up with both `xcoord` and `xcord` and the bug survives.

## What is an advantage of dictionaries over namedtuples?

A dictionary's keys do not have to be known in advance. They can be any
hashable value and keys can
be added or removed as the program runs, so
the set of names can grow, shrink, or differ from one record to the next. For instance, it can be handy when we want to maintain a list of student names and their corresponding gpa. Since the student in the class would add/drop from time to time, dictionary is better than namedtuples. 