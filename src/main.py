#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## Alexandre Wagner - Victor Rouxel
## File description:
## Groundhog projet
##

from src.groundhog import Groundhog
import sys

def groundhog_day():
    groundhog = Groundhog()
    groundhog.start()

if __name__ == '__main__':
    groundhog_day()
