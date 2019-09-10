#!/usr/bin/python3
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif index % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif index % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{:d}".format(index), end=" ")
