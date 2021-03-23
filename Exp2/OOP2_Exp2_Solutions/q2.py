# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:41:41 2019

@author: burak
"""

x=int(input('Enter x '))
y=int(input('Enter y '))
z=int(input('Enter z '))

if (x<y and y<z) or (x>y and y>z):
    result=True
else:
    result=False
    
if result:
    print("Three integers are in order")
else:
    print("Three integers are not in order")
    