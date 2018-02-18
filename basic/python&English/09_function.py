#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:02:54 2018

@author: wei
"""

'''
One day, you will often encounter calculation and logical operations repeatedly.

One way to handle this is to write the same code over, over, over....

A better solution is to write a function.

function enable you to reuse logic an infinite number of times without repeating yourself.
'''

# first, you can use def() to define the function
# def function_name():        ()parentheses :colon
#     pass                    it can let funtion skip it
print(dir())
def f():
    pass
f()# you have to use function() to call it, if you just type function you will get memory address

def ping():
    return "Ping!" # this is the function return value, it can be number, boolean or... something, also can function.
print(ping())
x = ping() # this is assign the function to x, so now x is also a function
print(x)
print(dir())

import math
print(dir(math))
print(math.pi)
def volume(r):
    """Return the volume of a sphere with radius r.""" 
    # this is call the "docstring", provides documentation on what the function does and how to use it.
    v = (4/3) * math.pi * r**3 
    return v

print(volume(2)) # test, if you don't have input the value, you will get error
# and ypu can use help() to view how to use
help(volume)

def triangle_area(b, h):
    """Return the area of a triangle with base b and height h."""
    return 0.5 * b * h
print(triangle_area(3, 6))

# keyword arguments(default arguments)
def cm(feet=0, inches=0):
    """Covert a length from feet and inches to centimeters."""
    inches2cm = inches * 2.54
    feet2cm = feet * 12 * 2.54
    return inches2cm + feet2cm

# use keyword, you can input place of argrments what you like
print(cm(5))
print(cm(inches=70))
print(cm(inches=8, feet=5), cm(feet=5, inches=8))

# there are two kinds of argumrnts, required and keyword
# notice keyword must to put the back, or you will get error
#def g(x=0, y):
#    return x + y
# because if you type keyword is front of required, Python will skip the required.
def g(y, x=0):
    return x + y

print(g(5))
print(g(7, x=3))




