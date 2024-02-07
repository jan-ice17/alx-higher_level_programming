#!/usr/bin/python3
import math

class MagicClass:
    """
    This is a class that defines a MagicClass.

    Attributes:
        __radius (float or int): radius of the circle.
    """

    def __init__(self, radius=0):
        """
        The constructor for the MagicClass class.

        Parameters:
           radius (float or int): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
         returns the current circle area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        In this it method returns the current circle circumference.
        """
        return 2 * math.pi * self.__radius