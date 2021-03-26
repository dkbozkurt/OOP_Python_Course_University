# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:20:13 2021

@author: Doğukan Bozkurt
"""

#The output of 2-input neuron,

from math import e

x1=float(input("Enter x1: "))
x2=float(input("Enter x2: "))
w1=float(input("Enter w1: "))
w2=float(input("Enter w2: "))
b=float(input("Enter b: "))

z=x1*w1+x2*w2+b

y=1/(1+e**(-z))


print("y=f(",z,")= ",y)
print("y=f({0:.2f})={1:.2f}".format(z,y))          