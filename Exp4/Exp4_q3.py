# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:45:23 2021

@author: Doğukan Bozkurt
"""
#The greatest common divisor(gcd) of two integers

num1=int(input("Enter an integer value for number1 :"))
num2=int(input("Enter an integer value for number2 :"))
gcd=0
if(num1<num2):
    num=num1
else:
    num=num2
    
for i in range(1,num+1):
    
    if (num1%i)==0 and (num2%i)==0:
        gcd=i
        
print("gcd of the two integers is: ",gcd)