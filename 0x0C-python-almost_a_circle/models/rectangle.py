#!/usr/bin/python3
"""Defines a Rectangle(Base) class"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class.

    Attributes:
        __width (private): The width of the rectangle.
        __height (private): The height of the rectangle.
        __x (private): The x-coordinate of the rectangle.
        __y (private): The y-coordinate of the rectangle.
    """
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            y (int, optional): The y-coordinate of the rectangle.
            id (int, optional): The unique identifier of the rectangle.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle to stdout using the character '#'.

        Takes care of x and y coordinates.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """

        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle using no-keyword arguments in
        the following order:
        1st argument: id attribute
        2nd argument: width attribute
        3rd argument: height attribute
        4th argument: x attribute
        5th argument: y attribute

        If **kwargs is provided, update attributes using key-value pairs.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary containing the attributes of the Rectangle.
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
