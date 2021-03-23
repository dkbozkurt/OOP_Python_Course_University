# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:41:41 2019

@author: burak
"""

x=int(input('Enter x '))

if x<-3:
    y=(x**3+4)/(x**2)
elif x<0:
    y=abs(x**2+3*x-10)
elif x<4:
    y=x**2-4*x
else:
    y="Undefined interval"

print(y)