# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:39:24 2017

@author: VX
"""

import os
import shutil
import time

start = time.time()

file_dir = "E:\python\code"# 注意 \\ ；windows 下是這麼表示的(其實也可以像我那樣打)；Linux 和 Mac 是 /
file_name = "BMI.py"

print (1,os.path.isabs(file_dir))# 判?是否??路?
print (2,os.path.isabs(file_name))
print ('--------------------------------------')                        
print (3,os.path.exists(os.path.join(file_dir,"BMI.py")))
print ('--------------------------------------')
print (4,os.path.isdir(file_dir))# 判?是否是?目?
print (5,os.path.isdir(file_name))
print ('--------------------------------------')
print (6,os.path.isfile(file_dir))# 判?是否是?文件
print (7,os.path.isfile(file_name))

print (os.getcwd())
# ?取?前工作目?
print (os.listdir(file_dir))
# 列出?前工作目?的所有文件 Python2 不支持 os.listdir()    Python3 ?列出?前工作目?下的所有文件

print ('程式共花費: %f秒' %(time.time() - start))
