# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:46:10 2021

@author: Doğukan Bozkurt
"""
def division(n1,n2):
    quotient=n1//n2
    remainder=n1%n2
    return quotient, remainder

def main():
    n1=int(input("Enter a value for Dividend: "))
    n2=int(input("Enter a value for Divisor: "))
    quo,rem=division(n1,n2)
    print("Dividend is:{0}\nDivisor is:{1}\nQuotient is:{2}\nRemainder is:{3}".format(n1,n2,quo,rem))
    
main()