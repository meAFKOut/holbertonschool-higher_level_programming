#!/usr/bin/python3



#!/usr/bin/python3
"""This class contains class named BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class.

    Attributes
    ----------
        __width : int
        __height : int
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = h
