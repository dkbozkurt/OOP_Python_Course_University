# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:41:41 2019

@author: burak
"""

a=int(input('Enter a '))
b=int(input('Enter b '))
c=int(input('Enter c '))

if (a<b+c) and (b<a+c) and (c<b+a):
    result=True
else:
    resulr=False

if result:
    print("These numbers can construct triangle")
else:
    print("These numbers can not construct triangle")