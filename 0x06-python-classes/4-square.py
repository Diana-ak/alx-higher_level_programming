#!/usr/bin/python3

class Square:
    def __init__(self, size=0)
    self.__size = size

    @property
    def size(self):
        return (self.__size)

    @property setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)