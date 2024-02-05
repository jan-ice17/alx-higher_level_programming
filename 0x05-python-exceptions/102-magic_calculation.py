#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    # Iterate from 1 to 2
    for i in range(1, 3):
        try:
            if i > a:
                # Raise an exception if i is greater than a
                raise Exception('Too far')
            else:
                # Calculate the result by raising a to the power of b and dividing by i
                result += a ** b / i
        except:
            # If an exception is caught, set the result to the sum of a and b
            result = b + a
            break
    return result
