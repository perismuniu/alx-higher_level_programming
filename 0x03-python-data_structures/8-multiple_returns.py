#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first_letter = None
    else:
        first_letter = sentence[0]

    return len(sentence), first_letter
