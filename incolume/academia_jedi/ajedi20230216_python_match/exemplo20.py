from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def location(point):
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f'Y={y} and the point is on the y-axis.')
        case Point(x=x, y=0):
            print(f'X={x} and the point is on the x-axis.')
        case Point():
            print('The point is located somewhere else on the plane.')
        case _:
            print('Not a point')


def run():
    points = (
        Point(0, 0),
        Point(-1, 1),
        Point(1, 1),
        Point(2, 0),
        # Point('s', 's'),
    )

    for point in points:
        location(point)


if __name__ == '__main__':  # pragma: no cover
    run()
