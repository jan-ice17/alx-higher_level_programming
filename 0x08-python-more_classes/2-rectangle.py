#!/usr/bin/python3

"""
Here is a  script that  demonstrates the usage of the Rectangle class from the module '2-rectangle'.
It creates a rectangle object, sets its dimensions, and calculates its area and perimeter.
"""

Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
