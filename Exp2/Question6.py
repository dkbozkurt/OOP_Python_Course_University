# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:06:38 2021

@author: Doğukan Bozkurt
"""
#Partial function
x=0
while(x!= 999):
    x=int(input("Enter an integer value for x :\n(Enter 999 to exit!)\n"))
    
    if(x<-3):
        y=(x**3+4)/x**2
    elif(-3<=x<0):
        y=abs(x**2+3*x-10)
    elif(0<=x<4):
        y=x**2-4*x
    elif(x==999):
        pass
    else:
        print("You entered wrong value. Please try again.")
        continue
    print("y= ",y)