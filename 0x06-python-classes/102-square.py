#!/usr/bin/python3
"""
This module contains a class Square that defines a square.
"""


class Square:
    """
    This is a class that defines a square.

    Attributes:
        __size (float or int): size of the side of the square.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
           size (float or int): The size of the side of the square.
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
           value (float or int): The size of the side of the square.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method returns the current square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        It checks if two squares are equal.--Method
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        It checks if two squares are not equal.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
         A method that checksif a square is less than another one.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        A method that if a square is less than or equal to another one.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        A method that checks if a square is greater than another one.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        checks if a square is greater than or equal to another one.
        """
        return self.area() >= other.area()
