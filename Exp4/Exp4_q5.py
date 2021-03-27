# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 13:56:58 2021

@author: Doğukan Bozkurt
"""
#Automorphic numbers

num=int(input("Enter an integer value: "))

sqr=num**2
n= len(str(num))  
last= sqr%pow(10,n)

if last == num:    
    print("Automorphic Number")
else:
    print("Non an Automorphic Number")