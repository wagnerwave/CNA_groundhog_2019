#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## Alexandre Wagner - Victor Rouxel
## File description:
## Groundhog projet
##

import sys
import math
import statistics as stats

class Groundhog:
    def __init__(self):
        self._nbTendency = 0
        self._weirdestValueList = []
        self._Lastr = 0
        self._r = 0
        self._g = 0
        self._s = 0
        self._period = 0
        self._temperature = []

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
            self._period = int(sys.argv[1])
        except ValueError:
            exit(84)

    def prompt(self):
        while(1):
            try:
                user_input = input()
            except EOFError:
                exit(84)
            except KeyError:
                exit(84)
            if user_input == 'STOP':
                if (len(self._temperature) < self._period):
                    exit(84)
                self.groundhog_end()
            else:
                try:
                    input_temperature = float(user_input)
                except ValueError:
                        exit(84)
                self._temperature.append(input_temperature)
                self.calcul_weather(user_input)
                self.display()

    def AdditionTemperatureByPeriod(self):
        i = 0
        result = 0

        while (i < self._period):
            result = result + self._temperature[i - self._period]
            i = i + 1
        return (result)

    def AddWeirdestValue(self, user_input):
        mobileAverage = (1 / self._period) * self.AdditionTemperatureByPeriod()
        HighBand = mobileAverage + 2 * float(self._s)
        LowBand = mobileAverage - 2 * float(self._s)
        List = []
        diff = 0

        List.append(user_input)
        try:
            diff = (float(user_input) - LowBand) / (HighBand / LowBand)
        except ZeroDivisionError:
            exit(84)
        if (diff > 0.5):
            List.append(1 - diff)
        else:
            List.append(diff)
        self._weirdestValueList.append(List)

    def calcul_weather(self, user_input):
        self.temperatureIncreaseAverage() # calcul for g value (self._g)
        self.relativeTemperatureEvolution() # calcul for r value (self._r)
        self.standardDeviation() # calcul for s value (self._s)
        if (len(self._temperature) >= self._period):
            self.AddWeirdestValue(user_input)

    def temperatureIncreaseAverage(self):
        if (len(self._temperature) >= self._period):
            count = len(self._temperature) - self._period
            self._g = 0
            while (count != len(self._temperature)):
                n  = self._temperature[count] - self._temperature[count - 1]
                self._g += n if n > 0 else 0
                count = count + 1
            self._g /= self._period
        else:
            self._g = "nan"

    def relativeTemperatureEvolution(self):
        if (len(self._temperature) >= self._period):
            if (self._r != "nan"):
                self._Lastr = self._r
            var1 = self._temperature[len(self._temperature) - self._period - 1]
            var2 = self._temperature[-1]
            if var1 == 0:
                self._r = int(0)
            else:
                self._r = int((round((var2-var1)/var1*100)))
        else:
            self._r = "nan"

    def standardDeviation(self):
        if (len(self._temperature) >= self._period - 1):
            self._s = stats.stdev(self._temperature)
        else:
            self._s = "nan"

    def temperatureSwitched(self):
        if (self._r != "nan"):
            if (self._Lastr < 0 and self._r > 0):
                return True
            elif (self._Lastr > 0 and self._r < 0):
                return True
            else:
                return False
        else:
            return False

    def display(self):
        if (self._r != "nan" and self._g != "nan" and self._s != "nan"):
            Weather_message = "g=" + str(round(self._g, 2)) + "\tr=" + str(round(self._r, 2)) + "%\ts=" + str(round(self._s, 2))
            if (self.temperatureSwitched() == True):
                Weather_message += "\ta switch occurs"
                self._nbTendency = self._nbTendency + 1
            print(Weather_message)
        elif (self._r == "nan" and self._g == "nan" and self._s != "nan"):
            Weather_message = "g=nan\tr=nan\ts=" + str(round(self._s, 2))
            print(Weather_message)
        else:
            print("g=nan\tr=nan%\ts=nan")

    def groundhog_end(self):
        FiveShapeOfWeirdestValue = []
        Message_tendency_witched = "Global tendency switched " + str(self._nbTendency) + " times"
        Message_weirdest_value = str(len(self._weirdestValueList)) + " weirdest values are [" + str(self._weirdestValueList)[1:-1], "]"

        print(Message_tendency_witched)
        self._weirdestValueList.sort(key=lambda x: x[1], reverse = False)
        if (len(self._weirdestValueList) >= 5):
            for x in range(0,5):
                FiveShapeOfWeirdestValue.append(self._weirdestValueList[x][0])
            print("5 weirdest values are ", FiveShapeOfWeirdestValue)
            exit(0)
        else:
            exit(84)

    def start(self):
        self.parsing()
        self.prompt()
