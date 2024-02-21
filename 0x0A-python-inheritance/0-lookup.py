#!/usr/bin/python3
def lookup(obj):
    """
    Function that gets a list of available attributes and methods of an object.

    Parameters:
    obj (any): Object to be inspected.

    Returns:
    list: List of strings representin the attributes and methods of the object.
    """
    return dir(obj)
