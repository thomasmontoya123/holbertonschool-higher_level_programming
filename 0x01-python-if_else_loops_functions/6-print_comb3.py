#!/usr/bin/python3
for first_digit in range(0, 10):
    for second_digit in range(0, 10):
        if first_digit == 8 and second_digit == 9:
            print("{}{}".format(first_digit, second_digit))
        elif second_digit > first_digit:
            print("{}{}, ".format(first_digit, second_digit), end="")
