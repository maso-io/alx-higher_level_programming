#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    value_of_key = a_dictionary.get(key)

    if value_of_key is not None:
        del a_dictionary[key]

    return a_dictionary
