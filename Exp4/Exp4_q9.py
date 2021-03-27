# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 01:00:33 2021

@author: Doğukan Bozkurt
"""
#Finding roots of a function.
def ffunction(asd):
    return(asd**3)-(5*asd)-9 

a=int(input("Enter a value for a: "))
b=int(input("Enter a value for b: "))
tol=float(input("Enter a tolerance value for tol: "))
fc=tol+1
   
while abs(fc)>tol:

    fa=ffunction(a)
    fb=ffunction(b)
    print ("f({0}) = {1} \nf({2}) = {3}".format(a,fa,b,fb))

    c=b-(fb*((b-a)/(fb-fa)))
    fc=ffunction(c)
    print("f({0}) = {1}".format(c,fc))
    
    if fa*fc<0:
        b=c
    else:
        a=c
    print("New intervals:\na={0}\tb={1}\tc={2}".format(a,b,c))
    print("fc:",fc)
    
print("The roots of the function after repetition is:\na={0}\tb={1}\tc={2}".format(a,b,c))