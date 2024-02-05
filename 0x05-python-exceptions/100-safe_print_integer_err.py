#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))  # Print the int value
        return True
    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)  # Print the exception message to stderr
        return False
