#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list)
    if i > 0:
        i -= 1
        while i:
            j = 0
            while j < i:
                if my_list[j] < my_list[j+1]:
                    tmp = my_list[j]
                    my_list[j] = my_list[j+1]
                    my_list[j + 1] = tmp
                j += 1
            i -= 1
        return my_list[0]
    else:
        return 'None'
