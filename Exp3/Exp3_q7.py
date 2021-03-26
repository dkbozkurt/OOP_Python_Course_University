# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 23:28:59 2021

@author: Doğukan Bozkurt
"""
#Classification problem for a door

from math import e

sOpen= float(input("Enter sOpen: "))
sClose= float(input("Enter sClose: "))
sSemiOpen= float(input("Enter sSemiOpen: "))

p=(e**sOpen+e**sClose+e**sSemiOpen)
pOpen= (e**sOpen)/p
pClose= (e**sClose)/p
pSemiOpen= (e**sSemiOpen)/p

if pOpen>pClose:
    if pOpen>pSemiOpen:
        print("Open Door")
    else:           
        print("Semi Open Door")
else:
    if pClose>pSemiOpen:
        print("Close Door")
    else:           
        print("Semi Open Door") 
        
"""
#-----WAY2-----
if pOpen>pClose:
    if pOpen>pSemiOpen:
        print("Open Door")
        exit()
else:
    if pClose>pSemiOpen:
        print("Close Door")
        exit()
print("Semi Open Door")  
"""