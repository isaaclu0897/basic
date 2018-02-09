#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 01:12:11 2018

@author: wei
"""
'''
Variable can let us to store anything,

first, we use variable to store string.
'''

# you can use signal quote or double quotes to let Python to know that is sting.
message1 = "How are you!"

message2 = 'I am fine, thank you, and you?' # then you can use print(Variable) to show it

# but sometimes you will use apostrophe(撇號) in string or we can say sentence, like under...
# message = 'I'm fine, thank you, and you?' # this is syntax error


# there are theree ways to fix it,

# one, use backslash(反斜槓), tell Python this is a charactor, not the end of string
message = 'I\'m fine, thank you, and you?' 

# two, use signal quote & double quotes at the same time
message = "I'm fine, thank you, and you?"  # 'I"m fine, thank you, and you?', that is also legal

sentence = ''' thsi is a good day,
and I'am write the code in home,
but this OK, I feel happy.
'''