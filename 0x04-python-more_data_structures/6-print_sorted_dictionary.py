#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """A function that prints a dictionary
    by ordered keys."""
    [print("{}: {}".format(item, a_dictionary[item]))
            for item in sorted(a_dictionary)]
