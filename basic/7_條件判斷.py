# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:56:59 2017

@author: VX
"""

#==============================================================================
# 條件判斷
#==============================================================================

age = 20
if age >= 18:
    print('your age is', age) # your age is 20
    print('adult')            # adult
    
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')  
else:
    print('your age is', age) # your age is 3
    print('teenager')         # teenager
    
age = 3
if age >= 18:
    print('adult')
elif age >= 6:               # elif 是 else if 的縮寫
    print('teenager')
else:
    print('kid')             # kid
    
''' elif 由來
age = 3
if age >= 18:
    print('adult')
    else:
        if age >= 6:
            print('teenager')
        else:
            print('kid')
'''           
            
    
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 1
if x:
    print('True')            # True
    
    
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
height = 1.75
weight = 80.5
BMI = weight/(pow(height, 2))
if 0 < BMI <= 18.5:
    print('your BMI is {}'.format(BMI))
    print('過輕')
elif 18.5 < BMI <= 25:
    print('your BMI is {}'.format(BMI))
    print('正常')
elif 25 < BMI <= 28:
    print('your BMI is {}'.format(BMI))
    print('肥胖')
else:
    print('your BMI is {}'.format(BMI))
    print('嚴重肥胖')