#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        # Handles whenb is zero
        pass
    finally:
        # Print the result regardlessexception occurred or not
        print("Inside result: {}".format(result))
        return result
