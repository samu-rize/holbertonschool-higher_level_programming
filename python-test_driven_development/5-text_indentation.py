#!/usr/bin/python3
"""text_indentation fuction"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    txt_len = len(text)
    out = ""
    idx = 0

    while idx < txt_len and text[idx] == " ":
        idx += 1

    while idx < txt_len:
        out += text[idx]
        if text[idx] == "\n" or text[idx] in ".?:":
            if text[idx] in ".?:":
                out += "\n"
            idx += 1
            while idx < txt_len and text[idx] == " ":
                idx += 1
            continue
        idx += 1
    print(out)    
