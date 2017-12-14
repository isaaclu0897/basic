# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 09:41:21 2017

@author: VX
"""
# 簡易文件開啟、讀、寫。
text = ('''#文件讀寫接上
text = "ggwp\\nhi\\nheollo python\\ni am pythoner \\n"\n
with open("newfile.txt", "w") as f:
    f.write(text)\n
with open("newfile.txt", "r") as f:
    print(f.read())\n''')

with open('filelink2.py', 'w') as f:
    f.write(text)

with open('filelink2.py', 'r') as f:
    print(f.read())
    