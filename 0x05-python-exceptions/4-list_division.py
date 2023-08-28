#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            r1 = my_list_1[i]
            r2 = my_list_2[i]
            result = 0
            if isinstance(r1, (int, float)) and isinstance(r2, (int, float)):
                if r2 != 0:
                    result = r1 / r2
                else:
                    print("division by 0")
            else:
                print("wrong type")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)

    return new_list
