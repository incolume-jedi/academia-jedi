import re
from dataclasses import dataclass


@dataclass
class RegexEqual(str):
    string: str
    match: re.Match = None

    def __eq__(self, pattern):
        self.match = re.search(pattern, self.string)
        return self.match is not None


def run():
    match RegexEqual("Something to match"):
        case "^...match":
            print("Nope...")
        case "^S.*ing$":
            print("Closer...")
        case "^S.*match$":
            print("Yep!")
    print(bool(RegexEqual("Something") == "^S.*ing$"))  # True


if __name__ == '__main__':  # pragma: no cover
    run()
