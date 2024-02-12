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

    def area(self):
        """
            Computes the area of a square of given `size`.

            Return:
                float: the area of the square.
        """
        return self._size ** 2

    @property
    def size(self):
        """
            Returns the size of a square

            Return:
                float: square size
        """
        return self._size

    @size.setter
    def size(self, value):
        """
            Set the size of the square

            Args:
                value (float): `size` of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        :x
