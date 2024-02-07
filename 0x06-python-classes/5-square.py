#!/usr/bin/python3
"""
Here is a  module which contains a class Square that defines a square.
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
           size (int): The size of the side of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        This is a getter for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter for size.

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
        This is a method which returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        IN this method it prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)