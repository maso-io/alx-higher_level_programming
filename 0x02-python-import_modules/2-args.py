#!/usr/bin/python3

if __name__ == "__main__":
   import sys

   i = len(sys.argv)
   if i == 1:
       print(f'0 arguments.')
   else:
       if i == 2:
           print(f'1 argument:')
           print(f'1: {sys.argv[1]}')
       else:
           print(f'{i - 1:d} arguments:')
           for x in range(1, i):
               print(f'{x:d}: {sys.argv[x]}')
