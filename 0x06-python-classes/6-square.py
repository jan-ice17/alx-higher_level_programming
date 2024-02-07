#!/usr/bin/python3
"""
Here is a module which contains a class Square that defines a square.
"""


class Square:
    """
    This is a class that defines a square.

    Attributes:
        __size (int): size of the side of the square.
        __position (tuple): position of the square in 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for the Square class.

        Parameters:
           size (int): The size of the side of the square.
           position (tuple): The position sof the square in 2D space.
        """
        self.size = size
        self.position = position

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
           value (int): The size of side of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        This is a getter for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is a setter for position.

        Parameters:
           value (tuple): The position of the square in 2D space.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        This method returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            print("\n".join([" " * self.position[0] + "#" * self.__size for _ in range(self.__size)]))
