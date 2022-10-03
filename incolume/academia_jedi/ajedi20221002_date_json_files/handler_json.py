from dataclasses import dataclass, field
import json
from pathlib import Path
from datetime import datetime
from itertools import count
from copy import copy
import logging
from inspect import stack

counter = count()
logFormat = '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;' \
            ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
logging.basicConfig(format=logFormat, level=logging.DEBUG)


@dataclass
class Event:
    message: str
    create_at: datetime = field(
        default_factory=lambda: datetime.now())
    index: int = field(default_factory=lambda: next(counter))

    def __repr__(self):
        logging.debug(f'{self.__class__.__name__}{stack()[0][3]}')
        return (
            "{}(message='{message}',create_at='{create_at}', index={index})"
            .format(self.__class__.__name__, **self.__dict__)
        )

    def jsonify(self):
        ...

    def toJSON(self):
        o = copy(self.__dict__)
        o['create_at'] = self.create_at.strftime('%Y-%m-%d %H:%M:%S.%f')
        logging.debug(f'{self.__class__.__name__}({o}).{stack()[0][3]}')
        return json.dumps(o, sort_keys=True, indent=4)


def get_events():
    logging.debug(f'{stack()[0][3]}')
    return [Event(f'event_{x:03}').toJSON() for x in range(1, 101)]


def write_json(list_events: list, filename: (Path | str)):
    logging.debug(f'{stack()[0][3]}')
    filename = filename or 'events.json'
    with Path(filename).open('w') as file:
        json.dump(list_events, file, indent=4)
        logging.debug(f'write file "{filename}"')


def run():
    logging.debug(f'{stack()[0][3]}')
    e = Event('')
    print(
        e,
        write_json(get_events(), 'events.json'),
        get_events(),
        sep='\n'
    )


if __name__ == '__main__':  # pragma: no cover
    run()
