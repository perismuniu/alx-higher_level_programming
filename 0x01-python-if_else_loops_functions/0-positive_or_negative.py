#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = int(input("Please enter a number : "))
if number > 0:
    print(number,'is positive')
elif number == 0:
    print(number,'is zero')
elif number < 0:
    print(number,'is negative')

