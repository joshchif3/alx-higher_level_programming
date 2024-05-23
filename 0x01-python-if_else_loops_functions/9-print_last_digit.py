#!/usr/bin/python3
def print_last_digit(input_number):
    if input_number < 0:
        last_digit = input_number % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = input_number % 10
        print(last_digit, end='')
    return abs(last_digit)
