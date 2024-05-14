#!/usr/bin/python3
def search_replace(my_list, search_term, replace_term):
    index = 0
    new_list = my_list.copy()
    for item in my_list:
        if item == search_term:
            new_list[index] = replace_term
        index += 1
    return new_list
