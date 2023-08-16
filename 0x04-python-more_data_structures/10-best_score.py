#!/usr/bin/python3

def best_score(a_dictionary):
    """A function that returns a key with
    the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    result_item = list(a_dictionary.keys())[0]
    biggest = a_dictionary[result_item]
    for i, j in a_dictionary.items():
        if j > biggest:
            biggest = j
            result_item = i
    return (result_item)
