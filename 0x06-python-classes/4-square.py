#!/usr/bin/python3
"""
This module contains a class Square that defines a square.
"""


class Square:
    """
    This is a class which will defines a square.

    Attributes:
        __size (int): size of the side of the square.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
           size (int): The size of the side of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        This is the used getter for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size.

        Parameters:
           value (int): The size of the side of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        The method returns the current square area.
        """
        return self.__size ** 2
