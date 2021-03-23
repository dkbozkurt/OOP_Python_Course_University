# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:48:26 2021

@author: Doğukan Bozkurt
"""
a=int(input("Enter an input for a: "))
b=int(input("Enter an input for b: "))
c=int(input("Enter an input for c: "))

if(a<b+c and b<a+c and c<b+a):
    bool_=True
else:
    bool_=False

#One Line boolean Check
print("We CAN construct a triangle." if bool_ else "We CAN NOT construct a triangle.")     