# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 13:02:53 2021

@author: Doğukan Bozkurt
"""
#Calculate cosine func. by using Taylor series

from math import factorial as f

x=float(input("Enter x: "))
th=float(input("Enter threshold value: "))
y=1
res=1
i=2

while abs(y)>th:
    y= ((x**i)/f(i))
    
    if i%4==0:
        res=res+y
    else:
        res=res-y
    i+=2

print("cos({0}) = {1}".format(x,res))
