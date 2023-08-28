#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element_count = 0
    for item in my_list:
        try:
            if element_count >= x:
                break
            print("{:d}".format(item), end="")
            element_count += 1
        except (TypeError, ValueError):
            continue
    print()
    return element_count
