# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:30:42 2021

@author: Doğukan Bozkurt
"""
#Binary number to Decimal

number=input("Enter a binary number: ")
j=0
dec=0

for i in number:
    dec = dec+ int(i)*(2**j)
    j+=1
    
#print("(",number,")_2 = (",dec,")_10")
print("({0})_2 = ({1})_10".format(number,dec))
