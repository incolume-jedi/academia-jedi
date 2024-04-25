import json
import logging
from copy import copy
from dataclasses import dataclass, field
from datetime import datetime
from inspect import stack
from itertools import count
from pathlib import Path

counter = count()
logFormat = (
    '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;'
    ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
)
logging.basicConfig(format=logFormat, level=logging.DEBUG)


@dataclass
class Event:
    message: str
    create_at: datetime = field(default_factory=lambda: datetime.now())
    index: int = field(default_factory=lambda: next(counter))

    def __repr__(self) -> str:
        logging.debug(f'{self.__class__.__name__}{stack()[0][3]}')
        return "{}(message='{message}',create_at='{create_at}', index={index})".format(
            self.__class__.__name__,
            **self.__dict__,
        )

    def jsonify(self): ...

    def to_json(self):
        o = copy(self.__dict__)
        o['create_at'] = self.create_at.strftime('%F %T.%f')
        logging.debug(f'{self.__class__.__name__}({o}).{stack()[0][3]}')
        return json.dumps(o, sort_keys=True, indent=4)


def get_events() -> list[Event]:
    logging.debug(f'{stack()[0][3]}')
    return [Event(f'event_{x:03}') for x in range(1, 101)]


def write_json(list_events: list, filename: (Path | str)):
    logging.debug(f'{stack()[0][3]}')
    filename = filename or 'events.json'
    with Path(filename).open('w') as file:
        logging.debug(f'write file "{filename}"')
        json.dump([e.to_json() for e in list_events], file, indent=4)


def run():
    logging.debug(f'{stack()[0][3]}')
    logging.debug(
        'logging date: '
        f"{datetime.fromisoformat('1978-06-20T01:23:45.6789-03:00')}",
    )
    e = Event('')
    print(e, write_json(get_events(), 'events.json'), get_events(), sep='\n')


if __name__ == '__main__':  # pragma: no cover
    run()
