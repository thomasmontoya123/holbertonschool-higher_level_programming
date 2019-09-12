#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_of_args = len(sys.argv)
    if number_of_args == 1:
        print("0 arguments.")
    elif number_of_args == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        i = 1
        number_of_args = number_of_args - 1
        print("{} arguments:".format(number_of_args))
        for j in range(number_of_args):
            print("{}: {}".format(i, sys.argv[j + 1]))
            i = i + 1
