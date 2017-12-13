# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:15:27 2017

@author: wei
"""

#==============================================================================
# 高級特性
#==============================================================================
''' 要點
1. 代碼越少、越簡單越好。
2. 1行代碼能寫成的絕不寫 5行。
'''
#==============================================================================
# 切片(slice)
#==============================================================================
# 取出 list 或 tuple 中的某部分元素
# 笨方法
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0], L[1], L[2])

# 通過 for 改善
r = []
for i in range(3):
    r.append(L[i])
    
print(r)

# python 有切片(slice)可用，與 for循環搭配 range生成列表的方式常像，並可以大大簡化操作。
# range(起始=0, 結束(不包), 間隔)
# list[起始=0:結束(包):間隔]
print(L[0:3]) 
print(L[:3])
print(L[1:3]) 
print(L[-2:])
print(L[-2:-1])

L = list(range(1,101))
print(L[:10]) # 前10
print(L[-10:]) # 後10
print(L[10:20]) # 11到20
print(L[:10:2]) # 前10每兩格取一個
print(L[::5]) # 每5取一個

# tuple , string 同樣可以如法炮製





















