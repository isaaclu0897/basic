# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:33:32 2017

@author: VX
"""
import math

def check(x):
    if not isinstance(x, (int, float)):
        raise TypeError('type error, please input int or float')


def quadratic(a, b, c):
    check(a)
    check(b)
    check(c)
    
    D = b ** 2 - 4 * a * c
    if D >= 0:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
        if D > 0:
            return x1, x2
        elif D == 0:
            return x1
    else:
            print(D)
            
print(quadratic(1, 5, 4))
print(quadratic(1, 4, 4))
print(quadratic(1, 3, 4))

f, g, h = float(input('input f: ')), float(input('input g: ')), float(input('input h: '))
print(quadratic(f, g, h))