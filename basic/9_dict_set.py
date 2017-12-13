# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 00:02:32 2017

@author: VX
"""

#==============================================================================
# dict
#==============================================================================

''' dict
1. dict 可以做到 list做不到的存值
2. dict 查找迅速，但其沒有順序性
3. list 越大查找越慢，dict 內存占地大，可謂dict用空間換取時間。

'''

# 存值
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# dict後
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 索引與list相同
print(d['Michael'])
# in 可判斷這個值，是否存在於list、 dict、 tuple ....。
print('Tony' in d)


# 通過get ，如果key不存在返回None，或者返回自己指定得值
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# pop 刪除key
d.pop('Bob')
print(d)

# 檢視所有德key
print(d.keys())

# 可賦值但不可變更key
d['Michael'] = 50
print(d['Michael'])

#==============================================================================
# set (集合) 
#==============================================================================

''' set
1. set 和dict類似，但set 不存值
2. set 中沒有重複的值，意即不可放入list這樣可變的數值
3. set 不可索引、不可排序(此點同dict)
4. 不可變得對象永遠不可變
5. key最常用的不可變對象為str，
'''
s1 = {-1, 1, 2, 3}
print(s1)
s1.add(4)
print(s1)
s1.remove(4)
print(s1)

s2 = {2, 3, 4, 5, 6}
print(s1 & s2,
      s1 | s2)

# list 可排序
a = ['c', 'b', 'a']
a.sort()
print(a)

# 字串為不可變得說明
a = 'abc'
a.replace('a', 'A')
print(a) 

# 看起來好像變了，但事實上是程式新建了一個'Abc'，而非改變原來的'abc'
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a) # 程式中這樣的做法可以保證，不可變得對象永遠不可變






























