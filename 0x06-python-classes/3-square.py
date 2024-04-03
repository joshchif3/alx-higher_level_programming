#!/usr/bin/python3

"""Def the class Square."""


class Square:
    """Takes a sqr."""

    def __init__(self, size=0):
        """Call a new sqr..

        Args:
            size (int): Size of sqr.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Show the current area of the sqr."""
        return (self.__size ** 2)
