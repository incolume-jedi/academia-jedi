# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Container, Iterable

__author__ = "@britodfbr"  # pragma: no cover

tup = (
    ("Boba", 21),
    ("Din", 18),
    ("Grogu", 40),
    ("Ahsoka", 21),
    ("Boba", 22),
    ("Din", 19),
    ("Grogu", 46),
    ("Ahsoka", 11),
    (11, "eleven"),
    (21, "mike"),
    (19, "dustin"),
    (46, "caleb"),
)
tups = list(tup)


def example01(t: tuple = None) -> dict:
    """
    Python tuple to dictionary

    To convert a tuple to dictionary in Python, use the dict() method.
    The dict() function takes a tuple of tuples as an argument and returns
    the dictionary. Each tuple contains a key-value pair.

    A dictionary object can be constructed using a dict() function.

    Output:
    ((11, 'eleven'), (21, 'mike'), (19, 'dustin'), (46, 'caleb'))
    {'eleven': 11, 'mike': 21, 'dustin': 19, 'caleb': 46}
    """
    dct = dict((y, x) for x, y in t)
    return dct


def example02(t: Iterable = None) -> dict:
    """
    Using dict(), map() and reversed() method
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
    dct = dict(map(reversed, t))
    return dct


def example03(t: Iterable = None):
    """
    To convert a list of tuples into a dictionary, use the setdefault() method.
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
    print(example01(tup), example02(tup), example03(tups), sep="\n")


if __name__ == "__main__":  # pragma: no cover
    run()
