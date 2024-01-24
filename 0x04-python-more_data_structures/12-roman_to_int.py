#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total_sum = 0
    prev_value = 0

    for current_num in reversed(roman_string):
        current_val = roman_numerals_dict[current_num]
        if current_val < prev_value:
            total_sum -= current_val
        else:
            total_sum += current_val
        prev_value = current_val

    return total_sum
