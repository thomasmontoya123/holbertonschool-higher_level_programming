#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length is 0:
        return (0, None)
    else:
        first_character = sentence[0]
        return (length, first_character)
