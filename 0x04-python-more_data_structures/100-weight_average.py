#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = 0
    total_weighted_sum = 0
    for value, weight in my_list:
        total_weighted_sum += (value * weight)
        total_weight += weight

    if total_weight == 0:
        return 0

    average = total_weighted_sum / total_weight
    return average
