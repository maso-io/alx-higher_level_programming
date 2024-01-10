#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    lst = my_list[:]
    for i in range(len(lst)):
        print("{}".format(lst[i]))
        if lst[i] == search:
            lst.insert(i, replace)
            return lst
