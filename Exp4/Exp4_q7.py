# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:46:10 2021

@author: Doğukan Bozkurt
"""
#Narcissistic Number

num=int(input("Enter a 4-digit number: "))
result=0
for i in str(num):
    
    result=result+(int(i)**4)

if result==num:
    print("{0} is a Narcissistic number!".format(num))
else:
    print("{0} is not a Narcissistic number!".format(num))