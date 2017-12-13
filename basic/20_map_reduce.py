# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 14:29:55 2017

@author: VX
"""

#==============================================================================
# map/reduce
#==============================================================================
# map(function, iterable, ...) function 為函數， iterable 則為迭代器，此函數取得依 function 計算 iterable 中每個元素的結果
# 意即map可以接受一函數，一可疊代數據，將可疊代數據一一丟掉函數中，並把結果返回。
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
''' 這裡用list 呼叫r的原因
map()传入的第一个参数是f，即函数对象本身。
由于结果r是一个Iterator，Iterator是惰性序列，
因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''
# 若用for 循環可以這樣寫
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
'''
的确可以，但是，从上面的循环代码與map() 相比之下，map()較為直觀，
且只需要一行代碼。
'''

# reduce
# reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x, y):
     return x + y
a = reduce(add, [1, 3, 5, 7, 9])
print(a) # 25
# 其實若需要相加，用函數sum()會更好，但若要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def fn(x, y):
     return x * 10 + y

a = reduce(fn, [1, 3, 5, 7, 9])
print(a) #13579
#==============================================================================
# map/reduce 合併使用
#==============================================================================
# 写出把str转换为int的函数
def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(type(reduce(fn, map(char2num, '13579'))))


# 整理成一个str2int的函数就是
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

# 还可以用lambda函数进一步简化成
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


'''练习
利用map()函数，把用户输入的不规范的英文名字，
变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']：
'''
# -*- coding: utf-8 -*-

def normalize(name):
    a = [i.lower() for i in name]
    a[0] = a[0].upper()
    a = ''.join(a)
    return a

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，
可以接受一个list并利用reduce()求积
'''
# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

'''
利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456
'''
# -*- coding: utf-8 -*-
# method 1

from functools import reduce

def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    
    L = list(s)
    for i in range(len(L)):
        if L[-i] == '.':
            L.pop(-i)
            num = reduce(fn, map(char2num,L))
            num = num / 10 ** (i-1)
            return num
    
print('str2float(\'123.456\') =', str2float('123.456'))

# method 2
# -*- coding: utf-8 -*-
# method 1

from functools import reduce

def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    
    num1 = s.split('.')[0]
    num1 = reduce(fn, map(char2num, num1))
    num2 = s.split('.')[1]
    num2 = reduce(fn, map(char2num, num2)) / 10 ** len(num2)
    return num1 + num2
    
    
print('str2float(\'123.456\') =', str2float('123.456'))











