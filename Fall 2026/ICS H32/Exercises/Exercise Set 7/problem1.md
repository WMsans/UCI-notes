# Problem 1

## 1. Why do we need to "flip" the display?

PyGame draws into a surface that lives in a buffer image, while the window
is showing a separate image owned by the display system. `pygame.display.flip()`
is the step that copies the finished surface in the buffer into the window.

Designing it this way means the window only changes from one complete frame to
the next. Without it a drawing call made halfway through a frame would be visible
which doesn't look nice.

## 2. What is the purpose of using PyGame's `Clock` class?

`tick(30)` caps how often the game loop runs, and the purpose is that the loop's
speed stops depending on the machine and on how much work a frame happens to
contain. If not, a fast machine draws many more
frames per second than a slow one, causing the game to behave differently on difference machines.
I believe the player would not want to fight really fast enemies just because they got a better device.
