#!/usr/bin/python3
"""
Module: 1-rectangle

A class that defines a rectangle
"""


class Rectangle:
    """
    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle

    Methods:
        __init__(self, width=0, height=0): Initialises a new
            instance of a rectangle

        width(self): Retrieves the width

        width(self, value): Determines whether the
            value is suitable for the width

        height(self): Retrieves the height

        height(self, value): Determines whether the
            value is suitable for the height

        area(self): Finds the area of the rectangle

        perimeter(self): Finds the perimeter of the rectangle

        __str__(self): Prints a rectangle

        __repr__(self): Returns a string representation of the rectangle
            object that can be used to create a normal rectangle

        __del__(self): Deletes a rectangle

        bigger_or_equal(rect_1, rect_2): Compares two rectangles
            and determines whether one is bigger than the other
            or if they have equal area
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialises a new instance of a rectangle

        Arguments:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        """
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieves itself
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Determines whether the value is suitable for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves itself
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Determines whether the value is suitable for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Finds the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Finds the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """
        Prints a rectangle
        """
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle = rectangle + str(self.print_symbol)
            if i != self.__height - 1:
                rectangle = rectangle + "\n"
        return rectangle

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        object that can be used to create a normal rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        Deletes the rectangle instance
        """
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and determines whether one rectangle is
        bigger than the other, or if they have equal area
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Prints a square-shaped reactangle using the Rectangle class
        with equal height and width

        Args:
            clas: the class
            size (int): The size of the square, i.e. side length

        Returns:
            Rectangle: A square-shaped rectangle
        """
        return cls(size, size)
