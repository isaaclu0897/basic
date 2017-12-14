# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 01:36:08 2017

@author: VX
"""

import os


'''
手動新建 1.dir、a.txt
'''


''' 
重命名文件夹/文件

os.rename(oldfileName, newFilename) 
'''
 
file_dir = "E:\python\TEST"
os.chdir (file_dir)
os.rename ("11","1")    
os.rename ("a","a.txt")
print (1,os.listdir(os.getcwd()))
os.rename ("1","11")    
os.rename ("a.txt","aa.txt")                # 重命名，注意需要带扩展名
print (2,os.listdir(os.getcwd()))


