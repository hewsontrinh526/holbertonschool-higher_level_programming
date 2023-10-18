#!/usr/bin/python3
"""
Module: 7-add_item - A script that adds all arguments to a Python List, and
then save them to a file
"""
import json
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

if not os.path.exists(filename):
    my_list = []
else:
    my_list = load_from_json_file(filename)

new_item = sys.argv[1:]
for i in new_item:
    my_list.append(i)
save_to_json_file(my_list, filename)
