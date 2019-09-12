#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for index in sys.argv[1:]:
        result += int(index)
    print("{}".format(result))
