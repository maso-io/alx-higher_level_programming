#!/usr/bin/python3
"""Defines a class Square."""


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
        self._size = size
