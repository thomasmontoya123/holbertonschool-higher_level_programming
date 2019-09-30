def safe_print_list(my_list=[], x=0):
    print_counter = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end='')
            print_counter += 1
        except IndexError:
            break
    print()
    return print_counter
