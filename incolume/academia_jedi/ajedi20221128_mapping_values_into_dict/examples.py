# !/usr/bin/env python

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from collections.abc import Iterable
from typing import Optional

__author__ = '@britodfbr'  # pragma: no cover

tup = (
    ('Boba', 21),
    ('Din', 18),
    ('Grogu', 40),
    ('Ahsoka', 21),
    ('Boba', 22),
    ('Din', 19),
    ('Grogu', 46),
    ('Ahsoka', 11),
    (11, 'eleven'),
    (21, 'mike'),
    (19, 'dustin'),
    (46, 'caleb'),
)
tups = list(tup)


def example01(t: Optional[tuple] = None) -> dict:
    """Python tuple to dictionary.

    To convert a tuple to dictionary in Python, use the dict() method.
    The dict() function takes a tuple of tuples as an argument and returns
    the dictionary. Each tuple contains a key-value pair.

    A dictionary object can be constructed using a dict() function.

    Output:
    ((11, 'eleven'), (21, 'mike'), (19, 'dustin'), (46, 'caleb'))
    {'eleven': 11, 'mike': 21, 'dustin': 19, 'caleb': 46}
    """
    return {y: x for x, y in t}


def example02(t: Optional[Iterable] = None) -> dict:
    """Using dict(), map() and reversed() method
    You can use the combination of the dict(), map(), and reversed()
    method to convert a tuple to the dictionary. The map() method returns a
    map object, which is an iterator. The changed () function returns the
    reversed iterator of the given sequence.

    tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))
    print(tup)


    Output:
    ((11, 'eleven'), (21, 'mike'), (19, 'dustin'), (46, 'caleb'))
    {'eleven': 11, 'mike': 21, 'dustin': 19, 'caleb': 46}
    """
    return dict(map(reversed, t))


def example03(t: Optional[Iterable] = None):
    """To convert a list of tuples into a dictionary, use the setdefault() method.
     The setdefault() method takes the first parameter to the key and the
     second parameter to a value of the dictionary.

     The setdefault() function searches for a key and displays its value,
     and creates a new key with def_value if the key is not present.
     See the following code.


    def conversion(tup, dict):
        for x, y in tup:
            dict.setdefault(x, []).append(y)
        return dict


    tups = [("Boba", 21), ("Din", 19), ("Grogu", 46), ("Ahsoka", 11)]

    dictionary = {}
    print(conversion(tups, dictionary))
    Output:
    {'Boba': [21], 'Din': [19], 'Grogu': [46], 'Ahsoka': [11]}
    """
    dct = {}
    for key, value in t:
        dct.setdefault(key, []).append(value)
    return dct


def run():
    print(example01(tup), example02(tup), example03(tups), sep='\n')


if __name__ == '__main__':  # pragma: no cover
    run()
