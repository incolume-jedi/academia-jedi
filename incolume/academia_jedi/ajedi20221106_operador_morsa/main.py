import easygui as eg
from enum import Enum, auto, unique
import logging
import PySimpleGUI as psg


__author__ = "@britodfbr"  # pragma: no cover


def gretting(username: str = '') -> str:
    if name := username or 'world':
        return f"Hello {name}."


def run():
    gretting(input('What is your name? '))


if __name__ == '__main__':  # pragma: no cover
    run()
