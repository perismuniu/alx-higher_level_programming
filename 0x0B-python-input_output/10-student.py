#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """
    A class representing a student with
    first name, last name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
           first_name (str): The first name of the student.
           last_name (str): The last name of the student.
           age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
            Defaults to None, which means all attributes will be retrieved.

        Returns:
             dict: A dictionary containing the student's
             first name, last name, and age.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)
                   }
