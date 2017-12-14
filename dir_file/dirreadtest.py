# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 09:19:50 2017

@author: VX
"""

import os

file_dir = 'E:\\python\\TEST'
file_name = '111.txt'
file_abs = os.path.join(file_dir, file_name)
print ('是否為一正確路徑 : %s'%(os.path.isabs(file_abs)))

with open (file_abs,'r') as f:
    fline = f.readlines()

for i in fline:
    print (i)