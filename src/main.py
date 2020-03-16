#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## Alexandre Wagner - Victor Rouxel
## File description:
## Groundhog projet
##

import sys

def groundhog():
    period = sys.argv[1] # nomber of days
    nb_tendency = 0 # nomber of global tendency switched
    wvlist = [1.32, 22.1] # list of weirdest values

    s = [] # standard deviate
    g = [] # temperature increase average
    r = [] # relative temparature evolution

    while(1):
        user_input = input()
        if user_input == 'STOP':
            groundhog_end(nb_tendency, wvlist)
        else:
            exit(0)

def groundhog_end(nb_tendency, wvlist):
    fbk = "["
    lbk = "]"
    print("Global tendency witched", nb_tendency, "times")
    print(len(wvlist),"weirdest values are ", fbk, str(wvlist)[1:-1], lbk)
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
        exit(0)


if __name__ == '__main__':
    parsing()
    groundhog()
