"""Matching Positional Arguments."""


class Location:
    __match_args__ = ("country", "city")

    def __init__(self, country, city):
        self.country = country
        self.city = city


def positional_args_test(location):
    match location:
        case Location("Germany", "Berlin"):
            print("Hallo Berlin!")
        case Location(_, "London"):
            print("There's London in multiple countries...")
        case Location("Canada", _):
            print("Hello Canada!")
        case Location("France", _):
            print("Bonjour la France!")
        case Location("Brazil", _):
            print(f"Olá Falante de português!!")
        case Location("Brazil|Portugal|Angola|Macau", _):
            print(f"Olá {Location}")


def run():
    locations = (
        Location("Canada", "Toronto"),
        Location("Germany", "Berlin"),
        Location("Brazil", "Brasilia"),
        Location("France", "Paris"),
        Location("Portual", "Porto"),
    )

    for location in locations:
        positional_args_test(location)


if __name__ == "__main__":  # pragma: no cover
    run()
