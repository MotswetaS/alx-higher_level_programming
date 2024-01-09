#!/usr/bin/python3
"""script that adds all arguments to a Python list, and save them to a fil"""
import sys


if__name = "__main__":
    save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file.py').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_items.json")
