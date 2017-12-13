# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:55:58 2017

@author: VX
"""

#==============================================================================
# 返回函数
#==============================================================================
'''
前面我們已經說到，高階函數可以接受函數作為參數，
其實他還可以將函數傳出作為輸出。
'''
# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print(calc_sum(1, 2, 3, 4))
# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算，我們便可以使其傳出一個求和的函數
def lazy_sum(*args):
    def calcsum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return calcsum
a = lazy_sum(1, 3, 5, 7, 9)
print(a) # <function lazy_sum.<locals>.sum at 0x000001D148F16A60>
print(a()) # 因傳出的是一個函數，我們需要這樣打印，才能調用出這個函數

'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力。
'''

# 注意，当我们调用lazy_sum()时，每次调用都会返回一个新的函数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2) # False ，函數互不影響
print(f1()==f2()) # True，值相等

#==============================================================================
# 闭包
#==============================================================================
'''
注意到返回的函数在其定义内部引用了局部变量args，
所以当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
因此闭包用起来简单，实现起来可不容易。
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
''' 原因
因為閉包是不會即刻執行的，在這裡返回的函数引用了变量i，
等到三個函數都返回時，它们所引用的变量i已经变成了3，因此最终结果为9。
因此，返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，
或者后续会发生变化的变量。
'''
'''
如果一定要引用循环变量怎么办？方法是再创建一个函数，
用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，
已绑定到函数参数的值不变：
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
# 缺点是代码较长，可利用lambda函数缩短代码。
def count():
    def f(f1):
        return (lambda f1:(lambda:f1*f1))(f1)
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs

f4,f5,f6=count()
print(f4(),f5(),f6())

def count():
    return list(map(lambda j: lambda: j*j, range(1, 4)))
f1, f2, f3 = count()
print(f1(), f2(), f3())
'''
一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，
返回函数中不要引用任何可能会变化的变量。
'''
















