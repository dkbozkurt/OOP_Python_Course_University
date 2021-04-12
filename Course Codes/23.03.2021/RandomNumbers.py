# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:38:10 2021

@author: Doğukan Bozkurt
"""
import random

#randint(x,y,z) : gives a random int value from x to y (x includes)
#randrange(x,y,z) : returns an int randomly selected value in range with step value z 
#random : Returns random flaoting number in the range of 0.0 up to 1.0 (1.0 not including)
#uniform(x,y,z) : Returns random floating number but allows to specift the range.
#seed(x) : program will always produce the same sequence of pseudorandom numbers
"""

def main():
    for count in range(5):
        
        number=random.randint(1,10)
        print("The number is", number)
    
main()

"""
