#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary
    with all values multiplied by 2."""
    return ({item: a_dictionary[item] * 2 for item in a_dictionary})
