#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)
    unique_list = list(unique_set)
    total = 0
    for i in unique_list:
        total += i
    return total
