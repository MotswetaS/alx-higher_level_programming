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
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """setting and getting width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """setting and getting height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gsetting and getting x coordinates of the rectangle"""

        return self.__x

    @x.setter
    def x(x, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """gsetting and getting x coordinates of the rectangle"""

        return self.__y

    @y.setter
    def y(y, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
