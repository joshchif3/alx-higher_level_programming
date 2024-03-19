#!/usr/bin/python3
def no_c(my_string):
    chrs = list(my_string)
    for onechr in listofchars:
        if onechr == 'c' or onechr == 'C':
            chrs.remove(onechr)
    return("".join(chrs))
