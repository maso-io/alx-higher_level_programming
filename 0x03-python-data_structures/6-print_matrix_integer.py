#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print("{}".format(""))
    else:
        for row in matrix:
            i = 0
            for elem in row:
                if i == len(row) - 1:
                    print("{:d}".format(elem))
                else:
                    print("{:d}".format(elem), end=" ")
                i += 1
