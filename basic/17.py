# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:06:09 2017

@author: wei
"""

#==============================================================================
# 生成器(generator)
#==============================================================================
'''
通过列表生成式，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
生成器可以邊計算邊生成，這樣能省去極大的內存
'''
# 創建生成器有很多方法，第一格方法是將列表生成式的[] 改成()
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
# next(g)
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b) # 這裡改成 yield 就變成了 generator
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(10))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b) 
        a, b = b, a + b
        n = n + 1
    return 'done'

for i in fib(10):
    print(i)

'''
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而generator的函数，在每次调用next()的时候执行，
遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
    
for i in odd():
    print(i)
    print()
    
'''
1. 使用生成器可以省下內存
2. 生成器原理是記下算法，下次調用時再算出來
3. 生成器遇到next()執行，yiele語句 返回，在執行從上次的yield繼續下去
'''
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 用generator的楊輝三角
def triangles():
    n = 1
    a = []
    b = 1
    a.insert(n, b)
    print(a)
   
print(triangles())
'''
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
'''



















