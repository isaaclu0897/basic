# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:05:17 2017

@author: VX
"""



# 在Python3字串已經全部統一成 unicode ，所以不必加上 u ，這是Python2和Python3的重要差別之一，需要特別注意
''' 編碼
1. 在 python3 當中，我們是以unicode編碼的(不需要再字串前面加u 讓電腦識別是unicode)。
2. unicode 基本單位是字。
3. utf-8 基本單位是byte。
4. 編碼、解碼的指令為 encode、decode
5. 計算字串裡有多少字使用 len
'''
# 將字串便成整數形式
print(ord('a'))

# 將編碼轉換成對應字符
print(chr(66))

# b'ABC' 不等於 'ABC' 前者是byte 後者是 字串

print(len('ABC'))
print('ABC'.encode('ascii'))
print(b'ABC'.decode('ascii'))
print('中文'.encode('utf8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf8'))