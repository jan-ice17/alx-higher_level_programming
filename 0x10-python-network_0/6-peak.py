#!/usr/bin/python3
"""Here I define an algorithm to locate a peak in a list of unsorted numbers."""

def find_peak(list_of_integers):
    """A class findpeak that returns the peak in a list of unsorted numbers."""
    if list_of_integers == []:
        # empty list case
        return None

    a = len(list_of_integers)
    if a == 1:
        # handle the single element case
        return list_of_integers[0]
    elif a == 2:
        # handle the two elements case
        return max(list_of_integers)

    mid = int(a / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        # return the peak if it is greater than its neighbors
        return peak
    elif peak < list_of_integers[mid - 1]:
        # try to recursively search the left subarray
        return find_peak(list_of_integers[:mid])
    else:
        # then search the right subarray
        return find_peak(list_of_integers[mid + 1:])

