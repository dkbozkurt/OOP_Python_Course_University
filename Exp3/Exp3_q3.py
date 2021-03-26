# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:49:26 2021

@author: Doğukan Bozkurt
"""
#The pose of 2 wheeled mobiele robot with a constant speed w

import math

x0=float(input("Enter x0: "))
y0=float(input("Enter y0: "))
Teta0=(float(input("Enter Teta0: ")))*math.pi/180
r=float(input("Enter r: "))
w=float(input("Enter w: "))
t=float(input("Enter t: "))

x=x0-r*math.sin(Teta0)+r*math.sin(Teta0+w*t)
y=y0+r*math.cos(Teta0)-r*math.cos(Teta0+w*t)
Teta=Teta0+w*t

print("x=",format(x,".2f"),"\ny=",format(y,".2f"),"\nTeta=",format(Teta,".2f"))
