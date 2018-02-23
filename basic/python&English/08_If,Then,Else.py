#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:21:26 2018

@author: wei
"""

'''
sometimes you need many kinds of direction, let you select,

this time the if, then eles statement can help you navigate these situations
'''

Input = input("please enter a test string: ") # let user input the values, the string can prompt user

# len() can calculate the length of object
if len(Input) < 6: # use if statement, if True it will do or skip
    print('your string is too short.')
    print('please entr a string with at least 6 characters')
# the line of if statement ends with a colon(冒號), the following lines are indented
# Python is not like C, C++, Java the indented is useles
    
#%%
number = int(input("please enter an integer: "))
# if you input the string, you will get valueerror since the string can not convert to number

if number % 2 == 0:
    print('your number is even')
else:
    print('your number is odd')
    
#%%
# scalene(不等邊) triangle: all sides have different lengths.
# isosceles(等腰) triangle: two sides have the same length.
# Equilateral(全等) triangle: all sides are equal
a = int(input("the length of side a = "))
b = int(input("the length of side b = "))
c = int(input("the length of side c = "))

if a!=b and b!=c and a!=c:
    print("this is a scalene triangle")
elif a==b and b==c: # this is short for else if
    print('this is a isosceles triangle')
else:
    print('this is a equilateral triangle')
