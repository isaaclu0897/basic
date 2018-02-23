#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:47:09 2018

@author: wei
"""

'''
Python have several numeric types, but there is only one logical type: booleans

A booleans can only take 2 values: True and False, this is all you need, if you are logical.

'''

# Booleans values: True, False, take care to note that "T"rue and "F"alse are both capitalized(大寫)
print(True)
print(False)
# if you type true or false you will get Nameerror
#print(true)
#print(false)

# Booleans are commonly encountered when comparing two objects.
a = 3
b = 5
# to compare two numbers, use double equals operator.
# one equal is assign; and two equal is compare
print(a == b) # we get "False", since a and b are different integers
print(a != b) # if you type not equal, it will return "True", because a doesn't equal to b
print(a > b) # type a greater than b, this is False statement
print(a < b) # type a less than b, this is True statement

# then we can use type to check it
print(type(True))
print(type(False)) # you will get type 'bool'
# that tell us, we can you bool() to convert values
print(bool(28))
print(bool(-2.718))
print(bool(0)) # In python, 0 is converted to False, while every other number is converted to True

print(bool("good"))
print(bool(" "))
print(bool("")) # the empty string is converted to False, other is True

# then you also can coverted bool to others type
print(str(True))
print(str(False))

print(int(True))
print(int(False))

# you also can use it to do arithmetic
print(5 + True)
print(10 * False) # it will autometic converted bool to numberics type
