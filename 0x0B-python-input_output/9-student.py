#!/usr/bin/python3
"""writes a class that defines a student by attribute"""


class Student:
    """will be a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of the student"""
        return self.__dict__
