#!/usr/bin/python3
"""
Here is a module which contains a class Square that defines a square.
"""


class Square:
    """
    This is a class that defines a square.

    Attributes:
        __size (int): size of the side of the square.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
           size (int): This will be size of the side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
