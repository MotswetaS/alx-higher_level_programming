#!/usr/bin/python3
"""Creating an object from a json file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""

    with open(filename, "w", encoding="utf-8")as f:
        return json.load(f)
