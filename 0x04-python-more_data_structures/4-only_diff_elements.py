#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uncommon_set_1 = set(set_1)
    uncommon_set_2 = set(set_2)
    uncommon_set = uncommon_set_1 ^ uncommon_set_2
    uncommon_list = list(uncommon_set)
    return uncommon_list
