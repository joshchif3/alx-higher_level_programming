#!/usr/bin/python3

"""Def a Sqr class."""


class Square:
    """Hold value sqr."""

    def __init__(self, size=0):
        """start a new Sqr.

        Args:
            size (int): SIZE OF square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
