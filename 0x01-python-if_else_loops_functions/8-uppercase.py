#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        upper_ch = chr(ord(ch) - 32) if 'a' <= ch <= 'z' else ch
        print("{}".format(upper_ch), end='')
    print()
