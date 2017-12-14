# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:13:31 2017

@author: VX
"""

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def info(self):
        return (self.name, self.job)
    

'''
tony = Person('tony', 'student')
print(tony.name)
print(tony.job)
print(tony.info())
'''

class man(Person):
    man.sex = 'male'

tony = man('tony', 'student')
print(tony.sex)
print(tony.info())
