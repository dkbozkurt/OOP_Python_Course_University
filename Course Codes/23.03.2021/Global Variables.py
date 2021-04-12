# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:21:03 2021

@author: Doğukan Bozkurt
"""
#Global Variables
number=0

def main():
    global number
    number= int(input("Enter a number: "))
    show_number()
    
def show_number():
    print("The number you entered is ",number)
    
main()