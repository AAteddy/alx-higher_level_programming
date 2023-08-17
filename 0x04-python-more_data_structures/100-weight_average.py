#!/usr/bin/python3

def weight_average(my_list=[]):
    """A function that returns the weighted
    average of all integers tuple."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avrg = 0
    size = 0
    for tup in my_list:
        avrg += (tup[0] * tup[1])
        size += tup[1]
    return (avrg / size)
