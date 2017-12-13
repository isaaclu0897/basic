# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:42:41 2017

@author: VX
"""
#==============================================================================
# list
#==============================================================================

classmates = ['Michael', 123, 'Tracy']
print(classmates)          # ['Michael', 'Bob', 'Tracy']
print(len(classmates))     # 3

# 空的list
t = []
print(t)                   # [] 

# 索引
print(classmates[1])       # Bob
print(classmates[-1])      # Tracy

# 增加元素至末尾
classmates.append('Adam') 
print(classmates)          # ['Michael', 'Bob', 'Tracy', 'Adam']

# 插入元素到指定位置
classmates.insert(1,'jack') 
print(classmates)          # ['Michael', 'jack', 'Bob', 'Tracy', 'Adam']

# 刪除末尾元素及指定元素
classmates.pop()
print(classmates)          # ['Michael', 'jack', 'Bob', 'Tracy']
classmates.pop(1)
print(classmates)          # ['Michael', 'Bob', 'Tracy']

# 替換某個元素
classmates[1] = 'Sarah'
print(classmates)          # ['Michael', 'Sarah', 'Tracy']

# list 中，也可以有list，索引其中list的方式為 xxx[第一層][第二層]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))              # 4
print(s[2][1])             # php

#==============================================================================
# tuple
#==============================================================================

''' tuple
1. tuple 和 list 很像，但tuple一旦設定，不能更改
2. tuple因為不能更改()，所以更安全
3. 索引方式和 list 相同，但沒有增加、插入、刪除的功能
4. tuple 不能更改，但若 tuple 中有 list ，其 list 是可以更改的
'''

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates[1])       # Bob
print(classmates[-1])      # Tracy

# 空的 tuple
t = ()
print(t)                   # ()

# 注意，若要定義一個元素的tuple，比需加 , ，否則系統會混淆為賦值
t = ('123', )
print(t)                   # ('123',)

# tuple 中有list，tuple 不可更改，但tuple中的list可以賦值
t = (1, 2, [3, 4], 5)
print(t)
t[2][1] = 7                # (1, 2, [3, 4], 5)
print(t)                   # (1, 2, [3, 7], 5)






