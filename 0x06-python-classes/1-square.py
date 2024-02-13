#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """
        Class that represents a square of a defined `size`
    """
    def __init__(self, size):
        """Initializes an instance of the class.

            Args:
            size (float): The size of the square
        """
        self.__size = size
