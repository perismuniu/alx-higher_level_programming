#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a specialized form of a rectangle.

    Attributes:
        size (int): The size (width and height) of the square.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): The unique identifier for the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Constructor for Square class.
        __str__(self): Returns a string representation of the square.

    Note:
        A Square is a specialized form of a Rectangle
        with equal width and height.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size (width and height) of the square.
            x (int, optional): The x-coordinate of the top-left corner
                               of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner
                               of the square. Defaults to 0.
            id (int, optional): The unique identifier for the square.
                                Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
         Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] (<id>) <x>/<y> - <size>"
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Get the size (width and height) of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size (width and height) of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if type(value) != int or value <= 0:
            raise ValueError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
         Update attributes of the square.

        Args:
            *args: List of arguments - no-keyworded arguments.
                1st argument: The id attribute.
                2nd argument: The size attribute.
                3rd argument: The x attribute.
                4th argument: The y attribute.

            **kwargs: Double pointer to a dictionary representing
            keyworded arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Return a dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the Square's attributes.
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
