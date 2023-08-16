#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """A function that computes the square value
    of all integers of a matrix."""
    return ([list(map(lambda item: item * item, row)) for row in matrix])
