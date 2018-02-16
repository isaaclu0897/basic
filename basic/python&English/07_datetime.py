#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:40:14 2018

@author: wei
"""

# that we import the datetime module and use dir() to view it

import datetime
print(dir(datetime))
# it contains date class, time class, and datetime class.
# they can give us different precise to use. first, let we see how to use date class
# help(datetime.date)
gvr = datetime.date(1956, 1, 31) # this is the birthday of Guido van Rossum, the creator of Python
# you can use print to show the beautiful format
print(gvr)
# then you can show the year, month, and day individualy.
print(gvr.year)
print(gvr.month)
print(gvr.day)
# we can use timedelta class to add or substract a number of days
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt)

# then we can change different format for datetime, you have two way to do
print(gvr.strftime('%A, %B, %d, %Y')) # old way
message = "GVR was born on {:%A, %B, %d, %Y}."
print(message.format(gvr)) # new way

# date, time, datetime class, we will now crete object using all three class
# the SpaceX first lanched a reuse rocket on March 30, 2017 at 22:27 UTC
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date) # it only can contains date information
print(launch_time) # the launch_time contain time information
print(launch_datetime) # and the datetime contain everything
# the time class is also like date class, can show the hour, minute, and second individualy.
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
# the datetime class also can separately year, month, day, hour, minute, and second
# you can use datetime module datetime class today method to get current time
now = datetime.datetime.today()
print(now)
print(now.microsecond)

# then you can take a strings repersentation of a datetime convert it
moon_landing = "7/20/1969" # first, date of landing moon
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime, type(moon_landing_datetime))
