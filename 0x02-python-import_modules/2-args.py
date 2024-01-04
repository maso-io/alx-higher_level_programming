#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = len(sys.argv)
    if i == 1:
        print(f'0 arguments.')
    else:
        print(f'{i - 1:d} arguments:')
        for x in range(1, i):
            print(f'{x:d}: {sys.argv[x]}')
