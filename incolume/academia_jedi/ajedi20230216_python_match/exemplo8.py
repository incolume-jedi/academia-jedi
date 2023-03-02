"""Branch Reachability."""


def run():
    rows = [
        {"success": True, "value": 100},
        {"success": False, "value": 200},
        {"success": True, "value": 200},  # Should be matched by 3rd case
        {"success": False, "value": 200},
    ]

    for row in rows:
        match row:
            case {"success": True, "value": _}:
                print("First")
            case {"success": _, "value": 200}:
                print("Second")
            # Unreachable, If we move it to the top, it will work correctly
            case {"success": True, "value": 200}:
                print("Third")
            case {"success": _, "value": _}:
                print("None matches")

    # Prints:
    # First
    # Second
    # First
    # Second


if __name__ == "__main__":  # pragma: no cover
    run()
