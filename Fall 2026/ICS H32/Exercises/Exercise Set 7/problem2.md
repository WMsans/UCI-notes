# Problem 2

## 1. What problem does a model focus on?

The mechanics and state of the game: what objects exist, where they are, 
what state they will be, etc.

## 2. What problem does a view focus on?

What the game looks like and how the user works it: drawing the current state in
pixels, converting coordinates for whatever size the window happens to be, etc.

View doesn't now any rules or state. They merely renders. To be honest the input
and event listening should be the controller's job.

## 3. What are two benefits of separating the model from the view?

A change on one side doesn't have to force to change on the other. Making the window
resizable and restyling render touches only the view,
while tuning the game mechanics touches only the model, with the other side
continuing to work.
