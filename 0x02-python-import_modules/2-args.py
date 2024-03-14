#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

arg_str_template = "{:d} argument"
arg_count = len(sys.argv) - 1
if arg_count == 0:
    arg_str_template += 's.'
elif arg_count == 1:
    arg_str_template += ':'
else:
    arg_str_template += 's:'
print(arg_str_template.format(arg_count))

index = 0
for arg in sys.argv:
    if index != 0:
        print("{:d}: {:s}".format(index, arg))
    index += 1
