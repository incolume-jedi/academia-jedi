"""Enum examples."""

from enum import Enum, auto, unique
import string


class Day(Enum):
    """Creating Enumerations With the Functional API"""

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class Season(Enum):
    """Creating Enumerations With the Functional API"""

    WINTER, SPRING, SUMMER, FALL = range(1, 5)


class Grade(Enum):
    """Creating Enumerations With the Functional API"""

    A = 90
    B = 80
    C = 70
    D = 60
    F = 0


class Size(Enum):
    """Creating Enumerations With the Functional API"""

    S = "small"
    M = "medium"
    L = "large"
    XL = "extra large"


class Size1(Enum):
    """Creating Enumerations With the Functional API"""

    S, M, L, XL = 1, 2, 3, 4


class SwitchPosition(Enum):
    """Creating Enumerations With the Functional API"""

    ON = True
    OFF = False


class BaseTextEnum(Enum):
    def as_list(self):
        try:
            return list(self.value)
        except TypeError:
            return [str(self.value)]


class Alphabet(BaseTextEnum):
    """Creating Enumerations With the Functional API"""

    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase


#   Creating Enumerations With the Functional API
HTTPMethod0 = Enum("HTTPMethod", ["GET", "POST", "PUSH", "PATCH", "DELETE"])


class HTTPMethod(Enum):
    """Creating Enumerations With the Functional API"""

    GET = 1
    POST = 2
    PUSH = 3
    PATCH = 4
    DELETE = 5


HTTPStatusCode = Enum(
    # Creating Enumerations With the Functional API
    value="HTTPStatusCode",
    names=[
        ("OK", 200),
        ("CREATED", 201),
        ("BAD_REQUEST", 400),
        ("NOT_FOUND", 404),
        ("SERVER_ERROR", 500),
    ],
)


class WDay(Enum):
    """Building Enumerations From Automatic Values"""

    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = 3
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = 7


class CardinalDirection(Enum):
    """Building Enumerations From Automatic Values"""

    def _generate_next_value_(name, start, count, last_values):
        return name[0]

    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class OperatingSystem0(Enum):
    UBUNTU = "linux"
    MACOS = "darwin"
    WINDOWS = "win"
    DEBIAN = "linux"


# @unique
# class OperatingSystem1(Enum):
#     """ValueError: duplicate values found in
#     <enum 'OperatingSystem1'>: DEBIAN -> UBUNTU"""
#     UBUNTU = "linux"
#     MACOS = "darwin"
#     WINDOWS = "win"
#     DEBIAN = "linux"


class CardinalDirection1(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


class Flavor(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    MINT = 3


def loop1():
    for flavor in Flavor:
        print(flavor)

    for flavor in Flavor:
        print(flavor.name, flavor.value)

    for name in Flavor.__members__:
        print(name)

    for name in Flavor.__members__.keys():
        print(name)

    for name in Flavor.__members__.values():
        print(name)

    for name in Flavor.__members__.items():
        print(name)


class Semaphore(Enum):
    RED, YELLOW, GREEN = 1, 2, 3


def handle_semaphore(light):
    match light:
        case Semaphore.RED:
            print("You must stop!")
        case Semaphore.YELLOW:
            print("Light will change to red, be careful!")
        case Semaphore.GREEN:
            print("You can continue!")


class Mood(Enum):
    FUNKY, MAD, HAPPY = 1, 2, 3

    def describe_mood(self):
        return self.name, self.value

    def __str__(self):
        return f"I feel {self.name}"

    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY


class Sort(Enum):
    ASCENDING = 1
    DESCENDING = 2

    def __call__(self, values):
        return sorted(values, reverse=self is Sort.DESCENDING)


def compare():
    print(Size1.S > Size.M)
    print(Size1.S < Size.M)
    print(Size1.L >= Size.M)
    print(Size1.L <= Size.M)
    print(Size1.L > 2)
    print(Size1.M < 1)


def run():
    print(
        *list(Day),
        "---",
        type(Day.SUNDAY),
        type(Day.TUESDAY),
        "---",
        *list(Season),
        "---",
        *list(Grade),
        "---",
        *list(Size),
        "---",
        list(SwitchPosition),
        "---",
        Alphabet.LOWERCASE.as_list(),
        "---",
        Alphabet.UPPERCASE.as_list(),
        "---",
        list(HTTPMethod0),
        "---",
        list(HTTPMethod),
        "---",
        list(HTTPStatusCode),
        "---",
        list(WDay),
        "---",
        list(CardinalDirection),
        "---",
        list(OperatingSystem0),
        "---",
        list(OperatingSystem0.__members__.items()),
        # '---',
        # list(OperatingSystem1),
        # '---',
        # list(OperatingSystem1.__members__.items()),
        "---",
        # Dot notation
        CardinalDirection1.NORTH,
        # Call notation
        CardinalDirection1("N"),
        # Subscript notation
        CardinalDirection1["NORTH"],
        "---",
        CardinalDirection1.NORTH.name,
        CardinalDirection1.NORTH.value,
        CardinalDirection1.WEST.name,
        "---",
        "---",
        sep="\n",
    )
    print("---")
    loop1()
    print("---")
    handle_semaphore(Semaphore.GREEN),
    handle_semaphore(Semaphore.YELLOW),
    handle_semaphore(Semaphore.RED),
    print("---")
    print(Mood.HAPPY.describe_mood(), Mood.HAPPY, Mood.favorite_mood(), sep="\n")
    print("---")
    numbers = [5, 2, 7, 6, 3, 9, 8, 4]
    print(Sort.ASCENDING(numbers), Sort.DESCENDING(numbers), sep="\n")
    print("---")

    ...


if __name__ == "__main__":
    run()
