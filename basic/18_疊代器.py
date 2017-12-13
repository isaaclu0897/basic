# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 22:44:08 2017

@author: VX
"""

#==============================================================================
# 疊代器
#==============================================================================
'''
for 循環可使用list、tuple、dict、set、str等數據類型，
以及生成器，這些可以作用於for循环的对象统称为可迭代对象(Iterable)，
其中在可疊代對象裡，可以不斷調用next() 為疊代器，
另外為了檢驗對象是否可疊代可以使用isinstance()判断。
'''
'''
1. 我們無法提前知道疊代器的長度，只能透過不斷的next()計算下一個數據。
2. 疊代器可以是一個無限大的數據流，而list無法達到此特性。
'''
from collections import Iterable, Iterator
# 可疊代對像, 可以直接被for 循環作用的
print(isinstance([], Iterable)) # True
print(isinstance({}, Iterable)) # True
print(isinstance('abc', Iterable)) # True
print(isinstance((x for x in range(10)), Iterable)) # True
print(isinstance(100, Iterable)) # False

# 疊代器
'''
P.S. 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
直到最后抛出StopIteration错误表示无法继续返回下一个值了
''' 
print(isinstance((x for x in range(10)), Iterator))# True
print(isinstance([], Iterator))# False
print(isinstance({}, Iterator))# False
print(isinstance('abc', Iterator))# False

# 一般數據可使用iter()，轉換類型為Iterator
print(isinstance(iter([]), Iterator)) # True
print(isinstance(iter('abc'), Iterator)) # True

# 其實for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 4, 5]:
    print(x)

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


























