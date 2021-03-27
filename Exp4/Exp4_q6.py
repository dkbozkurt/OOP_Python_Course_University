# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:06:36 2021

@author: Doğukan Bozkurt
"""
#Checksum formula
"""
ERROR DEVAMKE
"""
num=int(input("Enter your credit card num: "))
bnum=len(str(num))
ccnum=0
for i in range(bnum-1,0,-1): 
    print("i: ",i)

    if bnum%2==1:
        if i%2==0:
            num=num//(10**i)
        else:    
            num=num//(10**i)*2
        print("di:",num)
        ccnum=ccnum+num
    else:
        if i%2==0:
            num=num//(10**i)
        else: 
            num=num//(10**i)*2
        print("num:",num)
        ccnum=ccnum+num
        
print("ccnum: ",ccnum)

if ccnum%10==0:
    print("The credit card num is valid!")

else:
    print("The credit card num is unvalid!")