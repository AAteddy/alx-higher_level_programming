#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list.

    Args:
        my_list (list): the list to print elements from.
        x (int): the number of elements of my_list to print.

    Returns:
        the number of elements printed.
    """
    rtrn = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            rtrn += 1
        except IndexError:
            break
    print("")
    return (rtrn)
