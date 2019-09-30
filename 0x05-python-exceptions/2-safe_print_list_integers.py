#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_counter = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            print_counter += 1
        except (ValueError, TypeError):
            pass
        except IndexError as error:
            raise
    print()
    return print_counter
