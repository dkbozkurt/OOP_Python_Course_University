# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 23:45:02 2021

@author: Doğukan Bozkurt
"""

goal= float(input("Enter goal: "))
dist= float(input("Enter distance: "))

if goal==1:
    if dist >= 16.5:
        print("He scores, absolutely brilliant!")
    else:
        if dist >= 5.5:
            print("A fantastic move and good finish!")
        else:
            print("He finds the net with ease!")
else:
    print("He should have scored!")