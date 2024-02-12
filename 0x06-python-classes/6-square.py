#!/usr/bin/python3
class Square:
    """
        Class that represents a square of a defined `size`

        Attributes:
            size (float): The size of the square.
            position (:tuple: `int`, `int`): Position of the square

        Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
        self._position = position

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
            Updates the size of the square

            Args:
                value (float): `size` of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def my_print(self):
        """
            Prints in stdout the square with the character #
        """
        if self._size < 0:
            pass
        elif self._size == 0:
            print()
        else:
            if self._position[1] > 0:
                for _ in range(self._position[1]):
                    print("")
            for _ in range(self._size):
                tmp = ''
                if self._position[0] > 0:
                    tmp += "_" * self._position[0]
                tmp += '#' * self._size
                print("{}".format(tmp))

    @property
    def position(self):
        """
            Returns the position of the square

            Return:
                tuple (`int`, `int`): coordinate position of the square
        """
        return self._position[0], self._position[1]

    @position.setter
    def position(self, position=(0, 0)):
        """
            Updates the position of the square

            Args:
                position (:tuple: `int`, `int`): tuple to update the position
                of the square.
        """
        if not isinstance(position, type((0,0))):
            print("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0 or len(position) != 2:
            print("position must be a tuple of 2 positive integers")
        self._position = position[0], position[1]
