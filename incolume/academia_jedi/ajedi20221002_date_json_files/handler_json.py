from dataclasses import dataclass, field
import json
from pathlib import Path
from datetime import datetime
from itertools import count
from copy import copy

counter = count()


@dataclass
class Event:
    message: str
    create_at: datetime = field(
        default_factory=lambda: datetime.now())
    index: int = field(default_factory=lambda: next(counter))

    def __repr__(self):
        return (
            "{}(message='{message}',create_at='{create_at}', index={index})"
            .format(self.__class__.__name__, **self.__dict__)
        )

    def jsonify(self):
        ...

    def toJSON(self):
        o = copy(self.__dict__)
        o['create_at'] = self.create_at.strftime('%Y-%m-%d %H:%M:%S.%f')
        return json.dumps(o, sort_keys=True, indent=4)


def get_events():
    return [Event(f'event_{x:03}').toJSON() for x in range(1, 101)]


def write_json(list_events: list, filename: (Path | str)):
    filename = filename or 'events.json'
    with Path(filename).open('w') as file:
        json.dump(list_events, file, indent=4)


def run():
    e = Event('')
    print(
        e,
        write_json(get_events(), 'events.json'),
        get_events(),
        sep='\n'
    )


if __name__ == '__main__':  # pragma: no cover
    run()
