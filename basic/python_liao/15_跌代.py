# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:45:46 2017

@author: wei
"""

#==============================================================================
# 跌代 
#==============================================================================
'''
1. 跌代對象必須為可跌代
2. 任何可跌代對象都可以用，for 循環跌代
'''
# 在python的跌代是通過，for ... in 來實現的。

d = {'a': 1, 'b': 2, 'c': 3}
for i in d:
     print(i)

# 若想跌代出dict 的值，可以用 d.values()，若要同時跌代key 和value 可以用d.item()
for i in d.values():
    print(i)
    
for i, j in d.items():
    print(i, j)

# 跌代字串
for i in 'ABC':
     print(i)

# 通過collections模块的Iterable类型判断，可檢查物件是否可跌代
from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代 yes

print(isinstance([1,2,3], Iterable)) # list是否可迭代 yes

print(isinstance(123, Iterable)) # 整数是否可迭代 no

# enumerate(物件, 索引起始=0)函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C'], 1):
    print(i, value)
    
# 也可以如下，引入兩個參數，這樣的做法在python 很常見
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)























