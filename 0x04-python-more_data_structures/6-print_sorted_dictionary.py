#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """A function that prints a dictionary
    by ordered keys."""
    order_list = list(a_dictionary.keys())
    order_list.sort()
    for item in order_list:
        print("{}: {}".format(item, a_dictionary.get(item)))
