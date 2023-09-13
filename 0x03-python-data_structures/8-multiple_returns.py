#!/usr/bin/python3

def multiple_returns(sentence):
    lent = len(sentence)
    if lent == 0:
        return (0, None)
    else:
        store = (lent, sentence[0])
        return store
