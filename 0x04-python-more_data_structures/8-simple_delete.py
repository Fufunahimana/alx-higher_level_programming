#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    keys = list(a_dictionary.keys())

    for my_key in keys:
        if my_key == key:
            del a_dictionary[my_key]
    return a_dictionary
