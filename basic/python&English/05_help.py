#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:57:15 2018

@author: wei
"""

'''
Today will show you how to use interactive help of Built-in,

when you haven't internet access, that is very helpful,

and that can help you to learn the classes, modules and functions...etc. quickly.

'''

# first you need to use dir()(directory) to show that you have modules now.
print(dir()); print() # now we see some moudules
# then we can use dir(__builtins__) to view built-ins modules
print(dir(__builtins__)); print() 
# then you need to call the help() for learn, now let we see the pow function
help(pow)
# It tell as use pow(x, y) equivalent to x ** y, and pow(x, y, z) equivalent to x**y % z, let me show to you
print(pow(2, 10), 2 ** 10)
print(pow(2, 10, 3), 2 ** 10 % 3)

# let we see another sample, we see the hex function
help(hex)
print(hex(10)) # now you get the hex(10), and you use type() you will know that is string
# you can also use 0xa to covert the hex to dec, but you rememmber can't add quotes
print('0xa', 0xa) # because the python will interpret as a string, not a number

# then we can use help('modules') to view moudles what you have 
#help('modules')
# use import ... to call them
import math
print(dir()) # now you can see moudle of math
print(dir(math)) # use dir(math) can view functions what it have
# let we see how to use raadians, now if you type help(radians), you we get Nameerror
# because, radians in the modules of math, so you should use math.radians to call it
help(math.radians) 
# now you can use math.radians() to call it, let we check it
print(math.radians(180), math.pi)