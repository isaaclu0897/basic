# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:22:50 2017

@author: VX
"""

#==============================================================================
# sorted
#==============================================================================
'''排序算法
排序也是在程序中经常用到的算法。
无论使用泡泡排序还是快速排序，
排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，
但如果是字符串或者两个dict呢？直
接比较数学上的大小是没有意义的，
因此，比较的过程必须通过函数抽象出来。
'''
a = [36, 5, -12, 9, -21]
print(a)
# Python内置的sorted()函数就可以对list进行排序
print(sorted(a))

# 它还可以使用key接收一个函数来实现自定义的排序
print(sorted(a, key=abs))

a = ['bob', 'about', 'Zoo', 'Credit']
# 排序字串
# 默认情况，由于'Z' < 'a'，大写字母Z会排在小写字母a的前面
print(sorted(a))

# 若想忽略大小寫來比較字串，key值輸入str.lower
print(sorted(a, key=str.lower))

# 若想進行反向排序，不須更動key，只要追加第三個參數，reverse=True便行
print(sorted(a, key=str.lower, reverse=True))

'''练习
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    '''
    (x, y) = t
    name = x
    return name
    '''
    return t[0] # 其實這list傳進來一經是一個tuple了

L2 = sorted(L, key=by_name)
print(L2)

# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score, reverse=True)

print(L2)







