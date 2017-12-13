# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:03:40 2017

@author: VX
"""
# input() & output(print())

#==============================================================================
# input()
#==============================================================================
name = input('請輸入您的大名: ')
print('hello,', name)

''' 在 py2 當中，要輸入提示文字，必須使用 raw_input()
ex: name = rawinput('請輸入您的大名: ')
    print('hello,', name)
    # hello, name
'''

a = input('enter your name :')
b = input('enter your age :')
c = int(input('about yourself :\n'))
print()
print(a)
print(b)
print(c)

#==============================================================================
# output(print())
#==============================================================================
print(1024*768)