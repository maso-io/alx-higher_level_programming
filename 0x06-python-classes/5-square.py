#!/usr/bin/python3
"""Defining a Square Class"""


class Square:
    """
        Class that represents a square of a defined `size`
    """
    def __init__(self, size=0):
        """Initializes an instance of the square class

        Args:
        size (float): The size of the square.

        Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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
            for _ in range(self.__size):
                tmp = '#' * self.__size
                print("{}".format(tmp))
