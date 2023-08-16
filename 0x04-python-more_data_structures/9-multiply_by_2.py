#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        value_times_two = value * 2
        new_dictionary[key] = value_times_two
    return new_dictionary
