#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    padded_tuple_a = tuple_a + (0, 0)
    padded_tuple_b = tuple_b + (0, 0)

    result_one = padded_tuple_a[0] + padded_tuple_b[0]
    result_two = padded_tuple_a[1] + padded_tuple_b[1]

    result_tuple = (result_one, result_two)
    return result_tuple
