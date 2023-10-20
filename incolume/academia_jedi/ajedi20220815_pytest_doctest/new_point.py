from dataclasses import dataclass


@dataclass
class Point:
    """Class Point with dataclass decorator.

    >>> p1 = Point(4, 9)
    >>> p2 = Point(2, 3)

    >>> p1 - p2
    Point(x=2, y=6)

    >>> p1 -= p2
    Point(x=2, y=6)
    """

    x: int
    y: int

    def __sub__(self, o):
        return Point(self.x - o.x, self.y - o.y)

    def __isub__(self, o):
        self.x -= o.x
        self.y -= o.y
        return self
