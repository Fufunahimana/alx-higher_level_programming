#!/usr/bin/python3

def max_integer(my_list=[]):
    max_value = 0

    if len(my_list) > 0:
        for i in my_list:
            if i > max_value:
                max_value = i
    else:
        return None
    return max_value
