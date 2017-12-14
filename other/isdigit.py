# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:38:54 2017

@author: VX
"""
import time

# 從一段文字取出數字的方法
# method 1-1
start = time.time()
a = []
for x in 'ad32499adsfasd3asf654df65a4sdf13gsd2f1gs54df6ga2sd1fg3s5er46ga32df1g3a5erw46g3a21gf3a5wr41g3a2szd1v35ae41rg32vS'*100000:
    if x.isdigit():
        a.append(x)
''.join(a)
end = time.time()
print('1-1', end - start)

# method 1-2    
start = time.time()
''.join([x for x in 'ad32499adsfasd3asf654df65a4sdf13gsd2f1gs54df6ga2sd1fg3s5er46ga32df1g3a5erw46g3a21gf3a5wr41g3a2szd1v35ae41rg32vS'*100000 if x.isdigit()])
end = time.time()
print('1-2', end - start)
#==============================================================================
# method 2
import re
start = time.time()
'-'.join(re.findall('[0-9]+', 'ad32499adsfasd3asf654df65a4sdf13gsd2f1gs54df6ga2sd1fg3s5er46ga32df1g3a5erw46g3a21gf3a5wr41g3a2szd1v35ae41rg32vS'*100000))
end = time.time()
print('2', end - start)
#==============================================================================
a=filter(str.isdigit, "12dff412df54")
print(a)