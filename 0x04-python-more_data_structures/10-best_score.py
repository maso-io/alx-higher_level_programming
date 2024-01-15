#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return
    tmp = 0
    for k, v in a_dictionary.items():
        if tmp <= v:
            tmp = v
            key = k
    return key
