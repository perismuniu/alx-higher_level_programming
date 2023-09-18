#!/usr/bin/python3
"""Defines the Base for all other classes"""

import json
import csv
import turtle


class Base:
    """
    Base class for all other classes

    Attributes:
        __nb_objects (private): The number of objects that
        have been created from the class.
        id (public): The unique identifier of the object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor.

        Args:
            id (optional): The unique identifier of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries: A list of dictionaries.

        Returns:
            JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries, indent=4)

    @classmethod
    def save_to_file(cls, list_objs):
        """
         Save a list of objects to a JSON file.

        Args:
            list_objs: A list of objects to be saved.

        Notes:
            - If list_objs is None, save an empty list.
            - The filename must be: <Class name>.json (e.g., Rectangle.json).
            - It uses the static method to_json_string (created before).
            - It overwrites the file if it already exists.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            json_data = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
              json_string: A JSON string.

        Returns:
              List of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set using a dictionary.

        Args:
            dictionary: A dictionary containing attribute values.

        Returns:
            An instance of the class with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            List of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_data = file.read()
                dictionaries = cls.from_json_string(json_data)
                instances = [cls.create(**dictionary)
                             for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            list_objs: A list of objects to be saved in CSV format.

        Notes:
            - If list_objs is None, save an empty list.
            - The filename must be: <Class name>.csv (e.g., Rectangle.csv).
            - The format of the CSV file depends on the class
              (Rectangle or Square).
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    data = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns:
            List of instances loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                                "id": int(row[0]),
                                "width": int(row[1]),
                                "height": int(row[2]),
                                "x": int(row[3]),
                                "y": int(row[4])
                                }
                    elif cls.__name__ == "Square":
                        dictionary = {
                                "id": int(row[0]),
                                "size": int(row[1]),
                                "x": int(row[2]),
                                "y": int(row[3])
                                }
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return []
