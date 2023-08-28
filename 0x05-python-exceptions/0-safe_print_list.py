#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_count = 0
    for item in my_list:
        try:
            print(item, end="")
            element_count += 1
        except IndexError:
            print("Index is not available")
        if element_count == x:
            break
    print()
    return element_count
