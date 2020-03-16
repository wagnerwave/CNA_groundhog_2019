#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## Alexandre Wagner - Victor Rouxel
## File description:
## Groundhog projet
##

import sys

def groundhog_end():
    exit(84)

def groundhog():
    p = sys.argv[1]

    while(1):
        user_input = input()
        if user_input == 'STOP':
            groundhog_end()
        else:
            exit(0)

def help():
    print("SYNOPSIS")
    print("\t./groundhog period")
    print("")
    print("DESCRIPTION")
    print("\tperiod\tthe number of days defining a period")

def parsing():
    if len(sys.argv) < 2:
        help()
        exit(84)
    if sys.argv == "-h":
        help()
        exit(84)


if __name__ == '__main__':
    parsing()
    groundhog()
