#!/usr/bin/python3
"""This module defines a square object"""


class Square:

    """class Square contains method defining attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize method for storing attribute"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or\
                len(value) != 2 or\
                not isinstance(value[0], int) or\
                not isinstance(value[1], int) or\
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """prints a square"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")