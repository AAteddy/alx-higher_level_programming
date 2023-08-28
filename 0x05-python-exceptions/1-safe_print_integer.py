#!/usr/bin/python3

def safe_print_integer(value):
    """A function that prints an integer with "{:d}".format()

    Args:
        value (int): the integer to print

    Returns:
        if a TypeError or ValueError occurs - False
        otherwise - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
