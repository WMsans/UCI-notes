import math


class Circle:
    def __init__(self, x: float, y: float, radius: float) -> None:
        self._centroid = (x, y)
        self._radius = radius

    def centroid(self) -> tuple[float, float]:
        return self._centroid

    def move_to(self, x: float, y: float) -> None:
        self._centroid = (x, y)

    def area(self) -> float:
        return math.pi * self._radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def contains(self, x: float, y: float) -> bool:
        cx, cy = self._centroid
        return (x - cx) ** 2 + (y - cy) ** 2 <= self._radius ** 2


class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self._centroid = (x, y)
        self._width = width
        self._height = height

    def centroid(self) -> tuple[float, float]:
        return self._centroid

    def move_to(self, x: float, y: float) -> None:
        self._centroid = (x, y)

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def contains(self, x: float, y: float) -> bool:
        cx, cy = self._centroid
        within_x = cx - self._width / 2 <= x <= cx + self._width / 2
        within_y = cy - self._height / 2 <= y <= cy + self._height / 2
        return within_x and within_y


class RightTriangle:
    def __init__(self, x: float, y: float, horizontal_leg: float, vertical_leg: float) -> None:
        self._centroid = (x, y)
        self._horizontal_leg = horizontal_leg
        self._vertical_leg = vertical_leg

    def centroid(self) -> tuple[float, float]:
        return self._centroid

    def move_to(self, x: float, y: float) -> None:
        self._centroid = (x, y)

    def area(self) -> float:
        return self._horizontal_leg * self._vertical_leg / 2

    def perimeter(self) -> float:
        return (self._horizontal_leg + self._vertical_leg
                + math.hypot(self._horizontal_leg, self._vertical_leg))

    def _vertices(self) -> tuple[float, float, float, float]:
        cx, cy = self._centroid
        a = self._horizontal_leg
        b = self._vertical_leg
        x1, y1 = cx - 2 * a / 3, cy - b / 3  # bottom-left
        x2, y2 = cx + a / 3, cy + 2 * b / 3  # top-right
        return x1, y1, x2, y2

    def contains(self, x: float, y: float) -> bool:
        x1, y1, x2, y2 = self._vertices()
        a = self._horizontal_leg
        b = self._vertical_leg
        in_bounds = x1 <= x <= x2 and y1 <= y <= y2
        below_hypotenuse = (x - x1) * b - (y - y1) * a >= 0
        return in_bounds and below_hypotenuse


def sum_of_areas(shapes: list[object]) -> float:
    return sum(shape.area() for shape in shapes)


def _test_circle() -> None:
    c = Circle(0, 0, 2)
    assert c.centroid() == (0, 0)
    assert c.area() == 4 * math.pi
    assert c.perimeter() == 4 * math.pi
    assert c.contains(0, 0)
    assert c.contains(2, 0)
    assert not c.contains(2.01, 0)
    c.move_to(10, 0)
    assert c.centroid() == (10, 0)
    assert c.contains(12, 0)
    assert not c.contains(0, 0)


def _test_rectangle() -> None:
    r = Rectangle(0, 0, 4, 2)
    assert r.centroid() == (0, 0)
    assert r.area() == 8
    assert r.perimeter() == 12
    assert r.contains(0, 0)
    assert r.contains(2, 1)
    assert not r.contains(2.01, 0)
    r.move_to(1, 1)
    assert r.centroid() == (1, 1)
    assert r.contains(3, 2)
    assert not r.contains(3.01, 2)


def _test_right_triangle() -> None:
    t = RightTriangle(0, 0, 3, 3)
    assert t.centroid() == (0, 0)
    assert t.area() == 4.5
    assert t.perimeter() == 6 + math.hypot(3, 3)
    assert t.contains(-2, -1)
    assert t.contains(1, -1)
    assert t.contains(1, 2)
    assert not t.contains(-2, 2)
    t.move_to(10, 10)
    assert t.centroid() == (10, 10)
    assert t.contains(8, 9)
    assert not t.contains(8, 12)


def _test_sum_of_areas() -> None:
    shapes = [Circle(0, 0, 1), Rectangle(0, 0, 2, 2)]
    assert sum_of_areas(shapes) == math.pi + 4
    assert sum_of_areas([]) == 0


_test_circle()
_test_rectangle()
_test_right_triangle()
_test_sum_of_areas()
