#!/usr/bin/python3

"""
The 3-say_my_name module provides a function for printing out users name

Author: Gilbert Malova
Date: 05/06/2023
"""

def say_my_name(first_name, last_name=""):
    """
    Prints out name

    Args:
        first_name (string): Person's first name
        last_name (string): Person's last name

    Returns:
        string: Both names

    Raises:
        TypeError: When first_name or lastname is not string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
