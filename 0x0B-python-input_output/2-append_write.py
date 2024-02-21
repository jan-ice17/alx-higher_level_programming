#!/usr/bin/python3
"""This function appends a string of a text file"""


def append_write(filename="", text=""):
    """It appends a string of a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
