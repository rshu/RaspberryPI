#!/usr/bin/env python
import LCD1602
import time
from time import strftime
from datetime import datetime
from subprocess import *
from weather import Weather, Unit


def setup():
    LCD1602.init(0x27, 1)  # init(slave address, background light)
    LCD1602.clear()


def loop(content):
    space = '                '
    greetings = content
    greetings = space + greetings
    while True:
        tmp = greetings
        for i in range(0, len(greetings)):
            LCD1602.write(0, 2, tmp[:16])
            tmp = tmp[1:]
            time.sleep(0.1)
            LCD1602.clear()


def destroy():
    pass


def getWeather(area):
    weather = Weather(unit=Unit.CELSIUS)
    lookup = weather.lookup_by_location(area)
    condition = lookup.condition
    return condition.temp


if __name__ == "__main__":
    setup()
    condition = getWeather('raleigh')
    while True:
        #        LCD1602.init(0x27, 1)	# init(slave address, background light)
        LCD1602.write(0, 0, datetime.now().strftime("%b%d %a %H:%M"))
        LCD1602.write(0, 2, condition + " degree")
        time.sleep(10)
#    setup()
#    loop("Congrats for Patrick Xia passing the Written Exam!")
