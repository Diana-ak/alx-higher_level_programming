#!/usr/bin/python3

"""Define a class Square."""


class Square: 
    """ represents the class square"""

    def __init__(self, size=0):
        """ initialize new class.


        Args:
            size (int): The size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueErro("size must be >= 0")
        self.__size = size
