import json

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
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
