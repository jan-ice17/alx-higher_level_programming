#!/usr/bin/python3
"""
This is a module contains a class Square that defines a square.
"""


class Square:
    """
    This is a class that defines a square.

    Attributes:
        __size (int): size of the side of the square.
    """

    def __init__(self, size):
        """
        This is the constructor for the Square class.

        Parameters:
           size (int): The size of the side of the square.
        """
        self.__size = size
