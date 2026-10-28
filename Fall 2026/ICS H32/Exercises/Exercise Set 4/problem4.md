# Problem 4

## 1. `render_scene`

Interface name: **`Drawable`**

A type is compatible with `Drawable` if it has a `draw(display: Display)` method

## 2. `aggregate_length`

Interface name: **`Sized`**

A type is compatible with `Sized` if it supports `len()`

## 3. `find_largest_component`

1. `x` — interface name: **`ComponentSource`**. A type is compatible if it has an
  `all_components()` method that takes no parameters and returns a `ComponentSequence`.
2. `y` — interface name: **`ComponentSequence`**. A type is compatible if it has a
  `next_component()` method that takes no parameters and returns the next `Component`
3. `z` — interface name: **`Component`**. A type is compatible if it has a `size()` method that takes no parameters and returns an `int`.
