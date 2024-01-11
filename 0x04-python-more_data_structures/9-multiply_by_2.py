#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    new_dict = dict()
    for k, v in a_dictionary.items():
        new_dict[k] = 2*v
    return new_dict
