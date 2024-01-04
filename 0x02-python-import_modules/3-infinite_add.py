#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = len(sys.argv)
    if i == 1:
        print(f'{0:d}')
    else:
        val = 0
        for x in range(1, i):
            val += int(sys.argv[x])
        print(f'{val:d}')
