#!/usr/bin/python3
"""A locked class"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance
    except if the new instance attribute is called first_name
    """

    __slots__ = ["first_name"]
