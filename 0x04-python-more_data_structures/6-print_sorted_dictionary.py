#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    keys = list(a_dictionary)
    sorted_keys = sorted(keys)
    for i in sorted_keys:
        print('{}: {}'.format(i, a_dictionary[i]))
