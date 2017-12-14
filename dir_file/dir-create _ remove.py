# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 23:35:28 2017

@author: VX
"""

import os
import shutil

'''
a = "E:\python\TEST"
os.chdir(a)
shutil.rmtree("test_mkdir")
'''

'''
工作目录及创建文件夹操作
  
  
os.getcwd() 　　　　  # 获取当前工作目录

os.chdir(...)　　　　 # 改变工作目录

os.listdir(...)　　　 # 列出目录下的文件

os.mkdir(...)　　　　 # 创建单个目录    　　注意：创建多级用 os.makedirs()

os.makedirs(...)　　  # 创建多级目录
'''
print (1,os.getcwd())                                # 获取当前工作目录
file_dir =  'E:\python\TEST'        
os.chdir(file_dir)                                 # 改变工作目录
print (2,os.getcwd())                                # 获取当前工作目录
os.mkdir("test_mkdir")                             # 在当前工作目录下创建文件夹 test_mkdir；注意不可存在相同文件夹，不然会报错
os.makedirs("test_mkdir\\test1")
os.makedirs("test_mkdir\\test2")
os.makedirs("test_mkdir\\test2\\1\\2\\3")
print (3,os.getcwd())

'''
删除文件夹/文件
os.rmdir(...) 　　　　  # 删除空文件夹        注意：必须为空文件夹  如需删除文件夹及其下所有文件，需用 shutil

os.remove(...)          # 删除单一文件

shutil.rmtree(...)      # 删除文件夹及其下所有文件
'''
os.chdir(".\\test_mkdir")                          # . 表示本级目录； .. 表示上级目录
#os.chdir(file_dir+"\\test_mkdir")                    
print (4,os.getcwd())

print (5,os.listdir(os.getcwd()))                        # 查看当前文件夹下所有文件    
os.rmdir("test1")                                     # 删除 test1 文件夹（空文件夹）
print (6,os.listdir(os.getcwd()))    
os.mkdir("1")
for i in range(2,6):                               # 使用for循环等，可方便的创建多个文件夹
    dir_name = str(i)
    os.mkdir(dir_name)
print (7,os.listdir(os.getcwd()))    
os.chdir("..\\")
print (8,os.getcwd())
shutil.rmtree("test_mkdir")                           # 删除 test_mkdir 及其下所有文件
print (9,os.listdir(os.getcwd()))


