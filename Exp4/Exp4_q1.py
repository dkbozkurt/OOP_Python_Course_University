# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:20:55 2021

@author: Doğukan Bozkurt
"""
#Summation Operation

from math import factorial as f

x=int(input("Enter a x value: "))
res=0

for n in range (1,8):
    y= (-1)**(n+1)*(x**n/f(n))
    
    if 0<=y:
        res=res+y
        
    else:
        continue

print("The result is :",format(res,".4f"))