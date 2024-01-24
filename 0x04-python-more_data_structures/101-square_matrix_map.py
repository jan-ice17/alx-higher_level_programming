#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for tupel in my_list:
        average += tupel[0] * tupel[1]
        div += tupel[1]
    return float(average / div)
