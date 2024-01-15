#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    tmp = set(my_list)
    res = 0
    for x in tmp:
        res += x
    return res
