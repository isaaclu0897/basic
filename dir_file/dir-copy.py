# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 06:33:15 2017

@author: VX
"""

import os
import shutil

'''
shutil.copyfile("old","new") 　　　  # 复制文件，都只能是文件

shutil.copytree("old","new")　　　　 # 复制文件夹，都只能是目录，且new必须不存在

shutil.copy("old","new")　　　　     # 复制文件/文件夹，复制 old 为 new（new是文件，若不存在，即新建），复制 old 为至 new 文件夹（文件夹已存在）

shutil.move("old","new")  　　　　   # 移动文件/文件夹至 new 文件夹中
''' 
file_dir = "E:\python\TEST"
os.chdir(file_dir)
print (1,os.listdir(os.getcwd()))
shutil.copyfile("a.txt","a-copy.txt")        # copy test_org.txt 为 test_copy.txt 若存在，则覆盖
print (2,os.listdir(os.getcwd()))
shutil.copyfile("b.txt","b-copy.txt")            # 存在，覆盖
print (3,os.listdir(os.getcwd()))
shutil.copytree("1","1-copy")            # copy test_org 为 test_copytree（不存在的新目录）
print (4,os.listdir(os.getcwd()))
shutil.copy("b.txt","3")           # 同 copyfile
print (5,os.listdir(os.getcwd()))
shutil.copy("a-copy.txt","2")                # 将文件 copy 至 目标文件夹中（须存在）
print (6,os.listdir(os.getcwd()))
shutil.copy("a-copy.txt","g")                 # 将文件 copy 至 目标文件（该文件可不存在，注意类型！）
print (7,os.listdir(os.getcwd()))
shutil.move("a-copy.txt","3m")                # 将文件 move 至 目标文件夹中
print (8,os.listdir(os.getcwd()))
shutil.move("b-copy.txt","3m")                    # 将文件夹 move 至 目标文件夹中
print (9,os.listdir(os.getcwd()))
