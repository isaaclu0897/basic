#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:13:01 2018

@author: wei
"""

'''
In Python3 have 3 different types,

there are int, float, and complex,

then we need to learn how to arithmetic(算法, 四則運算) in Python,

there have 4 different operations,

+(addition), -(subtraction), *(multiplication), /(division),

today I will show you arithemic how to combine numbers and operations 
'''

# first, you need to understand the ideal of norrower and wider
x = 28; print(x) # int
y = 28.0; print(y) # float
y = float(28); print(y) # then you can use this way to convert number from integer to float constructor

# then pi = 3.1415926..... that is float, but you can't convert it to int
pi = 3.1415926; print(pi)
pi = int(3.1415926); print(pi) # that will show you 3, you won't want to see that


'''
so, we can say int narrower than float,

that is to say, float wider than int, float and complex also like that.

If you want to do arthmetic, you just convert the norrower to wider, do you know what I mean?

OR you will see something ridiculous.
'''
a = 2 # int
b = 6.0 # float
c = 12 + 0j # complex

# If you do arthmetic combine 2 different types, Python will automectic convert the norrower to wider
k = a + b; print(k) # int + float > float
k = b - a; print(k) # float - int > float
k = b * c; print(k) # float * complex > comlex
k = b / c; print(k) # float / complex > comlex

# when you division, you will see the float
print(16/5)
# but if you want to see quotient(商) and remainder(餘數), you can use // and %
print(16//5) # quotient
print(16%5) # reminder






