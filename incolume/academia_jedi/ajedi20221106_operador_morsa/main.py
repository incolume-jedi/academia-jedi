import easygui as eg
from enum import Enum, auto, unique
import logging
import PySimpleGUI as psg


__author__ = "@britodfbr"  # pragma: no cover


def gretting(username: str = '') -> str:
    if name := username or 'world':
        return f"Hello {name.title()}."


class Viewer(Enum):
    CLI = auto()
    EASYGUI = auto()

    def __call__(self, *args, **kwargs):
        logging.debug(self.__dict__)
        logging.debug(self.name)

        match self.name:
            case 'CLI':
                return gretting(input('What is your name? '))
            case 'EASYGUI':
                return gretting(
                    eg.enterbox(
                        msg='What is your username?',
                        title='Get username',
                        default=''
                    )
                )
            case _:
                raise NotImplemented


def viewer():
    return Viewer.EASYGUI(name='')


def run():
    # gretting(input('What is your name? '))
    # print(viewer())
    print(Viewer.CLI(msg=''))
    print(Viewer.EASYGUI(msg=''))


if __name__ == '__main__':  # pragma: no cover
    run()
