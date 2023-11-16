#!/usr/bin/python3
"""text_indentation fuction"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt_len = len(text)
    out = ""
    idx = 0
    while idx < txt_len:
        if text[idx] in [".", "?", ":"]:
            out += text[idx] + "\n" * 2
            idx += 1
            while idx < txt_len and text[idx] == " ":
                idx += 1
        else:
            out += text[idx]
            idx += 1
    print(out)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")