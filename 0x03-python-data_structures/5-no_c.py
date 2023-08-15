#!/usr/bin/python3

def no_c(my_string):
    """A function that removes all characters c and C from a string."""
    update_list = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(update_list))
