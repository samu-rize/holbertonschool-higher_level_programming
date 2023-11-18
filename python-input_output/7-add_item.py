#!/usr/bin/python3
"""Script to add command line arguments to a JSON file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    try:
        the_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        the_list = []

    the_list.extend(sys.argv[1:])
    save_to_json_file(the_list, 'add_item.json')
