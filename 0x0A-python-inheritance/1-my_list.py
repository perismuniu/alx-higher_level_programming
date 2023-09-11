#!/usr/bin/python3
""" Defines a class MyList"""


class MyList(list):
    """This class defines MyList"""

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
