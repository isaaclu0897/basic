# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:25:58 2017

@author: wei
"""

#==============================================================================
# 列表生成式(List Comprehensions)
#==============================================================================
'''
1. 運用列表生成式可以寫出簡單的代碼
'''
# 若要生成list 1~10可以這樣做
print(list(range(1, 11)))

# 若要生成1x1~10x10怎么做？方法: 循环
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 而列表生成式则可以用一行语句代替循环生成上面的list
L = [x * x for x in range(1, 11)]
print(L)

# 生成的元素放前面， 後面放上for 循環，甚至可以加上 if 條件判斷
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 还可以使用两层循环，可以生成全排列
A = [m + n for m in 'ABC' for n in 'XYZ']
print(A)

import os
print([d for d in os.listdir('.')])

# 同时使用两个甚至多个变量，上節的代碼
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
     print(k, '=', v)
    
# 上節的代碼，我們可以用列表生成式改寫
print([k + '=' + v for k, v in d.items()])

# 把所有字串變成小寫
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#==============================================================================
# 練習
#==============================================================================
'''
如果list中既包含字符串，又包含整数，
由于非字符串类型没有lower()方法，
所以列表生成式会报错
可使用內建函數isinstance函数可以判断一个变量是不是字符串
'''
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])



























