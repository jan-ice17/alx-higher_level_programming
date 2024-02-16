#!/usr/bin/python3
"""
This is a  script which defines a function that adds two integer.
"""


def add_integer(a, b=98):
    """
    IN this function it returns the sum of integer  of a and b.

    If either a or b is a not an integer orfloat, TypeError is raised.
    """

    # Checks if a is non-integer or non- float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Checks if b is non integer or a non- float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
