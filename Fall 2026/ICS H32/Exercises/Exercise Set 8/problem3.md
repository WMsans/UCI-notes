# Problem 3

## 1. Why we used bound methods to set up our event handlers

tkinter serves as the "controller" and our program serves as the "model". 
tkinter ensentially does all the decision of when and how an event handler gets called;
`button`'s `command` is called with no arguments, and a handler attached with
`bind()` is called with only the event object as parameter.

our handlers, on the other hand, need `self`. All the model properties (like the counter and stuff)
are managed by our program.

The bound method allows the gui to show what it need to show without knowing 
the detail of the model side (our program), which is good because we can tune
our program whatever we want without needing extra change in the tkinter side. a method whose `self`
has already been filled in by the object it was looked up on, so it can be
called with only the arguments tkinter knows how to provide. `self._increment`
is a ready-made zero-argument callable tied to one particular application object.

## 2. Another way without bound

Functions in Python are objects, and a function defined inside another function
can still use that function's local variables. So instead of a method plus
binding, the handler can be a nested function defined in `__init__` that closes
over `self` rather than receiving it as a parameter. This way, the gui is still encapsulated, the handler is still private to the view,
and tkinter still calls it with no arguments.

```python
class CounterApp:
    def __init__(self) -> None:
        self._count = 0
        self._window = tkinter.Tk()

        def increment() -> None:
            self._count += 1
            self._label.config(text=str(self._count))

        self._label = tkinter.Label(self._window, text='0')
        self._button = tkinter.Button(self._window, text='+1', command=increment)
        self._label.pack()
        self._button.pack()

    def run(self) -> None:
        self._window.mainloop()
```

the nested function taking the event object as its one parameter:

```python
    def reset(self) -> None:
        def on_click(event: tkinter.Event) -> None:
            self._count = 0
            self._label.config(text='0')

        self._label.bind('<Button-1>', on_click)
```
