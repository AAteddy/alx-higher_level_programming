#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """A function that computes the square value of
    all integers of a matrix using map."""
    return (list(map(lambda item: list(map(lambda y: y ** 2, item[:])), matrix)))
