#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dict_key in sorted(a_dictionary.keys()):
        print("{}: {}".format(dict_key, a_dictionary[dict_key]))

