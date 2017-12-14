# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 11:28:12 2017

@author: VX
"""

# 疊代器主要由疊代對象、疊代器、生成器

''' 容器
疊代器由容器所組成，那容器又是什麼呢? 容器裡面又可以放甚麼呢?
簡單的說，容器是一個存放元素的地方，這地方裡面放的，可以是 list、tuple、string、dict，
下面我們放上代碼實例
'''
# lists
assert 1 in [1, 2, 3]
assert 4 not in [1, 2, 3]

# sets
assert 1 in {1, 2, 3}
assert 4 not in {1, 2, 3}

# tuples
assert 1 in (1, 2, 3)
assert 4 not in (1, 2, 3)

# dict
d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d
assert 'foo' not in d  # 'foo' 不是dict中的元素

# string
s = 'foobar'
assert 'b' in s
assert 'x' not in s
assert 'foo' in s 



