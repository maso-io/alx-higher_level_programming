#!/usr/bin/python3
"""Defininng a Square Class"""


class Square:
    """
        Class that represents a square of a defined `size`.
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """
            Computes the area of a square of given `size`.

            Return:
            float: the area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
            Returns the size of a square

            Return:
            float: square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Updates the size of the square

            Args:
            value (float): `size` of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
            Prints in stdout the square with the character #
        """
        if self.__size < 0:
            pass
        elif self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for _ in range(self.__position[1]):
                    print("")
            for _ in range(self.__size):
                tmp = ''
                if self.__position[0] > 0:
                    tmp += " " * self.__position[0]
                tmp += '#' * self.__size
                print("{}".format(tmp))

    @property
    def position(self):
        """
            Returns the position of the square

            Return:
            tuple (`int`, `int`): coordinate position of the square
        """
        return self.__position[0], self.__position[1]

    @position.setter
    def position(self, position=(0, 0)):
        """
            Updates the position of the square

            Args:
            position (:tuple: `int`, `int`): tuple to update the position
            of the square.
        """
        if not isinstance(position, type((0, 0))):
            print("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0 or len(position) != 2:
            print("position must be a tuple of 2 positive integers")
        self.__position = position[0], position[1]
