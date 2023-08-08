#!/usr/bin/python3
for tens_digit in range(0, 10):
    for ones_digit in range(tens_digit + 1, 10):
        print(f"{tens_digit:01d}{ones_digit:01d}", end="")
        if tens_digit < 8 or ones_digit < 9:
            print(", ", end="")
        else:
            print("\n", end="")
