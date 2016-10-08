#!/usr/bin/env python3

import sys

def print_greetings(length):
    if length == 0:
        print('Hello World!')
    else:
        print("Hello " + sys.argv[1] + "!")

def arg_length():
    if len(sys.argv) == 1:
        return 0
    else:
        return 1

argument=arg_length()
print_greetings(argument)


