# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 07:34:40 2017

@author: VX
"""

import os

file_abs = "E:\\python\\TEST\\a.txt"

try:
    f = open (file_abs,'r')
    print (f.read())
    
finally:
    if f:
        f.close()