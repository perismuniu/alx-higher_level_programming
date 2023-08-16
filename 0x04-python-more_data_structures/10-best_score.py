#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    highest_score = max(a_dictionary, key=lambda key: a_dictionary[key])
    return highest_score
