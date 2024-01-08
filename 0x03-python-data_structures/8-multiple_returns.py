#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        char = 'None'
        x = 0
    else:
        char = sentence[0]
        x = len(sentence)
    return x, char
