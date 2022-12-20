#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """ represents the class quare"""

    def __init__(self, size=0):
        """initialize new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        size.__size = size

    def area(self):
        """Return the current area of the square."""
        return (size.__size * size.__size)
