# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:54:59 2021

@author: Doğukan Bozkurt
"""
#The inverse kinematics equations of a 2-DOF robot arm

import math

L1=float(input("Enter L1= "))
L2=float(input("Enter L2= "))
A=float(input("Enter A= "))
Z=float(input("Enter Z= "))

print("L1: ",L1,"\nL2: ",L2,"\nA: ",A,"\nZ: ",Z)

Teta1= math.acos((L1**2+A**2+Z**2-L2**2)/(2*L1*math.sqrt(A**2+Z**2)))
+math.atan(Z/A)

Teta2= math.acos((L1**2+L2**2-A**2-Z**2)/(2*L1*L2))

print("\nTeta1=",format(Teta1,".3f"),"\nTeta2=",format(Teta2,".3f"))