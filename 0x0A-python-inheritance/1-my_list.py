#!/usr/bin/python3
"""
MyList class function is used here
"""


class MyList(list):
    """The subclass of list"""
    def __init__(self):
        """It initializes the object"""
        super().__init__()

    def print_sorted(self):
        """It prints the sorted list"""
        print(sorted(self))
