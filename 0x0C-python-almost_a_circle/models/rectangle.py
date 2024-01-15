#!/usr/bin/python3
"""Inherits from base"""
from models.base import Base


class Rectangle(Base):
    """creates private attritbutes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """set attributes"""

        self.width = width
        self.height = height
        self.x = x
        self.y = 0
        super().__init__(id)
