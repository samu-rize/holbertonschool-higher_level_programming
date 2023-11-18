#!/usr/bin/python3
"""Script to add command line arguments to a JSON file."""
import sys

# Importing functions from external modules
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file.py').load_from_json_file

if __name__ == "__main__":

    # Load existing JSON file or initialize an empty list
    try:
        the_list = load_from_json_file('add_item.json')
    except BaseException:
        the_list = []

    # Add command line arguments to the list
    the_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(the_list, 'add_item.json')
