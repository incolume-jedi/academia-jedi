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

    def __call__(self, **kwargs):
        logging.debug(self.__dict__)
        logging.debug(self.name)
        msg = kwargs.get('msg')
        title = kwargs.get('title', 'App')
        default = kwargs.get('default', '')
        match self.name:
            case 'CLI':
                return gretting(input(f'{msg} '))
            case 'EASYGUI':
                return gretting(
                    eg.enterbox(
                        msg=f'{msg} ',
                        title=title,
                        default=default
                    )
                )
            case _:
                raise NotImplemented


def viewer():
    return Viewer.EASYGUI(name='')


def run():
    # gretting(input('What is your name? '))
    # print(viewer())
    print(Viewer.CLI(msg='What is your name?'))
    print(Viewer.EASYGUI(msg='What is your name?'))
    print(Viewer.EASYGUI(msg='What is your name?', title='Get username'))


if __name__ == '__main__':  # pragma: no cover
    run()
