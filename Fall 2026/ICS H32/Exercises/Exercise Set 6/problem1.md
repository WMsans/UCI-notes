# Problem 1

## 1. Are `Course` objects mutable or immutable?

They are mutable. `add_student` changes the state of an existing `Course` object
by adding to its enrollment list. There is no method that returns a new
`Course`, thus it has to be mutable.

## 2. Storing the caller's list in `__init__`

Yes, it is a risk. If the caller keeps a reference to the list they passed in and
later appends or removes students, the course's enrollment changes without
`add_student` ever being called. 

Copying the list in `__init__` (`self._students = list(students)`) removes the
aliasing of the list itself.

## 3. Returning the internal list from `students`

The method hands out the course's own
list, so any caller can append to it, remove from it, or clear it and change the
enrollment without `add_student`. A caller may also find that the list is changed
while holding it.

Returning a copy, `list(self._students)`, or an immutable `tuple(self._students)`
gives callers the roster without allowing them to
modify it. The tradeoff is that a caller cannot hold on to the returned
collection and expect it to update afterwards.
