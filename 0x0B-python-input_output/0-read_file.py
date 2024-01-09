#!/usr/bin/python3
"""defines a function that reads a text-file"""


def read_file(filename=""):
    """prints the contents to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
