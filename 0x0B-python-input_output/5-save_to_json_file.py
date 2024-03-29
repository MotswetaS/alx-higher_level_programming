#!/usr/bin/python3
"""This function saves an object toa file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    my_obj : object that you need to serialize to JSON and save to the file
    filename : name of the text file to which you should write the JSON
    representation of the object.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
