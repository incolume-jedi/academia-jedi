class Point:
    """
    Class Point.

    >>> p1 = Point(4, 6)
    >>> p2 = Point(2, 3)

    >>> p1 + p2
    Point(6, 9)

    >>> p1 - p2
    Point(2, 3)

    >>> p1 / p2
    Point(2.0, 2.0)

    >>> p1 // p2
    Point(2, 2)

    >>> p1 * p2
    Point(8, 18)

    >>> p1 += p2
    Point(6, 9)

    >>> p1 -= p2
    Point(2, 3)

    >>> p1 *= p2
    Point(8, 18)

    >>> p1 /= p2
    Point(2.0, 2.0)

    >>> p1 //= p2
    Point(2, 2)
    """

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x!r}, {self.y!r})"

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)

    def __radd__(self, o):
        return self.__add__(o)

    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        return self

    def __sub__(self, o):
        return Point(self.x - o.x, self.y - o.y)

    def __floordiv__(self, o):
        return Point(self.x // o.x, self.y // o.y)

    def __ifloordiv__(self, o):
        return self.__floordiv__(o)

    def __truediv__(self, o):
        return Point(self.x / o.x, self.y / o.y)

    def __itruediv__(self, o):
        return self.__truediv__(o)

    def __mul__(self, o):
        return Point(self.x * o.x, self.y * o.y)

    def __rmul__(self, o):
        return self.__mul__(o)

    def __imul__(self, o):
        return self.__mul__(o)
