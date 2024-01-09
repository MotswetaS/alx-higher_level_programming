#!/usr/bin/python3
"""function writes a string to a textfile"""


def write_file(filename="", text=""):
    """We are returning number of characters written"""

    with open(text, encoding="utf-8") as f:
        print(f.write(), end="")
