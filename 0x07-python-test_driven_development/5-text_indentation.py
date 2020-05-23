#!/usr/bin/python3
"""[summary]"""


def text_indentation(text):
    """[summary]

    Arguments:
        text {[type]} -- [description]

    Raises:
        TypeError: [description]
    """

    if type(text) in [str]:
        for idx in range(len(text)):
            if text[idx] in [".", "?", ":"]:
                print(text[idx] + '\n', end='\n')

            else:
                if (text[idx-1] not in [".", "?", ":"]):
                    print(text[idx], end='')
    else:
        raise TypeError("text must be a string")
