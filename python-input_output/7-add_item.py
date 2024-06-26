#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then save them to a file"""
import sys
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_file = 'add_item.json'
my_list = []
if os.path.exists(my_file) and os.path.getsize(my_file) > 0:
    my_list = load_from_json_file(my_file)

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        my_list.append(elem)
save_to_json_file(my_list, my_file)