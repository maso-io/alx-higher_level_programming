#!/usr/bin/python3
class Square:
    """
        Class that represents a square of a defined `size`

        Attributes:
            size (float): The size of the square.

        Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
