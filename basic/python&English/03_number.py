#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 00:31:53 2018

@author: wei
"""

'''
In Python2 have 4 types of numbers,

Python3 have 3 types of numbers,

then, they are int(integer), float and complex,

different Python2, version 3 don't need to judge the number is integer or long,

no size limits no overflowers

that's why, Python3 easier and fast than version 2.
'''

# integer
a = 496 # this is perfect number
# you can use type(var) to show the type
print(type(a)) # if you in the commander, just type the type(var)


# float, that is store the decimal(十進制) point of number
e = 2.718281828
print(type(e))


# complex, that can store the real and imaginary
z = 2 - 6j
print(type(z))
# then you can use attributes to show real and imaginary(虛部) by individually(個別的)
print(z.real)
print(z.imag)
print(type(z.imag)) # and type of the part is the float
