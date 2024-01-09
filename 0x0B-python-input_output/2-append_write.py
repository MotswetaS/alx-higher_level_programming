#!/usr/bin/python3
"""Appends a srting to end of file"""


def append_write(filename="", text=""):
    """returns the number of characters added"""

    with open(filename, 'a', encoding="utf-8") ass f:
        return f.write(text)
