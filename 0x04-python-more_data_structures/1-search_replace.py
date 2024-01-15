#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    lst = my_list[:]
    for i in range(len(lst)):
        if lst[i] == search:
            lst[i] = replace
    return lst
