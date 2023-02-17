import logging


def check_point(point: tuple) -> None:
    # point is an (x, y) tuple
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


def run():
    points = (
        (0, 0),
        (-1, 1),
        (1, 1),
        (2, 0),
        (),
    )
    for point in points:
        try:
            check_point(point)
        except ValueError as e:
            logging.error(f"{e}")


if __name__ == '__main__':  # pragma: no cover
    run()
