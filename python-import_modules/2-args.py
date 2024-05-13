#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_count = len(argv) - 1
    print("Number of argument{}: {}".format('' if arg_count == 1 else 's', arg_count), end='')
    print('' if arg_count == 0 else ':')
    for i in range(arg_count):
        print("{}: {}".format(i + 1, argv[i + 1]))
