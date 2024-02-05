#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]  # Perform the division
        except TypeError:
            print("wrong type")  # Handle TypeError
            res = 0
        except ZeroDivisionError:
            print("division by 0")  # Handle ZeroDivision-error
            res = 0
        except IndexError:
            print("out of range")  # Handle an Indexerror
            res = 0
        finally:
            result.append(res)  # Append res to result list
    return result
