#!/usr/bin/python3
"""Text indentation

    * text must be a string, otherwise
    raise a TypeError exception with the message:
    "text must be a string"

    * There should be no space at the beginning or
    at the end of each printed line
"""


def text_indentation(text):
    """prints a text with 2 new lines after each
        of these characters: ., ? and :

        Parameters
        ----------
        text : str
        text to ident

        """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    else:
        new_text = ""
        for i in range(len(text)):
            if (text[i] in ['.', '?', ':']):
                new_text += text[i] + "\n\n"
            else:
                if (text[i] is " " and text[i - 1]
                        in ['.', '?', ':'] and i != 0):
                    pass
                else:
                    new_text += text[i]
    print(new_text, end="")
