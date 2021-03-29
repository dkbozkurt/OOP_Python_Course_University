# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 23:11:27 2021

@author: Doğukan Bozkurt
"""
from fractions import gcd

def primes(n):

    for i in range (0,n+1):
        
        for j in range(1,n+1):
            if i==0:
                print("{:>3}".format(j),end='')
            elif gcd(i,j)==1:
                print("{:>3}".format("*"),end='')
            else:
                print("{:>3}".format(" "),end='')
                
        if i==0:
            print(" ")
        else:  
            print(" ",i)
    
def main():
    n=int(input("Enter a number: "))
    print(n)
    primes(n)    
    
main()