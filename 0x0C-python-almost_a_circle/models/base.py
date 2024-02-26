#!/usr/bin/python3
""" A class Base that will be the “base” of all other classes in my project """
class Base:
    """Class with a private class attribute 
    __nb_objects = 0"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
