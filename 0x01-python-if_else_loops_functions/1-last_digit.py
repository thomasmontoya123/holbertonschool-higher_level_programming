#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str1 = " and is greater than 5"
str2 = " and is less than 6 and not 0"
if last_digit > 5:
    print("Last digit of {:d} is {:d}".format(number, last_digit) + str1)
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {:d} is {:d}".format(number, last_digit) + str2)
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))