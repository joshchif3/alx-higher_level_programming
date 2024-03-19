#!/usr/bin/python3
def no_c(my_string):
    characters = list(my_string)
    for character in characters:
        if character == 'c' or character == 'C':
            characters.remove(character)
    return "".join(characters)
