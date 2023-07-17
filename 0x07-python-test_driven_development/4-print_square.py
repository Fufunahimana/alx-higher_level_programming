#!/usr/bin/python3

"""
The 4-print_square module provides a function that prints squares
"""

def print_square(size):
    """
    Prints squares with #

    Args:
        size(int): size of the square

    Returns:
        Nothing
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for i in range(size):
            print("#".format(), end='')
        print()

