# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:35:44 2021

@author: Doğukan Bozkurt
"""
import math

p1x=float(input("Enter p1x: "))
p1y=float(input("Enter p1y: "))
p1z=float(input("Enter p1z: "))
p2x=float(input("Enter p2x: "))
p2y=float(input("Enter p2y: "))
p2z=float(input("Enter p2z: "))
rOuter=float(input("Enter rOuter: "))
rInner=float(input("Enter rInner: "))

distP1P2=math.sqrt((p1x-p2x)**2+(p1y-p2y)**2+(p1z-p2z)**2)

if distP1P2<rOuter:
    if distP1P2<rInner:
        print("Inner Region")
    else:
        print("Outher Region")
else:
    print("Not in Region")