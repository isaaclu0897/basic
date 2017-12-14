# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 07:38:26 2017

@author: VX
"""

file_abs = "E:\\python\\TEST\\a.txt"

with open(file_abs,'r') as f:
    print(f.read())
    print(f)
    print(f.closed, f.mode, f.encoding, f.newlines)
    
with open(file_abs,'w') as f:
    f.write ('hi\n')
    f.write ('hello world\n')
    f.write ('hi python\n')
    f.write ('good for you\n')
    f.write ('i am a pythoner\n')

with open(file_abs,'r') as f:
    print(f.read())
print('//////////////////////////////////////////////////////////')
with open(file_abs,'r') as f:
    listq = f.readlines()
    
print (type(listq))
for i in listq:
    print (i)


    