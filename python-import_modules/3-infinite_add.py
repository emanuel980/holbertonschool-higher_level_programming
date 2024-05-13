#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total_sum = 0
    count = len(sys.argv) - 1
    for i in range(count):
        total_sum += int(sys.argv[i + 1])
    print("{}".format(total_sum))
