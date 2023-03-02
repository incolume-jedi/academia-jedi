import re
from dataclasses import dataclass


@dataclass
class RegexEqual(str):
    string: str
    match: re.Match = None

    def __eq__(self, pattern):
        self.match = re.search(pattern, self.string)
        return self.match is not None

    def __getitem__(self, group):
        return self.match[group]


def run():
    match RegexEqual("Something to match"):
        case "^Some(.*ing).*$" as capture:
            print(f"Captured: '{capture}'")  # Captured: 'thing'
            print(f"Captured: '{capture[1]}'")  # Captured: 'thing'


if __name__ == "__main__":  # pragma: no cover
    run()
