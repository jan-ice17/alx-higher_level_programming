#!/usr/bin/python3
"""
Here is a module which contains a class Square that defines a square.
"""


class Square:
    """
    This is the class will define a square.

    Attributes:
        __size (int): size of the side of the square.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
           size (int): The size of the side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        THere is a method which returns the current square area.
        """
        return self.__size ** 2
    