#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## Alexandre Wagner - Victor Rouxel
## File description:
## Groundhog projet
##

import sys
import math

class Groundhog:
    def __init__(self):
        self._nbTendency = 0
        self._weirdestValueList = []
        self._Lastr = 0
        self._r = 0
        self._g = 0
        self._s = 0
        self._period = 0

    def help():
        print("SYNOPSIS")
        print("\t./groundhog period")
        print("")
        print("DESCRIPTION")
        print("\tperiod\tthe number of days defining a period")

    def parsing(self):
        if len(sys.argv) != 2:
            exit(84)
        if sys.argv[1] == "-h":
            help()
            exit(0)
        try:
            self._period = (int)sys.argv[1]
        except BadArgument:
                exit(84)

    def prompt(self):
        temperature = []

        while(1):
            user_input = input()
            if user_input == 'STOP':
                self.groundhog_end()
            else:
                temperature.append(user_input)
                self.calcul_weather(temperature)
                self.display(temperature)


    def calcul_weather(self, temperature):
        if (len(self._weirdestValueList) <= self._period)
            return
        self.temperatureIncreaseAverage(temperature) # calcul for g value (self._g)
        self.relativeTemperatureEvolution(temperature) # calcul for r value (self._r)
        self.standardDeviation(temperature) # calcul for s value (self._s)

    def temperatureIncreaseAverage(self):
        self._g = 0

    def relativeTemperatureEvolution(self):
        self._Lastr = self._r
        var1 = temperature[len(temperature) - self._period - 1]
        var2 = temperature[-1]
        self._r = (int)(round((var2-var1)/var1*100))


    def standardDeviation(self):
        self._s = 0

    def display(self)
        if (len(temperature) <= self._period)
            print("g=nan\tr=nan%\ts=nan")
        else
            Weather_message = "g=" + str(self._g) + "\tr=" + str(self._r) + "%\ts=" + str(self._s)
            if (((self._Lastr < 0 and self._r  >= 0) or (self._Lastr >= 0 and self._r < 0)) and self._Lastr)
                Weather_message += "\ta switch occurs"
                self._nbTendency += 1
            print(Weather_message)

    def groundhog_end(self):
        Message_tendency_witched = "Global tendency witched " + str(self._nbTendency) + " times"
        Message_weirdest_value = str(len(self._weirdestValueList)) + " weirdest values are [" + str(self._weirdestValueList)[1:-1], "]"

        print(Message_tendency_witched)
        print(Message_weirdest_value)
        exit(0)


    def start(self):
        self.parsing()
        self.prompt()
