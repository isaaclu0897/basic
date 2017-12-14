# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:56:01 2017

@author: VX
"""
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve



page_target = 'https://www.ptt.cc/bbs/Beauty/M.1489927057.A.B97.html'
res = requests.get(page_target)
soup = BeautifulSoup(res.text, 'lxml')

for a in soup.select('a'):
    url = a.text
    print(url)
    try:
        for i in range(0, 20):
            urlretrieve(url, 'E:\\python\\beauty\\{}.jpg'.format(i))
    except:
        print('123')
    