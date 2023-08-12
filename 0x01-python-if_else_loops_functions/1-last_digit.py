#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
str_p = "Last digit of"
str_s = "is"

if digit > 5:
    print(f'{str_p} {number} {str_s} {digit} and is greater than 5')
elif digit == 0:
    print(f'{str_p} {number} {str_s} {digit} and is 0')
elif 0 < digit < 6:
    print(f'{str_p} {number} {str_s} {digit} and is less than 6 and not 0')
elif digit < 0:
    print(f'{str_p} {number} {str_s} {digit} and is less than 6 and not 0')
