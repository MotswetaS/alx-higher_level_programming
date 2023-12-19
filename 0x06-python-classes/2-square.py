#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize new Square.
        Args:
            size (int): new suare size
        """
        if not isinstance(size, int):
            raise TypeError("size should be an integer")
        elif size < 0:
            raise ValueError("size should be >= 0")
        self.__size = size
