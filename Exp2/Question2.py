# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 00:49:37 2021

@author: Doğukan Bozkurt
"""

x=int(input("Please enter a value for x: "))
y=int(input("Please enter a value for y: "))
z=int(input("Please enter a value for z: "))

if(x<y<z or x>y>z):
    a= True
else:
    a= False
    
print("Is the type of \'a\' is bool?",type(a) is bool)

if(a):
    print("The values are either ascending or descending.")
else:
    print("The valuse are neither ascending or descending.")