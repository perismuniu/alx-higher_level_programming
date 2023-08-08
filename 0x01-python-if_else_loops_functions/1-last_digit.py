#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str_prefix = "Last digit of"
str_suffix = "is"

if number > 5:
    print(f'{str_prefix} {number} {str_suffix} {last_digit} and is greater than 5')
elif number == 0:
    print(f'{str_prefix} {number} {str_suffix} {last_digit} and is 0')
elif number < 6 and number > 0:
    print(f'{str_prefix} {number} {str_suffix} {last_digit} and is less than 6 and not 0')
elif number < 0:
    print(f'{str_prefix} {number} {str_suffix} {last_digit} and is less than 6 and not 0')
