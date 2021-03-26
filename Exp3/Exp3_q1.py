# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 20:33:02 2021

@author: Doğukan Bozkurt
"""
import math
#Forier series funcs.

a_1=int(input("Please enter a value for a1: "))
b_1=int(input("Please enter a value for b1: "))
#Teta will be converted Degree to Radian
Teta_1=(int(input("Please enter a value for Teta_1: ")))*math.pi/180
t=7
print("\na_1: {0}\nb_1: {1}\nTeta_1: {2}".format(a_1,b_1,Teta_1))

A_1= math.sqrt(a_1**2+b_1**2)

g_1=A_1*math.cos(math.pi/4*t+Teta_1)

print("g_1({0})= {1}".format(t,g_1))
