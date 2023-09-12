#!/usr/bin/python3
"""Defines a file reading functions"""


def read_file(filename=""):
    """Prints the content of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
