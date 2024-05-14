#!/usr/bin/python3
def uniq_add(my_list=None):
    if my_list is None:
        my_list = []
    total = 0
    for unique_element in set(my_list):
        total += unique_element
    return total
